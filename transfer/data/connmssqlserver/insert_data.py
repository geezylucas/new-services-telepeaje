from transfer.data.connmssqlserver.connection import ConnMSSQLServer


class InsertData(ConnMSSQLServer):

    def __init__(self, server, database, user, password):
        ConnMSSQLServer.__init__(self, server, database, user, password)

    def insert_transactions(self, transactions):
        self.insert_many('{CALL dbo.spInsetarTransaccion(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)}',
                         transactions)
