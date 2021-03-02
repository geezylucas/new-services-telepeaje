import cx_Oracle


class ConnOracle(object):

    def __init__(self, server=str, port=int, service_name=str, user=str, password=str):
        self.__server = server
        self.__port = port
        self.__service_name = service_name
        self.__user = user
        self.__password = password
        self.__conn = None

    def open_connection(self):
        print("open oracle")
        dsn_tns = cx_Oracle.makedsn(
            self.__server, self.__port, service_name=self.__service_name)
        try:
            self.__conn = cx_Oracle.connect(
                user=self.__user, password=self.__password, dsn=dsn_tns)
        except cx_Oracle.Error as err:
            print(err)

    def execute_query(self, query=str):
        try:
            cursor = self.__conn.cursor()
            return cursor.execute(query)
        except cx_Oracle.Error as err:
            print(err)

    def close_connection(self):
        print("close oracle")
        self.__conn.close()
