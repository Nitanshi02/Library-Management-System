from django.shortcuts import render
from django.http import HttpResponse
import sqlite3 as s

# Create your views here.

def search_form(request):
    return render(request,"webapp/page1.html")
def search_form1(request):
    return render(request,"webapp/login.html")

#login form
def fetch(request):
    if request.method=="GET":
        conn=s.connect("sqlite3\\library")
        c=conn.cursor()
        id1=request.GET["t1"]
        pswd=request.GET["p1"]
        c.execute("insert into login values(?,?)",(id1,pswd))
        conn.commit()
        conn.close()
        return render(request,"webapp/welcome.html")
    
def  update(request):
      return render(request,"webapp/update.html")

#update entry
def  update1(request):
      if  request.method=='GET':
            conn=s.connect("sqlite3\\library")
            c=conn.cursor()
            cd=request.GET["t1"]
            bn=request.GET["t2"]
            au=request.GET["t3"]
            p=request.GET["t4"]
            bp=request.GET["t5"]
            pd=request.GET["d1"]
            qty=request.GET["t6"]
            c.execute("insert into buk_update values(?,?,?,?,?,?,?)",(cd,bn,au,p,bp,pd,qty))
            conn.commit()
            conn.close()
            return render(request,"webapp/display.html")
      
def  issue(request):
      return render(request,"webapp/issue.html")

#issue records
def  issue1(request):
      conn=s.connect("sqlite3\\library")
      c=conn.cursor()
      a=request.GET["t1"]
      b=request.GET["t2"]
      n=request.GET["t3"]
      d=request.GET["t4"]
      e=request.GET["t5"]
      c.execute("insert into issue values(?,?,?,?,?)",(a,b,n,d,e))
      conn.commit()
      conn.close()
      return render(request,"webapp/display.html")

def  issue2(request):
      return render(request,"webapp/issue.html")

def returns(request):
      return render(request,"webapp/return.html")

#return records
def  retrieves(request):
      conn=s.connect("sqlite3\\library")
      c=conn.cursor()
      bid=request.GET["t1"]
      bc=request.GET["t2"]
      bn=request.GET["t3"]
      sid=request.GET["t4"]
      na=request.GET["t5"]
      d=request.GET["t6"]
      rd=request.GET["d1"]
      c.execute("insert into returned values(?,?,?,?,?,?,?)",(bid,bc,bn,sid,na,d,rd))
      conn.commit()
      conn.close()
      return render(request,"webapp/display.html")

def display1(request):
      return render(request,"webapp/display.html")

#display issue records
def issue_tab (request):
      conn=s.connect("C:\library\management\sqlite3\library")
      c=conn.cursor()
      c.execute("select * from issue")
      data=c.fetchall()
      x=""
      for row in data:
            k=str(row[0])
            m=str(row[1])
            n=str(row[2])
            o=str(row[3])
            ut=str(row[4])
            x+=(k+"\t"+m+"\t"+n+"&nbsp"+o+"\t"+ut+"<br>")
      conn.commit()
      conn.close()
      return HttpResponse(x)

#display return records
def hello(request):
      conn=s.connect("C:\library\management\sqlite3\library")
      c=conn.cursor()
      c.execute("select * from returned")
      data=c.fetchall()
      x=""
      for row in data:
            k=str(row[0])
            m=str(row[1])
            n=str(row[2])
            o=str(row[3])
            pq=str(row[4])
            uy=str(row[5])
            rf=str(row[6])
            x+=(k+"\t"+m+"\t"+n+"&nbsp"+o+"\t"+pq+"\t"+uy+"\t"+rf+"<br>")
      conn.commit()
      conn.close()
      return HttpResponse(x)

#display update records      
def book(request):
      conn=s.connect("C:\library\management\sqlite3\library")
      c=conn.cursor()
      c.execute("select * from buk_update")
      data=c.fetchall()
      x=""
      for row in data:
            k=str(row[0])
            m=str(row[1])
            n=str(row[2])
            o=str(row[3])
            pq=str(row[4])
            uy=str(row[5])
            rf=str(row[6])
            x+=(k+"\t"+m+"\t"+n+"&nbsp"+o+"\t"+pq+"\t"+uy+"\t"+rf+"<br>")
      conn.commit()
      conn.close()
      return HttpResponse(x)

