#/usr/local/bin/python3
import psycopg2

class queries:

    @staticmethod
    def insert_logmessage(date, logmessage):
        SQL = "INSERT INTO logmessages(date, logmessage) VALUES ("
        SQL += '\'' + str(date) + '\', '
        SQL += '\'' + str(logmessage) + '\''
        SQL += ');'
        print("SQL: " + SQL)
        return SQL

class db_parser:

    @staticmethod
    def writelog(date, logmessage, sql_session):
        
        cursor = sql_session.cursor()
        cursor.execute(queries.insert_logmessage(date,logmessage))
        sql_session.commit()
        cursor.close()
        

class db:

    def __init__(self, **db_options):

        try:
            self.sql_session = psycopg2.connect(user=db_options.get('user'), password=db_options.get('password'), host=db_options.get('host'), port=db_options.get('port'), database=db_options.get('database'))
            print("Openned new DB connection")
        
        except BaseException as err:
            print("DB ERROR: Something is wrong in connecting to DB: " + str(err.__str__()))
            raise Exception
    
    def writelogtodb(self,date,logmessage):
        try:
            db_parser.writelog(date, logmessage,self.sql_session)
        except:
             return False
        
        return True

    def close_db(self):
        self.sql_session.close()
        print("Db connection closed")
