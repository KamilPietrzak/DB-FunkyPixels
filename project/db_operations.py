from os import getenv
from exceptions import ConnectOperationalError, ConnectSomthingWentWrong, ConnectSuccess
import psycopg2

def connect():
    try:
      connect=psycopg2.connect(host=getenv('HOST'), port=getenv('PORT'), user=getenv('USER'), password=getenv('PASSWORD'), dbname="Test")
    except psycopg2.OperationalError:
        raise ConnectOperationalError()
    except Exception as error:
        raise ConnectSomthingWentWrong(error)
    else:
        raise ConnectSuccess(connect)

class OperationsDataBase:
    def test():
        try:
            connect()
        except ConnectOperationalError as e:
            print(e.message)
        except ConnectSomthingWentWrong as e:
            print(e.message)
        except ConnectSuccess as e:
            cur=e.connect.cursor()
            cur.execute("SELECT * FROM test")
            cur.fetchone()
            for record in cur:
                print(record)