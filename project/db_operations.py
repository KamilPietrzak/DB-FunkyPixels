from os import getenv
from sys import exit
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
    finally:
        del connect

class OperationsDataBase():
    def __init__(self):
        self.cur=None
        self.__run()

    def __connect(self):
        try:
            connect()
        except ConnectOperationalError as e:
            print(e.message)
            return exit(1)
        except ConnectSomthingWentWrong as e:
            print(e.message)
            return exit(1)
        except ConnectSuccess as e:
            self.cur=e.connect.cursor()
            return
    
    def __run(self):
        self.__connect()