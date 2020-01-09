#!e:/ProgramData/Anaconda3/python.exe

import mysql.connector
import cgi

form=cgi.FieldStorage()


mydb= mysql.connector.connect(host="localhost",user= "proj",passwd="proj",database="SupplyDB",use_pure=True)
mycursor= mydb.cursor()


print("Content-type: text/html")
print("")
if 'cost' not in form:
    print('<h2>Error</h2>')
    print('<p>please enter a cost</p>')
    print('<a href="http://localhost:80/xl0471.html">Go back</a> ')

else: 
    print('<table align="center" border><tr><th>sname</th></tr>') 
    cost = form['cost'].value 
    sql = "select DISTINCT suppliers.sname from catalog, suppliers where catalog.cost>="+cost+" and catalog.sid=suppliers.sid"    
    mycursor.execute(sql) 
    myresult = mycursor.fetchall() 
    for x in myresult: 
        print('<tr><td>'+str(x[0])+'</td></tr>') 
    print('</table><br>')
    print('<div style="text-align:center"><a  href="http://localhost:80/xl0471.html">Go back</a></div> ')
