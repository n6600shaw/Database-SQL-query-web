#!e:/ProgramData/Anaconda3/python.exe

import mysql.connector
import cgi

form=cgi.FieldStorage()


mydb= mysql.connector.connect(host="localhost",user= "proj",passwd="proj",database="SupplyDB",use_pure=True)
mycursor= mydb.cursor()


print("Content-type: text/html")
print("")
if ('color' not in form) or ('address' not in form):
    print('<h2>Error</h2>')
    print('<p>please enter color and address</p>')
    print('<a href="http://localhost:80/xl0471.html">Go back</a> ')

else: 
    print('<table align="center" border><tr><th>pname</th></tr>') 
    color = form['color'].value 
    address = form['address'].value 

    sql = "select p1.pname from parts p1 where p1.color='"+color+"' and not exists (select suppliers.sid from suppliers where suppliers.address='" +address + "' and suppliers.sid NOT IN (select c2.sid from catalog c2 where c2.pid=p1.pid))"
    mycursor.execute(sql) 
    myresult = mycursor.fetchall() 
    for x in myresult: 
        print('<tr><td>'+str(x[0])+'</td></tr>') 
    print('</table><br>')
    print('<div style="text-align:center"><a  href="http://localhost:80/xl0471.html">Go back</a></div> ')
