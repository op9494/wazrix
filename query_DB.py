import sqlite3
conn = sqlite3.connect('wz.db')
print ("Opened database successfully")

#To add table
def add_table_to_db():
    conn.execute('''CREATE TABLE NEWCOINDETAIL(ID INTEGER PRIMARY KEY  AUTOINCREMENT   NOT NULL ,
         NEW_COIN_DETAIL INT    NOT NULL);''')
    print("added new table")    

def close_connection():
    conn.close()
    print("DB Connection Closed")
#To add row

def add_row_to_db():
    conn.execute("INSERT INTO NEWCOINDETAIL (NEW_COIN_DETAIL) VALUES (72)");
    conn.commit()
    print("added new row")
    

#To update value
def Update_row_in_table_NEWCOINDETAIL(value):
    query=f"UPDATE NEWCOINDETAIL set NEW_COIN_DETAIL = {value}  where ID = 1"
    conn.execute(query)
    conn.commit()
    print("Update value succefull")
Update_row_in_table_NEWCOINDETAIL(71)
    
#To delete
def delete_row_in_table():
    conn.execute("DELETE from NEWCOINDETAIL where ID = 2;")
    conn.commit()
    print("Value deleted")
    
    
def get_past_value():
    print("Getting past value....")
    cursor=conn.execute("SELECT NEW_COIN_DETAIL from NEWCOINDETAIL where ID=1")
    for row in cursor:
       return row[0]
    
