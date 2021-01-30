import mysql.connector
import random

def genrateSAP():
    return "%s:%s:%s:%s" % (
        random.randint(1, 9),
        random.randint(1, 9),
        random.randint(1, 9),
        random.randint(1, 9)
        )

def genrateLoopback():
    return "%s:%s:%s:%s" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
        )

def genrateHostname():
    return "%s:%s:%s:%s" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
        )


def generateMAC():
    return "%02x:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
        )

records = 0
val = input("How many records do you want Enter value: ")
if not val.isnumeric():
    print('Invalid')
elif int(val) > 0:
    records = int(val)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="gautam",
  database="cisco_db"
)

mycursor = mydb.cursor()
for i in range(records):
    sql = """INSERT INTO router_details
            (sapid, loopback, hostname, mac_address,status) 
            VALUES (%s, %s, %s, %s, %s)"""
    val = (genrateSAP(), genrateLoopback(), genrateHostname(),generateMAC(),1)
    mycursor.execute(sql, val)

mydb.commit()
print(records, "record inserted.")