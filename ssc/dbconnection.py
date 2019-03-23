import os
import psycopg2
import urllib.parse as urlparse

# from ssc.dbconfig import user, password, database

ON_HEROKU = 'ON_HEROKU' in os.environ


try:
    if (ON_HEROKU):
        print('Connecting to heroku db')
        url = urlparse.urlparse(os.environ['DATABASE_URL'])
        dbname = url.path[1:]
        user = url.username
        password = url.password
        host = url.hostname
        port = url.port

        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
    else:

        connection = psycopg2.connect(
            # user=user,
            # password=password,
            database="ssc")
    cursor = connection.cursor()
except:
    connection = None
    cursor = None



def getAsyncConn():
    if (ON_HEROKU):
        url = urlparse.urlparse(os.environ['DATABASE_URL'])
        dbname = url.path[1:]
        user = url.username
        password = url.password
        host = url.hostname
        port = url.port

        dsn = "dbname="+dbname+" user="+user+" password="+password+" host="+host+" port="+port
        return dsn
    else:
        return 'dbname=ssc'
