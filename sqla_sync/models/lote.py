import sqlalchemy as sa
from datetime import datetime
from model_base import ModelBase
from .tipo_picole import TipoPicole
import sqlalchemy.orm as orm


class Lote(ModelBase):
    __tablename__: str = 'lotes'
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    quantidade: int = sa.Column(sa.Integer, nullable=False)
    id_tipo_picole: int = sa.Column(sa.Integer, sa.ForeignKey('tipos_picoles.id'))
    tipo_picole: TipoPicole = orm.relationship('TipoPicole', lazy='joined')

    def __repr__(self) -> str:
        return f"<Lote: {self.nome}>"
