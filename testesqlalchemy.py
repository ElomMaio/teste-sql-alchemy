from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Date, DateTime, Text, Sequence, Boolean, Float, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, declarative_base
from datetime import datetime, timedelta
import random

Base = declarative_base()

class Forms(Base):
    __tablename__ = "forms"
    uuid_form: Mapped[str] = mapped_column(primary_key=True)
    id_form: Mapped[str] = mapped_column()
    tp_form: Mapped[str] = mapped_column()

    def __init__(self, uuid_form, id_form, tp_form):
        self.uuid_form = uuid_form
        self.id_form = id_form
        self.tp_form = tp_form

class DadosFiscalizacao(Base):
    __tablename__ = "dados_fiscalizacao"
    id_relatorio: Mapped[str] = mapped_column(primary_key=True)
    data_fiscalizacao: Mapped[datetime] = mapped_column(nullable=False)
    hora_inicio: Mapped[datetime] = mapped_column(nullable=False)
    hora_fim: Mapped[datetime] = mapped_column(nullable=False)
    data_escrita: Mapped[str] = mapped_column(nullable=False)  
    registro: Mapped[bool] = mapped_column(nullable=False)
    art: Mapped[str] = mapped_column(nullable=False)
    possui_vetzoo: Mapped[bool] = mapped_column(nullable=False)
    lavratura_igual: Mapped[bool] = mapped_column(nullable=False)
    gera_tcpj: Mapped[bool] = mapped_column(nullable=False)
    gera_tcpf: Mapped[bool] = mapped_column(nullable=False)
    gera_ai_art: Mapped[bool] = mapped_column(nullable=False)
    gera_ai_registro: Mapped[bool] = mapped_column(nullable=False)
    gera_ai_comerciovacina: Mapped[bool] = mapped_column(nullable=False)
    gera_ai_outros: Mapped[bool] = mapped_column(nullable=False)
    uuid_form: Mapped[str] = mapped_column(ForeignKey("forms.uuid_form", ondelete="CASCADE"), nullable=False)

    def __init__(self, id_relatorio, data_fiscalizacao, hora_inicio, hora_fim, data_escrita, registro, art, possui_vetzoo, lavratura_igual, gera_tcpj, gera_tcpf, gera_ai_art, gera_ai_registro, gera_ai_comerciovacina, gera_ai_outros, uuid_form):
        self.id_relatorio = id_relatorio
        self.data_fiscalizacao = data_fiscalizacao
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.data_escrita = data_escrita
        self.registro = registro
        self.art = art
        self.possui_vetzoo = possui_vetzoo
        self.lavratura_igual = lavratura_igual
        self.gera_tcpj = gera_tcpj
        self.gera_tcpf = gera_tcpf
        self.gera_ai_art = gera_ai_art

# Gerando dados aleatórios para DadosFiscalizacao

def gerar_dados_fiscalizacao(session):
    for i in range(15):
        id_relatorio = f"relatorio_{i + 1}"
        data_fiscalizacao = datetime.now().date()
        hora_inicio = datetime.now() + timedelta(hours=random.randint(-5, 0))
        hora_fim = hora_inicio + timedelta(hours=random.randint(1, 5))
        data_escrita = datetime.now().strftime("%Y-%m-%d")
        registro = random.choice([True, False])
        art = f"ART-{random.randint(1000, 9999)}"
        possui_vetzoo = random.choice([True, False])
        lavratura_igual = random.choice([True, False])
        gera_tcpj = random.choice([True, False])
        gera_tcpf = random.choice([True, False])
        gera_ai_art = random.choice([True, False])
        gera_ai_registro = random.choice([True, False])
        gera_ai_comerciovacina = random.choice([True, False])
        gera_ai_outros = random.choice([True, False])
        uuid_form = f"-{random.randint(1000, 9999)}"


class FiscaisAtv(Base):
    __tablename__ = "id_fiscais_atv"
    id_fiscais_atv: Mapped[int] = mapped_column(Integer, Sequence('id_fiscais_atv_seq'), primary_key=True)
    id_relatorio: Mapped[str] = mapped_column(ForeignKey("dados_fiscalizacao.id_relatorio", ondelete="CASCADE"), nullable=False)
    matricula: Mapped[str] = mapped_column(nullable=False)
    nome: Mapped[str] = mapped_column(nullable=False)
    cargo: Mapped[str] = mapped_column(nullable=False)
    img_assinatura: Mapped[str] = mapped_column(nullable=False)

    def __init__(self, id_relatorio, matricula, nome, cargo, img_assinatura):
        self.id_relatorio = id_relatorio
        self.matricula = matricula
        self.nome = nome
        self.cargo = cargo
        self.img_assinatura = img_assinatura

#Gerando dados aleatórios para FiscaisAtv

def gerar_dados_fiscais_atv(session):
    for i in range(15):
        id_relatorio = f"relatorio_{random.randint(1, 15)}"  # Assume que existem dados na tabela de fiscalizações
        matricula = f"matricula_{random.randint(1000, 9999)}"
        nome = f"Fiscal {i + 1}"
        cargo = random.choice(["Fiscal", "Assistente", "Supervisor"])
        img_assinatura = f"assinatura_{random.randint(1, 10)}.png"  # Simulando a assinatura como um arquivo de imagem

        fiscal = FiscaisAtv(
            id_relatorio=id_relatorio,
            matricula=matricula,
            nome=nome,
            cargo=cargo,
            img_assinatura=img_assinatura
        )
        session.add(fiscal)


class Estabelecimento(Base):
    __tablename__ = "estabelecimentos"
    id_estabelecimento: Mapped[int] = mapped_column(Integer, Sequence("id_estabelecimento"), primary_key=True)
    id_relatorio: Mapped[str] = mapped_column(ForeignKey("dados_fiscalizacao.id_relatorio", ondelete="CASCADE"), nullable=False)
    est_crmv: Mapped[str] = mapped_column(nullable=False)
    est_razsoc: Mapped[str] = mapped_column(nullable=False)
    est_cpf_cnpj: Mapped[str] = mapped_column(nullable=False)
    est_local: Mapped[str] = mapped_column(nullable=False)
    est_bairro: Mapped[str] = mapped_column(nullable=False)
    est_cidade: Mapped[str] = mapped_column(nullable=False)
    est_uf: Mapped[str] = mapped_column(nullable=False)
    est_cep: Mapped[str] = mapped_column(nullable=False)
    contato_email: Mapped[str] = mapped_column(nullable=False)
    contato_telcel: Mapped[str] = mapped_column(nullable=False)
    latitude: Mapped[str] = mapped_column(nullable=False)
    longitude: Mapped[str] = mapped_column(nullable=False)

    def __init__(self, id_relatorio, est_crmv, est_razsoc, est_cpf_cnpj, est_local, est_bairro, est_cidade, est_uf, est_cep, contato_email, contato_telcel, latitude, longitude):
        self.id_relatorio = id_relatorio
        self.est_crmv = est_crmv
        self.est_razsoc = est_razsoc
        self.est_cpf_cnpj = est_cpf_cnpj
        self.est_local = est_local
        self.est_bairro = est_bairro
        self.est_cidade = est_cidade
        self.est_uf = est_uf
        self.est_cep = est_cep
        self.contato_email = contato_email
        self.contato_telcel = contato_telcel
        self.latitude = latitude
        self.longitude = longitude

#Gerando dados aleatórios para Estabelecimento

def gerar_dados_estabelecimento(session):
    for i in range(15):
        id_relatorio = f"relatorio_{random.randint(1, 15)}"  # Assume que existem dados na tabela de fiscalizações
        est_crmv = f"CRMV-{random.randint(1000, 9999)}"
        est_razsoc = f"Razão Social {i + 1}"
        est_cpf_cnpj = f"{random.randint(10000000000, 99999999999)}"  # Simulando CPF ou CNPJ
        est_local = f"Local {i + 1}"
        est_bairro = f"Bairro {random.randint(1, 10)}"
        est_cidade = f"Cidade {random.randint(1, 10)}"
        est_uf = random.choice(["SP", "RJ", "MG", "RS", "PR"])  # Estados
        est_cep = f"{random.randint(10000, 99999)}-{random.randint(100, 999)}"
        contato_email = f"contato{random.randint(1, 15)}@exemplo.com"
        contato_telcel = f"(11) 9{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"
        latitude = f"{random.uniform(-23.0, -22.0)}"  # Simulando latitude
        longitude = f"{random.uniform(-46.0, -45.0)}"  # Simulando longitude

        estabelecimento = Estabelecimento(
            id_relatorio=id_relatorio,
            est_crmv=est_crmv,
            est_razsoc=est_razsoc,
            est_cpf_cnpj=est_cpf_cnpj,
            est_local=est_local,
            est_bairro=est_bairro,
            est_cidade=est_cidade,
            est_uf=est_uf,
            est_cep=est_cep,
            contato_email=contato_email,
            contato_telcel=contato_telcel,
            latitude=latitude,
            longitude=longitude
        )

        session.add(estabelecimento)

class DadosLavraturas(Base):
    __tablename__ = "dados_lavraturas"
    id_lavratura: Mapped[int] = mapped_column(Integer, Sequence("id_lavratura"), primary_key=True)
    id_relatorio: Mapped[str] = mapped_column(ForeignKey("dados_fiscalizacao.id_relatorio", ondelete="CASCADE"), nullable=False)
    cep: Mapped[str] = mapped_column(nullable=False)
    logradouro: Mapped[str] = mapped_column(nullable=False)
    bairro: Mapped[str] = mapped_column(nullable=False)
    cidade: Mapped[str] = mapped_column(nullable=False)
    uf: Mapped[str] = mapped_column(nullable=False)
    
    def __init__(self, id_relatorio, cep, logradouro, bairro, cidade, uf):
        self.id_relatorio = id_relatorio
        self.cep = cep
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf

#Gerando dados aleatórios para DadosLavraturas

def gerar_dados_lavraturas(session):
    for i in range(15):
        id_relatorio = f"relatorio_{random.randint(1, 15)}"  # Assume que existem dados na tabela de fiscalizações
        cep = f"{random.randint(10000, 99999)}-{random.randint(100, 999)}"
        logradouro = f"Logradouro {i + 1}"
        bairro = f"Bairro {random.randint(1, 10)}"
        cidade = f"Cidade {random.randint(1, 10)}"
        uf = random.choice(["SP", "RJ", "MG", "RS", "PR"])  # Estados

        lavratura = DadosLavraturas(
            id_relatorio=id_relatorio,
            cep=cep,
            logradouro=logradouro,
            bairro=bairro,
            cidade=cidade,
            uf=uf
        )

        session.add(lavratura)


# Configuração do banco de dados
engine = create_engine("postgresql://elom:123456@192.168.1.159/alchemy", echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


# Commit e fechamento da sessão
session.commit()
session.close()
