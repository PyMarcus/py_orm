from conf import create_session
from models.__all_models import *


def insert_aditivo_nutritivo() -> None:
    print("Cadastrando aditivo nutritivo")
    an: AditivoNutritivo = AditivoNutritivo(nome="Agua", formula_quimica="H2O")
    with create_session() as session:
        session.add(an)
        session.commit()
    print(f"Aditivo nutritivo {an.id} cadastrado em {an.data_criacao}.")


def insert_sabor() -> None:
    sabor: Sabor = Sabor(nome="Insípido")
    with create_session() as session:
        session.add(sabor)
        session.commit()


def insert_tipo_embalagem() -> None:
    print("Inserindo tipo embalagem")
    embalagem: TipoEmbalagem = TipoEmbalagem(nome="Tensão superficial")
    with create_session() as session:
        session.add(embalagem)
        session.commit()


def insert_tipo_picole() -> None:
    print("Inserindo tipo picole")
    picole: TipoPicole = TipoPicole(nome="Aguado")
    with create_session() as session:
        session.add(picole)
        session.commit()


def insert_ingrediente() -> None:
    print("Inserindo ingredientes")
    ingrediente: Ingrediente = Ingrediente(nome="Água com gás")
    with create_session() as session:
        session.add(ingrediente)
        session.commit()


def insert_conservantes() -> None:
    print("Inserindo conservantes")
    conservante: Conservante = Conservante(nome="Hidrogênio", descricao="Composto de baixa massa atômica")
    with create_session() as session:
        session.add(conservante)
        session.commit()


def insert_revendedor() -> None:
    print("Inserindo revendedor")
    revendedor: Revendedor = Revendedor(nome="Copasa", contato="1111-1111", razao_social="Copasa e Cia")
    with create_session() as session:
        session.add(revendedor)
        session.commit()


if __name__ == '__main__':
    #insert_aditivo_nutritivo()
    #insert_sabor()
    insert_revendedor()
    insert_tipo_embalagem()
    insert_conservantes()
    insert_ingrediente()
    insert_tipo_picole()
