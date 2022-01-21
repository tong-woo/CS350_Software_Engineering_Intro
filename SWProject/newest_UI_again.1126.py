import tkinter as tk
import tkinter.messagebox
from datetime import date
import clss1 as soft
import ree as re
import funcDiabetes
import funcHeart

 

#  log in page
window = tk.Tk()
window.title('Health check')
window.geometry('600x500')

# user information


patient=None
doctor=None
pima=soft.disease('pima',funcDiabetes)
heart=soft.disease('heart',funcHeart)
#pima=soft.disease('pima',funcDiabetes)
#heart=soft.disease('heart',funcHeart)
var_sex='M'
con=[1,0]
_sug={'pima':['1 Have a balanced and healty diet','2 Keep exercise'],'heart':['1 Give up smoking','2 Lose weight'],'both':['1 both suggestoin','2 both suggestion']} #sug: suggestion
varh=[('Give up smoking',1),('Lose weight',2),('Sufficient sleeping',3)]
vard=[('Have a balanced and healty diet',1),('Keep exercise',2),("Don't stay up late",3)]

#healthdata page
height = 0
weight = 0
skin = 0
chol = 0
glu = 0
a=4

# sign_up variable
email = 0
password = 0
reconfirm = 0
year = 2000
month = 9
day = 25
age = 0
city = 0
sex = 0
gender_value = 0

# health data
varheight = tk.IntVar()
varweight = tk.IntVar()
varskin = tk.IntVar()
varchol = tk.IntVar()
varglu = tk.IntVar()

# welcom image
canvas = tk. Canvas(window, height=100,width=400)
image_file = tk.PhotoImage(file='title.gif')
image = canvas.create_image(45,20, anchor='nw', image=image_file)
canvas.pack(side='top')

# user informaiton
var_email = tk.StringVar()
var_email.set('healthcheck@gmail.com')
tk.Label(window, text='email: ',bg='skyblue',font=('Arial',15),height=1,width=20).place(x=40,y=130)
tk.Label(window, text='password: ',bg='skyblue',font=('Arial',15),height=1,width=20).place(x=40,y=200)
entry_emial = tk.Entry(window,text=var_email,font=('Arial',15))
entry_emial.place(x=320,y=130)
var_password = tk.StringVar()
var_password.set('1asd')
var_password = tk.Entry(window, text=var_password,show='*',font=('Arial',15))
var_password.place(x=320,y=200)
emile_list = ['xhaoboooo@gmail.com']
password_list = ['12345678']
choose_var = tk.IntVar()
SID = tk.StringVar()
varID=''
IDdata = '1'
#temporary avarible for the doctor page
varadd = 0
#main_page
def main_page():
    mainpage = tk.Toplevel(window)
    mainpage.geometry('600x500')
    mainpage.title('User main page')
    #health data page
    def data_page():
        datapage = tk.Toplevel(mainpage)
        datapage.title('input health data')
        datapage.geometry('600x500')

        Height = tk.Label(datapage, bg='skyblue', width=20, height=1, text='Height', font=('Arial', 15))
        Height.place(x=50, y=30, anchor='nw')

        Height_an = tk.Entry(datapage,textvariable=varheight,show=None)
        Height_an.place(x=350, y=35, anchor='nw')

        Height_un = tk.Label(datapage, bg='Aliceblue', width=2, height=1, text='cm', font=('Arial', 10))
        Height_un.place(x=500, y=35, anchor='nw')

        Weight = tk.Label(datapage, bg='skyblue', width=20, height=1, text='Weight', font=('Arial', 15))
        Weight.place(x=50, y=100, anchor='nw')

        Weight_an = tk.Entry(datapage,textvariable=varweight,show=None)
        Weight_an.place(x=350, y=105, anchor='nw')

        Weight_un = tk.Label(datapage, bg='Aliceblue', width=2, height=1, text='kg', font=('Arial', 10))
        Weight_un.place(x=500, y=105, anchor='nw')

        Skin = tk.Label(datapage, bg='skyblue', width=20, height=1, text='Skin thickness at tricepts', font=('Arial', 15))
        Skin.place(x=50, y=170, anchor='nw')

        Skin_an = tk.Entry(datapage,textvariable=varskin,show=None)
        Skin_an.place(x=350, y=175, anchor='nw')

        Skin_un = tk.Label(datapage, bg='Aliceblue', width=2, height=1, text='mm', font=('Arial', 10))
        Skin_un.place(x=500, y=175, anchor='nw')

        chol = tk.Label(datapage, bg='skyblue', width=20, height=1, text='Cholesterol level', font=('Arial', 15))
        chol.place(x=50, y=240, anchor='nw')

        cholan = tk.Entry(datapage,textvariable=varchol,show=None)
        cholan.place(x=350, y=245, anchor='nw')

        cholun = tk.Label(datapage, bg='Aliceblue', width=6, height=1, text='mmol/L', font=('Arial', 10))
        cholun.place(x=500, y=245, anchor='nw')

        glu = tk.Label(datapage, bg='skyblue', width=20, height=1, text='Glucose level', font=('Arial', 15))
        glu.place(x=50, y=310, anchor='nw')

        gluan = tk.Entry(datapage,textvariable=varglu,show=None)
        gluan.place(x=350, y=315, anchor='nw')

        gluun = tk.Label(datapage, bg='Aliceblue', width=6, height=1, text='mmol/L', font=('Arial', 10))
        gluun.place(x=500, y=315, anchor='nw')

        notice=tk.Label(datapage, bg='Crimson', width=50, height=2, text='You must input the real exact data.'+'\n'+"Otherwise we aren't responsible for the result.", font=('Arial', 15))
        notice.place(x=30,y=350,anchor='nw')
    
        def goto_confirm():
            global height
            height = int(Height_an.get())
            global weight
            weight = int(Weight_an.get())
            global skin
            skin = int(Skin_an.get())
            global chol
            chol = int(cholan.get())
            global glu
            glu = int(gluan.get())
            global age
            global gender_value
            global patient
            hdata=[]
            hdata=[age,gender_value,weight,height,chol,skin,glu]
            #c1=0
            #c2=0
            c1=pima.prediction(hdata)
            c2=heart.prediction(hdata)
            patient.con=[c1,c2]
            #global con
            #con=[c1,c2]
            datapage.destroy()
            


        Confirm = tk.Button(datapage, bg='pink', width=10, height=2, text='Confirm', font=('Arial', 20),
                            command=goto_confirm)
        Confirm.place(x=220, y=410, anchor='nw')

    data = tk.Button(mainpage, text='health data ', bg='skyblue', font=('Arial', 15), height=1, width=20,command=data_page)
    data.place(x=180, y=80)
    # suggestion_page
    def suggestion_page():
        suggpage = tk.Toplevel(mainpage)
        suggpage.geometry('600x500')
        suggpage.title('Suggestion')
        tk.Label(suggpage, text='health condition: ', bg='skyblue', font=('Arial', 15), height=1, width=20).place(x=40, y=30)
        tk.Label(suggpage, text='suggestion: ', bg='skyblue', font=('Arial', 15), height=1, width=20).place(x=40, y=200)
        health_text=tk.Text(suggpage,height=5,width=40 ,font=('Arial', 15))
        health_text.place(x=70,y=65)
        """
        global _con
        global _sug
        if ((_con[0]==1) and (_con[1]==0)):
            health_text.insert('end','You possibily have diabetes.'+'\n'+"You don't have heart disease.")
        elif ((_con[0]==0) and (_con[1]==1)):
            health_text.insert('end', 'You possibily have heart disease.' + '\n' + "You don't have diabetes.")
        elif ((_con[0]==1) and (_con[1]==1)):
            health_text.insert('end', 'You possibily have diabetes.' + '\n' + "You possibily have heart disease.")
        else:
            pass
        """
        global patient
        if patient.con[0]==1 and patient.con[1]==0:
            health_text.insert('end','You possibily have diabetes.'+'\n'+"You don't have heart disease.")
        elif patient.con[0]==0 and patient.con[1]==1:
            health_text.insert('end', 'You possibily have heart disease.' + '\n' + "You don't have diabetes.")
        elif patient.con[0]==1 and patient.con[1]==1:
            health_text.insert('end', 'You possibily have diabetes.' + '\n' + "You possibily have heart disease.")
        else:
            health_text.insert('end', 'You have no disease')
        
        
        
        
        

        sugg_text = tk.Text(suggpage, height=8, width=40, font=('Arial', 15))
        sugg_text.place(x=70, y=240)
        """
        
        if ((_con[0]==1) & (_con[1]==0)):
            for j in range(len(_sug['pima'])):
                sugg_text.insert('end',_sug['pima'][j]+'\n')
        elif ((_con[0]==0) & (_con[1]==1)):
            for j in range(len(_sug['heart'])):
                sugg_text.insert('end', _sug['heart'][j] + '\n')
        elif ((_con[0]==1) & (_con[1]==1)):
            for j in range(len(_sug['both'])):
                sugg_text.insert('end',_sug['both'][j]+'\n')
        else:
            pass
        """
        
        patient.sugg()
        global con
        con=patient.con
        #print(con)
        if con==[1,0]:
            #print(1)
            for j in range(len(patient.sug['pima'])):
                sugg_text.insert('end',patient.sug['pima'][j].cont+'\n')
        elif con==[0,1]:
            #print(2)
            for j in range(len(patient.sug['heart'])):
                sugg_text.insert('end', patient.sug['heart'][j].cont + '\n')
        elif con==[1,1]:
            #print(3)
            for j in range(len(patient.sug['both'])):
                sugg_text.insert('end',patient.sug['both'][j].cont+'\n')
        else:
            sugg_text.insert('end','good job, you have a good health condition. So suggestion'+'\n')
        

        back1 = tk.Button(suggpage, text='back', width=10, height=1, font=('Arial', 15), bg='pink',command=suggpage.destroy)
        back1.place(x=35,y=450)
    suggestion = tk.Button(mainpage, text='Suggestions ', bg='skyblue', font=('Arial', 15), height=1, width=20,command=(suggestion_page))
    suggestion.place(x=180, y=180)
    def set_page():
        setpage = tk.Toplevel(mainpage)
        setpage.title('Settings')
        setpage.geometry('600x500')
        email = tk.Label(setpage, bg='skyblue', width=20, height=1, text='Email', font=('Arial', 15))
        email.place(x=50, y=30, anchor='nw')

        email_an = tk.Label(setpage, bg='Aliceblue', width=20, height=1, text='xhaoboooo@gmail.com', font=('Arial', 10))
        email_an.place(x=350, y=35, anchor='nw')

        def modifybirth():
            window_birthday = tk.Toplevel(setpage)
            window_birthday.title('Age')
            window_birthday.geometry('350x200')

            varbiry = tk.StringVar()
            varbirm = tk.StringVar()
            varbird = tk.StringVar()
            birth = tk.Label(window_birthday, bg='skyblue', width=20, height=1, text='Modify Birthday',font=('Arial', 15))
            birth.place(x=60, y=20, anchor='nw')

            y=tk.Label(window_birthday,bg='Aliceblue', width=4, height=1, text='year', font=('Arial', 10))
            y.place(x=100,y=80,anchor='nw')
            m = tk.Label(window_birthday, bg='Aliceblue', width=5, height=1, text='month', font=('Arial', 10))
            m.place(x=150, y=80, anchor='nw')
            d = tk.Label(window_birthday, bg='Aliceblue', width=3, height=1, text='day', font=('Arial', 10))
            d.place(x=200, y=80, anchor='nw')

            new_year = tk.Entry(window_birthday,width=6, textvariable=varbiry, show=None)
            new_year.place(x=100, y=100, anchor='nw')
            new_month = tk.Entry(window_birthday, width=6, textvariable=varbirm, show=None)
            new_month.place(x=150, y=100, anchor='nw')
            new_day = tk.Entry(window_birthday, width=6, textvariable=varbird, show=None)
            new_day.place(x=200, y=100, anchor='nw')

            def con_bir():
                var_year = new_year.get()
                var_month = new_month.get()
                var_day = new_day.get()
                birth_an.config(text=str(var_year)+'/'+str(var_month)+'/'+str(var_day))
                window_birthday.destroy()

            def gocancel():
                window_birthday.destroy()

            confirm = tk.Button(window_birthday, bg='pink', width=10, height=1, text='Confirm', font=('Arial', 15),
                                command=con_bir)
            confirm.place(x=40, y=160, anchor='nw')
            cancel = tk.Button(window_birthday, bg='lightgreen', width=10, height=1, text='Cancel', font=('Arial', 15),
                               command=gocancel)
            cancel.place(x=200, y=160, anchor='nw')

            window.wait_window(window_birthday)

        birthday = tk.Button(setpage, bg='skyblue', width=20, height=1, text='Birthday', font=('Arial', 15),
                             command=modifybirth)
        birthday.place(x=50, y=100, anchor='nw')

        birth_an = tk.Label(setpage, bg='Aliceblue', width=10, height=1,text=str(year)+'/'+str(month)+'/'+str(day), font=('Arial', 10))
        birth_an.place(x=390, y=105, anchor='nw')

        def modifysex():
            window_sex = tk.Toplevel(setpage)
            window_sex.title('Sex')
            window_sex.geometry('350x200')

            varsex = tk.StringVar()
            sex_ = tk.Label(window_sex, bg='skyblue', width=20, height=1, text='Modify Sex', font=('Arial', 15))
            sex_.place(x=60, y=20, anchor='nw')

            new_sex = tk.Entry(window_sex, textvariable=varsex, show=None)
            new_sex.place(x=100, y=100, anchor='nw')

            def con_sex():
                global patient
                global gender_value
                var_sex = new_sex.get()
                if var_sex == 'F':
                    gender_value=0
                elif var_sex =='M':
                    gender_value=1
                sex_an.config(text=var_sex)
                
                #patient.s=gender_value
                window_sex.destroy()

            def gocancel():
                window_sex.destroy()

            confirm = tk.Button(window_sex, bg='pink', width=10, height=1, text='Confirm', font=('Arial', 15),
                                command=con_sex)
            confirm.place(x=40, y=160, anchor='nw')
            cancel = tk.Button(window_sex, bg='lightgreen', width=10, height=1, text='Cancel', font=('Arial', 15),
                               command=gocancel)
            cancel.place(x=200, y=160, anchor='nw')

            setpage.wait_window(window_sex)

        sex = tk.Button(setpage, bg='skyblue', width=20, height=1, text='Sex', font=('Arial', 15), command=modifysex)
        sex.place(x=50, y=170, anchor='nw')

        sex_an = tk.Label(setpage, bg='Aliceblue', width=6, height=1, text=var_sex, font=('Arial', 10))
        sex_an.place(x=410, y=175, anchor='nw')

        sex_h = tk.Label(setpage, bg='Aliceblue', width=18, height=1, text='(Female:F ; Male:M)', font=('Arial', 10))
        sex_h.place(x=350,y=200,anchor='nw')
        def goback():
            setpage.destroy()

        back = tk.Button(setpage, bg='lightgreen', width=10, height=2, text='Back', font=('Arial', 20), command=goback)
        back.place(x=220, y=400, anchor='nw')


    setting = tk.Button(mainpage, text='setting ', bg='skyblue', font=('Arial', 15), height=1, width=20,command=set_page)
    setting.place(x=180, y=280)
    # user log_out function
    def log_out():
        global patient
        patient.log_out()
        #patient.log_out()
        mainpage.destroy()
    # user log out
    logout = tk.Button(mainpage,text='Log out ', bg='skyblue', font=('Arial', 15), height=1, width=20,command=log_out)
    logout.place(x=180, y=380)
#doctor main page
def doctor_page():
    doctorpage = tk.Toplevel(window)
    doctorpage.geometry('600x500')
    doctorpage.title('Doctor main page')
    #Suggestion table page
    #choose disease page
    def choose_dis():
        choosedis = tk.Toplevel(doctorpage)
        choosedis.geometry('600x500')
        choosedis.title('Choose disease')
        # heart disease page
        def heartpage():
            heartpage = tk.Toplevel(choosedis)
            heartpage.title('Heart page')
            heartpage.geometry('600x500')
            #heart page destroy
            def heart_des():
                heartpage.destroy()
            global varh
            varh=re.re_heart()
            heart=tk.Label(heartpage, text='heart suggestions:',bg='skyblue',font=('Arial',15),height=1,width=20)
            heart.place(x=40,y=30)
            sugg=tk.Text(heartpage,font=('Arial',15),height=18,width=45)
            sugg.place(x=40,y=70)
            for i in range(len(varh)):
                sugg.insert('end',varh[i][0]+'--------'+str(varh[i][1])+'\n')
            bac=tk.Button(heartpage, text='back', bg='pink', font=('Arial', 15), height=1, width=10,command=heart_des)
            bac.place(x=450,y=25)
        # diabetes page
        def diabetes_page():
            diabetespage = tk.Toplevel(choosedis)
            diabetespage.title('Diabetes page')
            diabetespage.geometry('600x500')
            # diabetes page destroy
            def diabetes_des():
                diabetespage.destroy()
            global vard
            vard=re.re_pima()
            diab=tk.Label(diabetespage, text='Diabetes suggestions:', bg='skyblue', font=('Arial', 15), height=1, width=20)
            diab.place(x=40, y=30)
            sugg=tk.Text(diabetespage, font=('Arial', 15), height=18, width=45)
            sugg.place(x=40, y=70)
            for i in range(len(vard)):
                sugg.insert('end',vard[i][0]+'--------'+str(vard[i][1])+'\n')
            bac=tk.Button(diabetespage, text='back', bg='pink', font=('Arial', 15), height=1, width=10,command=diabetes_des)
            bac.place(x=450, y=25)
         #choose which page show
        def choose():
            choose_var.get()
            if choose_var.get() ==1:
                heartpage()
            if choose_var.get() ==2:
                diabetes_page()
        r1 = tk.Radiobutton(choosedis, text = 'Heart disease',variable=choose_var, value = 1,font=('Arial', 25),height=1,width=20)
        r1.place(x=90,y=100)
        r2 = tk.Radiobutton(choosedis, text='Diabetes', variable=choose_var, value=2, font=('Arial', 25),height=1, width=20)
        r2.place(x=90, y=200)
        confirm1 = tk.Button(choosedis, text='Confirm ', width=10, height=2, font=('Arial', 20), bg='pink',command=choose)
        confirm1.place(x=210,y=320)
    table = tk.Button(doctorpage, text='Suggestion table ', bg='skyblue', font=('Arial', 15), height=1, width=20,command=choose_dis)
    table.place(x=180, y=80)
    #Add table page
    def add_page():
        addpage = tk.Toplevel(doctorpage)
        addpage.title('Add a suggestion')
        addpage.geometry('600x500')
        # label to show the information about suggestion
        sug = tk.Label(addpage, bg='skyblue', width=20, height=1, text='Suggestion:', font=('Arial', 15))
        sug.place(x=50, y=50, anchor='nw')
        # entry let doctors to type in a new suggestion
        sugan = tk.Entry(addpage, width=84, show=None, font=('Arial', 15))
        sugan.place(x=3, y=120, anchor='nw')
        # we give a limitation about the size of the string which shown in a label
        limit = tk.Label(addpage, bg='LemonChiffon', width=16, height=1, text='<= 50 characters', font=('Arial', 8))
        limit.place(x=450, y=150, anchor='nw')
        # label to show the information to choose a type of disease which corresponds to the suggestion
        type = tk.Label(addpage, bg='skyblue', width=20, height=1, text='Type of disease', font=('Arial', 15))
        type.place(x=50, y=200, anchor='nw')

        # function for choosing a disease
        def select():
            Typ=''
            if ck1.get() == 1 & ck2.get() == 0:
                Typ='heart'
            elif ck2.get() == 1 & ck1.get() == 0:
                Typ='pima'
            elif ck1.get() == 1 & ck2.get() == 1:
                Typ='both'
            return Typ

        ck1 = tk.IntVar()
        ck2 = tk.IntVar()
        # define two option to let doctor to choose which disease
        check1 = tk.Checkbutton(addpage, text='Heart disease', variable=ck1, onvalue=1, offvalue=0, command=select)
        check1.place(x=300, y=200, anchor='nw')
        check2 = tk.Checkbutton(addpage, text='Diabetes', variable=ck2, onvalue=1, offvalue=0, command=select)
        check2.place(x=480, y=200, anchor='nw')
        # label to show the information about rank
        rank = tk.Label(addpage, bg='skyblue', width=20, height=1, text='Rank of suggestion', font=('Arial', 15))
        rank.place(x=50, y=300, anchor='nw')
        # we give the range of rank shown in this label
        range = tk.Label(addpage, bg='LightCyan', width=10, height=1, text='Range: [0,5]', font=('Arial'))
        range.place(x=100, y=330, anchor='nw')

        r=''

        # function of choosing a rank of this suggestion
        def chorank(r):
            return r
            

        # the range of rank and let doctor to sliding the progress bar
        scale = tk.Scale(addpage, label='Rank', from_=0, to=5, orient=tk.HORIZONTAL, 
                         showvalue=5, tickinterval=1,length=200, resolution=1, command=chorank)
        scale.place(x=320, y=285, anchor='nw')

        # function to add a new suggestion
        def addin():
            global varadd
            global doctor
            global a
            #varadd = sugan.get()
            #varh.append((varadd,4))
            sugg=sugan.get()
            typp=select()
            
            doctor.add(sugg,a,typp)
            addpage.destroy()

        # button to add the new suggestion
        add = tk.Button(addpage, bg='lightgreen', width=10, height=2, text='Add', font=('Arial', 20), command=addin)
        add.place(x=220, y=400, anchor='nw')

    Add = tk.Button(doctorpage, text='Add ', bg='skyblue', font=('Arial', 15), height=1, width=20,command=add_page)
    Add.place(x=180, y=180)
    #Modify page
    # the page to input suggestion ID to choose a suggestion to modify
    def choose_page():
        choosepage = tk.Toplevel(doctorpage)
        choosepage.title('Choose one suggestion')
        choosepage.geometry('600x500')
        # the label to show the ID information
        ID = tk.Label(choosepage, bg='skyblue', width=20, height=1, text='Suggestion ID', font=('Arial', 15))
        ID.place(x=180, y=100, anchor='nw')
        # the entry let doctor to type in the suggestion ID
        choID = tk.Entry(choosepage, textvariable=SID, show=None)
        choID.place(x=220, y=200, anchor='nw')
        # label to give hint to doctors
        hint = tk.Label(choosepage, bg='LemonChiffon', width=35, height=1,
                        text='(Input the ID of a suggestion you want to modify!)',
                        font=('Arial'))
        hint.place(x=140, y=270, anchor='nw')

        # the page for modifying a suggestion
        def modify_suggestion():
            modifypage = tk.Toplevel(doctorpage)
            modifypage.title('Choose one suggestion')
            modifypage.geometry('600x500')
            # label to show the information about suggestion
            sug = tk.Label(modifypage, bg='skyblue', width=20, height=1, text='Suggestion:',font=('Arial', 15))
            sug.place(x=50, y=50, anchor='nw')

            su = tk.StringVar()
            su.set('Give up smoking')
            # entry let doctors to modify the suggestion
            sugan = tk.Entry(modifypage, width=84, show=None, textvariable=su, font=('Arial', 15))
            sugan.place(x=3, y=120, anchor='nw')
            # we give a limitation about the size of the string which shown in a label
            limit = tk.Label(modifypage, bg='LemonChiffon', width=16, height=1, text='<= 50 characters', font=('Arial', 8))
            limit.place(x=450, y=150, anchor='nw')
            # label to show the information to choose a type of disease which corresponds to the suggestion
            type = tk.Label(modifypage, bg='skyblue', width=20, height=1, text='Type of disease', font=('Arial', 15))
            type.place(x=50, y=200, anchor='nw')

            # function for choosing a disease
            def select():
                tyP=''
                if ck1.get() == 1 & ck2.get() == 0:
                    tyP='heart'
                elif ck2.get() == 1 & ck1.get() == 0:
                    tyP='pima'
                elif ck1.get() == 1 & ck2.get() == 1:
                    tyP='both'
                return tyP
                

            ck1 = tk.IntVar()
            ck2 = tk.IntVar()
            # define two option to let doctor to choose which disease
            check1 = tk.Checkbutton(modifypage, text='Heart disease', variable=ck1, onvalue=1, offvalue=0, command=select)
            check1.place(x=300, y=200, anchor='nw')
            check2 = tk.Checkbutton(modifypage, text='Diabetes', variable=ck2, onvalue=1, offvalue=0, command=select)
            check2.place(x=480, y=200, anchor='nw')
            # label to show the information about rank
            rank = tk.Label(modifypage, bg='skyblue', width=20, height=1, text='Rank of suggestion', font=('Arial', 15))
            rank.place(x=50, y=300, anchor='nw')
            # we give the range of rank shown in this label
            range = tk.Label(modifypage, bg='LightCyan', width=10, height=1, text='Range: [0,5]', font=('Arial'))
            range.place(x=100, y=330, anchor='nw')

            r = ''

            # function of choosing a rank of this suggestion
            def chorank(r):
                
                return r

            # the range of rank and let doctor to sliding the progress bar
            scale = tk.Scale(modifypage, label='Rank', from_=0, to=5, orient=tk.HORIZONTAL, showvalue=5, tickinterval=1,
                             variable=r,
                             length=200, resolution=1, command=chorank)
            scale.place(x=320, y=285, anchor='nw')
            # function to modify the suggestion
            def addin():
                global doctor
                global SID
                varmodi=sugan.get()
                #varh[0]=(varmodi,1)
                typ1=select()
                #r1=chorank(r)
                doctor.modify(SID,varmodi,a,typ1)
                modifypage.destroy()

            # button to modify the suggestion
            add = tk.Button(modifypage, bg='lightgreen', width=10, height=2, text='Modify', font=('Arial', 20),
                            command=addin)
            add.place(x=220, y=400, anchor='nw')

        # function of button modify
        def choose():
            varID = choID.get()
            global doctor
            current=doctor.find_s(varID)
            if current:
                modify_suggestion()
            else:
                # if the input ID is wrong, there does not exist that suggestion, there is a child window comes out
                win_note = tk.Toplevel(choosepage)
                win_note.title('Error!')
                win_note.geometry('350x200')
                # label to show the information about wrong ID
                error = tk.Label(win_note, bg='Crimson', width=25, height=1, text='Suggestion does not exist! ',
                                 font=('Arial', 15))
                error.place(x=35, y=20, anchor='nw')
                # label to let doctor to input ID again
                noti = tk.Label(win_note, bg='LemonChiffon', width=18, height=1, text='Please input again.',
                                font=('Arial', 10))
                noti.place(x=90, y=100, anchor='nw')

                # the button to close the child window
                def again():
                    win_note.destroy()

                # button let doctor to go back to the choose page
                OK = tk.Button(win_note, bg='lightgreen', width=10, height=1, text='OK', font=('Arial', 15),
                               command=again)
                OK.place(x=110, y=160, anchor='nw')

        # button to let doctor go to a page to modify the suggestion chosen
        confirm = tk.Button(choosepage, bg='lightgreen', width=10, height=2, text='Confirm', font=('Arial', 20),
                            command=choose)
        confirm.place(x=210, y=380, anchor='nw')

    Modify = tk.Button(doctorpage, text='Modify ', bg='skyblue', font=('Arial', 15), height=1, width=20,command=choose_page)
    Modify.place(x=180, y=280)
    # doctor log_out function
    def log_out1():
        global doctor
        doctor.log_out()
        doctorpage.destroy()
    # doctor log out
    logout = tk.Button(doctorpage, text='Log out ', bg='skyblue', font=('Arial', 15), height=1, width=20, command=log_out1)
    logout.place(x=180, y=380)
#check user or doctor information
def check_conf1():
    var1=var_email.get()
    var2=var_password.get()
    result=re.log_in(var1,var2)
    if result[1]=='P':
        global patient
        patient=result[0]
        main_page()
    elif result[1] == 'D':
            global doctor
            doctor=result[0]
            doctor_page()
    else:
        tk.messagebox.showerror(title='Error!',message='Please sign up at first!')
#go to the main page after checking!
confirm1=tk.Button(window,text='Confirm',width=10,height=2,font=('Arial',20),bg='pink',command=check_conf1 )
confirm1.place(x=200,y=300)
#sign up page
#sign up page
def sign_page():
    signpage = tk.Toplevel(window)
    signpage.geometry('600x500')
    signpage.title('Sign up')
    tk.Label(signpage, text='Email: ', bg='skyblue', font=('Arial', 15), height=1, width=20).place(x=40, y=30)
    tk.Label(signpage, text='Password: ', bg='skyblue', font=('Arial', 15), height=1, width=20).place(x=40, y=90)
    tk.Label(signpage, text='Reconfirm:', bg='skyblue', font=('Arial', 15), height=1, width=20).place(x=40, y=150)
    tk.Label(signpage, text='Birthday:', bg='skyblue', font=('Arial', 15), height=1, width=20).place(x=40, y=210)
    tk.Label(signpage, text='City:', bg='skyblue', font=('Arial', 15), height=1, width=20).place(x=40, y=270)
    tk.Label(signpage, text='Sex(F/M):', bg='skyblue', font=('Arial', 15), height=1, width=20).place(x=40, y=330)
    sign_email = tk.Entry(signpage, font=('Arial', 15))
    sign_email.place(x=300, y=30)
    sign_password = tk.Entry(signpage, font=('Arial', 15))
    sign_password.place(x=300, y=90)
    password = sign_password.get()
    sign_recheck = tk.Entry(signpage, font=('Arial', 15))
    sign_recheck.place(x=300, y=150)
    reconfirm = sign_recheck.get()
    sign_year = tk.Entry(signpage, font=('Arial', 15),width=4)
    sign_year.place(x=300, y=210)
    tk.Label(signpage, text='Y', bg='skyblue', font=('Arial', 15), height=1, width=3).place(x=355, y=210)
    sign_month = tk.Entry(signpage, font=('Arial', 15),width=2)
    sign_month.place(x=400, y=210)
    tk.Label(signpage, text='M', bg='skyblue', font=('Arial', 15), height=1, width=3).place(x=434, y=210)
    sign_day = tk.Entry(signpage, font=('Arial', 15), width=2)
    sign_day.place(x=480, y=210)
    tk.Label(signpage, text='D', bg='skyblue', font=('Arial', 15), height=1, width=3).place(x=510, y=210)
    sign_city = tk.Entry(signpage, font=('Arial', 15))
    sign_city.place(x=300, y=270)
    sign_sex = tk.Entry(signpage, font=('Arial', 15))
    sign_sex.place(x=300, y=330)
    def verify_page():
        tk.messagebox.showinfo(title='Verify',message='Please go to email for activation')
    verify = tk.Button(signpage, text='Verify', bg='pink', font=('Arial', 15), height=1, width=20,command=verify_page)
    verify.place(x=180, y=380)
    #check if the user wanna sign up
    def check_conf2():
        answer=tk.messagebox.askyesno(title='sign up',message='Do you wanna sign up now?')
        if answer == True:
            check_conf3()
            signpage.destroy()
        else:
            signpage.destroy()
    #save the user data
    #just use the list now to operate simply
    def check_conf3():
        #get the varible value from the sign up entry
        global email
        email = str(sign_email.get())
        global password
        password = str(sign_password.get())
        global reconfirm
        reconfirm = str(sign_recheck.get())
        global year
        year = int(sign_year.get())
        global month
        month = int(sign_month.get())
        global day
        day = int(sign_day.get())
        global city
        city = str(sign_city.get())
        global sex
        sex = str(sign_sex.get())
        global gender_value
        if sex == 'F':
            gender_value=0
        elif sex =='M':
            gender_value=1
        global age
        b = date.today() - date(year, month, day)
        a = b.days
        age = a // 365
        #judge if the password for 2 times are right
        if password!=reconfirm:
            tk.messagebox.showerror(title='Error password',message='please meke sure the password are same!')
            sign_page()
        else:
            global patient
            patient=re.sign_up(email,password,city,gender_value,age)
    confirm2 = tk.Button(signpage, text='sign up ', width=20, height=1, font=('Arial', 15), bg='pink',command=check_conf2)
    confirm2.place(x=180, y=430)
#sign up button
signup_button=tk.Button(window, text='sign up',bg='skyblue',font=('Arial',15),height=1,width=20,command=sign_page)
signup_button.place(x=170,y=410)

window.mainloop()