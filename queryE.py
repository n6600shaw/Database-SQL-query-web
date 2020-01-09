#!e:/ProgramData/Anaconda3/python.exe

import mysql.connector
import cgi

form=cgi.FieldStorage()


mydb= mysql.connector.connect(host="localhost",user= "proj",passwd="proj",database="SupplyDB",use_pure=True)
mycursor= mydb.cursor()


print("Content-type: text/html")
print("")
if 'address' not in form:
    print('<h2>Error</h2>')
    print('<p>please enter an address</p>')
    print('<a href="http://localhost:80/xl0471.html">Go back</a> ')

else: 
    print('<table align="center" border><tr><th>sid</th><th>sname</th></tr>') 
    address = form['address'].value 
    sql = "select suppliers.sid, suppliers.sname from suppliers where suppliers.address='"+address+"' and suppliers.sid NOT IN (select catalog.sid from catalog)"
    mycursor.execute(sql) 
    myresult = mycursor.fetchall() 
    for x in myresult: 
        print('<tr><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td></tr>') 
    print('</table><br>')
    print('<div style="text-align:center"><a  href="http://localhost:80/xl0471.html">Go back</a></div> ')
