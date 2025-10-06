import uuid

from sqlalchemy import Column, Uuid, String, Integer, DECIMAL, Boolean, ForeignKey
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import relationship

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

    atuacoes = relationship("atuacao", back_populates="filme")
    participacoes = relationship("participacao", back_populates="filme")
    generos = relationship("filmeGenero", back_populates="filme")
    avaliacoes = relationship("avaliacao", back_populates="filme")

class Genero(db.Model, BasicRepositoryMixin):
    __tablename__ = "genero"
    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(255), nullable=False)
    ativo = Column(Boolean, default=False, nullable=False)

    filmes = relationship("filmeGenero", back_populates="genero")


class FilmeGenero(db.Model, BasicRepositoryMixin):
    __tablename__ = "filmeGenero"
    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    generoPrincipal = Column(Boolean,  nullable=False)
    idFilme = Column(Integer, ForeignKey('filmes.id'), nullable=False)
    idGenero = Column(Integer, ForeignKey('genero.id'), nullable=False)

    filme = relationship("Filme", back_populates="generos")
    genero = relationship("Genero", back_populates="filmes")


class Avalicoes(db.Model, BasicRepositoryMixin):
    __tablename__ = "avaliacoes"
    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nota = Column(DECIMAL(precision=10, scale=2),nullable=False)
    dataAvaliacao = Column(DATETIME)
    comentario = Column(String(255))
    recomenda = Column(Boolean, default=False, nullable=False)
    idFilme = Column(Integer, ForeignKey('filmes.id'), nullable=False)
    idUsuario = Column(Integer, ForeignKey('usuario.id'), nullable=False)

    usuario = relationship("Usuario", back_populates="avaliacoes")
    filme = relationship("Filme", back_populates="avaliacoes")
