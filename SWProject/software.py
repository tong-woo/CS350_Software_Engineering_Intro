# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 21:59:49 2018

@author: admin
"""

import mysql.connector
import datetime


db=mysql.connector.connect(host="localhost",user="root",password="password",
                           db="healthcheck10",auth_plugin='mysql_native_password')

cur=db.cursor(buffered=True)

class suggestion(object):
    #suggestion to patients
    def __init__(self,sid,rank,cont,dtype,uid,did):
        self._sid=sid
        self._rank=rank
        self._cont=cont
        self._typ=dtype
        self._uid=uid
        self._did=did
    
    @property
    def uid(self):
        #return sid
        return self._uid
    
    @uid.setter
    def uid(self,u):
        #set sid
        self._uid=u
        
    @property
    def sid(self):
        #return sid
        return self._sid
    
    @sid.setter
    def sid(self,s):
        #set sid
        self._sid=s
        
    @property    
    def rank(self):
        #return rank
        return self._rank
    
    @rank.setter
    def rank(self,r):
        #set rank
        self._rank=r
        
    @property
    def cont(self):
        #get content
        return self._cont
    
    @cont.setter
    def cont(self,content):
        #set content
        self._cont=content
    
    @property
    def typ(self):
        #return type
        return self._typ
    
    @typ.setter
    def typ(self,dtyp):
        #set type
        self._typ=dtyp
    
    @property
    def did(self):
        #get doctor id
        return self._did
    
    @did.setter
    def did(self,ui):
        #set doctor's id
        self._did=ui
        
    
        
    

    
    
class disease(object):
    #store info of different disease, we will discuss this one in sprint2
    def __init__(self,name,m_file):
        
        self._model=m_file #that file models in
        self._name=name #disease name
        
    @property
    def name(self):
        return self.name
    
    def prediction(self,healthdata):
        
        return self._model.predict(healthdata)
    
    

class user(object):
    #check user type in database
    #log in and sign up define outside of class u
    def __init__(self,uid,password,email,typ=None,state=0):
        self._uid=uid
        self._p=password #p: password
        self._e=email   #e:email
        self._type=typ  #typ: type
        self._state=state
        
        
    @property
    def uid(self):
        return self._uid
    
    @uid.setter
    def uid(self,Uid):
        self._uid=Uid
        
    @property
    def e(self):
        return self._e
    
    @e.setter
    def e(self,email):
        self._e=email
    
    @property
    def p(self):
        return self._p
    
    @p.setter
    def p(self,new):
        #change the password of user
        self._p=new
        global cur
        sql="""update Users set userpassword=%s
            WHERE userID=%s"""
        cur.execute(sql,(new,self._uid))
        db.commit()
        db.close()
            
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self,st):
        self._state=st        
    
    def log_out(self):
        self._state=0
        #cur=db.cursor(buffered=True)
        global cur
        sql="""SET SQL_SAFE_UPDATES = 0"""
        cur.execute(sql)
        db.commit()
        sql1="""update Users set state=0 WHERE userID=%s"""
        cur.execute(sql1%self._uid)
        db.commit()
        db.close()

    
    
class doctor(user):
    def __init__(self,uid, name, email, password,personalInfo=None):
        user.__init__(self,uid,password,email,typ='D')
        self._n=name
        self._info = personalInfo
        
    def show(self):
        return(self._n,self._e,self._info)
        
    def profilo(self):
        #doctor edit his or her profilo
        pro=input("Please create profilo(100-150 words)")
        self._info=pro
        return (self._uid,pro)
    @property
    def n(self):
        return self._n
        
    @n.setter
    def n(self,name):
        self._n=name
    @property   
    def info(self):
        return self._info
    
    @info.setter
    def info(self,info):
        self._info=info
    
    def find_s(self,sid):
        #cur=db.cursor(buffered=True)
        global cur
        sql="""select sugID from Suggestions AS sug where sugID=%s"""
        cur.execute(sql%sid)
        s=cur.fetchone()
        if s[0]:
            return True
        else:
            return None
    
    def modify(self,SugID,sug,rank,dtyp):
        #modify suggestion
        #cur=db.cursor(buffered=True)
        global cur
        sql="""SET SQL_SAFE_UPDATES = 0"""
        cur.execute(sql)
        db.commit()
        sql1="""update Suggestions set suggestion=%s, ranking=%s,
            userID=%s, disID=%s WHERE sugID=%s"""
        cur.execute(sql1,(sug,rank,self._uid,dtyp,SugID))
        db.commit()
        db.close()
        
    def add(self,con,rank,typ):
        global cur
        #cur=db.cursor(buffered=True)
        sql1="""SELECT sugID FROM Suggestions ORDER BY sugID DESC LIMIT 1"""
        cur.execute(sql1)
        sid=cur.fetchone()[0]+1
        #print(sid)
        sql2="""insert into Suggestions(sugID,suggestion,ranking,userID,disID) values
            (%s,%s,%s,%s,%s)"""
        cur.execute(sql2,(sid,con,rank,self._uid,typ))
        db.commit()
        db.close()
    
    
    
class Patient(user):
    

    def __init__(self, uid,email,password,city,age,sex,s=None,c=None,g=None,h=None,w=None):
        #h_data: health data
        
        user.__init__(self,uid,password,email,typ='P')
        self._city=city
        self._age= age
        self._skin=s
        self._chol=c
        self._gluc=g
        self._hei=h #height
        self._wei=w #weight
        self._sug={'pima':[],'heart':[],'both':[]} #sug: suggestion
        self._con=[]
        self._s=sex #s:sex
    
    @property
    def city(self):
        return self._city
     
    @city.setter
    def city(self,c):
        self._city=c
        global cur
        #cur=db.cursor(buffered=True)
        sql="""SET SQL_SAFE_UPDATES = 0"""
        cur.execute(sql)
        db.commit()
        sql1="""update Patient set city=%s where userID=%s"""
        cur.execute(sql1,(c,self._uid))
        db.commit()
        db.close()
        
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,a):
        self._age=a
        global cur
        #cur=db.cursor(buffered=True)
        sql1="""update Patient set age=%s where userID=%s"""
        cur.execute(sql1,(a,self._uid))
        db.commit()
        db.close()
        
        
    @property
    def skin(self):
        #this function is for prediction
        return self._skin
    
    @skin.setter
    def skin(self,s):
        self._skin=s
        
    @property
    def chol(self):
        #this function is for prediction
        return self._chol
    
    @chol.setter
    def chol(self,ch):
        self._chol=ch
        
    @property
    def gluc(self):
        #this function is for prediction
        return self._gluc
    
    @gluc.setter
    def gluc(self,gl):
        self._gluc=gl
                    
    @property
    def hei(self):
        return self._hei
    
    @hei.setter
    def hei(self,height):
        self._hei=height
        
    @property
    def wei(self):
        return self._wei
    
    @wei.setter
    def wei(self,weight):
        self._wei=weight
        
    @property
    def s(self):
        return self._s
    
    @s.setter
    def s(self,sex):
        self._s=sex
        global cur
        #cur=db.cursor(buffered=True)
        sql1="""update Patient set sex=%s where userID=%s"""
        cur.execute(sql1,(sex,self._uid))
        db.commit()
        db.close()
        
    @property
    def sug(self):
        #get suggestion
        return self._sug
    
    def addDB(self):
        #update health data in DB
        #cur=db.cursor(buffered=True)
        global cur
        sql1="""update Patient set weight=%s, height=%s,
            chol=%s, skin_thickness=%s, glucose=%s WHERE userID=%s"""
        cur.execute(sql1,(self._wei,self._hei,self._chol,self._skin,self._gluc,self._uid))
        db.commit()
        db.close()
    
    
    def sugg(self):
        #set suggestion
        #for patient get sug
        #condition[0]:pima
        #condition[1]:heart
        global cur
        #cur=db.cursor(buffered=True)
        if self._con[0]==1 and self._con[1] ==0:
            sql1="""select * from Suggestions AS sug where disID='pima'  
                 order by sug.ranking DESC"""
            cur.execute(sql1)
            sug1=cur.fetchmany(2)
            s1=suggestion(sug1[0][0],int(sug1[0][2]),sug1[0][1],'pima',sug1[0][3],sug1[0][4])
            s2=suggestion(sug1[1][0],int(sug1[1][2]),sug1[1][1],'pima',sug1[1][3],sug1[1][4])
            self._sug['pima'].append(s1)
            self._sug['pima'].append(s2)
        
        elif self._con[1]==1 and self._con[0]==0:
            sql2="""select * from Suggestions AS sug where disID='heart' 
                 order by sug.ranking DESC"""
            cur.execute(sql2)
            sug2=cur.fetchmany(2)
            ss1=suggestion(sug2[0][0],int(sug2[0][2]),sug2[0][1],'heart',sug2[0][3],sug2[0][4])
            ss2=suggestion(sug2[1][0],int(sug2[1][2]),sug2[1][1],'heart',sug2[1][3],sug2[1][4])
            self._sug['heart'].append(ss1)
            self._sug['heart'].append(ss2)
        else:
            sql3="""select * from Suggestions AS sug where disID='both'
                 order by sug.ranking DESC"""
            cur.execute(sql3)
            sug3=cur.fetchmany(2)
            S1=suggestion(sug3[0][0],int(sug3[0][2]),sug3[0][1],'both',sug3[0][3],sug3[0][4])
            S2=suggestion(sug3[1][0],int(sug3[1][2]),sug3[1][1],'both',sug3[1][3],sug3[1][4])
            self._sug['both'].append(S1)
            self._sug['both'].append(S2)
        db.close()
        
    @property
    def con(self):
        #get condition
        return self._con
    
    @con.setter
    def con(self,condition):
        
        self._con=condition
        
    def log(self):
        time=datetime.datetime.now()
        global cur
        #cur = db.cursor(buffered=True)
        sql = """INSERT INTO Log(userID,city,sex,weight,height,chol,skinthickness,gluc,Timestamps)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cur.execute(sql,(self._uid,self._city,self._s,self._wei,self._hei,self._chol,self._skin,self._gluc,time))
        db.commit()
        db.close()
        

        