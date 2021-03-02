import pyodbc


class ConnMSSQLServer(object):

    def __init__(self, server, database, user, password):
        self.__server = server
        self.__database = database
        self.__user = user
        self.__password = password
        self.__conn = None

    def open_connection(self):
        print("open sql")
        self.__conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                                     f'Server={self.__server};'
                                     f'Database={self.__database};'
                                     f'UID={self.__user};'
                                     f'PWD={self.__password};')

    def execute_query(self, query):
        try:
            cursor = self.__conn.cursor()
            return cursor.execute(query)
        except pyodbc.Error as err:
            print(err)

    def insert_many(self, query, params):
        cursor = self.__conn.cursor()
        try:
            cursor.fast_executemany = True
            cursor.executemany(query, params)
            cursor.commit()
        except pyodbc.Error as err:
            print(err)

    def close_connection(self):
        print("close sql")
        self.__conn.close()
