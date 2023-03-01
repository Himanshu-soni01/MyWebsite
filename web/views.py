from django.shortcuts import render,HttpResponse

import sqlite3
conn=sqlite3.connect('user.db')
cur=conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS user (Fname TEXT , Lname Text , Sex Text , EMAIL TEXT , Password TEXT)')

email={}
res = cur.execute('select EMAIL,Password from user').fetchall()[0]
for i in res:
    email[i[0]] = i[1]

def index(request):
    return render(request,'index.html')

fn=''
ln=''
s=''
em=''
pwd=''

def signaction(request):
    global fn,ln,s,em,pwd,email
    conn=sqlite3.connect('user.db')
    if request.method=="POST":
        cursor=conn.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                if value in email:
                    return render(request,'login_page.html')
                em=value
            if key=="password":
                pwd=value
        
        c="insert into user Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        cursor.execute(c)
        conn.commit()

    return render(request,'signup_page.html')

def loginaction(request):
    global em,pwd
    if request.method=="POST":
        conn=sqlite3.connect('user.db')
        cursor=conn.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="select * from user where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"welcome.html")
# (('Himanshu', 'Soni', 'male', 'rockstar733987@gmail.com', 'asdf'),)
    return render(request,'login_page.html')

def contactus(request):
    return render(request,'contactus.html')

def welcome(request):
    cursor=conn.cursor()
    c="select Fname from user where email='{}' and password='{}'".format(em,pwd)
    cursor.execute(c)
    t=cursor.fetchall()[0]
    
    data={
        'name' : t
    }
    return (request,'welcome.html',data)
