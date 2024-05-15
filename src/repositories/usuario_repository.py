from src.configs.databse_config import get_db_connection


def consultar_por_email(email):
    database_connection = get_db_connection()
    cursor = database_connection.cursor()
    cursor.execute("SELECT id, nome, email, senha FROM usuario WHERE email like %s", (email,))
    resultado = cursor.fetchone()

    if resultado is None:
        return None

    usuario = {
        "id": resultado[0],
        "nome": resultado[1],
        "email": resultado[2],
        "senha": resultado[3],
    }
    cursor.close()
    database_connection.close()
    return usuario


def inserir(usuario):
    database_connection = get_db_connection()
    cursor = database_connection.cursor()
    sql = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)"
    parametros = (usuario.get('nome'), usuario.get('email'), usuario.get('senha'))
    cursor.execute(sql, parametros)
    database_connection.commit()
    cursor.close()
    database_connection.close()


def deletar_por_email(email):
    database_connection = get_db_connection()
    cursor = database_connection.cursor()
    sql = "DELETE FROM usuario WHERE email like %s"
    parametros = (email,)
    cursor.execute(sql, parametros)
    database_connection.commit()
    cursor.close()
    database_connection.close()


def atualizar(usuario):
    database_connection = get_db_connection()
    cursor = database_connection.cursor()
    sql = "UPDATE usuario SET nome=%s, email=%s, senha=%s WHERE email like %s"
    parametros = (usuario.get('nome'), usuario.get('email'), usuario.get('senha'), usuario.get('email'))
    cursor.execute(sql, parametros)
    database_connection.commit()
    cursor.close()
    database_connection.close()
