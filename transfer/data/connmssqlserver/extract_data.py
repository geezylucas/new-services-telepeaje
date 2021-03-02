from datetime import datetime, timedelta
from transfer.data.connmssqlserver.connection import ConnMSSQLServer


class ExtractData(ConnMSSQLServer):

    def __init__(self, server, database, user, password):
        ConnMSSQLServer.__init__(self, server, database, user, password)

    def get_last_row(self):
        cursor = self.execute_query(
            'select top (1) Fecha, Hora from Transacciones order by Fecha desc, Hora desc ')
        return cursor.fetchone()
