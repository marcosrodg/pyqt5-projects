import pymysql


def conecta():
    try:
        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='poobanck',
        )
        return conexao
    except Exception:
        return False


