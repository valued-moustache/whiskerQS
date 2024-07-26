import pyodbc
import os

def get_sql_connector():
    server=os.environ["SQLSERVER"]
    port = os.environ["SQLPORT"]
    user = os.environ["SQLUSER"]
    password = os.environ["SQLSEC"]
    database = os.environ["SQLDB"]
    connect_string = 'DRIVER={ODBC Driver 18 for SQL Server};' \
                     'SERVER='+server+','+port+';DATABASE='+database+';ENCRYPT=yes;TrustServerCertificate=yes;UID='+user+';PWD='+ password

    i=0
    while i < 100:
        try:
            # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
            cnxn = pyodbc.connect(connect_string, timeout=15)
            break
        except pyodbc.Error:
            i += 1
            if i>5:
                raise ConnectionError("Unable to Make Connection")

    return cnxn
