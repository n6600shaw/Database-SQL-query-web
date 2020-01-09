#!e:/ProgramData/Anaconda3/python.exe

import mysql.connector
import cgi

form=cgi.FieldStorage()


mydb= mysql.connector.connect(host="localhost",user= "proj",passwd="proj",database="SupplyDB",use_pure=True)
mycursor= mydb.cursor()
info=form.getlist('supplierinfo')

print("Content-type: text/html")
print("")


if ('pname' not in form) or len(info)==0:
    print('<h2>Error</h2>')
    print('<p>please enter a part name, or you need to check at least one supplier\' info</p>')
    print('<a href="http://localhost:80/xl0471.html">Go back</a> ')

else: 
    info=form.getlist('supplierinfo')
    table='<table align="center" border><tr>'
    for field in info:
        table=table+'<th>'+field+'</th>'
    table=table+'</tr>'
    print(table) 
    pname = form['pname'].value 
    sql="select "
    
    for field in info:
        if(field=='cost'):
            sql=sql+"catalog."+field+","
        else:
            sql=sql+"suppliers."+field+","
    sql = sql[:-1]
    sql=sql+" from catalog, parts, suppliers where parts.pname='"+pname+"' and catalog.pid=parts.pid and catalog.sid=suppliers.sid"
        
    mycursor.execute(sql) 
    myresult = mycursor.fetchall() 
    for x in myresult: 
        row='<tr>'
        for field in x:
            row=row+'<td>'+str(field)+'</td>'
        row=row+'</tr>'
        print(row) 
    print('</table><br>')
    print('<div style="text-align:center"><a  href="http://localhost:80/xl0471.html">Go back</a></div> ')
