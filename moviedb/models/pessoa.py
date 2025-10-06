from typing import Text

from sqlalchemy import Column, Uuid, String, Integer, DECIMAL, Boolean, ForeignKey
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import relationship

from moviedb.models.mixins import BasicRepositoryMixin

from moviedb import db

class Sexo(db.Model, BasicRepositoryMixin):
    __tablename__ = "sexo"
    id = Column(Uuid(as_uuid=True), primary_key=True, default=Uuid.uuid4)
    nome = Column(String(100), nullable=False)

    pessoas = relationship("pessoa", back_populates="sexo")

class Pessoa(db.Model, BasicRepositoryMixin):
    __tablename__ = "pessoa"
    id = Column(Uuid(as_uuid=True), primary_key=True, default=Uuid.uuid4)
    nome = Column(String(100), nullable=False)
    nacionalidade = Column(String(255), nullable=False)
    dataNascimento = Column(DATETIME, nullable=False)
    biografia = Column(String(255), nullable=False)
    foto_base64 = Column(Text, nullable=True, default=None)
    idSexo = Column(Integer, ForeignKey("sexo.id"))

    sexo = relationship("sexo", back_populates="pessoas")
    participacoes = relationship("participacao", back_populates="pessoa")

class Ator(db.Model, BasicRepositoryMixin):
    __tablename__ = "ator"
    idAtor = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    nomeArtistico = Column(String(150),primary_key=True, default=Uuid.uuid4)

    atuacoes = relationship("atuacao", back_populates="ator")

class FuncaoTecnica(db.Model, BasicRepositoryMixin):
    __tablename__ = "funcaoTecnica"
    id = Column(Uuid(as_uuid=True), primary_key=True, default=Uuid.uuid4)
    nome = Column(String(100), nullable=False)
    categoria = Column(String(100), nullable=False)
    descricao = Column(String(255), nullable=False)
    ativa = Column(Boolean, default=False, nullable=False)

class Atuacao(db.Model, BasicRepositoryMixin):
    __tablename__ = "atuacao"
    id = Column(Uuid(as_uuid=True), primary_key=True, default=Uuid.uuid4)
    papel = Column(String(100), nullable=False)
    protagonista = Column(Boolean, default=False, nullable=False)
    creditado = Column(Boolean, default=False, nullable=False)
    cache = Column(DECIMAL(precision=10, scale=2),nullable=False)
    tempoTela = Column(Integer, nullable=False)
    idAtor = Column(Integer, ForeignKey("ator.id"), nullable=False)
    idFilme = Column(Integer, ForeignKey("filme.id"), nullable=False)

    ator = relationship("ator", back_populates="atuacoes")
    filme = relationship("filme", back_populates="atuacoes")

class Participacao(db.Model, BasicRepositoryMixin):
    __tablename__ = "participacao"
    id = Column(Uuid(as_uuid=True), primary_key=True, default=Uuid.uuid4)
    inicioTrabalho = Column(DATETIME, nullable=False)
    fimTranalho = Column(DATETIME, nullable=False)
    remuneracao = Column(DECIMAL(precision=10, scale=2), nullable=False)
    observacoes = Column(String(100), nullable=False)
    idPessoa = Column(Integer, ForeignKey("pessoa.id"), nullable=False)
    idFilme = Column(Integer, ForeignKey("filme.id"), nullable=False)
    idFuncaoTecnica = Column(Integer, ForeignKey("funcaotecnica.id"), nullable=False)

    pessoa = relationship("Pessoa", back_populates="participacoes")
    filme = relationship("Filme", back_populates="participacoes")
    funcao = relationship("FuncaoTecnica", back_populates="participacoes")






