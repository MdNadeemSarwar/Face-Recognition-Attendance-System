from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognizer import Face_Recognition
from attendence import Attendance
from support import Helps
from login import Login
from Registers import Register
import tkinter
from developer import Developer
from time import strftime
from datetime import datetime


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
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        
        lbl=Label(title_lbl,font=("times new roman",14,"bold"),bg="white", fg="black")
        lbl.place(x=0,y=0,width=110, height=50)
        time()

        
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

    ##########################  Exit Window  ####################
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


if __name__ == "__main__":
   root=Tk()
   obj = Face_Recognition_System(root)
   root.mainloop()


        