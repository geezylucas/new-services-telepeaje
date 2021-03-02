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
    # open connections
    oracle_extract.open_connection()
    mssql_extract.open_connection()
    mssql_insert.open_connection()

    # get last transaction in sql server
    last_transaction = mssql_extract.get_last_row()

    start = None
    end = None
    if last_transaction is None:
        start = datetime.datetime(2020, 10, 22)
        end = datetime.datetime(2020, 10, 23)
    else:
        minutes = 5
        minutes_subtract = datetime.timedelta(minutes=minutes)

        start_str = f'{last_transaction[0]} {last_transaction[1]}'
        start = datetime.datetime.strptime(
            start_str, '%Y-%m-%d %H:%M:%S') - minutes_subtract
        end = datetime.datetime.now()

    # get transactions
    transactions = oracle_extract.get_transactions(start, end)

    # insert transactions
    mssql_insert.insert_transactions(transactions)

    # close connections
    oracle_extract.close_connection()
    mssql_extract.close_connection()
    mssql_insert.close_connection()
