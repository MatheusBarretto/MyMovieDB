from typing import Text

from sqlalchemy import Column, Uuid, String, Integer, DECIMAL, Boolean
from sqlalchemy.dialects.mysql import DATETIME

from moviedb.models.mixins import BasicRepositoryMixin

from moviedb import db

class Pessoa(db.Model, BasicRepositoryMixin):
    __tablename__ = "pessoa"
    id = Column(Uuid(as_uuid=True), primary_key=True, default=Uuid.uuid4)
    nome = Column(String(100), nullable=False)
    nacionalidade = Column(String(255), nullable=False)
    dataNascimento = Column(DATETIME, nullable=False)
    biografia = Column(String(255), nullable=False)
    foto_base64 = Column(Text, nullable=True, default=None)

class Sexo(db.Model, BasicRepositoryMixin):
    __tablename__ = "sexo"
    id = Column(Uuid(as_uuid=True), primary_key=True, default=Uuid.uuid4)
    nome = Column(String(100), nullable=False)

class Ator(db.Model, BasicRepositoryMixin):
    __tablename__ = "ator"
    nomeArtistico = Column(String(150),primary_key=True, default=Uuid.uuid4)

class Atuacao(db.Model, BasicRepositoryMixin):
    __tablename__ = "atuacao"
    id = Column(Uuid(as_uuid=True), primary_key=True, default=Uuid.uuid4)
    papel = Column(String(100), nullable=False)
    protagonista = Column(Boolean, default=False, nullable=False)
    creditado = Column(Boolean, default=False, nullable=False)
    cache = Column(DECIMAL(precision=10, scale=2),nullable=False)
    tempoTela = Column(Integer, nullable=False)

class FuncaoTecnica(db.Model, BasicRepositoryMixin):
    __tablename__ = "funcaoTecnica"
    id = Column(Uuid(as_uuid=True), primary_key=True, default=Uuid.uuid4)
    nome = Column(String(100), nullable=False)
    categoria = Column(String(100), nullable=False)
    descricao = Column(String(255), nullable=False)
    ativa = Column(Boolean, default=False, nullable=False)

class Participacao(db.Model, BasicRepositoryMixin):
    __tablename__ = "participacao"
    id = Column(Uuid(as_uuid=True), primary_key=True, default=Uuid.uuid4)
    inicioTrabalho = Column(DATETIME, nullable=False)
    fimTranalho = Column(DATETIME, nullable=False)
    remuneracao = Column(DECIMAL(precision=10, scale=2), nullable=False)
    observacoes = Column(String(100), nullable=False)






