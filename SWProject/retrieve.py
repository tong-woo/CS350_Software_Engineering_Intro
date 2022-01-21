# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 17:54:29 2018

@author: admin
"""

import mysql.connector
import software as obj
import datetime
#import app

#import software as obj
#from datetime import date, datetime, timedelta
db=mysql.connector.connect(host="localhost",user="root",password="password",
                           db="healthcheck10",auth_plugin='mysql_native_password')

cur=db.cursor(buffered=True)

def log_in(email,password):
    
    global cur
    sql="""SELECT * FROM users WHERE email=%s AND userpassword=%s"""
    cur.execute(sql,(email,password))
    #db.commit()
    result=cur.fetchone()
    #db.close()
    if result==None:
        print("Please check your username or password")
        #db.close()
        return (None,None)
    else:
        sqll="""SET SQL_SAFE_UPDATES = 0"""
        cur.execute(sqll)
        Sql="""update Users set state=1 WHERE userID=%s"""
        cur.execute(Sql%result[0])
        user=None
        if result[3]=='D':
           sql2="""SELECT * FROM doctor WHERE userID=%s """
           cur.execute(sql2%result[0])
           info=cur.fetchone()
           
           user=obj.doctor(info[0],info[1]+' '+info[2],result[1],result[2])
        else:
            sql3="""SELECT * FROM patient WHERE userID=%s """
            cur.execute(sql3%result[0])
            info1=cur.fetchone()
            user=obj.Patient(info1[0],result[1],result[2],info1[1],
                            info1[2],info1[3],info1[4],info1[5],info1[6],info1[7],info1[8])
        #db.close()
        return (user,result[3])
    
def sign_up(email,password,city,sex,age):
    
    
    global cur
    time=datetime.datetime.now()
    #cur=db.cursor(buffered=True)
    sql1="""insert into NewUsers(email,Timestamps) values (%s,%s)"""
    cur.execute(sql1,(email,time))
    db.commit()
    #db.close()
    #send email
    #token=app.index()
    #t=app.confirm_email(token)
    
    #if t==True:
    #cur=db.cursor(buffered=True)
    sql="""SELECT userID FROM Users ORDER BY userID  DESC LIMIT 1"""
    cur.execute(sql)
    uid=cur.fetchone()+1
    db.close()
        
    user=obj.Patient(uid,email,password,age,sex)
    #else:
        #user=None    
    return user

def re_pima():
    sug=[]
    global cur
    #cur=db.cursor(buffered=True)
    sql="""select suggestion, sugID from Suggestions
            WHERE disID != 'heart' """
    
    cur.execute(sql)
    for row in cur:
        sug.append(row)
    return sug

def re_heart():
    sug=[]
    #cur=db.cursor(buffered=True)
    global cur
    sql="""select suggestion, Suggestions.sugID from Suggestions
            WHERE disID != 'pima' """
    
    cur.execute(sql)
    for row in cur:
        sug.append(row)
    return sug


#print(re_pima())
#sign_up('user@user8.com','12367','busan','f',20)


