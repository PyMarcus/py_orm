import typing
import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from sqlalchemy.orm import Mapped
from .model_base import ModelBase
from .revendedor import Revendedor
from .lote import Lote

lotes_nota_fiscal = sa.Table(
    "lotes_nota_fiscal",
    ModelBase.metadata,
    sa.Column("id_nota_fiscal", sa.Integer, sa.ForeignKey("notas_fiscais.id")),
    sa.Column("id_lote", sa.Integer, sa.ForeignKey("lotes.id"))
)

class NotaFiscal(ModelBase):
    __tablename__: str = 'notas_fiscais'
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    valor: float = sa.Column(sa.DECIMAL(8, 2), nullable=False)
    numero_serie: str = sa.Column(sa.String(45), unique=True, nullable=False)
    descricao: str = sa.Column(sa.String(200), nullable=False)
    id_revendedor: int = sa.Column(sa.Integer, sa.ForeignKey('revendedores.id'))
    revendedor: Mapped[typing.Type[typing.Optional[Revendedor]]] = orm.relationship("Revendedor", lazy="joined")
    lotes: Mapped[typing.List[typing.Type[typing.Optional[Lote]]]] = orm.relationship("Lote",
                                                                                      secondary=lotes_nota_fiscal,
                                                                                      backref="lote",
                                                                                      lazy="dynamic")

    def __repr__(self) -> str:
        return f"<NotaFiscal: {self.nome}>"
