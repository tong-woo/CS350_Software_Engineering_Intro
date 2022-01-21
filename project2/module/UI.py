import tkinter as tk
import tkinter.messagebox
import database_connect as DB
#  log in page
window = tk.Tk()
window.title('Welcome to healthcheck')
window.geometry('600x500')

# user information
var_birthday='1998-04-04'
var_age=20
var_phone='01057579804'

# welcom image
#canvas = tk. Canvas(window, height=100,width=400)
#image_file = tk.PhotoImage(file='title.gif')
#image = canvas.create_image(45,20, anchor='nw', image=image_file)
#canvas.pack(side='top')

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
emile_list = []
password_list = []
#main_page
def main_page():
    mainpage = tk.Toplevel(window)
    mainpage.geometry('600x500')
    mainpage.title('Main page')
    #health data page
    def data_page():
        datapage = tk.Toplevel(mainpage)
        datapage.title('input health data')
        datapage.geometry('600x500')

        Height = tk.Label(datapage, bg='skyblue', width=20, height=1, text='Height', font=('Arial', 15))
        Height.place(x=50, y=30, anchor='nw')

        Height_an = tk.Entry(datapage, show=None)
        Height_an.place(x=350, y=35, anchor='nw')

        Height_un = tk.Label(datapage, bg='Aliceblue', width=2, height=1, text='cm', font=('Arial', 10))
        Height_un.place(x=500, y=35, anchor='nw')

        Weight = tk.Label(datapage, bg='skyblue', width=20, height=1, text='Weight', font=('Arial', 15))
        Weight.place(x=50, y=100, anchor='nw')

        Weight_an = tk.Entry(datapage, show=None)
        Weight_an.place(x=350, y=105, anchor='nw')

        Weight_un = tk.Label(datapage, bg='Aliceblue', width=2, height=1, text='kg', font=('Arial', 10))
        Weight_un.place(x=500, y=105, anchor='nw')

        Skin = tk.Label(datapage, bg='skyblue', width=20, height=1, text='Skin', font=('Arial', 15))
        Skin.place(x=50, y=170, anchor='nw')

        Skin_an = tk.Entry(datapage, show=None)
        Skin_an.place(x=350, y=175, anchor='nw')

        Blood_press = tk.Label(datapage, bg='skyblue', width=20, height=1, text='Blood Pressure', font=('Arial', 15))
        Blood_press.place(x=50, y=240, anchor='nw')

        Blood_pressan = tk.Entry(datapage, show=None)
        Blood_pressan.place(x=350, y=245, anchor='nw')

        Blood_pressun = tk.Label(datapage, bg='Aliceblue', width=4, height=1, text='mmHg', font=('Arial', 10))
        Blood_pressun.place(x=500, y=245, anchor='nw')

        def goto_confirm():
            datapage.destroy()

        Confirm = tk.Button(datapage, bg='pink', width=10, height=2, text='Confirm', font=('Arial', 20),
                            command=goto_confirm)
        Confirm.place(x=220, y=400, anchor='nw')

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
        sugg_text = tk.Text(suggpage, height=8, width=40, font=('Arial', 15))
        sugg_text.place(x=70, y=240)
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

        email_an = tk.Label(setpage, bg='Aliceblue', width=20, height=1, text='1213809967@qq.com', font=('Arial', 10))
        email_an.place(x=350, y=35, anchor='nw')

        def modifybirthday():
            window_birthday = tk.Toplevel(setpage)
            window_birthday.title('Date of Birth')
            window_birthday.geometry('350x200')

            varbirth = tk.StringVar()
            birth = tk.Label(window_birthday, bg='skyblue', width=20, height=1, text='Modify Date of Birth',
                             font=('Arial', 15))
            birth.place(x=60, y=20, anchor='nw')

            new_bir = tk.Entry(window_birthday, textvariable=varbirth, show=None)
            new_bir.place(x=100, y=100, anchor='nw')

            def con_bir():
                var_birthday = new_bir.get()
                birthday_an.config(text=var_birthday)
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

        birthday = tk.Button(setpage, bg='skyblue', width=20, height=1, text='Date of Birth', font=('Arial', 15),
                             command=modifybirthday)
        birthday.place(x=50, y=100, anchor='nw')

        birthday_an = tk.Label(setpage, bg='Aliceblue', width=10, height=1, text=var_birthday, font=('Arial', 10))
        birthday_an.place(x=390, y=105, anchor='nw')

        def modifyage():
            window_age = tk.Toplevel(setpage)
            window_age.title('Age')
            window_age.geometry('350x200')

            varage = tk.StringVar()
            age_ = tk.Label(window_age, bg='skyblue', width=20, height=1, text='Modify Age', font=('Arial', 15))
            age_.place(x=60, y=20, anchor='nw')

            new_age = tk.Entry(window_age, textvariable=varage, show=None)
            new_age.place(x=100, y=100, anchor='nw')

            def con_age():
                var_age = new_age.get()
                age_an.config(text=var_age)
                window_age.destroy()

            def gocancel():
                window_age.destroy()

            confirm = tk.Button(window_age, bg='pink', width=10, height=1, text='Confirm', font=('Arial', 15),
                                command=con_age)
            confirm.place(x=40, y=160, anchor='nw')
            cancel = tk.Button(window_age, bg='lightgreen', width=10, height=1, text='Cancel', font=('Arial', 15),
                               command=gocancel)
            cancel.place(x=200, y=160, anchor='nw')

            setpage.wait_window(window_age)

        age = tk.Button(setpage, bg='skyblue', width=20, height=1, text='Age', font=('Arial', 15), command=modifyage)
        age.place(x=50, y=170, anchor='nw')

        age_an = tk.Label(setpage, bg='Aliceblue', width=2, height=1, text=var_age, font=('Arial', 10))
        age_an.place(x=420, y=175, anchor='nw')

        def modifyphone():
            window_phone = tk.Toplevel(setpage)
            window_phone.title('Phone Number')
            window_phone.geometry('350x200')

            varpho = tk.StringVar()
            pho = tk.Label(window_phone, bg='skyblue', width=20, height=1, text='Modify Phone Number',
                           font=('Arial', 15))
            pho.place(x=60, y=20, anchor='nw')

            new_pho = tk.Entry(window_phone, textvariable=varpho, show=None)
            new_pho.place(x=100, y=100, anchor='nw')

            def con_bir():
                var_phone = new_pho.get()
                phone_an.config(text=var_phone)
                window_phone.destroy()

            def gocancel():
                window_phone.destroy()

            confirm = tk.Button(window_phone, bg='pink', width=10, height=1, text='Confirm', font=('Arial', 15),
                                command=con_bir)
            confirm.place(x=40, y=160, anchor='nw')
            cancel = tk.Button(window_phone, bg='lightgreen', width=10, height=1, text='Cancel', font=('Arial', 15),
                               command=gocancel)
            cancel.place(x=200, y=160, anchor='nw')
            setpage.wait_window(window_phone)

        phone = tk.Button(setpage, bg='skyblue', width=20, height=1, text='Phone Number', font=('Arial', 15),
                          command=modifyphone)
        phone.place(x=50, y=240, anchor='nw')

        phone_an = tk.Label(setpage, bg='Aliceblue', width=15, height=1, text=var_phone, font=('Arial', 10))
        phone_an.place(x=370, y=245, anchor='nw')

        def goback():
            setpage.destroy()

        back = tk.Button(setpage, bg='lightgreen', width=10, height=2, text='Back', font=('Arial', 20), command=goback)
        back.place(x=220, y=400, anchor='nw')


    setting = tk.Button(mainpage, text='setting ', bg='skyblue', font=('Arial', 15), height=1, width=20,command=set_page)
    setting.place(x=180, y=280)
    # log_out function
    def log_out():
        mainpage.destroy()
    #log out
    logout = tk.Button(mainpage,text='Log out ', bg='skyblue', font=('Arial', 15), height=1, width=20,command=log_out)
    logout.place(x=180, y=380)
#check information
def check_conf1():
    var1=var_email.get()
    var2=var_password.get()
    #if (var1 in emile_list )&(var2 in password_list):
        #main_page()
    login=DB.log_in(var1,var2)
    if login != None and login.type=='P':
        main_page()
        
    else:
        tk.messagebox.showerror(title='Error!',message='Please sign up at first!')
#go to the main page after checking!
confirm1=tk.Button(window,text='Confirm',width=10,height=2,font=('Arial',20),bg='pink',command=check_conf1 )
confirm1.place(x=200,y=300)
#sign up page
def sign_page():
    signpage = tk.Toplevel(window)
    signpage.geometry('600x500')
    signpage.title('Sign up')
    tk.Label(signpage, text='email: ', bg='skyblue', font=('Arial', 15), height=1, width=20).place(x=40, y=60)
    tk.Label(signpage, text='password: ', bg='skyblue', font=('Arial', 15), height=1, width=20).place(x=40, y=140)
    tk.Label(signpage, text='reconfirm:', bg='skyblue', font=('Arial', 15), height=1, width=20).place(x=40, y=220)
    sign_emial = tk.Entry(signpage, font=('Arial', 15))
    sign_emial.place(x=300, y=60)
    sign_password = tk.Entry(signpage, font=('Arial', 15))
    sign_password.place(x=300, y=140)
    sign_recheck = tk.Entry(signpage, font=('Arial', 15))
    sign_recheck.place(x=300, y=220)
    signup = tk.Button(signpage, text='Verify', bg='pink', font=('Arial', 15), height=1, width=20)
    signup.place(x=180, y=310)
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
        var1= sign_emial.get()
        var2 = sign_password.get()
        var3 = sign_recheck.get()
        #check if the password are same for 2 times writing
        if var2!=var3:
            tk.messagebox.showerror(title='Error password',message='please meke sure the password are same!')
            sign_page()
        else:
            emile_list.append(var1)
            password_list.append(var2)
    confirm2 = tk.Button(signpage, text='sign up ', width=20, height=1, font=('Arial', 15), bg='pink',command=check_conf2)
    confirm2.place(x=180, y=390)
#sign up button
signup_button=tk.Button(window, text='sign up',bg='skyblue',font=('Arial',15),height=1,width=20,command=sign_page)
signup_button.place(x=170,y=410)

window.mainloop()