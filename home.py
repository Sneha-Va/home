import mysql.connector
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
        sql='INSERT INTO `sensorvalue`(` `temprature`, `hummidity`, `moisture`, `date`) VALUES (%s,%s,%s,%s)'
        data=(temprature,hummidity,moisture,date)
        mycursor.execute(sql,data)
        mydb.commit()
        print("view employee")
    if(choice==2):
        print("view details")
    if(choice==3):
        print(" search details")
    if(choice==4):
        print("exit")
        break;
    
        
            
        