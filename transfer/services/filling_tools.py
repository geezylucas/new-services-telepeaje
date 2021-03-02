import datetime
import transfer.data.connoracle.extract_data as oracle_extract_data
import transfer.data.connmssqlserver.extract_data as mssql_extract_data
import transfer.data.connmssqlserver.insert_data as mssql_insert_data

oracle_extract = oracle_extract_data.ExtractData(
    '192.168.0.221', 1521, 'GEAPROD', 'GEAINT', 'GEAINT')


mssql_extract = mssql_extract_data.ExtractData(
    'localhost', 'TelepeajeDemo', 'sa', 'LaVacaLoca16')

mssql_insert = mssql_insert_data.InsertData(
    'localhost', 'TelepeajeDemo', 'sa', 'LaVacaLoca16')


def fill_db_prosis():
    # get last transaction in sql server
    last_transaction = mssql_extract.get_last_row()

    start = None
    end = None
    if last_transaction is None:
        start = datetime.datetime(2020, 10, 22)
        end = datetime.datetime(2020, 10, 23)
    else:
        start_str = f'{last_transaction[0]} {last_transaction[1]}'
        start = datetime.datetime.strptime(
            start_str, '%Y-%m-%d %H:%M:%S')
        end = datetime.datetime.now()

    # get transactions
    transactions = oracle_extract.get_transactions(start, end)

    # insert transactions
    mssql_insert.insert_transactions(transactions)
