import pandas as pd
from dotenv import load_dotenv
from os import getenv
import psycopg2
load_dotenv()

#build a dataframe
class TSQL:
    __user = getenv("USER")
    __password= getenv("PASSWORD")
    __server= getenv("SERVER")
    
    #used for to_sql function
    __sql_url = 'postgresql://kmswoiej:rM93CPw2SSm90qPata_-UdC9G8T49lEB@batyr.db.elephantsql.com/kmswoiej'
    #used for querying
    __TS_con= psycopg2.connect(
        dbname = __user,
        user= __user,
        password = __password,
        host = __server
        )
    __cur=__TS_con.cursor()

    def create_dataframe(self):
        self.fpath = r'C:\Users\Logan\Documents\GitHub\bootcamp\week_5\homework_5_1.py\titanic.csv'
        #Grabs the data from the titanic file and cleans the columns etc

        self.df = pd.read_csv(self.fpath)
        self.df.columns = self.df.columns.str.lower()
        self.df.columns = self.df.columns.str.strip()
        self.df.columns = self.df.columns.map(lambda x : x.replace('.', '_').replace(' ', '_'))
          

    def update_data_sql(self):
        #Used to take my DF and send into database
        self.df.to_sql('titanic',con=self.__sql_url, if_exists='replace')

    def query_db(self, sql_filepath: str):
        start = self.create_file(sql_filepath)
        queries = start.split(';')
        for query in queries:
            try:
                print(query)
                self.__cur.execute(query)
                self.__TS_con.commit()
                print(self.__cur.fetchall())
            except psycopg2.ProgrammingError as msg:
                print(f'Error: {msg}')
          
    @staticmethod
    def create_file(fpath: str):
        """ Open a file by filepath and apply it to an SQL table """
        with open(fpath, 'r') as f:
            sql_file = f.read()
            f.close()
        return sql_file

  
titan = TSQL()
titan.create_dataframe()
titan.update_data_sql()
titan.query_db(r"C:\Users\Logan\Documents\GitHub\bootcamp\week_5\homework_5_1.py\titanic.sql")