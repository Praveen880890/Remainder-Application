import sqlite3
con=sqlite3.connect("remainder.db")
c=con.cursor()


try:
    c.execute("""create table rem (name text,desc text,date text)""")

except:
    print("..")

try:
    c.execute("""create table email (email text)""")
except:
    pass


def insert(name,desc,date):
    con = sqlite3.connect("remainder.db")
    c = con.cursor()
    st="INSERT INTO rem VALUES (\'"+name+"\',\'"+desc+"\',\'"+date+"\')"
    #print(st)
    c.execute(st)
    con.commit()
    con.close()


def retrive():
    con = sqlite3.connect("remainder.db")
    c = con.cursor()
    c.execute("select * from rem")
    r=c.fetchall()
    con.commit()
    con.close()
    return r


def delete(name):
    con = sqlite3.connect("remainder.db")
    c = con.cursor()
    c.execute(f"delete from rem where name='{name}'")
    con.commit()
    con.close()

def insert_email(email):
    if email=="":
        pass
    else:
        con = sqlite3.connect("remainder.db")
        c = con.cursor()
        st = f"INSERT INTO email VALUES ('{email}')"
        #print(st)
        c.execute(st)
        con.commit()
        con.close()

def retrive_email():
    con = sqlite3.connect("remainder.db")
    c = con.cursor()
    c.execute("select * from email")
    r=c.fetchall()
    con.commit()
    con.close()
    return r
def delete_email(email):
    con = sqlite3.connect("remainder.db")
    c = con.cursor()
    c.execute(f"delete from email where email='{email}'")
    con.commit()
    con.close()
def clear_email():
    con = sqlite3.connect("remainder.db")
    c = con.cursor()
    c.execute("delete from email")
    con.commit()
    con.close()

con.commit()
con.close()

