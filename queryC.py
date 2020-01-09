#!e:/ProgramData/Anaconda3/python.exe

import mysql.connector
import cgi

form=cgi.FieldStorage()


mydb= mysql.connector.connect(host="localhost",user= "proj",passwd="proj",database="SupplyDB",use_pure=True)
mycursor= mydb.cursor()


print("Content-type: text/html")
print("")
if 'pid' not in form:
    print('<h2>Error</h2>')
    print('<p>please enter a part name</p>')
    print('<a href="http://localhost:80/xl0471.html">Go back</a> ')

else: 
    print('<table align="center" border><tr><th>sname</th><th>address</th><th>cost</th></tr>') 
    pid = form['pid'].value 
    sql = "select suppliers.sname, suppliers.address, catalog.cost from catalog, suppliers where catalog.sid=suppliers.sid and catalog.cost=((select Max(c2.cost) from catalog c2 where c2.pid='"+pid+"') ) and catalog.pid='"+pid+"'"
    mycursor.execute(sql) 
    myresult = mycursor.fetchall() 
    for x in myresult: 
        print('<tr><td>'+str(x[0])+'</td><td>'+str(x[1])+'</td><td>'+str(x[2])+'</td></tr>') 
    print('</table><br>')
    print('<div style="text-align:center"><a  href="http://localhost:80/xl0471.html">Go back</a></div> ')
