import uuid

from sqlalchemy import Column, Uuid, String, Integer, DECIMAL, Boolean
from sqlalchemy.dialects.mysql import DATETIME

from moviedb.models.mixins import BasicRepositoryMixin

from moviedb import db

class Filme(db.Model, BasicRepositoryMixin):
    __tablename__ = "filmes"
    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    titulo_original = Column(String(255), nullable=False)
    titulo_nacional = Column(String(255), nullable=False)
    ano_lancamento = Column(Integer, nullable=False)
    duracao = Column(Integer, nullable=False)
    sinopse = Column(String(255), nullable=False)
    orcamento = Column(DECIMAL(precision=10, scale=2),nullable=False)
    faturamentoLancamento = Column(DECIMAL(precision=10, scale=2),nullable=False)
    posterPrincipal = Column(String, nullable=False)
    linkTrailer = Column(String(255), nullable=False)

class Genero(db.Model, BasicRepositoryMixin):
    __tablename__ = "genero"
    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(255), nullable=False)
    ativo = Column(Boolean, default=False, nullable=False)


class FilmeGenero(db.Model, BasicRepositoryMixin):
    __tablename__ = "filmeGenero"
    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    generoPrincipal = Column(Boolean,  nullable=False)


class Avalicoes(db.Model, BasicRepositoryMixin):
    __tablename__ = "avaliacoes"
    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nota = Column(DECIMAL(precision=10, scale=2),nullable=False)
    dataAvaliacao = Column(DATETIME)
    comentario = Column(String(255))
    recomenda = Column(Boolean, default=False, nullable=False)