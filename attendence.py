from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog

#Global variable for importCsv Function 

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0") 
        self.root.title("Attendance Record")

        #-----------Variables-------------------
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\att.jpg")
        img=img.resize((1530,430),Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1530,height=430)

        # backgorund image 
        bg1=Image.open(r"C:\Users\caree\Desktop\Face Reco\Image\student.jpg")
        bg1=bg1.resize((1530,540),Image.ADAPTIVE)
        self.photobg1=ImageTk.PhotoImage(bg1)       # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=145,width=1530,height=540)


        #title section
        title_lb1 = Label(bg_img,text="ATTENDANCE DETAILS",font=("verdana",20,"bold"),bg="navyblue",fg="white")
        title_lb1.place(x=0,y=0,width=1530,height=60)

        #========================Section Creating==================================

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=0,y=60,width=1530,height=480)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=100,y=10,width=645,height=480)

        

        # ==================================Text boxes and Combo Boxes====================

        #Student id
        attendanceID_label = Label(left_frame,text="AttendenceID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        attendanceID_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        attendanceID_entry = ttk.Entry(left_frame,textvariable=self.var_id,width=15,font=("verdana",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Studnet Name
        student_name_label = Label(left_frame,text="Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(left_frame,textvariable=self.var_name,width=15,font=("verdana",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #Student Roll
        roll_label = Label(left_frame,text="Roll:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        roll_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(left_frame,textvariable=self.var_roll,width=15,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        # #Department
        # dep_label = Label(left_frame,text="Department:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        # dep_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        # dep_entry = ttk.Entry(left_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"))
        # dep_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #time
        timeLabel = Label(left_frame,text="Time:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        timeLabel.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        time_entry = ttk.Entry(left_frame,textvariable=self.var_time,width=15,font=("verdana",12,"bold"))
        time_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Date 
        dateLabel = Label(left_frame,text="Date:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        dateLabel.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(left_frame,textvariable=self.var_date,width=15,font=("verdana",12,"bold"))
        date_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Attendance
        attendanceLabel = Label(left_frame,text="Attend:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        attendanceLabel.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        attend_combo=ttk.Combobox(left_frame,textvariable=self.var_attend,width=13,font=("verdana",12,"bold"),state="readonly")
        attend_combo["values"]=("Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=2,column=3,padx=5,pady=5,sticky=W)

    #     # ===============================Table Sql Data View==========================
        table_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=100,width=635,height=280)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport_left = ttk.Treeview(table_frame,column=("ID","Roll_No","Name","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport_left.xview)
        scroll_y.config(command=self.attendanceReport_left.yview)

        self.attendanceReport_left.heading("ID",text="ID")
        self.attendanceReport_left.heading("Roll_No",text="Roll")
        self.attendanceReport_left.heading("Name",text="Name")
        self.attendanceReport_left.heading("Time",text="Time")
        self.attendanceReport_left.heading("Date",text="Date")
        self.attendanceReport_left.heading("Attend",text="Attend")
        self.attendanceReport_left["show"]="headings"


    #     # Set Width of Colums 
        self.attendanceReport_left.column("ID",width=100)
        self.attendanceReport_left.column("Roll_No",width=100)
        self.attendanceReport_left.column("Name",width=100)
        self.attendanceReport_left.column("Time",width=100)
        self.attendanceReport_left.column("Date",width=100)
        self.attendanceReport_left.column("Attend",width=100)
        
        self.attendanceReport_left.pack(fill=BOTH,expand=1)
        self.attendanceReport_left.bind("<ButtonRelease>",self.get_cursor_left)
    

    #     # =========================button section========================

        #Button Frame
        btn_frame = Frame(left_frame,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=375,width=635,height=40)

        #Improt button
        save_btn=Button(btn_frame,command=self.importCsv,text="Import CSV",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=6,pady=10,sticky=W)

        #Exprot button
        update_btn=Button(btn_frame,command=self.exportCsv,text="Export CSV",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=6,pady=8,sticky=W)

        #Update button                    ###*****command=self.action add hoga
        del_btn=Button(btn_frame,text="Update",command=self.action,width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=6,pady=10,sticky=W)



    #     # Right section=======================================================

        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Details",font=("Attendence Details",12,"bold"),fg="navyblue")
        right_frame.place(x=780,y=10,width=660,height=480)


    #     # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=70,width=660,height=360)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

    #    #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("ID","Roll_No", "Name","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("ID",text="ID")
        self.attendanceReport.heading("Roll_No",text="Roll")
        self.attendanceReport.heading("Name",text="Name")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Attend",text="Attend")
        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport.column("ID",width=30)
        self.attendanceReport.column("Roll_No",width=70)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("Time",width=75)
        self.attendanceReport.column("Date",width=80)
        self.attendanceReport.column("Attend",width=120)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor_right)
        self.fetch_data()
    # # =================================update for mysql button================
        
    # #Update button
        del_btn=Button(right_frame,command=self.update_data,text="Update",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=1,padx=6,pady=10,sticky=W)
    #Update button
        del_btn=Button(right_frame,command=self.delete_data,text="Delete",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)
    # ===============================update function for mysql database=================
    def update_data(self):
        if self.var_id.get()=="" or self.var_roll.get=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(user='root', password='Nadeem@786',host='localhost',database='face_recognizer',port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("update stdattendance set std_id=%s,std_roll_no=%s,std_name=%s,std_time=%s,std_date=%s,std_attendance=%s where std_id=%s",( 
                    self.var_id.get(),
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_time.get(),
                    self.var_date.get(),
                    self.var_attend.get(),
                    self.var_id.get()  
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Data is updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    # =============================Delete Attendance form my sql============================
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Please select a student to delete" ,parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Are you sure you want to delete this student?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(user='root', password='2912002',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from stdattendance where std_id=%s"
                    val=(self.var_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Xóa thành công!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  
    # ===========================fatch data form mysql attendance===========

    def fetch_data(self):
        conn = mysql.connector.connect(user='root', password='Nadeem@786',host='localhost',database='face_recognizer',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from stdattendance")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            for i in data:
                self.attendanceReport.insert("",END,values=i)
            conn.commit()
        conn.close()

    # # #============================Reset Data======================
    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status")

    # # # =========================Fetch Data Import data ===============

    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
        for i in rows:
            self.attendanceReport_left.insert("",END,values=i)
            print(i)
        

    def importCsv(self):
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)
            

    # # #==================Experot CSV=============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Your data is exported!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    # # #=============Cursur Function for CSV========================

    def get_cursor_left(self,event=""):
        cursor_focus = self.attendanceReport_left.focus()
        content = self.attendanceReport_left.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_roll.set(data[1]),
        self.var_name.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attendance.set(data[5])
        self.var_dep.set(data[6]),

    #  #=============Cursur Function for mysql========================

    def get_cursor_right(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_roll.set(data[1]),
        self.var_name.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attend.set(data[5])    
    # #=========================================Update CSV============================

    # # export upadte
    def action(self):
        if self.var_id.get()=="" or self.var_roll.get=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
            messagebox.showerror("Error","Please fill in all required fields!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='Nadeem@786',host='localhost',database='face_recognizer',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("insert into stdattendance values(%s,%s,%s,%s,%s,%s)",(
                self.var_id.get(),
                self.var_roll.get(),
                self.var_name.get(),
                self.var_time.get(),
                self.var_date.get(),
                self.var_attend.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All records are saved in the database!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


        conn = mysql.connector.connect(user='root', password='Nadeem@786',host='localhost',database='face_recognizer',port=3306)
        mycursor = conn.cursor()
        if messagebox.askyesno("Confirmation","Are you sure you want to save attendance on database?"):
            for i in mydata:
                uid = i[0]
                uroll = i[1]
                uname = i[2]
                utime = i[3]
                udate = i[4]
                uattend = i[5]
                qury = "INSERT INTO stdattendance(std_id, std_roll_no, std_name, std_time, std_date, std_attendance) VALUES(%s,%s,%s,%s,%s,%s)"
                mycursor.execute(qury,(uid,uroll,uname,utime,udate,uattend))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
        else:
            return False

if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()