import typing
import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from model_base import ModelBase
from .sabor import Sabor
from .tipo_embalagem import TipoEmbalagem
from .tipo_picole import TipoPicole
from .ingrediente import Ingrediente
from .conservante import Conservante
from .aditivo_nutritivo import AditivoNutritivo

# picole pode ter varios ingredientes
ingredientes_picole = sa.Table(
    "ingredientes_picole",
    ModelBase.metadata,
    sa.Column("id_picole", sa.Integer, sa.ForeignKey("picoles.id")),
    sa.Column("id_ingredientes", sa.Integer, sa.ForeignKey("ingredientes.id"))
)


# picole pode ter varios conservantes
conservantes_picole = sa.Table(
    "conservantes_picole",
    ModelBase.metadata,
    sa.Column("id_picole", sa.Integer, sa.ForeignKey("picoles.id")),
    sa.Column("id_conservante", sa.Integer, sa.ForeignKey("conservantes.id"))
)

# picole pode ter varios aditivos nutritivos
aditivos_nutritivos_picole = sa.Table(
    "aditivos_nutritivos_picole",
    ModelBase.metadata,
    sa.Column("id_picole", sa.Integer, sa.ForeignKey("picoles.id")),
    sa.Column("id_aditivos_nutritivos", sa.Integer, sa.ForeignKey("aditivos_nutritivos.id"))
)


class Picole(ModelBase):
    __tablename__: str = 'picoles'
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    nome: str = sa.Column(sa.String(45), unique=True, nullable=False)
    preco: float = sa.Column(sa.DECIMAL(8, 2), nullable=False)
    id_sabor: int = sa.Column(sa.Integer, sa.ForeignKey("sabores.id"))
    sabor: Sabor = orm.relationship("Sabor", lazy="joined")

    id_tipo_embalagem: int = sa.Column(sa.Integer, sa.ForeignKey("tipos_embalagens.id"))
    tipo_embalagem: TipoEmbalagem = orm.relationship("TipoEmbalagem", lazy="joined")

    id_tipo_picole: int = sa.Column(sa.Integer, sa.ForeignKey("tipos_picoles.id"))
    tipo_picole: TipoPicole = orm.relationship("TipoPicole", lazy="joined")

    # um picole pode ter varios ingredientes
    ingredientes: typing.List[Ingrediente] = orm.relationship("Ingrediente",
                                                              secondary=ingredientes_picole,
                                                              backref="ingrediente",
                                                              lazy="joined",
                                                              )
    # um picole pode ter conservantes ou nenhum
    conservantes: typing.Optional[typing.List[Conservante]] = orm.relationship("Conservante",
                                                              secondary=conservantes_picole,
                                                              backref="conservante",
                                                              lazy="joined",
                                                              )
    # um picole pode ter varios aditivos nutritivos ou nenhum
    aditivos: typing.Optional[typing.List[AditivoNutritivo]] = orm.relationship("AditivoNutritivo",
                                                                               secondary=aditivos_nutritivos_picole,
                                                                               backref="aditivo",
                                                                               lazy="joined",
                                                                               )

    def __repr__(self) -> str:
        return f"<Picole: {self.nome}>"
