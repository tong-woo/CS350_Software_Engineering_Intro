# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 17:54:29 2018

@author: admin
"""

import mysql.connector
import software as obj
#from datetime import date, datetime, timedelta


def log_in(email,password):
    db=mysql.connector.connect(host="localhost",user="root",password="@wsx156fCL",
                           db="healthcheck")
    cur=db.cursor(buffered=True)
    sql="""SELECT * FROM users WHERE email=%s AND userpassword=%s"""
    cur.execute(sql,(email,password))
    #db.commit()
    result=cur.fetchone()
    #db.close()
    if result==None:
        print("Please check your username or password")
        db.close()
        return None
    else:
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
            user=obj.Patient(info1[0],result[1],result[2])
        db.close()
        return user
        
        
    
    
    
t=log_in('user@user1.com', '1234')
#print(t.type)
    
