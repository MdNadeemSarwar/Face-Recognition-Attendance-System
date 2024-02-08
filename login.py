import os
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from face_recognizer import Face_Recognition
from student import Student
from train import Train
from attendence import Attendance
from developer import Developer
from support import Helps
from Registers import Register
import tkinter
# import tkinter as tk
from time import strftime
# from datetime import datetimes
from tkinter import messagebox
import cv2
import mysql.connector
import numpy as np

class Login:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0") 
        self.root.title("Registers Record")
        # self.root.configure(bg="#002B53")

        # Background colr
        left_lbl = Label(self.root, bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=600)

        right_lbl = Label(self.root, bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)


        # Frame
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=350, y=100, width=800, height=500)

        title = Label(login_frame, text="ADMIN LOGIN!", font=("times new roman", 30, "bold"), bg="white", fg="navyblue")
        title.place(x=305, y=50)

        #variable
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        email = Label(login_frame, text="Email", font=("times new roman", 18, "bold"), bg="white", fg="navyblue").place(x=250, y=150)
        self.txtuser = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txtuser.place(x=250, y=180, width=350, height=35)

        pass_ = Label(login_frame, text="Password", font=("times new roman", 18, "bold"), bg="white", fg="navyblue").place(x=250, y=250)
        self.txtpwd = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txtpwd.place(x=250, y=280, width=350, height=35)

        btn_reg = Button(login_frame, cursor="hand2", command=self.reg, text="Register an account", font=("times new roman", 14), bg="white", bd=0, fg="navyblue").place(x=250, y=330)

        btn_forgetpwd = Button(login_frame, cursor="hand2", command=self.forget_pwd, text="Forget password", font=("times new roman", 14), bg="white", bd=0, fg="navyblue").place(x=500, y=330)

        btn_login = Button(login_frame, text="Login", command=self.login, font=("times new roman", 20, "bold"), fg="white", cursor="hand2", bg="navyblue").place(x=250, y=380, width=180, height=40)


    #  THis function is for open register window
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        # self.new_window.state('zoomed')

        #  THis function is for open login frame
    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error", "All fields are required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
            messagebox.showinfo("Sussessfully", "Welcome to the Facial Recognition Attendance Management System")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(user='root', password='Nadeem@786',host='localhost',database='face_recognizer',port=3306)
            mycursor = conn.cursor()
            mycursor.execute("select * from regteach where email=%s and pwd=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Invalid Email and password!")
            else:
                open_min=messagebox.askyesno("Admin","Admin access only")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()
#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Security question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error", "Please enter your Email ID to reset your password!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error", "Please enter your Email ID to reset your password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(user='root', password='Nadeem@786',host='localhost',database='face_recognizer',port=3306)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s and ss_que=%s and s_ans=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update regteach set pwd=%s where email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Success! Your password has been reset.",parent=self.root2)
                



# =====================Forget window=========================================
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Reset your password!")
        else:
            conn = mysql.connector.connect(user='root', password="Nadeem@786",host='localhost',database='face_recognizer',port=3306)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please enter a valid email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title( "Forgot password")
                self.root2.geometry("350x450+80+120")
                l=Label(self.root2,text="Forgot password",font=("times new roman",25,"bold"),fg="#fff",bg="#002B53")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select security question",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=45,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Date of Birth","Nick Name","Previous School")
                self.combo_security.current(0)
                self.combo_security.place(x=45,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=45,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=45,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text= "New password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=45,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=45,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text= "Reset password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=45,y=300,width=270,height=35)


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0") 
        self.root.title("face Recognition System")
 
    #FIRST IMAGE
        
        img=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\Galgotias-University.jpg")
        img=img.resize((500,130),Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl =Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0, width=500, height=130)
    #SECOND IMAGE
        
        img1=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\facialrecognition.png")
        img1=img1.resize((500,130),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl =Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0, width=500, height=130)
    #THIRD IMAGE
        
        img2=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\gu.jpg")
        img2=img2.resize((500,130),Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl =Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0, width=550, height=130)

    #Baground IMAGE
        
        img3=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\bgs.jpg")
        img3=img3.resize((1530,710),Image.ADAPTIVE)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130, width=1530, height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white", fg="red")
        title_lbl.place(x=0,y=0,width=1530, height=50)

        ######## Time Update #################
  

        
    # #student Bottom
        img4=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\sts.jpg")
        img4=img4.resize((220,220),Image.ADAPTIVE)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img, image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1=Button(bg_img, text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

    #Detection face button
        img5=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\facess.jpg")
        img5=img5.resize((220,220),Image.ADAPTIVE)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500, y=100, width=220, height=220)

        b1_1=Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)

    #Attendance button
        img6=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\att.jpg")
        img6=img6.resize((220,220),Image.ADAPTIVE)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800, y=100, width=220, height=220)

        b1_1=Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data, font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)


    #HelpDesk button
        img7=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\help-desk.png")
        img7=img7.resize((220,220),Image.ADAPTIVE)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1=Button(bg_img, text="Help Desk", command=self.help_data, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)

    #Train face button
        img8=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\train.jpg")
        img8=img8.resize((220,220),Image.ADAPTIVE)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200, y=380, width=220, height=220)

        b1_1=Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)

    #Photos face button
        img9=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\facede.jpg")
        img9=img9.resize((220,220),Image.ADAPTIVE)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500, y=380, width=220, height=220)

        b1_1=Button(bg_img, text="Photos", cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)
    
    #Developer  button
        img10=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\deve.jpg")
        img10=img10.resize((220,220),Image.ADAPTIVE)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800, y=380, width=220, height=220)

        b1_1=Button(bg_img, text="Developer",command=self.developer_data, cursor="hand2", font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=800, y=580, width=220, height=40)

    #Exit button
        img11=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\exit.png")
        img11=img11.resize((220,220),Image.ADAPTIVE)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.exitkardu)
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1=Button(bg_img, text="Exit", cursor="hand2",command=self.exitkardu, font=("times new roman",15,"bold"),bg="darkblue", fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)

        #######################  Exit Window  ####################
    def open_img(self):
        os.startfile("data")  
    
    def exitkardu(self):
        self.exitkardu=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project",parent=self.root)
        if self.exitkardu >0:
            self.root.destroy()
        else:
            return
     ############################   Function Botton       #################
        
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Helps(self.new_window)

    # def reg(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Register(self.new_window)


if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()
    