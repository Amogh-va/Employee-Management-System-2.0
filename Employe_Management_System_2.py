#Employee Management System 2.0
def configureall():
    empno=empnoentry.get()
    name=nameentry.get()
    job=jobentry.get()
    mgr=mgrentry.get()
    hiredate=hiredateentry.get()
    sal=salentry.get()
    comm=commentry.get()
    deptno=deptnoentry.get()

    outputmsg=f"emp- {empno}, {name}, {job}, {mgr}, {hiredate}, {sal}, {comm}, {deptno} is added"
    labeloutput.configure(text=outputmsg)

    mydb=rob.connect(
        host='localhost',
        user='root',
        password='Tiger@123',
        database='project'
    )

    if mydb == None:
        print("Could not Connect")

    else:
        print('Connected')

        sql_query = 'INSERT INTO projemploye(empno,empname,job,mgr,hiredate,sal,comm,deptno) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        values=(empno,name,job,mgr,hiredate,sal,comm,deptno)

        mycursor=mydb.cursor()
        mycursor.execute(sql_query,values)
        mydb.commit()
        mydb.close()

def display():
    mydb = rob.connect(
        host='localhost',
        user = 'root',
        password = 'Tiger@123',
        database = 'project'
    )

    if mydb == None:
        print('Could not connect')

    else:
        print('Connected successfully')

    sql_query = 'SELECT * FROM projemploye;'

    mycursor = mydb.cursor()
    mycursor.execute(sql_query)

    student =mycursor.fetchall()

    if len(student)==0:
        print('Employee not found')
    else:
        print('Employe found:',student)

        for row in treeview.get_children():
            treeview.delete(row)

        for student in student:
            treeview.insert(parent='',index='end',values=student)

def searchempno():
    empno=empnoentry.get()

    mydb=rob.connect(
        host='localhost',
        user='root',
        password='Tiger@123',
        database='project'
    )

    if mydb == None:
        print('Could not connect')

    else:
        print('Connected successfully')

    sql_query = 'SELECT * FROM projemploye WHERE empno=%s;'
    values=[empno]

    mycursor=mydb.cursor()
    mycursor.execute(sql_query,values)

    student=mycursor.fetchall()

    if len(student)==0:
        print('Employee not found')

    else:
        print('Employee found:',student)

        for row in treeview.get_children():
            treeview.delete(row)

        for student in student:
            treeview.insert(parent='',index='end',values=student)

def searchname():
    name=nameentry.get()

    mydb=rob.connect(
        host='localhost',
        user='root',
        password='Tiger@123',
        database='project'
    )

    if mydb == None:
        print('Could not connect')

    else:
        print('Connected successfully')
    
    sql_query = 'SELECT * FROM projemploye WHERE empname LIKE %s;'
    values=[name+'%']

    mycursor=mydb.cursor()
    mycursor.execute(sql_query,values)

    student=mycursor.fetchall()
    if len(student)==0:
        print('Employee not found')

    else:
        print('Employee found:',student)

        for row in treeview.get_children():
            treeview.delete(row)

        for student in student:
            treeview.insert(parent='',index='end',values=student)

def searchjob():
    job=jobentry.get()

    mydb=rob.connect(
        host='localhost',
        user='root',
        password='Tiger@123',
        database='project'
    )

    if mydb == None:
        print('Could not connect')

    else:
        print('Connected successfully')

    sql_query = 'SELECT * FROM projemploye WHERE job = %s;'
    values=[job]

    mycursor=mydb.cursor()
    mycursor.execute(sql_query,values)

    student=mycursor.fetchall()
    if len(student)==0:
        print('Employee not found')

    else:
        print('Employee found:',student)

        for row in treeview.get_children():
            treeview.delete(row)

        for student in student:
            treeview.insert(parent='',index='end',values=student)

def searchsal():
    sal=salentry.get()

    mydb=rob.connect(
        host='localhost',
        user='root',
        password='Tiger@123',
        database='project'
    )

    if mydb == None:
        print('Could not connect')
    
    else:
        print('Connected successfully')

    sql_query = 'SELECT * FROM projemploye WHERE sal = %s;'
    values=[sal]

    mycursor=mydb.cursor()
    mycursor.execute(sql_query,values)

    student=mycursor.fetchall()
    if len(student)==0:
        print('Employee not found')
    
    else:
        print('Employee found:',student)

        for row in treeview.get_children():
            treeview.delete(row)

        for student in student:
            treeview.insert(parent='',index='end',values=student)

def searchdeptno():
    deptno=deptnoentry.get()

    mydb=rob.connect(
        host='localhost',
        user='root',
        password='Tiger@123',
        database='project'
    )

    if mydb == None:
        print('Could not connect')

    else:
        print('Connected successfully')
    
    sql_query = 'SELECT * FROM projemploye WHERE deptno = %s;'
    values=[deptno]

    mycursor=mydb.cursor()
    mycursor.execute(sql_query,values)

    student=mycursor.fetchall()
    if len(student)==0:
        print('Employee not found')
    
    else:
        print('Employee found:',student)

        for row in treeview.get_children():
            treeview.delete(row)

        for student in student:
            treeview.insert(parent='',index='end',values=student)

import tkinter as bot
import mysql.connector as rob
from tkinter import ttk

rootwindow = bot.Tk()
rootwindow.title("Employe Management System")
rootwindow.geometry("800x700")
rootwindow.configure(background="coral")

#headings and frames

labelheading=bot.Label(
    master=rootwindow,
    text='Employee Management System',
    font=('arial',25,'bold','underline'),
    background='coral',
    foreground='black'
)
labelheading.pack()


labelframeinput=bot.LabelFrame(
    master=rootwindow,
    text='Employee Input',
    font=('arial',15,'italic'),
    background='light blue',

    foreground='black'
)
labelframeinput.pack(fill='both',expand='yes',padx=10,pady=10)

labelframeoutput=bot.LabelFrame(
    master=rootwindow,
    text='Employee Output',
    font=('arial',15,'italic'),
    background='light blue',
    foreground='black'
)
labelframeoutput.pack(fill='both',expand='yes',padx=10,pady=10)

labelframeoperation=bot.LabelFrame(
    master=rootwindow,
    text='Employee Operation',
    font=('arial',15,'italic'),
    background='light blue',
    foreground='black'
)

labelframeoperation.pack(fill='both',expand='yes',padx=10,pady=10)

#inner frames
frameinput1=bot.Frame(
    master=labelframeinput,
    background='light blue'
)
frameinput1.pack(side=bot.LEFT,fill='both',expand='yes',padx=10,pady=10)

frameinput2=bot.Frame(
    master=labelframeinput,
    background='light blue'
)
frameinput2.pack(side=bot.LEFT,fill='both',expand='yes',padx=10,pady=10)

#input things
#rollno
empnola=bot.Label(
    master=frameinput1,
    text='Employe no',
    font=('arial',15,'bold'),
    background='light green',
    foreground='black'
)

empnoentry=bot.Entry(
    master=frameinput1,
    font=('arial',15,'bold'),
    foreground='black'
)

search_empno=bot.Button(
    master=frameinput1,
    text='Search empno',
    font=('arial',15,'bold'),
    background='light green',
    foreground='black',
    command=searchempno
)

empnola.grid(row=0,column=0,padx=10,pady=10)
empnoentry.grid(row=0,column=1,padx=10,pady=10)
search_empno.grid(row=0,column=2,padx=10,pady=10)

#name
namela=bot.Label(
    master=frameinput1,
    text='Name',
    font=('arial',15,'bold'),
    background='light green',
    foreground='black'
)

nameentry=bot.Entry(
    master=frameinput1,
    font=('arial',15,'bold'),
    foreground='black'
)

search_name=bot.Button(
    master=frameinput1,
    text='Search name',
    font=('arial',15,'bold'),
    background='light green',
    foreground='black',
    command=searchname
)

namela.grid(row=1,column=0,padx=10,pady=10)
nameentry.grid(row=1,column=1,padx=10,pady=10)
search_name.grid(row=1,column=2,padx=10,pady=10)

#job
jobla=bot.Label(
    master=frameinput1,
    text='Job',
    font=('arial',15,'bold'),
    background='light green',
    foreground='black'
)

jobentry=bot.Entry(
    master=frameinput1,
    font=('arial',15,'bold'),
    foreground='black'
)

search_job=bot.Button(
    master=frameinput1,
    text='Search job',
    font=('arial',15,'bold'),
    background='light green',
    foreground='black',
    command=searchjob
)

jobla.grid(row=2,column=0,padx=10,pady=10)
jobentry.grid(row=2,column=1,padx=10,pady=10)
search_job.grid(row=2,column=2,padx=10,pady=10)

#mgr
mgrla=bot.Label(
    master=frameinput1,
    text='Mgr',
    font=('arial',15,'bold'),
    background='light green',
    foreground='black'
)

mgrentry=bot.Entry(
    master=frameinput1,
    font=('arial',15,'bold'),
    foreground='black'
)

mgrla.grid(row=3,column=0,padx=10,pady=10)
mgrentry.grid(row=3,column=1,padx=10,pady=10)

#hiredate
hiredatela=bot.Label(
    master=frameinput2,
    text='Hiredate',
    font=('arial',15,'bold'),
    background='light green',
    foreground='black'
)

hiredateentry=bot.Entry(
    master=frameinput2,
    font=('arial',15,'bold'),
    foreground='black'
)

hiredatela.grid(row=0,column=0,padx=10,pady=10)
hiredateentry.grid(row=0,column=1,padx=10,pady=10)

#sal
salla=bot.Label(
    master=frameinput2,
    text='Salary',
    font=('arial',15,'bold'),
    background='light green',
    foreground='black'
)

salentry=bot.Entry( 
    master=frameinput2,
    font=('arial',15,'bold'),
    foreground='black'
)

search_sal=bot.Button(
    master=frameinput2,
    text='Search sal',
    font=('arial',15,'bold'),
    background='light green',
    foreground='black',
    command=searchsal
)

salla.grid(row=1,column=0,padx=10,pady=10)
salentry.grid(row=1,column=1,padx=10,pady=10)
search_sal.grid(row=1,column=2,padx=10,pady=10)

#comm
commla=bot.Label(
    master=frameinput2,
    text='Comm',
    font=('arial',15,'bold'),
    background='light green',
    foreground='black'
)

commentry=bot.Entry(
    master=frameinput2,
    font=('arial',15,'bold'),
    foreground='black'
)

commla.grid(row=2,column=0,padx=10,pady=10)
commentry.grid(row=2,column=1,padx=10,pady=10)

#deptno
deptnola=bot.Label(
    master=frameinput2,
    text='Deptno',
    font=('arial',15,'bold'),
    background='light green',
    foreground='black'
)

deptnoentry=bot.Entry(
    master=frameinput2,
    font=('arial',15,'bold'),
    foreground='black'
)

search_deptno=bot.Button(
    master=frameinput2,
    text='Search deptno',
    font=('arial',15,'bold'),
    background='light green',
    foreground='black',
    command=searchdeptno
)

deptnola.grid(row=3,column=0,padx=10,pady=10)
deptnoentry.grid(row=3,column=1,padx=10,pady=10)
search_deptno.grid(row=3,column=2,padx=10,pady=10)

#operation
buttonconfigure=bot.Button(
    master=labelframeoperation,
    text='Configure',
    font=('arial',15,'bold'),
    background='orange',
    foreground='black',
    command=configureall
)

buttondisplay=bot.Button(
    master=labelframeoperation,
    text='Display',
    font=('arial',15,'bold'),
    background='orange',
    foreground='black',
    command=display
)

labeloutput=bot.Label(
    master=labelframeoperation,
    text='Outputmsg',
    font=('arial',15,'bold'),
    background='light green',
    foreground='black'
)

buttonconfigure.grid(row=0,column=0,padx=10,pady=10)
buttondisplay.grid(row=0,column=1,padx=10,pady=10)
labeloutput.grid(row=0,column=2,padx=10,pady=10)

#treeview thing
treeview=ttk.Treeview(
    master=labelframeoutput,
    columns=(1,2,3,4,5,6,7,8),
    show='headings',
    height=3
)

treeview.heading(1,text='Empno')
treeview.heading(2,text='Name')
treeview.heading(3,text='Job')
treeview.heading(4,text='Mgr')
treeview.heading(5,text='Hiredate')
treeview.heading(6,text='Sal')
treeview.heading(7,text='Comm')
treeview.heading(8,text='Deptno')

treeview.pack(fill='both',expand='yes',padx=10,pady=10)

rootwindow.mainloop()