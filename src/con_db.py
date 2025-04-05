import pymysql
import pandas as pd
class ConnectDB:
    def __init__(self):
        self.con=pymysql.connect(host='localhost',user='root',password='password',database='database name')#enter your password and database name
    def insert_records(self):
        self.cursor=self.con.cursor()
        #inserting records
        df=pd.read_csv('archive/doctors.csv')
        for index, row in df.iterrows():
            query = "INSERT INTO doctor (did, dname, d_experience, dspecialist, dcontactno) VALUES (%s, %s, %s, %s, %s)"
            values = (int(row["Doctor ID"]), row["Name"], int(row["Experience"]), row["Specialization"], row["Contact No"])
            self.cursor.execute(query, values)
        print('rows interted successfully')

        self.con.commit()
        self.cursor.close()
        self.con.close()
    def search(self,disease):
        self.cursor=self.con.cursor()
        self.disease=disease
        print(self.disease)
        fquery = "SELECT dname, dcontactno FROM doctor WHERE dspecialist = %s"
        self.cursor.execute(fquery, (self.disease,))

        data=self.cursor.fetchall()
        return data


con=ConnectDB()
con.search('allergy')
