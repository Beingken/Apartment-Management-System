def merror():
    messagebox.showerror('ERROR', 'Module(s) is missing ')
    quit()
    exit()
    # root1 = Tk()
    # root1.title("ERROR")
    # root1.geometry("400x100+500+200")
    # lbl=Label(root1,text="Module Error",font=("arial",20,"bold")).pack()
    # lbl=Label(root1,text="Check that all modules are installed on you computer",font=("arial",10,"bold")).pack()
    # def close():
    #     root1.destroy()
    # btn=ttk.Button(root1,text="Close",width=60,command=close).pack()
    # app.destroy()
try:  
    from tkinter import *
    from tkinter import ttk,messagebox
    from random import randint
    import tkinter as tk
    from PIL import Image,ImageTk
    import time
    import random
    import pymysql 
    from pymysql import Error
    import pymysql
    import xlwt
    import pandas.io.sql as sql
    import os
    import pandas as pd
    import os,sys
    from datetime import date,time
    from datetime import datetime
    from datetime import timedelta
    from tkinter import messagebox as mb
    
    
except:
    merror()
    
    



def main():

    
    app = SampleApp()
    app.mainloop()
    

def ss():
    x="C:/xampp/xampp-control.exe"
    os.startfile(x)



def check_db():
    try:
        
        conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
        
        # my_cursor = conn.cursor()
        
        
        main()
    #     if (conn):
    #         print("Connection successful")
    # # else:
    #     print("Connection Unsuccessful")
        
    except pymysql.err.OperationalError:
        win = Tk()
        win.title("ERROR")
        win.geometry("700x100+500+200")
        lbl=Label(win,text="Connection Unsuccessful",font=("arial",20,"bold")).pack()
        lbl=Label(win,text="On the Xampp Control Panel start the Apache and MySQL options",font=("arial",10,"bold")).pack()
        def close():
            win.destroy()
        btn=ttk.Button(win,text="Close",width=60,command=close).pack()
        def qq():
            win.destroy()
            
            
        win.after(40000,qq)
        
        win.mainloop()
        ss()
    except Error as e:
        messagebox.showwarning('Warning',f'Something went wrong: {str(e)}')
        
        # messagebox.showerror("Connection Unsuccessful","Open Xampp and start MySql connection")
        # print('\n')
        # # messagebox.showwarning('Warning',f'Something went wrong: {str(e)}')
        # print("----------- Connection Unsuccessful ------------------")
        # print('\n')
        # print(" Open Xampp and start MySql connection      ")
             
        # print('\n')
        
class SampleApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

                    

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (start,login,menu,client_window,house_window,report,details,expense_window):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("start")

    def show_frame(self, page_name):
        # '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


        
class start(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        self.controller.title('Start')
        self.controller.geometry("100x100+200+200") 
        try:
            load = Image.open(r"C:\Users\ADMIN\Downloads\Compressed\ken project 2021\Images\image1.jpg")
            load.resize((900,900),Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(load)
            label_image = tk.Label(self,image=photo)
            label_image.image=photo
            label_image.place(x=10,y=140,width=1480,height=800)
        except:
            messagebox.showerror('ERROR', 'Some image(s) is missing')
            self.controller.destroy()
        
        heading_label = tk.Label(self,
                                                     text='WELCOME TO APARTMENT MANAGEMENT SYSTEM',
                                                     font=('orbitron',30,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        heading_label.pack(pady=25)  
         
        user_label = tk.Label(self,
                                                     text='Made By @BeingKen',
                                                     
                                                     font=('orbitron',20,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        user_label.pack()
        
        user_label = tk.Label(self,
                                                     text='LOADING........',
                                                     
                                                     font=('orbitron',30,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        user_label.pack()

        def contt():
            controller.show_frame("login")
            
        self.after(10,contt)
        
class login(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        self.controller.title('Login')
        self.controller.geometry("1500x900+50+100")

        try:
            load = Image.open(r"C:\Users\ADMIN\Downloads\Compressed\ken project 2021\Images\image2.jpg")
            load.resize((900,900),Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(load)
            label_image = tk.Label(self,image=photo)
            label_image.image=photo
            label_image.place(x=10,y=140,width=1480,height=800)
        except:
            messagebox.showerror('ERROR', 'Some image(s) is missing')
            self.controller.destroy()
      
      
        global var_user
        global var_pass


        var_user = StringVar()
        var_pass = StringVar()
        
        def __resett__():
            var_user.set("")
            var_pass.set("")
            
        def __Exitt__():
            self.Exit = messagebox.askokcancel("Apartment System", "Confirm if you want to Exit")
            if self.Exit > 0:
                controller.destroy()

        def verify():
            user = (str(var_user.get()))
            pas = (str(var_pass.get()))
            l=(user,pas)
            
            conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
            my_cursor = conn.cursor()
            sql=("SELECT * FROM `login` where Username = %s and Password = %s")
            
            results = my_cursor.execute(sql,l)
            
            if results == True:
                controller.show_frame('menu')
                var_user.set("")
                var_pass.set("")
                
         
        
            else:
                messagebox.showerror('ERROR', 'incorrect username or password')
                var_user.set("")
                var_pass.set("")
                
        # def forgot():
        #     controller.show_frame('forgot_pass') 
  
        heading_label = tk.Label(self,
                                                     text='APARTMENT MANAGEMENT SYSTEM',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        heading_label.pack(pady=25)   
        
        user_label = tk.Label(self,
                                                     text='Username',
                                                     
                                                     font=('orbitron',20,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        user_label.place(x=200,y=200) 
        
        user_entry = ttk.Entry(self,
                                                     
                                                     font=('orbitron',20,'bold'),
                                                     textvariable=var_user,
                                                      width=22)
        user_entry.place(x=400,y=200)                 
        
        # =========================================
        user_label = tk.Label(self,
                                                     text='Password',
                                                     
                                                     font=('orbitron',20,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        user_label.place(x=200,y=300) 
        
        user_entry = ttk.Entry(self,
                                                     
                                                     font=('orbitron',20,'bold'),
                                                     textvariable=var_pass,show="*",
                                                      width=22)
        user_entry.place(x=400,y=300)    
        
        enter_button =ttk.Button(self,
                                                     text='Login',
                                                     command=verify,
                                                 
                                                    
                                                     width=20,
        )
        enter_button.place(x=200,y=400) 
        
        enter_button =ttk.Button(self,
                                                     text='Reset',
                                                     command=__resett__,
                                                 
                                                    
                                                     width=20,
        )
        enter_button.place(x=400,y=400) 
        
        enter_button =ttk.Button(self,
                                                     text='Exit',
                                                     command=__Exitt__,
                                                 
                                                    
                                                     width=20,
        )
        enter_button.place(x=600,y=400)
        
        # enter_button =ttk.Button(self,
        #                                              text='Forgot Password',
        #                                              command=forgot,
                                                 
                                                    
        #                                              width=70,
        # )
        # enter_button.place(x=200,y=500)
        
        var_date = StringVar()
        var_time = StringVar()
        
        
        def __date__():
            global today
            self.controller.update_idletasks()
            today = date.today()
            now=datetime.now()
            current_time = now.strftime("%H:%M:%S")
            var_date.set(today)
            var_time.set(current_time)
            # lbl_time.config({"background":"red"})
        
        
        # lbl_time = Entry(self,text=var_date,background='#3d3d5c').place(x=900,y=200) 
        # lbl_time = Entry(self,text=var_time,background='#3d3d5c').place(x=900,y=220) 
            lbl_time = Label(self,text=f"Date: {today}",foreground='#ffffff',
                                                     background='#3d3d5c').place(x=200,y=100)
            lbl_time = Label(self,text=f"Time: {current_time}",foreground='#ffffff',
                                                     background='#3d3d5c').place(x=400,y=100)
            

        self.controller.after(1,__date__)   
        
        # __date__()
        
        
# class forgot_pass(tk.Frame):
    
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent,bg='#3d3d5c')
#         self.controller = controller

#         self.controller.title('Login')
#         self.controller.geometry("1500x900+50+100")
        
#         def __back__():
#             controller.show_frame('login')
            
#             var_pass.set("")
#             var_repass.set("")
            
#             var_username.set("")
#             var_reusername.set("")
        
#         heading_label = tk.Label(self,
#                                                      text='Reset Password ',
#                                                      font=('orbitron',45,'bold'),
#                                                      foreground='#ffffff',
#                                                      background='#3d3d5c')
        
#         heading_label.pack(pady=25)  
        
#         enter_button =ttk.Button(self,
#                                                      text='Back',
#                                                      command=__back__,
                                                 
                                                    
#                                                      width=30,
#         )
#         enter_button.place(x=10,y=140) 
        
#         var_pass = StringVar()
#         var_repass = StringVar()
        
#         var_username = StringVar()
#         var_reusername = StringVar()
        
#         def ll():

#             conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
#             my_cursor = conn.cursor()
#             my_cursor.execute("SELECT  `Username`  FROM `login`")
#             row22 = my_cursor.fetchone()

#             var_user.set(row22)

#             conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
#             my_cursor = conn.cursor()
#             my_cursor.execute("SELECT  `Password`  FROM `login`")
#             row33 = my_cursor.fetchone()

#             var_pass.set(row33)

#         def aa():
#             try:
#                 conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
#                 my_cursor = conn.cursor()
#                 my_cursor.execute("UPDATE `login` SET `Username` =  %s  WHERE `Password` =  %s",(

#                                                                             var_username.get(),
#                                                                             var_pass.get(),

#                 ))
                
                                                                                                                                                                                                                                
                                                                                                                                                                                                                                
                                                                        
#                 conn.commit()  
            
#                 conn.close()
                
#                 messagebox.showinfo("Success","Password and Username has been updated successfully ")                                                                                                                                                                                                                                                                                                             
            
#             except Exception as es:
#                 #messagebox.showerror('ERROR', 'Open Xampp and start connection')
#                 messagebox.showwarning('Warning',f'Something went wrong: {str(es)}') 

#             # l=(var_pass.get())
#             # o=(var_username.get())
#             # p=(l,o)
#             # if var_pass.get() == "" or var_repass.get() == "" or var_username.get() == "" or var_reusername.get() == ""  :
                    
                    
#             #         messagebox.showerror("Error","All fields required")
                    
#             # elif var_pass.get() != var_repass.get():
#             #     messagebox.showerror("Error","Password does not match")
                
                
#             # elif var_username.get() != var_reusername.get():
#             #     messagebox.showerror("Error","Username does not match")
                
                
#             # else:
                        
#             #     try:
#             #         conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
#             #         my_cursor = conn.cursor()
#             #         q=("UPDATE `login` SET `Username` =  %s  WHERE `Password` =  %s")
#             #         my_cursor.execute(q,p)
                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                    
                                                                          
#             #         conn.commit()  
                
#             #         conn.close()
                    
#             #         messagebox.showinfo("Success","Password has been updated successfully ")                                                                                                                                                                                                                                                                                                             
                
#             #     except Exception as es:
#             #         #messagebox.showerror('ERROR', 'Open Xampp and start connection')
#             #         messagebox.showwarning('Warning',f'Something went wrong: {str(es)}') 
        
#         ss_label = tk.Label(self,
#                                                      text='Reset Password',
#                                                      font=('orbitron',45,'bold'),
#                                                      foreground='#ffffff',
#                                                      background='#3d3d5c')
        
        
        
#         user_label = tk.Label(self,
#                                                      text='Enter Password',
                                                     
#                                                      font=('orbitron',20,'bold'),
#                                                      foreground='#ffffff',
#                                                      background='#3d3d5c')
#         user_label.place(x=10,y=200) 
        
#         user_entry = ttk.Entry(self,
                                                     
#                                                      font=('orbitron',20,'bold'),
#                                                      textvariable=var_pass,show="*",
#                                                       width=20)
#         user_entry.place(x=300,y=200)                 
        
#         # =========================================
#         # user_label = tk.Label(self,
#         #                                              text='Re-enter Password',
                                                     
#         #                                              font=('orbitron',20,'bold'),
#         #                                              foreground='#ffffff',
#         #                                              background='#3d3d5c')
#         # user_label.place(x=10,y=300) 
        
#         # user_entry = ttk.Entry(self,
                                                     
#         #                                              font=('orbitron',20,'bold'),
#         #                                              textvariable=var_repass,show="*",
#         #                                               width=20)
#         # user_entry.place(x=300,y=300)  
        
        
#         enter_button =ttk.Button(self,
#                                                      text='Autofill',
#                                                      command=ll,
                                                 
                                                    
#                                                      width=20,
#         )
#         enter_button.place(x=200,y=500)

#         enter_button =ttk.Button(self,
#                                                      text='Change Details',
#                                                      command=aa,
                                                 
                                                    
#                                                      width=20,
#         )
#         enter_button.place(x=450,y=500)
        
        
        
        
#         user_label = tk.Label(self,
#                                                      text='Enter Username',
                                                     
#                                                      font=('orbitron',20,'bold'),
#                                                      foreground='#ffffff',
#                                                      background='#3d3d5c')
#         user_label.place(x=700,y=200) 
        
#         user_entry = ttk.Entry(self,
                                                     
#                                                      font=('orbitron',20,'bold'),
#                                                      textvariable=var_username,
#                                                       width=20)
#         user_entry.place(x=1000,y=200)   
        
        
        
#         # user_label = tk.Label(self,
#         #                                              text='Re-Enter Username',
                                                     
#         #                                              font=('orbitron',20,'bold'),
#         #                                              foreground='#ffffff',
#         #                                              background='#3d3d5c')
#         # user_label.place(x=700,y=300) 
        
#         # user_entry = ttk.Entry(self,
                                                     
#         #                                              font=('orbitron',20,'bold'),
#         #                                              textvariable=var_reusername,
#         #                                               width=20)
#         # user_entry.place(x=1000,y=300)  
        
        
        
        
        
class menu(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        self.controller.title('Menu')
        self.controller.geometry("1500x900+50+100")
        
        try:
            load = Image.open(r"C:\Users\ADMIN\Downloads\Compressed\ken project 2021\Images\image3.jpg")
            load.resize((900,900),Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(load)
            label_image = tk.Label(self,image=photo)
            label_image.image=photo
            label_image.place(x=10,y=140,width=1480,height=800)
        except:
            messagebox.showerror('ERROR', 'Some image(s) is missing')
            self.controller.destroy()

        var_welcome = StringVar()

        def __logout__():
            
            controller.show_frame('login')
            
        def __exitt__():
            self.Exit = messagebox.askokcancel("Apartment System", "Confirm if you want to Exit")
            if self.Exit > 0:
                controller.destroy()
            
#============ client window ==========+================
        def client_details():
                
            controller.show_frame("client_window")
            
        def house_booking():
            
            controller.show_frame("house_window")
            
        # def __report__():
            
        #     controller.show_frame('report')
            
        def __report__():
            
            controller.show_frame("report")
            
        def __details__():
            
            controller.show_frame("details")

        def __ex__():
            
            controller.show_frame("expense_window")
            
        def __date__():
            
            global today
            today = date.today()
            now=datetime.now()
            current_time = now.strftime("%H:%M:%S")
            
            # lbl_time.config({"background":"red"})
        
        
        # lbl_time = Entry(self,text=var_date,background='#3d3d5c').place(x=900,y=200) 
        # lbl_time = Entry(self,text=var_time,background='#3d3d5c').place(x=900,y=220) 
            lbl_time = Label(self,text=f"Date: {today}",foreground='#ffffff',
                                                     background='#3d3d5c').place(x=600,y=100) 
            lbl_time = Label(self,text=f"Time: {current_time}",foreground='#ffffff',
                                                     background='#3d3d5c').place(x=800,y=100) 
            

        self.after(10,__date__) 
           
                    
        
            
            
        # def change():
        #     var_welcome.set("Welcome") 
            
        # change()
            
        heading_label = tk.Label(self,
                                                     text='APARTMENT MANAGEMENT SYSTEM',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        heading_label.pack(pady=25)     
        
        menu_label = tk.Label(self,
                                                     text='MENU',
                                                     font=('orbitron',20,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        menu_label.place(x=10,y=100) 

        
        # user_label = Label(self,
        #                                              text=var_user.get(),
        #                                              font=('orbitron',20,'bold'),
        #                                              foreground='#ffffff',
        #                                              background='#3d3d5c')
        # menu_label.pack()
        
        enter_button =ttk.Button(self,
                                                     text='Client',
                                                     command=client_details,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=10,y=140) 
        
        enter_button =ttk.Button(self,
                                                     text='House',
                                                     command=house_booking,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=10,y=180) 
        
        enter_button =ttk.Button(self,
                                                     text='Details',
                                                     command=__details__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=10,y=220) 
        
        enter_button =ttk.Button(self,
                                                     text='Report',
                                                     command=__report__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=10,y=260) 
        
        enter_button =ttk.Button(self,
                                                     text="Log Out",
                                                     command=__logout__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=10,y=340) 
        
        enter_button =ttk.Button(self,
                                                     text='Expenses',
                                                     command=__ex__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=10,y=300) 


        enter_button =ttk.Button(self,
                                                     text='Exit',
                                                     command=__exitt__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=10,y=380) 

class  expense_window(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        self.controller.title('client window')
        self.controller.geometry("1500x900+50+100")
        
        heading_label = tk.Label(self,
                                                     text='EXPENSE DETAILS',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        heading_label.place(x=0,y=0,   width=970,     height=70)
        
        def __logout__():
            
            controller.show_frame('login')
            
        def __menu__():
            controller.show_frame('menu')
            
        def __house__():
            controller.show_frame('house_window')
            
        def __report__():
            controller.show_frame('report')
        def __details__():
            controller.show_frame('details')
        
        enter_button =ttk.Button(self,
                                                     text='Menu',
                                                     command=__menu__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=10,y=100)
        
        enter_button =ttk.Button(self,
                                                     text='House',
                                                     command=__house__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=270,y=100)
        
        enter_button =ttk.Button(self,
                                                     text='Report',
                                                     command=__report__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=530,y=100)
        
        enter_button =ttk.Button(self,
                                                     text='Details',
                                                     command=__details__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=800,y=100)
        
        enter_button =ttk.Button(self,
                                                     text="Log Out",
                                                     command=__logout__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=1100,y=100)
        
        
        
        

        # ============ variables ====================================================



        var_ref = StringVar()
        ex_type = StringVar()
        sp_type = StringVar() 
        debname = StringVar()
        ex_amt = StringVar()
        amt_paid = StringVar()
        var_Payment_Option = StringVar()
        var_Code = StringVar()
        var_Balance = StringVar()
        var_Next_Date = StringVar()


        var_Search_Option_Expense = StringVar()
        var_Search_Expense = StringVar()
        
        def __random__():
            
            y = random.randint(9999, 99999)
            var_ref.set(str(y))

        __random__()
        
        lbl_client_ref = Label(self, text='Expense ref', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=180)
        entry_client_ref = ttk.Entry(self, font=('arial', 10), width=30, textvariable=var_ref,
                                     state='readonly').place(x=110, y=180)

        lbl_gender = Label(self, text='Expense Type', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=220)
                                                                                                           
         
        combo_gender = ttk.Combobox(self, font=('arial', 10), width=27, state='readonly', textvariable=ex_type)
        combo_gender['value'] = ('Select','Electricity', 'Plumbing','Other')
        combo_gender.current(0)
        combo_gender.place( x=110, y=220)

        lbl_fname = Label(self, text='Specify Type', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=260)
        entry_fname = ttk.Entry(self, font=('arial', 10), width=30, textvariable=sp_type).place(x=110,
                                                                                                                 y=260)

        lbl_fname = Label(self, text="Debtor's Name", font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=300)
        entry_fname = ttk.Entry(self, font=('arial', 10), width=30, textvariable=debname).place(x=110,
                                                                                                                 y=300)

        lbl_fname = Label(self, text='Expense Amt', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=340)
        entry_fname = ttk.Entry(self, font=('arial', 10), width=30, textvariable=ex_amt).place(x=110,
                                                                                                                 y=340)

        lbl_fname = Label(self, text='Amt Paid', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=380)
        entry_fname = ttk.Entry(self, font=('arial', 10), width=30, textvariable=amt_paid).place(x=110,
                                                                                                                 y=380)


        lbl_identification_proof = Label(self, text='Pay Option', font=('arial', 10) ,foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=420)
        combo_id = ttk.Combobox(self, font=('arial', 10), width=27, state='readonly',textvariable=var_Payment_Option)
        combo_id['value'] = ("Select","Bank","Mpesa","Airtel Money","T-Kash")
        combo_id.current(0)
        combo_id.place(x=110,  y=420)
        
        lbl_identification_no = Label(self, text='Code', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=460)
        entry_identification_no = ttk.Entry(self, font=('arial', 10), width=30,textvariable=var_Code).place(x=110,  y=460)  
        
        
        lbl_identification_no = Label(self, text='Balance', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=500)
        entry_identification_no = ttk.Entry(self, font=('arial', 10), width=30,textvariable=var_Balance,state='readonly').place(x=110,  y=500)  
        
        lbl_identification_no = Label(self, text='Pay Date', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=540)

        entry_identification_no = ttk.Entry(self, font=('arial', 10), width=30,textvariable=var_Next_Date).place(x=110,  y=540)  

        def calc_expense():
            if ex_amt.get() == "":
                messagebox.showerror('ERROR', 'Enter expense amount')

            elif amt_paid.get() == "":
                messagebox.showerror('ERROR', 'Enter amount paid')

            else:
                x=int(ex_amt.get())
                y=int(amt_paid.get())
                z=int(x-y)

            var_Balance.set(z)

        def __date__():
            global today
            today = date.today()
            now=datetime.now()
            current_time = now.strftime("%H:%M:%S")
            var_Next_Date.set(today)
        

        btnfetch = Button(self, text='Get Date', font=('arial', 10), bg='black', fg='gold',command = __date__).place(x=10, y=580)

        btnfetch = Button(self, text='Calculate', font=('arial', 10), bg='black', fg='gold',command = calc_expense).place(x=110, y=580)

        def dele():
            res= mb.askquestion('Delete expense', 
                         'Do you really want to delete this expense?')

            
            if res == 'yes' :
                dele_cont()

            

            
        def dele_cont():
            conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
            my_cursor = conn.cursor()
            query="DELETE FROM `expense` WHERE  `Expense ref` = %s "
            value = (var_ref.get(),)
            my_cursor.execute(query,value)

            conn.commit()  
            fetch_data()
            conn.close()
            
            messagebox.showinfo("Success","Expense has been deleted successfully ") 
            fetch_data()
        
       

        def cuersor(events=""):
            cursor_rows = self.expense_tables.focus()
            content= self.expense_tables.item(cursor_rows)
            row=content["values"]
            
            var_ref.set(row[0]),
            ex_type.set(row[1]),
            sp_type.set(row[2]), 
            debname.set(row[3]),
            ex_amt.set(row[4]),
            amt_paid.set(row[5]),
            var_Payment_Option.set(row[6]),
            var_Code.set(row[7]),
            var_Balance.set(row[8]),
            var_Next_Date.set(row[9]),

        def clear_tree():
            self.expense_tables.delete(*self.expense_tables.get_children())

        def type():
            sp_type.set("None")

        type()

        def reset_expense():
            __random__()

            ex_type.set("Select")
            sp_type.set("None") 
            debname.set("")
            ex_amt.set("")
            amt_paid.set("")
            var_Payment_Option.set("Select")
            var_Code.set("")
            var_Balance.set("")
            var_Next_Date.set("")

        def fetch_data():
            try:
                conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM `expense`")
                rows = my_cursor.fetchall()
                if len(rows)!= 0:
                    self.expense_tables.delete(*self.expense_tables.get_children())
                    for i in rows:
                        self.expense_tables.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                    # messagebox.showerror('ERROR', 'Open Xampp and start connection')
                    messagebox.showwarning('Warning',f'Something went wrong: {str(es)}')

        def add_expense():
              
            
            if var_ref.get() == "" or debname.get() == "" :
                messagebox.showerror('ERROR', 'All fields are required')
                
                
            
           
            else:
                try:
                    conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
                    my_cursor = conn.cursor()
                    my_cursor.execute('INSERT INTO `expense`  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                                                                                        var_ref.get(),
                                                                                        ex_type.get(),
                                                                                        sp_type.get(), 
                                                                                        debname.get(),
                                                                                        ex_amt.get(),
                                                                                        amt_paid.get(),
                                                                                        var_Payment_Option.get(),
                                                                                        var_Code.get(),
                                                                                        var_Balance.get(),
                                                                                        var_Next_Date.get(),
                                                                                                                
                                                                                                
                                                                                        ))
                                                               

                    conn.commit()  
                    fetch_data()
                    conn.close()
                    
                    
                    messagebox.showinfo('Success','Expense has been added Successfully')
                   
                   
                    
                    
                        
                except Exception as es:
                    # messagebox.showerror('ERROR', 'Open Xampp and start connection')
                    messagebox.showwarning('Warning',f'Something went wrong: {str(es)}')


        def search_Expense():
            
            
            if var_Search_Option_Expense.get() == 'Code':
                pp()
            elif var_Search_Option_Expense.get() == 'Select':
                messagebox.showerror('ERROR', 'Choose a search option')
                
            elif var_Search_Option_Expense.get() == "Expense Ref":
                ii()
                
            
                
        def pp():
            conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
            my_cursor = conn.cursor()
            query=("SELECT * FROM `expense` WHERE `Code` = %s")
            value = (var_Search_Expense.get())
            my_cursor.execute(query,value)
            
            row =  my_cursor.fetchall()
            
            if row ==  None:
                messagebox.showerror('ERROR', 'Code cannot be found')
                  
            elif len(row)!= 0:
                    self.expense_tables.delete(*self.expense_tables.get_children())
                    for i in row:
                        self.expense_tables.insert("",END,values=i)
                    conn.commit()
            conn.close()
            
        def ii():
            conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
            my_cursor = conn.cursor()
            query=("SELECT * FROM `expense` WHERE `Expense ref` = %s")
            value = (var_Search_Expense.get())
            my_cursor.execute(query,value)
            
            row =  my_cursor.fetchall()
            
            if row ==  None:
                messagebox.showerror('ERROR', 'Expense ref cannot be found')
                  
            elif len(row)!= 0:
                    self.expense_tables.delete(*self.expense_tables.get_children())
                    for i in row:
                        self.expense_tables.insert("",END,values=i)
                    conn.commit()
            conn.close()

        
        def update_expense(): 
          
          if ex_amt.get() == "" or amt_paid.get() == "":
                
                
                messagebox.showerror("Error","Enter Expense amount or Amount paid")
          else:
                    
              try:
                conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE `expense` SET `Expense Type` = %s, `Specify Type`= %s ,`Debtors name` = %s,`Expense Amount`= %s, `Amount Paid` = %s,`Pay Option`= %s, `Code`= %s,  `Balance`= %s, `Pay Date` =  %s WHERE `Expense Ref` = %s",(
                                                                                                         
                                                                                        ex_type.get(),
                                                                                        sp_type.get(), 
                                                                                        debname.get(),
                                                                                        ex_amt.get(),
                                                                                        amt_paid.get(),
                                                                                        var_Payment_Option.get(),
                                                                                        var_Code.get(),
                                                                                        var_Balance.get(),
                                                                                        var_Next_Date.get(), 

                                                                                        var_ref.get(),                                                                                                                      
                                                                                                                                                                                                                                 
                                                                                                                                                                                                              
                                                                       
                                                                                                ))
                conn.commit()  
                fetch_data()
                conn.close()
                
                messagebox.showinfo("Success","Expense has been updated successfully ")                                                                                                                                                                                                                                                                                                             
              
              except Exception as es:
                  #messagebox.showerror('ERROR', 'Open Xampp and start connection')
                  messagebox.showwarning('Warning',f'Something went wrong: {str(es)}')    


        def gggg():
            import numpy as np
            import matplotlib.pyplot as plt

            conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT `Expense_Amount`, `Debtors_name` FROM  `expense` ")
            results = my_cursor.fetchall



            Expense_Amount = []
            Debtors_name = []



            for i in my_cursor:
                Expense_Amount.append(i[0])
                Debtors_name.append(i[1])

            plt.bar(Debtors_name,Expense_Amount)
            plt.xlabel("Debtors")
            plt.ylabel("Expense Amount")
            plt.title("Summarized Expense information")
            plt.show()

        
                  



        btnadd = Button(self, text='Add', font=('arial', 10), bg='black', fg='gold', width=10,
                        command=add_expense).place(x=10, y=620)

        btnupdate = Button(self, text='Update', font=('arial', 10), bg='black', fg='gold', width=10,command = update_expense).place(x=120,
                                                                                                                y=620)

        btnreset = Button(self, text='Clear', font=('arial', 10), bg='black', fg='gold', width=10,command=reset_expense).place(x=240, y=620)
        
        btnreset = Button(self, text='Delete', font=('arial', 10), bg='black', fg='gold', width=10,command= dele).place(x=240, y=660)

        btnreset = Button(self, text='Graph', font=('arial', 10), bg='black', fg='gold', width=10,command= gggg).place(x=10, y=660)





        lbl_search = Label(self, text='Search', font=('arial', 10), bg='red', fg='white').place(x=380, y=180)


       

        combo_id = ttk.Combobox(self, font=('arial', 10),state='readonly',textvariable=var_Search_Option_Expense)
        combo_id['value'] = ('Select','Code','Expense Ref')
        combo_id.current(0)
        combo_id.place(x=450, y=180)
        
        entry_search = ttk.Entry(self, font=('arial', 10),textvariable=var_Search_Expense).place(x=640, y=180)

        btnadd = Button(self, text='Search', font=('arial', 10), bg='black', fg='gold',command=search_Expense).place(x=820, y=180)

        btnreset = Button(self, text='Show All', font=('arial', 10), bg='black', fg='gold',command = fetch_data).place(x=900, y=180)

        btnadd = Button(self, text='Hide All', font=('arial', 10), bg='black', fg='gold',command=clear_tree).place(x=1000, y=180)

     
        # ===================== Show data ==========================================

        self.expense_tables= ttk.Treeview(self, columns=('Expense ref', 'Expense Type', 'Specify Type','Debtors Name','Expense Amount', 'Amount Paid','Pay Option', 'Code',  'Balance', 'Pay Date'), selectmode='browse', style="mystyle.Treeview",show=['headings'])

        		#SETTING THE SCROLLBARS
        vsb = Scrollbar(self, orient="vertical", command=self.expense_tables.yview)
        vsb.place(x=1118,y=230,height=330)
        hsb = Scrollbar(self, orient="horizontal", command=self.expense_tables.xview)
        hsb.place(x=390,y=555,width=740)

        self.expense_tables.configure(xscrollcommand=hsb.set,yscrollcommand=vsb.set)
        self.expense_tables.place(x=385, y=225,  width=750,height=350)
        
        self.expense_tables.column('Expense ref',width=100)
        self.expense_tables.column('Expense Type',width=100)
        self.expense_tables.column('Specify Type',width=100)
        self.expense_tables.column('Debtors Name',width=150)
        self.expense_tables.column('Expense Amount',width=150)
        self.expense_tables.column('Amount Paid',width=100)
        self.expense_tables.column('Pay Option',width=100)
        self.expense_tables.column('Code',width=100)
        self.expense_tables.column('Balance',width=100)
        self.expense_tables.column('Pay Date',width=100)
        
        
        self.expense_tables.heading('Expense ref', text='Expense ref')
        self.expense_tables.heading('Expense Type', text='Expense Type')
        self.expense_tables.heading('Specify Type', text='Specify Type')
        self.expense_tables.heading('Debtors Name', text='Debtors Name')
        self.expense_tables.heading('Expense Amount', text='Expense Amount')
        self.expense_tables.heading('Amount Paid', text='Amount Paid')
        self.expense_tables.heading('Pay Option', text='Pay Option')
        self.expense_tables.heading('Code', text='Code')
        self.expense_tables.heading('Balance', text='Balance')
        self.expense_tables.heading('Pay Date', text='Pay Date')
        
        
        self.expense_tables.bind("<ButtonRelease-1>",cuersor)
                                           

        
        


class  client_window(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        self.controller.title('client window')
        self.controller.geometry("1500x900+50+100")
        
        heading_label = tk.Label(self,
                                                     text='CLIENT DETAILS',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        heading_label.place(x=0,y=0,   width=970,     height=70)
        
        def __logout__():
            
            controller.show_frame('login')
            
        def __menu__():
            controller.show_frame('menu')
            
        def __house__():
            controller.show_frame('house_window')
            
        def __report__():
            controller.show_frame('report')
        def __details__():
            controller.show_frame('details')
        
        enter_button =ttk.Button(self,
                                                     text='Menu',
                                                     command=__menu__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=10,y=100)
        
        enter_button =ttk.Button(self,
                                                     text='House',
                                                     command=__house__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=270,y=100)
        
        enter_button =ttk.Button(self,
                                                     text='Report',
                                                     command=__report__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=530,y=100)
        
        enter_button =ttk.Button(self,
                                                     text='Details',
                                                     command=__details__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=800,y=100)
        
        enter_button =ttk.Button(self,
                                                     text="Log Out",
                                                     command=__logout__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=1100,y=100)
        
        
        
        

        # ============ variables ====================================================



        var_ref = StringVar()
        
        def __random__():
            
            x = random.randint(9999, 99999)
            var_ref.set(str(x))

        global var_First_Name 
        var_First_Name = StringVar()
        var_Last_Name = StringVar()
        
        
        var_Nationality = StringVar()
        var_identification_Type = StringVar()
        var_identification_Number = StringVar()
        var_Occupation = StringVar()
        var_Gender = StringVar()
        var_Phone_Number = StringVar()
        var_Marital_Status = StringVar()
        var_Search_Client = StringVar()
        var_Search_Option_client = StringVar()
        
        
        __random__()
        
        
          # ========= label frame =================================================================================================================

        # label_frame_left = LabelFrame(self, bd=2, relief=RIDGE, text='customer Details').place(x=3, y=70,
        #                                                                                             width=350,
        #                                                                                             height=370)

        # ========= label and entries =================================================================================================================

        lbl_client_ref = Label(self, text='client ref', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=180)
        entry_client_ref = ttk.Entry(self, font=('arial', 10), width=30, textvariable=var_ref,
                                     state='readonly').place(x=110, y=180)

        lbl_fname = Label(self, text='First Name', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=220)
        entry_fname = ttk.Entry(self, font=('arial', 10), width=30, textvariable=var_First_Name).place(x=110,
                                                                                                                 y=220)

        lbl_lname = Label(self, text='Last Name', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=260)
        entry_lname = ttk.Entry(self, font=('arial', 10), width=30, textvariable=var_Last_Name).place(x=110, 
                                                                                                                y=260)
        
        
        lbl_gender = Label(self, text='Gender', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=300)
                                                                                                           
         
        combo_gender = ttk.Combobox(self, font=('arial', 10), width=27, state='readonly', textvariable=var_Gender)
        combo_gender['value'] = ('Select','Male', 'Female')
        combo_gender.current(0)
        combo_gender.place( x=110, y=300)
        
        lbl_gender = Label(self, text='Marital Status', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10,
                                                                                                                 y=340)
        combo_gender = ttk.Combobox(self, font=('arial', 10), width=27, state='readonly', textvariable=var_Marital_Status)
        combo_gender['value'] = ('Select','Single', 'Married')
        combo_gender.current(0)
        combo_gender.place(x=110, y=340)

        lbl_identification_proof = Label(self, text='ID Type', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c' ).place(x=10,
                                                                                                                 y=380)
        combo_id = ttk.Combobox(self, font=('arial', 10), width=27, state='readonly',textvariable=var_identification_Type)
        combo_id['value'] = ('Select','National ID', 'Passport')
        combo_id.current(0)
        combo_id.place(x=110, y=380)
        
        lbl_identification_no = Label(self, text='ID Number', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=420)
        entry_identification_no = ttk.Entry(self, font=('arial', 10), width=30, textvariable=var_identification_Number).place(x=110,
                                                                                                                 y=420)
        
        
        lbl_nationality = Label(self, text='Nationality', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=460)
        entry_nationality = ttk.Entry(self, font=('arial', 10), width=30, textvariable=var_Nationality).place(
            x=110, y=460)
        
        lbl_occupation = Label(self, text='Occupation', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=500)
        entry_occupation = ttk.Entry(self, font=('arial', 10), width=30, textvariable=var_Occupation).place(
             x=110, y=500)
        
        
        lbl_phone = Label(self, text='Phone Number', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=540)
        entry_phone = ttk.Entry(self, font=('arial', 10), width=30, textvariable=var_Phone_Number).place(
             x=110, y=540)
        
        def __proceed__():
            add_data()
       
                
        
        def clear():
            var_First_Name.set("")
            var_Last_Name.set("")
            var_Nationality.set("")
            var_identification_Type.set("Select")
            var_identification_Number.set("")
            var_Occupation.set("")
            var_Gender.set("Select")
            var_Phone_Number.set("")
            var_Marital_Status.set("Select")
            
           
            __random__()
          
        
        # def nextt():
        #     print ('next button was clicked')

        #     add_data()
            
        #     # if self.var_Marital_Status.get() == "Married" and add_data() == True :  
        #     #     return # reset_data_spouse()
        #     #     status()

        def add_data():
              
            
            if var_First_Name.get() == '' or var_Last_Name.get() == '' or var_Nationality.get() == '' or var_identification_Number.get() == '' or var_Occupation.get() == '' or var_Phone_Number.get() == '':
                messagebox.showerror('ERROR', 'All fields are required')
                
                
            elif var_identification_Type.get() == "Select" or var_Gender.get() == "Select" or var_Marital_Status.get() == "Select" :
                
                messagebox.showerror('ERROR', 'Check gender or identification type or marital status ')
                
            elif len(var_Phone_Number.get()) < 10 :
                messagebox.showerror('PHONE ERROR', 'Phone Number Must be 10 digits or more')
                
            elif len(var_identification_Number.get() ) < 8:
                messagebox.showerror('ID ERROR', 'ID Number Must be 8 digits or more ')
                
            
            elif  var_Phone_Number.get().isalpha() or var_identification_Number.get().isalpha():
                messagebox.showerror('ERROR', 'Phone Number or ID Number cannot be letters ')
                
    
           
           
            else:
                try:
                    conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
                    my_cursor = conn.cursor()
                    my_cursor.execute('INSERT INTO `client details`  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                                                                                                                var_ref.get(),
                                                                                                                var_First_Name.get(),
                                                                                                                var_Last_Name.get(),
                                                                                                                var_Gender.get(),
                                                                                                                var_Marital_Status.get(),
                                                                                                                var_identification_Type.get(),
                                                                                                                var_identification_Number.get(),
                                                                                                                var_Nationality.get(),
                                                                                                                var_Occupation.get(),
                                                                                                                var_Phone_Number.get()
                                                                                                
                                                                                                                                            ))
                                                               

                    conn.commit()  
                    fetch_data()
                    conn.close()
                    
                    
                    messagebox.showinfo('Success',f'{var_First_Name.get()} {var_Last_Name.get()} has been added Successfully')
                   
                   
                    
                    
                        
                except Exception as es:
                    # messagebox.showerror('ERROR', 'Open Xampp and start connection')
                    messagebox.showwarning('Warning',f'Something went wrong: {str(es)}')
                    
        def login():
            
            
            root = Tk()
            root.maxsize(width=500,height=500)
            root.minsize(width=500,height=500)
            root.config(bg="#3d3d5c")
            root.title("Delete Confirmation")

            
            
            def verify():
                user = (str(var_user.get()))
                pas = (str(var_pass.get()))
                l=(user,pas)
                
                conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
                my_cursor = conn.cursor()
                sql=("SELECT * FROM `login` where Username = %s and Password = %s")
                
                results = my_cursor.execute(sql,l)
                
                if results == True:
                    dele_cont()
                    messagebox.showerror('SUCCESS', 'Record Deleted Successfully',parent=root)
                    var_user.set("")
                    var_pass.set("")
                    root.destroy()
                
                else:
                    messagebox.showerror('ERROR', 'incorrect username or password',parent=root)
                    var_user.set("")
                    var_pass.set("")
            
            
            lbl_user = Label(root,text="Delete Confirmation",font=("arial",20,"bold"),foreground='#ffffff',
                                                            background='#3d3d5c').pack()
            
            lbl_user = Label(root,text="Username",font=("arial",20,"bold"),foreground='#ffffff',
                                                            background='#3d3d5c').place(x=50,y=100)
            lbl_user = ttk.Entry(root,width=15,textvariable=var_user,font=('orbitron',20,'bold')).place(x=200,y=110)
            
            lbl_user = Label(root,text="Password",font=("arial",20,"bold"),foreground='#ffffff',
                                                            background='#3d3d5c').place(x=50,y=200)
            lbl_user = ttk.Entry(root,width=15,textvariable=var_pass,show="*",font=('orbitron',20,'bold')).place(x=200,y=210)
            
            btn = ttk.Button(root,text="Confrim Delete",width=20,command=verify).place(x=200,y=300)
            
            
            lbl_user = Label(root,text="By clicking 'Confirm Delete'\n the record will be deleted permenatly",font=("arial",10,"bold"),foreground='#ffffff',
                                                            background='#3d3d5c').place(x=100,y=400)
            
            
            
            root.mainloop()

        def dele():
            res= mb.askquestion('Delete Contact', 
                         'Do you really want to delete this contact?')

            
            if res == 'yes' :
                dele_cont()

            

            
        def dele_cont():
            conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
            my_cursor = conn.cursor()
            query="DELETE FROM `client details` WHERE  `Client ref` = %s "
            value = (var_ref.get(),)
            my_cursor.execute(query,value)

            conn.commit()  
            fetch_data()
            conn.close()
            
            messagebox.showinfo("Success","Client details has been deleted successfully ") 
    
        
        def delete_data():
            
            
            # conn.commit()  
            # fetch_data()
            # conn.close()
            
            conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
            my_cursor = conn.cursor()
            q="INSERT INTO `client deleted` SELECT * FROM `client details` WHERE  `Client ref` = %s "
            query="DELETE FROM `client details` WHERE  `Client ref` = %s "
            value = (var_ref.get(),)
            my_cursor.execute(q,query,value)
            
            
            
            conn.commit()  
            fetch_data()
            conn.close()
            
            messagebox.showinfo("Success","Client details has been deleted successfully ")  
            
         
            
            
        
        def update_data(): 
            # if var_Phone_Number == "":
            #     messagebox.showerror("Error","Enter Phone Number")
                
            if var_First_Name.get() == '' or var_Last_Name.get() == '' or var_Nationality.get() == '' or var_identification_Number.get() == '' or var_Occupation.get() == '' or var_Phone_Number.get() == '':
                messagebox.showerror('ERROR', 'All fields are required')
                
                
            elif var_identification_Type.get() == "Select" or var_Gender.get() == "Select" or var_Marital_Status.get() == "Select" :
                
                messagebox.showerror('ERROR', 'Check gender or identification type or marital status ')
                
            elif len(var_Phone_Number.get()) < 10 or len(var_Phone_Number.get()) > 10 :
                messagebox.showerror('PHONE ERROR', 'Phone Number Must be 10 digits ')
                
            elif len(var_identification_Number.get() ) < 8:
                messagebox.showerror('ID ERROR', 'ID Number Must be 8 digits or more ')
                
            
            elif  var_Phone_Number.get().isalpha() or var_identification_Number.get().isalpha():
                messagebox.showerror('ERROR', 'Phone Number or ID Number cannot be letters ')
            
            else:
                try:
                    conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE `client details` SET  `First Name` = %s, `Last Name` = %s,`Gender`= %s ,`Marital Status` =  %s ,`ID Type`= %s, `ID Number` = %s,`Nationality` = %s,`Occupation` = %s, `Phone Number` = %s WHERE `Client ref` = %s",(
                    
                    
                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                    var_First_Name.get(),
                                                                                                                                                                                                                                    var_Last_Name.get(),
                                                                                                                                                                                                                                    var_Gender.get(),
                                                                                                                                                                                                                                    var_Marital_Status.get(),
                                                                                                                                                                                                                                    var_identification_Type.get(),
                                                                                                                                                                                                                                    var_identification_Number.get(),
                                                                                                                                                                                                                                    var_Nationality.get(),
                                                                                                                                                                                                                                    var_Occupation.get(),
                                                                                                                                                                                                                                    var_Phone_Number.get(),
                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                    var_ref.get() ,
                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                        ))
                    
                    
                    conn.commit()  
                    fetch_data()
                    conn.close()
                    
                    messagebox.showinfo("Success","Client details has been updated successfully ")                                                                                                                                                                                                                                                                                                             
                    
                except Exception as es:
                    #messagebox.showerror('ERROR', 'Open Xampp and start connection')
                    messagebox.showwarning('Warning',f'Something went wrong: {str(es)}')    
                    
                    
                   
       # ================= btn frame ========================================================================

        
        btnadd = Button(self, text='Add', font=('arial', 10), bg='black', fg='gold', width=10,
                        command=__proceed__).place(x=10, y=600)

        btnupdate = Button(self, text='Update', font=('arial', 10), bg='black', fg='gold', width=10,command = update_data).place(x=120,
                                                                                                                y=600)

        btnreset = Button(self, text='Clear', font=('arial', 10), bg='black', fg='gold', width=10,command=clear).place(x=240, y=600)
        
        btnreset = Button(self, text='Delete', font=('arial', 10), bg='black', fg='gold', width=10,command=dele).place(x=240, y=650)
                                           

        
          # ======================== tableframe ==================================================================

        def search_client():
            
            
            if var_Search_Option_client.get() == 'Phone Number':
                pp()
            elif var_Search_Option_client.get() == 'Select':
                messagebox.showerror('ERROR', 'Choose a search option')
                
            elif var_Search_Option_client.get() == "ID Number":
                ii()
                
            elif var_Search_Option_client.get() == 'Client Ref':
                cc()
                
        def pp():
            conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
            my_cursor = conn.cursor()
            query=("SELECT * FROM `client details` WHERE `Phone Number` = %s")
            value = (var_Search_Client.get())
            my_cursor.execute(query,value)
            
            row =  my_cursor.fetchall()
            
            if row ==  None:
                messagebox.showerror('ERROR', 'Number cannot be found')
                  
            elif len(row)!= 0:
                    self.customer_details_tables.delete(*self.customer_details_tables.get_children())
                    for i in row:
                        self.customer_details_tables.insert("",END,values=i)
                    conn.commit()
            conn.close()
            
        def ii():
            conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
            my_cursor = conn.cursor()
            query=("SELECT * FROM `client details` WHERE `ID Number` = %s")
            value = (var_Search_Client.get())
            my_cursor.execute(query,value)
            
            row =  my_cursor.fetchall()
            
            if row ==  None:
                messagebox.showerror('ERROR', 'Number cannot be found')
                  
            elif len(row)!= 0:
                    self.customer_details_tables.delete(*self.customer_details_tables.get_children())
                    for i in row:
                        self.customer_details_tables.insert("",END,values=i)
                    conn.commit()
            conn.close()
            
        def cc():
            conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
            my_cursor = conn.cursor()
            query=("SELECT * FROM `client details` WHERE `Client Ref` = %s")
            value = (var_Search_Client.get())
            my_cursor.execute(query,value)
            
            row =  my_cursor.fetchall()
            
            if row ==  None:
                messagebox.showerror('ERROR', 'Number cannot be found')
                  
            elif len(row)!= 0:
                    self.customer_details_tables.delete(*self.customer_details_tables.get_children())
                    for i in row:
                        self.customer_details_tables.insert("",END,values=i)
                    conn.commit()
            conn.close()
                
            
          

        
        def fetch_data():
            try:
                conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM `client details`")
                rows = my_cursor.fetchall()
                if len(rows)!= 0:
                    self.customer_details_tables.delete(*self.customer_details_tables.get_children())
                    for i in rows:
                        self.customer_details_tables.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                    # messagebox.showerror('ERROR', 'Open Xampp and start connection')
                    messagebox.showwarning('Warning',f'Something went wrong: {str(es)}')
                    
        
        def cuersor(events=""):
            cursor_rows = self.customer_details_tables.focus()
            content= self.customer_details_tables.item(cursor_rows)
            row=content["values"]
            
            var_ref.set(row[0]),
            var_First_Name.set(row[1]),
            var_Last_Name.set(row[2]),
            var_Gender.set(row[3]),
            var_Marital_Status.set(row[4])
            var_identification_Type.set(row[5]),
            var_identification_Number.set(row[6]),
            var_Nationality.set(row[7]),
            var_Occupation.set(row[8]),
            var_Phone_Number.set(row[9]),
            
        def clear_tree():
            self.customer_details_tables.delete(*self.customer_details_tables.get_children())
           
            
        
        
        lbl_search = Label(self, text='Search', font=('arial', 10), bg='red', fg='white').place(x=380, y=180)
       

        combo_id = ttk.Combobox(self, font=('arial', 10),state='readonly',textvariable=var_Search_Option_client)
        combo_id['value'] = ('Select','Phone Number', 'ID Number','Client Ref')
        combo_id.current(0)
        combo_id.place(x=450, y=180)
        
        entry_search = ttk.Entry(self, font=('arial', 10),textvariable=var_Search_Client).place(x=640, y=180)

        btnadd = Button(self, text='Search', font=('arial', 10), bg='black', fg='gold',command=search_client).place(x=820, y=180)

        btnreset = Button(self, text='Show All', font=('arial', 10), bg='black', fg='gold',command = fetch_data).place(x=900, y=180)

        btnadd = Button(self, text='Hide All', font=('arial', 10), bg='black', fg='gold',command=clear_tree).place(x=1000, y=180)

     
        # ===================== Show data ==========================================

        self.customer_details_tables= ttk.Treeview(self, columns=('Client ref', 'First Name', 'Last Name','Gender','Marital Status', 'ID Type','ID Number', 'Nationality',  'Occupation', 'Phone Number'), selectmode='browse', style="mystyle.Treeview",show=['headings'])

        		#SETTING THE SCROLLBARS
        vsb = Scrollbar(self, orient="vertical", command=self.customer_details_tables.yview)
        vsb.place(x=1118,y=230,height=330)
        hsb = Scrollbar(self, orient="horizontal", command=self.customer_details_tables.xview)
        hsb.place(x=390,y=555,width=740)

        self.customer_details_tables.configure(xscrollcommand=hsb.set,yscrollcommand=vsb.set)
        self.customer_details_tables.place(x=385, y=225,  width=750,height=350)
        
        self.customer_details_tables.column('Client ref',width=100)
        self.customer_details_tables.column('First Name',width=100)
        self.customer_details_tables.column('Last Name',width=100)
        self.customer_details_tables.column('Gender',width=100)
        self.customer_details_tables.column('Nationality',width=100)
        self.customer_details_tables.column('ID Type',width=100)
        self.customer_details_tables.column('ID Number',width=100)
        self.customer_details_tables.column('Occupation',width=100)
        self.customer_details_tables.column('Phone Number',width=100)
        self.customer_details_tables.column('Marital Status',width=100)
        
        self.customer_details_tables.heading('Client ref', text='Client ref')
        self.customer_details_tables.heading('First Name', text='First Name')
        self.customer_details_tables.heading('Last Name', text='Last Name')
        self.customer_details_tables.heading('Gender', text='Gender')
        self.customer_details_tables.heading('Nationality', text='Nationality')
        self.customer_details_tables.heading('ID Type', text='ID Type')
        self.customer_details_tables.heading('ID Number', text='ID Number')
        self.customer_details_tables.heading('Occupation', text='Occupation')
        self.customer_details_tables.heading('Phone Number', text='Phone Number')
        self.customer_details_tables.heading('Marital Status', text='Marital Status')
        
        self.customer_details_tables.bind("<ButtonRelease-1>",cuersor)
        # fetch_data()
       
        


class  house_window(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        self.controller.title('House window')
        self.controller.geometry("1500x900+50+100")
        
        heading_label = tk.Label(self,
                                                     text='HOUSE DETAILS',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        heading_label.place(x=0,y=0,   width=970,     height=70)
        
        def __logout__():
            
            controller.show_frame('login')
            
        def __menu__():
            controller.show_frame('menu')
            
        def __client__():
            controller.show_frame('client_window')
            
        def __report__():
            controller.show_frame('report')
            
        def __details__():
            controller.show_frame('details')
        
        

        enter_button =ttk.Button(self,
                                                     text='Menu',
                                                     command=__menu__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=10,y=100)
        
        enter_button =ttk.Button(self,
                                                     text='Client',
                                                     command=__client__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=270,y=100)
        
        enter_button =ttk.Button(self,
                                                     text='Report',
                                                     command=__report__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=530,y=100)
        
        enter_button =ttk.Button(self,
                                                     text='Details',
                                                     command=__details__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=800,y=100)
        enter_button =ttk.Button(self,
                                                     text="Log Out",
                                                     command=__logout__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=1100,y=100)


        var_Contact = StringVar()
        var_Date=StringVar()
        var_Apartment_Type=StringVar()
        var_Available_House = StringVar()
        var_Deposit= StringVar()
        var_Rent= StringVar() 
        var_water= StringVar() 
        var_electricity= StringVar() 
        var_security= StringVar() 
        var_garbage= StringVar() 
        
        def check_price():
            
            if var_Apartment_Type.get() == "4 Bedroom":
                bed_four()
            elif var_Apartment_Type.get() == "3 Bedroom":
                bed_three()
            elif var_Apartment_Type.get() == "2 Bedroom":
                bed_two()
            elif var_Apartment_Type.get() == "1 Bedroom":
                bed_one()
            elif var_Apartment_Type.get() == "Select":
                messagebox.showerror("Error","Choose an option")
                
                
        def bed_four():
           
            var_Rent.set(250000) 
            var_Deposit.set(250000) 
            
            var_water.set(10000)
            var_electricity.set(10000)
            var_security.set(10000)
            var_garbage.set(10000)
            
        def bed_three():
            var_Rent.set(150000)
            var_Deposit.set(150000)
            
            var_water.set(10000)
            var_electricity.set(10000)
            var_security.set(10000)
            var_garbage.set(10000)
            
        def bed_two():
            var_Rent.set(100000)
            var_Deposit.set(100000)
            
            var_water.set(10000)
            var_electricity.set(10000)
            var_security.set(10000)
            var_garbage.set(10000)
            
        def bed_one():
            var_Rent.set(50000)
            var_Deposit.set(50000)
            
            var_water.set(10000)
            var_electricity.set(10000)
            var_security.set(10000)
            var_garbage.set(10000)
            
        def calc():
            if  var_Date.get() == "":
                messagebox.showerror('ERROR', 'Please enter Date')
            elif var_Rent.get() == "":
                messagebox.showerror('ERROR', 'Rent is blank')
            elif var_Amt_Paid.get() == "":
                messagebox.showerror('ERROR', 'Please enter Amount paid') 
            
            try:
                q1 = int(var_Rent.get())
                q2= int(var_Amt_Paid.get())
                q3 = int(q1-q2)
                
                var_Balance.set(q3)
            except ValueError:
                messagebox.showerror('ERROR', 'Invalid Amount Format') 

            try:
            
                d= (var_Date.get())
                begin=datetime.strptime(d,"%Y-%m-%d")
                enddate=begin+timedelta(days=30)
                var_Next_Date.set(enddate)

            except ValueError: 
                messagebox.showerror('ERROR', 'Invalid Date Format')
                messagebox.showinfo('Date Format', 'Use eg 2020-12-31')  
            
        
        
        def fetch_contact():
              if var_Contact.get() == "":
                messagebox.showerror('ERROR', 'Please enter contact number')
              
              else:
                  
                        
                conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
                my_cursor = conn.cursor()
                query=("SELECT `First Name` FROM `client details` WHERE `Phone Number` = %s")
                value = (var_Contact.get())
                my_cursor.execute(query,value)
                row =  my_cursor.fetchone()
                
                if row ==  None:
                    messagebox.showerror('ERROR', 'Number cannot be found')
                else:
                    conn.commit()
                    conn.close()
                    
                    
                    
                    lblname=Label(self,text="First Name: ",font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=740,y=180)
                    
                    lbl = Label(self,text=row,font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=840,y=180)
                    
                    
                    conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
                    my_cursor = conn.cursor()
                    query=("SELECT `Last Name` FROM `client details` WHERE `Phone Number` = %s")
                    value = (var_Contact.get())
                    my_cursor.execute(query,value)
                    row =  my_cursor.fetchone()
                    
                    if row ==  None:
                        messagebox.showerror('ERROR', 'Number cannot be found')
                    else:
                        conn.commit()
                        conn.close()
                    
                    lblgender=Label(self,text="Second Name: ",font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=740,y=220)
                    
                    lbl2 = Label(self,text=row,font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=840,y=220)
                  
     

        def cuersor(events=""):
            cursor_rows = self.customer_details_tables.focus()
            content= self.customer_details_tables.item(cursor_rows)
            row=content["values"]
            
            var_Contact.set(row[0]),
          
            var_Apartment_Type.set(row[1]),
            var_Available_House.set(row[2]),
            var_Deposit.set(row[3]),
            var_Rent.set(row[4]),
            var_water.set(row[5]),
            var_electricity.set(row[6]),
            var_security.set(row[7]),
            var_garbage.set(row[8]),
            var_Date.set(row[9]),
            var_Payment_Option.set(row[10]),
            var_Code.set(row[11]),
            var_Amt_Paid.set(row[12]),
            var_Balance.set(row[13]),
           
                        
        def fetch_data_house():
            try:
                conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM `house`")
                rows = my_cursor.fetchall()
                if len(rows)!= 0:
                    self.customer_details_tables.delete(*self.customer_details_tables.get_children())
                    for i in rows:
                        self.customer_details_tables.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                    #messagebox.showerror('ERROR', 'Open Xampp and start connection')
                    messagebox.showwarning('Warning',f'Something went wrong: {str(es)}')
                    
                    
        def update_data_house(): 
          
          if var_Contact == "":
                
                
                messagebox.showerror("Error","Enter Phone Number")
          else:
                    
              try:
                conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE `house` SET `Apartment Type` = %s, `House Number` = %s, `Deposit` = %s, `Rent`= %s,`Water` = %s, `Electricity` = %s,`Security` = %s,`Garbage` = %s, `Date Entered`= %s ,`Pay Opt` =  %s ,`Code` =  %s ,`Amt Paid` =  %s ,`Balance` =  %s WHERE `Client Contact` = %s",(
                                                                                                                                                                                                                                
                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                var_Apartment_Type.get(),
                                                                                                                                                                                                                                var_Available_House.get(),
                                                                                                                                                                                                                                var_Deposit.get(),
                                                                                                                                                                                                                                var_Rent.get(),
                                                                                                                                                                                                                                var_water.get(),
                                                                                                                                                                                                                                var_electricity.get(),
                                                                                                                                                                                                                                var_security.get(),
                                                                                                                                                                                                                                var_garbage.get(),
                                                                                                                                                                                                                                var_Date.get(),
                                                                                                                                                                                                                                var_Payment_Option.get(),
                                                                                                                                                                                                                                var_Code.get(),
                                                                                                                                                                                                                                var_Amt_Paid.get(),
                                                                                                                                                                                                                                var_Balance.get(),
                                                                                                                                                                                                                                
                                                                                                                                                                                                                                var_Contact.get(),
                                                                                                                                                                                                                                
                                                                                                                                                                                                                                    ))
                conn.commit()  
                fetch_data_house()
                conn.close()
                
                messagebox.showinfo("Success","House details has been updated successfully ")                                                                                                                                                                                                                                                                                                             
              
              except Exception as es:
                  #messagebox.showerror('ERROR', 'Open Xampp and start connection')
                  messagebox.showwarning('Warning',f'Something went wrong: {str(es)}')    
                  

       # ========= label and entries =================================================================================================================

        lbl_contact = Label(self, text='client contact', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=180)
        entry_contact = ttk.Entry(self, font=('arial', 10), width=20,textvariable=var_Contact ).place(x=110, y=180)
                                   
        
        btnfetch = Button(self, text='Fetch data', font=('arial', 10), bg='black', fg='gold',command = fetch_contact).place(x=260, y=180)
                        
        def __date__():
            global today
            today = date.today()
            now=datetime.now()
            current_time = now.strftime("%H:%M:%S")
            var_Date.set(today)
            
            # lbl_time.config({"background":"red"})
        
        
        # lbl_time = Entry(self,text=var_date,background='#3d3d5c').place(x=900,y=200) 
        # lbl_time = Entry(self,text=var_time,background='#3d3d5c').place(x=900,y=220) 
            # lbl_time = Label(self,text=f"Date: {today}",foreground='#ffffff',
            #                                          background='#3d3d5c').place(x=900,y=200) 
            # lbl_time = Label(self,text=f"Time: {current_time}",foreground='#ffffff',
            #                                          background='#3d3d5c').place(x=900,y=220)         
                
        
        lbl_date = Label(self, text='Date Entered', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=540)
        entry_date = ttk.Entry(self, font=('arial', 10), width=20,textvariable=var_Date).place(x=110, y=540)
        
        btnfetch = Button(self, text='Get Date', font=('arial', 10), bg='black', fg='gold',command = __date__).place(x=260, y=540)
        
                                                                                                            
        # conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
        # my_cursor = conn.cursor()
        # my_cursor.execute("SELECT  `Apartment Type`  FROM `details`")
        # rows = my_cursor.fetchall()
        
        lbl_identification_proof = Label(self, text='Apartment Type', font=('arial', 10) ,foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=220)
        combo_id = ttk.Combobox(self, font=('arial', 10), width=27, state='readonly',textvariable=var_Apartment_Type)
        combo_id['value'] = ("Select","4 Bedroom","3 Bedroom","2 Bedroom","1 Bedroom")
        combo_id.current(0)
        combo_id.place(x=110,  y=220)
        
        
        conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT  `House Number`  FROM `details`")
        row2 = my_cursor.fetchall()
        
        lbl_identification_proof = Label(self, text='House Number', font=('arial', 10) ,foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=260)
        combo_id = ttk.Combobox(self, font=('arial', 10), width=27, state='readonly',textvariable=var_Available_House)
        combo_id['value'] = row2
        combo_id.current(0)
        combo_id.place(x=110, y=260)
        
       

     
        lbl_nationality = Label(self, text='Deposit', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10,y=300)
                                                                                                                 
        entry_nationality = ttk.Entry(self, font=('arial', 10), width=30,textvariable=var_Deposit,state='readonly').place(x=110, y=300)  
        
        lbl_identification_no = Label(self, text='Rent', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=340)
        entry_identification_no = ttk.Entry(self, font=('arial', 10), width=30,textvariable=var_Rent,state='readonly').place(x=110,  y=340)  
        
        
        
        lbl_identification_no = Label(self, text='Water', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=380)
        lbl_test= ttk.Entry(self, font=('arial', 10),state='readonly',textvariable=var_water, width=30).place(x=110,  y=380) 
        # entry_identification_no = ttk.Entry(self, font=('arial', 10), width=30,textvariable=var_water,state='readonly').place(x=110,  y=340)  
        
        lbl_identification_no = Label(self, text='Electricity', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=420)
        entry_identification_no = ttk.Entry(self, font=('arial', 10), width=30,textvariable=var_electricity,state='readonly').place(x=110,  y=420)  
        
        lbl_identification_no = Label(self, text='Security', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=460)
        entry_identification_no = ttk.Entry(self, font=('arial', 10), width=30,textvariable=var_security,state='readonly').place(x=110,  y=460)  
        
        lbl_identification_no = Label(self, text='Garbage', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=500)
        entry_identification_no = ttk.Entry(self, font=('arial', 10), width=30,textvariable=var_garbage,state='readonly').place(x=110,  y=500)  
        
        btnfetch = Button(self, text='check price', font=('arial', 10), bg='black', fg='gold',command = check_price).place(x=240, y=600)
        
     #============ payment =====[========================]   
     
        var_Payment_Option = StringVar()
        var_Code = StringVar()
        var_Amt_Paid = StringVar()
        var_Balance = StringVar()
        
        var_Next_Date = StringVar()
        
        
        
        lbl_identification_proof = Label(self, text='Pay Option', font=('arial', 10) ,foreground='#ffffff',
                                                     background='#3d3d5c').place(x=350, y=180)
        combo_id = ttk.Combobox(self, font=('arial', 10), width=27, state='readonly',textvariable=var_Payment_Option)
        combo_id['value'] = ("Select","Bank","Mpesa","Airtel Money","T-Kash")
        combo_id.current(0)
        combo_id.place(x=440,  y=180)
        
        lbl_identification_no = Label(self, text='Code', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=350, y=220)
        entry_identification_no = ttk.Entry(self, font=('arial', 10), width=30,textvariable=var_Code).place(x=440,  y=220)  
        
        lbl_identification_no = Label(self, text='Amt Paid', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=350, y=260)
        entry_identification_no = ttk.Entry(self, font=('arial', 10), width=30,textvariable=var_Amt_Paid).place(x=440,  y=260)  
        
        lbl_identification_no = Label(self, text='Balance', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=350, y=300)
        entry_identification_no = ttk.Entry(self, font=('arial', 10), width=30,textvariable=var_Balance,state='readonly').place(x=440,  y=300)  
        
        lbl_identification_no = Label(self, text='Pay Date', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=350, y=340)
       
        entry_identification_no = ttk.Entry(self, font=('arial', 10), width=30,textvariable=var_Next_Date,state='readonly').place(x=440,  y=340)  
        
        btnfetch = Button(self, text='Calculate', font=('arial', 10), bg='black', fg='gold',command = calc).place(x=440, y=400)
        
        def www():
            y = random.randint(9999, 99999)

            file = (f"C:/Users/Mercy/Desktop/ken project 2021/Receipts/test.txt")
            new= open(file,"w")
            
            new.write(f"========= RECEIPT NO {y} ========= \n ")
            new.write(f"Client contact\t\t\t{var_Contact.get()} \n")
            new.write(f"Apartment Type\t\t\t{var_Apartment_Type.get()} \n")
            new.write(f"House Number\t\t\t{var_Available_House.get()}  \n")
            new.write(f"Rent\t\t\t\t{var_Rent.get()}  \n")
            new.write(f"Date Entered\t\t\t{var_Date.get()} \n ")
            new.write(f"Amount Paid\t\t\t{var_Amt_Paid.get()} \n ")
            new.write(f"Pay Option\t\t\t{var_Payment_Option.get()} \n ")
            new.write(f"Code\t\t\t\t{var_Code.get()} \n")
            new.write(f"Balance\t\t\t\t{var_Balance.get()}  \n")
            new.write(f"Next Pay Date\t\t\t{var_Next_Date.get()} \n ")
            new.write("================================================\n")

            new.close()

            try:
               

                files=r"C:/Users/Mercy/Desktop/ken project 2021/Receipts/test.txt"
                os.startfile(files)
                os.startfile(file,'Print')
            except:
                messagebox.showerror('Error','File Not Found')



            

        btnfetch = Button(self, text='Receipt', font=('arial', 10), bg='black', fg='gold',command = www).place(x=440, y=440)
        
        
        def clear_house():
                
            var_Contact.set("")
            var_Date.set("")
            var_Apartment_Type.set("Select")
            var_Available_House.set("")
            var_Deposit.set("")
            var_Rent.set("")
            
            var_Payment_Option.set("Select")
            var_Code.set("")
            var_Amt_Paid.set("")
            var_Balance.set("")
            
            
            var_water.set("")
            var_electricity.set("") 
            var_security.set("")
            var_garbage.set("")
        
            
            

            
        def add_house():
              
          
            
        
            if var_Contact.get() == '' or var_Date.get() == '' or var_Apartment_Type == "Select" or  var_water.get() == "" or var_electricity.get() == "" or var_security.get() == "" or var_garbage.get() == "" or var_Code.get() == "" or var_Amt_Paid.get() == "" or var_Balance.get() == "" or var_Rent.get() == "" or  var_Deposit.get() == "":
                messagebox.showerror('ERROR', 'All fields are required')
                
     
        
            else:
                try:
                
                    conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
                    my_cursor = conn.cursor()
                    my_cursor.execute('INSERT INTO house  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                                                                                                    var_Contact.get(),
                                                                                                    var_Apartment_Type.get(),
                                                                                                    var_Available_House.get(),
                                                                                                    var_Deposit.get(),
                                                                                                    var_Rent.get(),
                                                                                                    var_water.get(),
                                                                                                    var_electricity.get(),
                                                                                                    var_security.get(),
                                                                                                    var_garbage.get(),
                                                                                                    var_Date.get(),
                                                                                                    var_Payment_Option.get(),
                                                                                                    var_Code.get(),
                                                                                                    var_Amt_Paid.get(),
                                                                                                    var_Balance.get(),
                                                                                                    var_Next_Date.get()
                                                                                                
                                                                                                ))
                                                                

                    conn.commit()  
                    fetch_data_house()
                    conn.close()
                    
                    
                    messagebox.showinfo('Success','House has been booked Successfully')
                    
                
                except Exception as es:
                
                    # messagebox.showerror('ERROR', 'Open Xampp and start connection')
                    messagebox.showwarning('Warning',f'Something went wrong: {str(es)}')
                    
        def clear_tree():
            self.customer_details_tables.delete(*self.customer_details_tables.get_children())
                   
           
        
        # btnadd = Button(self, text='Validate', font=('arial', 10), bg='black', fg='gold', width=10,command= ""
        #               ).place(x=10, y=300)
        
        
      
        btnadd = Button(self, text='Add', font=('arial', 10), bg='black', fg='gold', width=10,command=add_house
                      ).place(x=10, y=640)

        btnupdate = Button(self, text='Update', font=('arial', 10), bg='black', fg='gold', width=10,command=update_data_house).place(x=120,
                                                                                                              y=640)

        btnreset = Button(self, text='Clear', font=('arial', 10), bg='black', fg='gold', width=10,command=clear_house).place(x=240,
                                                                                                            y=640) 
                                                                                                                                                                                          
        

        # ===================== Show data ==========================================
                                                                                      
  

        lbl_search = Label(self, text='Search', font=('arial', 10), bg='red', fg='white').place(x=700, y=360)
       
        var_search_options = StringVar()

        combo_id = ttk.Combobox(self, font=('arial', 10),state='readonly',textvariable=var_search_options)
        combo_id['value'] = ('Select','Phone Number', 'House')
        combo_id.current(0)
        combo_id.place(x=790, y=360)
        
        # entry_search = ttk.Entry(self, font=('arial', 10)).place(x=800, y=180)

        # btnadd = Button(self, text='Search', font=('arial', 10), bg='black', fg='gold').place(x=900, y=340)

        btnreset = Button(self, text='Show All', font=('arial', 10), bg='black', fg='gold',command=fetch_data_house).place(x=960, y=360)
        
        btnreset = Button(self, text='Hide All', font=('arial', 10), bg='black', fg='gold', width=10,command=clear_tree).place(x=1200,
                                                                                                            y=360) 
        
         # ===================== Show data ==========================================

        self.customer_details_tables= ttk.Treeview(self, columns=('Client Contact', 'Apartment Type', 'House Number', 'Deposit', 'Rent','Water','Electricity','Security','Garbage', 'Date Entered','Pay Opt','Code','Amt Paid','Balance','Pay Date'), selectmode='browse', style="mystyle.Treeview",show=['headings'])

        		#SETTING THE SCROLLBARS
        vsb = Scrollbar(self, orient="vertical", command=self.customer_details_tables.yview)
        vsb.place(x=1298,y=400,height=200)
        hsb = Scrollbar(self, orient="horizontal", command=self.customer_details_tables.xview)
        hsb.place(x=700,y=598,width=598)

        self.customer_details_tables.configure(xscrollcommand=hsb.set,yscrollcommand=vsb.set)
        self.customer_details_tables.place(x=700, y=400, width=598,height=200)
        

       
        self.customer_details_tables.heading('Client Contact', text='Client Contact')  
        self.customer_details_tables.heading('Apartment Type', text='Apartment Type')
        self.customer_details_tables.heading('House Number', text='House Number')
        self.customer_details_tables.heading('Deposit', text='Deposit')
        self.customer_details_tables.heading('Rent', text='Rent')
        self.customer_details_tables.heading('Water', text='Water')
        self.customer_details_tables.heading('Electricity', text='Electricity')
        self.customer_details_tables.heading('Security', text='Security')
        self.customer_details_tables.heading('Garbage', text='Garbage')
        self.customer_details_tables.heading('Date Entered', text='Date Entered')
        self.customer_details_tables.heading('Pay Opt', text='Pay Opt')
        self.customer_details_tables.heading('Code', text='Code')
        self.customer_details_tables.heading('Amt Paid', text='Amt Paid')
        self.customer_details_tables.heading('Balance', text='Balance')
        self.customer_details_tables.heading('Pay Date', text='Balance')
       
        
        self.customer_details_tables['show'] = 'headings'
        
        self.customer_details_tables.column('Client Contact',width=100)
        self.customer_details_tables.column('Apartment Type',width=100)
        self.customer_details_tables.column('House Number',width=100)
        self.customer_details_tables.column('Deposit',width=100)
        self.customer_details_tables.column('Rent',width=100)
        self.customer_details_tables.column('Water',width=100)
        self.customer_details_tables.column('Electricity',width=100)
        self.customer_details_tables.column('Security',width=100)
        self.customer_details_tables.column('Garbage',width=100)
        self.customer_details_tables.column('Date Entered',width=100)
        self.customer_details_tables.column('Pay Opt',width=100)
        self.customer_details_tables.column('Code',width=100)
        self.customer_details_tables.column('Amt Paid',width=100)
        self.customer_details_tables.column('Balance',width=100)
        self.customer_details_tables.column('Pay Date',width=100)
        
        
        self.customer_details_tables.bind("<ButtonRelease-1>",cuersor)

class  report(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        self.controller.title('Report')
        self.controller.geometry("1500x900+50+100")
        
        heading_label = tk.Label(self,
                                                     text='REPORT',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        heading_label.place(x=0,y=0,   width=970,     height=70)



        try:
            load = Image.open(r"C:\Users\ADMIN\Downloads\Compressed\ken project 2021\Images\image6.jpg")
            load.resize((900,900),Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(load)
            label_image = tk.Label(self,image=photo)
            label_image.image=photo
            label_image.place(x=10,y=140,width=1480,height=800)
        except:
            messagebox.showerror('ERROR', 'Some image(s) is missing')
            self.controller.destroy()
        
        def __logout__():
            
            controller.show_frame('login')
            
        def __menu__():
            controller.show_frame('menu')
            
        def __client__():
            controller.show_frame('client_window')
            
        def __house__():
            controller.show_frame('house')
            
        def __details__():
            controller.show_frame('details')
        
        

        enter_button =ttk.Button(self,
                                                     text='Menu',
                                                     command=__menu__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=10,y=100)
        
        enter_button =ttk.Button(self,
                                                     text='Client',
                                                     command=__client__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=270,y=100)
        
        enter_button =ttk.Button(self,
                                                     text='House',
                                                     command=__house__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=530,y=100)
        
        enter_button =ttk.Button(self,
                                                     text='Details',
                                                     command=__details__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=800,y=100)
        enter_button =ttk.Button(self,
                                                     text="Log Out",
                                                     command=__logout__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=1100,y=100)

        var_report_search = StringVar()
        var_report_print = StringVar()
        
        def report_search():
            if var_report_search.get() == 'Client details Mysql Table':
               
                client()
            elif var_report_search.get() == 'Select':
                messagebox.showinfo("Error","Choose an option")
            elif var_report_search.get() == 'House Mysql Table':
                house()
            elif var_report_search.get() == 'Details Mysql Table':
                details()
            elif var_report_search.get() == 'Expense Mysql Table':
                exx()
                
        def exx():
            try:
                conn = pymysql.connect(host='localhost', user='root', password='', db='apartment')
                my_cursor = conn.cursor()
                df=sql.read_sql("SELECT * FROM `expense`",conn)
                # print(df)
                df.to_excel("C:/Users/Mercy/Desktop/ken project 2021/Reports/expense.xlsx")
                conn.commit()  
                conn.close()
                # messagebox.showinfo('Success','Converted successfully')
            except Exception as es:
                messagebox.showwarning('Warning',f'Something went wrong: {str(es)}')

            try:
                df=pd.read_excel("C:/Users/Mercy/Desktop/ken project 2021/Reports/expense.xlsx")
                # print(df)

                files=r"C:/Users/Mercy/Desktop/ken project 2021/Reports/expense.xlsx"
                os.startfile(files)
            except:
                messagebox.showerror('File Not Found','Convert Mysql to excel then print')
            
      
        def client():
            try:
                conn = pymysql.connect(host='localhost', user='root', password='', db='apartment')
                my_cursor = conn.cursor()
                df=sql.read_sql("SELECT * FROM `client details`",conn)
                # print(df)
                df.to_excel("C:/Users/Mercy/Desktop/ken project 2021/Reports/client.xlsx")
                conn.commit()  
                conn.close()
                # messagebox.showinfo('Success','Converted successfully')
            except Exception as es:
                messagebox.showwarning('Warning',f'Something went wrong: {str(es)}')

            try:
                df=pd.read_excel("C:/Users/Mercy/Desktop/ken project 2021/Reports/client.xlsx")
                # print(df)

                files=r"C:/Users/Mercy/Desktop/ken project 2021/Reports/client.xlsx"
                os.startfile(files)
            except:
                messagebox.showerror('File Not Found','Convert Mysql to excel then print')
                
        def house():
            try:
                conn = pymysql.connect(host='localhost', user='root', password='', db='apartment')
                my_cursor = conn.cursor()
                df=sql.read_sql("SELECT * FROM `house`",conn)
                # print(df)
                df.to_excel("C:/Users/Mercy/Desktop/ken project 2021/Reports/house.xlsx")
                conn.commit()  
                conn.close()
                # messagebox.showinfo('Success','Converted successfully')
            except Exception as es:
                messagebox.showwarning('Warning',f'Something went wrong: {str(es)}')

            try:
                df=pd.read_excel("C:/Users/Mercy/Desktop/ken project 2021/Reports/house.xlsx")
                # print(df)

                files=r"C:/Users/Mercy/Desktop/ken project 2021/Reports/house.xlsx"
                os.startfile(files)
            except:
                messagebox.showerror('File Not Found','Convert Mysql to excel then print')
                
                
        def details():
            try:
                conn = pymysql.connect(host='localhost', user='root', password='', db='apartment')
                my_cursor = conn.cursor()
                df=sql.read_sql("SELECT * FROM `details`",conn)
                # print(df)
                df.to_excel("C:/Users/Mercy/Desktop/ken project 2021/Reports/details.xlsx")
                conn.commit()  
                conn.close()
                # messagebox.showinfo('Success','Converted successfully')
            except Exception as es:
                messagebox.showwarning('Warning',f'Something went wrong: {str(es)}')

            try:
                df=pd.read_excel("C:/Users/Mercy/Desktop/ken project 2021/Reports/details.xlsx")
                # print(df)

                files=r"C:/Users/Mercy/Desktop/ken project 2021/Reports/details.xlsx"
                os.startfile(files)
            except:
                messagebox.showerror('File Not Found','Convert Mysql to excel then print')
                   
        
        lbl_search = Label(self, text='Choose ', font=('arial', 10), bg='red', fg='white').place(x=10, y=180)

        combo_gender = ttk.Combobox(self, font=('arial', 10), width=27, state='readonly', textvariable=var_report_search)
        combo_gender['value'] = ('Select','Client details Mysql Table', 'House Mysql Table','Details Mysql Table',"Expense Mysql Table")
        combo_gender.current(0)
        combo_gender.place( x=70, y=180)
        
        enter_button =ttk.Button(self,
                                                     text='print',
                                                     command=report_search,
                                                 
                                                    
                                                     width=20,
        )
        enter_button.place(x=290,y=180)
        
        
        def report_print():
            if var_report_print.get() == 'Client details Mysql Table':
                   
                client1()
            elif var_report_print.get() == "Select":
                messagebox.showerror('Error','Choose an option')
            elif var_report_print.get() == 'House Mysql Table':
                house1()
            elif var_report_print.get() == 'Details Mysql Table':
                details1()
                
                
        def client1():
            try:
                df=pd.read_excel("C:/Users/Stano/Pictures/ken full project/reports/client.xlsx")
                # print(df)

                files=r"C:/Users/Stano/Pictures/ken full project/reports/client.xlsx"
                os.startfile(files)
            except:
                messagebox.showerror('File Not Found','Convert Mysql to excel then print')
                
        def house1():
            try:
                df=pd.read_excel("C:/Users/Stano/Pictures/ken full project/reports/house.xlsx")
                # print(df)

                files=r"C:/Users/Stano/Pictures/ken full project/reports/house.xlsx"
                os.startfile(files)
            except:
                messagebox.showerror('File Not Found','Convert Mysql to excel then print')
                
        def details1():
            try:
                df=pd.read_excel("C:/Users/Stano/Pictures/ken full project/reports/details.xlsx")
                # print(df)

                files=r"C:/Users/Stano/Pictures/ken full project/reports/details.xlsx"
                os.startfile(files)
            except:
                messagebox.showerror('File Not Found','Convert Mysql to excel then print')

            
        
        # lbl_search = Label(self, text='Choose ', font=('arial', 10), bg='red', fg='white').place(x=10, y=220)

        # combo_gender = ttk.Combobox(self, font=('arial', 10), width=27, state='readonly', textvariable=var_report_print)
        # combo_gender['value'] = ('Select','Client details Mysql Table', 'House Mysql Table','Details Mysql Table')
        # combo_gender.current(0)
        # combo_gender.place( x=70, y=220)
        
        # enter_button =ttk.Button(self,
        #                                              text='Open to Print',
        #                                              command=report_print,
                                                 
                                                    
        #                                              width=20,
        # )
        # enter_button.place(x=290,y=220)




class  details(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        self.controller.title('Details')
        self.controller.geometry("1500x900+50+100")
        
        heading_label = tk.Label(self,
                                                     text='DETAILS',
                                                     font=('orbitron',45,'bold'),
                                                     foreground='#ffffff',
                                                     background='#3d3d5c')
        heading_label.place(x=0,y=0,   width=970,     height=70)
        
        def __logout__():
            
            controller.show_frame('login')
            
        def __menu__():
            controller.show_frame('menu')
            
        def __client__():
            controller.show_frame('client_window')
            
        def __report__():
            controller.show_frame('report')
            
        def __details__():
            controller.show_frame('details')
        
        

        enter_button =ttk.Button(self,
                                                     text='Menu',
                                                     command=__menu__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=10,y=100)
        
        enter_button =ttk.Button(self,
                                                     text='Client',
                                                     command=__client__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=270,y=100)
        
        enter_button =ttk.Button(self,
                                                     text='Report',
                                                     command=__report__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=530,y=100)
        
        enter_button =ttk.Button(self,
                                                     text='Details',
                                                     command=__details__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=800,y=100)
        enter_button =ttk.Button(self,
                                                     text="Log Out",
                                                     command=__logout__,
                                                 
                                                    
                                                     width=30,
        )
        enter_button.place(x=1100,y=100)



        var_Apartment_Type=StringVar()
        var_House_Number = StringVar()
        
        
        
        def add_house():
              
           
              
            
              if var_Apartment_Type.get() == '' or var_House_Number.get() == '' :
                  messagebox.showerror('ERROR', 'All fields are required')
                  
             
            
              else:
                  try:
                    
                    conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
                    my_cursor = conn.cursor()
                    my_cursor.execute('INSERT INTO details  VALUES(%s,%s)', (
                                                                                  var_Apartment_Type.get(),
                                                                                  var_House_Number.get()
                                                                                                ))
                                                               

                    conn.commit()  
                    fetch_details()
                    conn.close()
                    
                    
                    messagebox.showinfo('Success','New House Number has been added Successfully')
                   
                   
                  except Exception as es:
                    
                    # messagebox.showerror('ERROR', 'Open Xampp and start connection')
                    messagebox.showwarning('Warning',f'Something went wrong: {str(es)}')
        
        
        
        
        
        
        def fetch_details():
              try:
                conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM `details`")
                rows = my_cursor.fetchall()
                if len(rows)!= 0:
                    self.customer_details_tables.delete(*self.customer_details_tables.get_children())
                    for i in rows:
                        self.customer_details_tables.insert("",END,values=i)
                    conn.commit()
                conn.close()
              except Exception as es:
                      #messagebox.showerror('ERROR', 'Open Xampp and start connection')
                      messagebox.showwarning('Warning',f'Something went wrong: {str(es)}')
        
        def cuersor(events=""):
              
            cursor_rows = self.customer_details_tables.focus()
            content= self.customer_details_tables.item(cursor_rows)
            row=content["values"]
            
            
            var_Apartment_Type.set(row[0]),
            var_House_Number.set(row[1])
              
        def clear():
            var_Apartment_Type.set("")
            var_House_Number.set("")
        

        def update_details(): 
          
          if var_Apartment_Type.get() == "" or var_House_Number.get() == "":
                
                
                messagebox.showerror("Error","Enter Phone Number")
          else:
                    
              try:
                conn = pymysql.connect(host= 'localhost', user='root', password='', db='apartment')
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE `details` SET `Apartment Type` =  %s WHERE`House Number` = %s",(
                                                                                                                                                                                                                                
                                                                                                                                                                                                                                 
                                                                                                                                                                                                              
                                                                        var_Apartment_Type.get(),
                                                                        var_House_Number.get(),
                                                                                                ))
                conn.commit()  
                fetch_details()
                conn.close()
                
                messagebox.showinfo("Success","details has been updated successfully ")                                                                                                                                                                                                                                                                                                             
              
              except Exception as es:
                  #messagebox.showerror('ERROR', 'Open Xampp and start connection')
                  messagebox.showwarning('Warning',f'Something went wrong: {str(es)}')    
                  
                  
        def clear_tree():
            self.customer_details_tables.delete(*self.customer_details_tables.get_children())
                  

      
         # ========= label and entries =================================================================================================================
     
        lbl_date = Label(self, text='Apartment Type', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=180)
        lbl_identification_proof = Label(self, text='Apartment Type', font=('arial', 10) ,foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=220)
        combo_id = ttk.Combobox(self, font=('arial', 10), width=27, state='readonly',textvariable=var_Apartment_Type)
        combo_id['value'] = ("Select","4 Bedroom","3 Bedroom","2 Bedroom","1 Bedroom")
        combo_id.current(0)
        combo_id.place(x=110,  y=180)
                                                                                                            
        
          
        lbl_date = Label(self, text='House Number', font=('arial', 10),foreground='#ffffff',
                                                     background='#3d3d5c').place(x=10, y=220)
        entry_date = ttk.Entry(self, font=('arial', 10), width=30,textvariable=var_House_Number).place(x=110, y=220)
        
      
         
        btnadd = Button(self, text='Add', font=('arial', 10), bg='black', fg='gold', width=10,command=add_house
                      ).place(x=10, y=260)

        btnupdate = Button(self, text='Update', font=('arial', 10), bg='black', fg='gold', width=10,command=update_details).place(x=120,
                                                                                                              y=260)

        btnreset = Button(self, text='Clear', font=('arial', 10), bg='black', fg='gold', width=10,command=clear).place(x=250,
                                                                                                            y=260) 
        
        
        
        
        # ===================== Show data ==========================================

        
        self.customer_details_tables= ttk.Treeview(self, columns=('Apartment Type','House Number'), selectmode='browse', style="mystyle.Treeview",show=['headings'])

        		#SETTING THE SCROLLBARS
        vsb = Scrollbar(self, orient="vertical", command=self.customer_details_tables.yview)
        vsb.place(x=1298,y=220,height=200)
        hsb = Scrollbar(self, orient="horizontal", command=self.customer_details_tables.xview)
        hsb.place(x=700,y=400,width=598)

        self.customer_details_tables.configure(xscrollcommand=hsb.set,yscrollcommand=vsb.set)
        self.customer_details_tables.place(x=700, y=220, width=598,height=200)
 
        
        self.customer_details_tables.heading('Apartment Type', text='Apartment Type')
        self.customer_details_tables.heading('House Number', text='House Number')
       
        
        self.customer_details_tables['show'] = 'headings'
        
        
        self.customer_details_tables.column('Apartment Type',width=100)
        self.customer_details_tables.column('House Number',width=100)
        
        self.customer_details_tables.bind("<ButtonRelease-1>",cuersor)
        
      
        # customer_details_tables.place(x=410, y=100,width=350,height=250)
        
        
        btnreset = Button(self, text='Show All', font=('arial', 10), bg='black', fg='gold', width=10,command=fetch_details).place(x=860, y=180)
        
        btnreset = Button(self, text='Hide All', font=('arial', 10), bg='black', fg='gold', width=10,command=clear_tree).place(x=960, y=180)
        
                                                                                                    
                                                                                                    



check_db()