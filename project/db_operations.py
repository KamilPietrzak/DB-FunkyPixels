from os import getenv
from exceptions import ConnectOperationalError, ConnectSomthingWentWrong, ConnectSucess
import psycopg2

def connect():
    try:
      db=psycopg2.connect(host=getenv('HOST'), port=getenv('PORT'), user=getenv('USER'), password=getenv('PASSWORD'), dbname="Test")
    except psycopg2.OperationalError:
        raise ConnectOperationalError()
    except Exception as error:
        raise ConnectSomthingWentWrong(error)
    else:
        raise ConnectSucess(db)

class OperationDataBase:
    def test():
        try:
            connect()
        except ConnectOperationalError as e:
            print(e.message)
        except ConnectSomthingWentWrong as e:
            print(e.message)
        except ConnectSucess as d:
            cur=d.db.cursor()
            cur.execute("SELECT * FROM test")
            cur.fetchone()
            for record in cur:
                print(record)