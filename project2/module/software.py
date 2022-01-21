# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 21:59:49 2018

@author: admin
"""

class suggestion(object):
    #suggestion to patients
    def __init__(self,sid,rank,content,dtype):
        self.sid=sid
        self.rank=rank
        self.content=content
        self.type=dtype
        
    def get_con(self):
        #return content of suggestion 
        return self.content
    
    def get_type(self):
        #for search suggestion
        return self.type
    
    def get_id(self):
        #maybe will be used later
        return self.sid
        
    
        
    

    
    
class disease(object):
    #store info of different disease, we will discuss this one in sprint2
    def __init__(self,did,name,model=None):
        #did: disease id
        self.did=did
        self.model=model
        self.name=name #disease name
        
class model(object):
    def predict(X,y):
        pass
    def predict(X):
        pass
        
class user(object):
    #check user type in database
    #log in and sign up define outside of class u
    def __init__(self,uid,password,email,typ):
        self.uid=uid
        self.p=password #p: password
        self.e=email   #e:email
        self.type=typ  #typ: type
        
    def change_pass(self):
        new=input("New password")
        self.p=new
        return (self.uid,new )

        
class doctor(user):
    def __init__(self,uid, name, email, password,personalInfo=None):
        user.__init__(self,uid,password,email,typ='D')
        self.n=name
        self.info = personalInfo
        
    def show(self):
        return(self.n,self.e,self.info)
        
    def profilo(self):
        #doctor edit his or her profilo
        pro=input("Please create profilo(100-150 words)")
        self.info=pro
        return (self.uid,pro)
     #if doctor wants to add or delete suggestion
     #use the methods of database
    
    
class Patient(user):
    

    def __init__(self, uid,email,password,h_data=None,condition=None):
        #h_data: health data
        
        user.__init__(self,uid,password,email,typ='P')
        self.h_data=h_data
        self.sug={} #sug: suggestion
        self.condition=condition
    
    def get_hdata(self):
        #this function is for prediction
        return self.h_data
        
    def get_suggestion(self):
        #patient inserts health data
        return self.sug

    def get_condition(self):
        #get health condition of patient and show on screen
        return self.condition