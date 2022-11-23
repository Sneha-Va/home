import mysql.connector
from datetime import datetime
mydb=mysql.connector.connect(host='localhost',user='root',password='',database='homeautomationdb')
mycursor = mydb.cursor()
while True:
    print("select an option from the menu")
    print('1 insert')
    print('2 view')
    print('3 search')
    print('4 exit')
    choice=int(input("enter the option:"))
    if(choice==1):
        print("insert details")
        temprature=input('enter tempreature:')
        hummidity=input("enter hummidity:")
        moisture=input('enter moisture:')
        date=input("enter date:")
        sql='INSERT INTO `sensorvalue`(`temprature`, `hummidity`, `moisture`, `date`) VALUES (%s,%s,%s,now())'
        data=(temprature,hummidity,moisture)
        mycursor.execute(sql,data)
        mydb.commit()
        print("sucess fully inserted")
    if(choice==2):
        print("view details")
        sql='SELECT * FROM `sensorvalue`'
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
    if(choice==3):
        print(" search details")
        empcode=input("enter date:")
        sql='SELECT `id`, `temprature`, `hummidity`, `moisture`, `date` FROM `sensorvalue` WHERE `date`='+date
        mycursor.execute(sql)
        result=mycursor.fetchall()
        print(result)
    if(choice==4):
        print("exit")
        break;
    
        
            
        