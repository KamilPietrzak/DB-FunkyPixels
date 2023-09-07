from os import getenv
from exceptions import ConnectOperationalError, ConnectSomthingWentWrong, ConnectSuccess
import psycopg2

def connect():
    try:
      connect=psycopg2.connect(host=getenv('HOST'), port=getenv('PORT'), user=getenv('USER'), password=getenv('PASSWORD'))
    except psycopg2.OperationalError:
        raise ConnectOperationalError()
    except Exception as error:
        raise ConnectSomthingWentWrong(error)
    else:
        raise ConnectSuccess(connect)

class OperationsDataBase():
    def __init__(self):
        self.cur=None
        self.__run()

    def __connect(self):
        try:
            connect()
        except ConnectOperationalError as e:
            print(e.message)
        except ConnectSomthingWentWrong as e:
            print(e.message)
        except ConnectSuccess as e:
            self.cur=e.connect.cursor()
    
    def __run(self):
        self.__connect()