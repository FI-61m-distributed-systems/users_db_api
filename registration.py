import psycopg2
import hashlib

def get_login():
    login= raw_input("login ")
    return login
def get_password():
    password = raw_input("password ")
    h = hashlib.md5(password)
    p = h.hexdigest()
    return p
def get_email():
    email= raw_input("email ")
    return email 
def reg(login, p, email):
    try:
    
        connect = psycopg2.connect(database='Game_Webmoney', user='postgres', host='localhost', password='medvedka123',port = '5433')
        cursor = connect.cursor()

    except:
        print("no db")

    try:
    
        cursor.execute(
        """INSERT INTO account  ( id,login, password, email, money) VALUES(default, %s , %s, %s,default );""",
        (login, p, email))
        connect.commit()

    except psycopg2.Error:
        try: 
        
            connect.rollback()
            print "Your data is not correct"
            connect.close()

        except:
            connect.close()        
            print ("Your data is not written")
        
    connect.close()
    
   
reg(get_login(),get_password(),get_email())