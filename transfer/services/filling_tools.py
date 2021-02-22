import datetime
import transfer.data.connoracle.extract_data as oracle_extract_data


oracle_extract = oracle_extract_data.ExtractData(
    '192.168.0.221', 1521, 'GEAPROD', 'GEAINT', 'GEAINT')


def fill_db_prosis():
    # get transactions
    start = datetime.datetime(2020, 10, 22)
    end = datetime.datetime(2020, 12, 4)
    transactions = oracle_extract.get_transactions(start, end)

    for row in transactions:
        print(row)
