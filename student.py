from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import numpy as np 
import tkinter
from tkinter import StringVar
import tkinter as tk

class Student:
    def __init__(self,root):
        self.var_search = tkinter.StringVar()
        self.var_searchTX = tkinter.StringVar()
        self.root=root
        self.root.geometry("1530x790+0+0") 
        self.root.title("face Recognition System")

        ########## Variable ###############

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        # self.var_radio1=StringVar()

     #FIRST IMAGE
        
        img=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\atts.jpg")
        img=img.resize((500,130),Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl =Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0, width=500, height=130)
     #SECOND IMAGE
        
        img1=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\ff.jpg")
        img1=img1.resize((500,130),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl =Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0, width=500, height=130)
     #THIRD IMAGE
        
        img2=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\hii.jpg")
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

        title_lbl=Label(bg_img,text="STUDENTS MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white", fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530, height=45)


        main_frame=Frame(bg_img,bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)

     #left label frame
        
        Left_frame=LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height= 580)

        
        img_left=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\stude.jpeg")
        img_left=img_left.resize((720,130),Image.ADAPTIVE)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl =Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0, width=720, height=130)

    #current course information
        current_course_frame=LabelFrame(Left_frame, bd=2,bg="white", relief=RIDGE,text="Current course information",font=("times new roman",12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height= 115)

    # Department
        dep_label=Label(current_course_frame, text="Department", font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10, sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="read only",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1,padx=2,pady=10,sticky=W)

    #course
        course_label=Label(current_course_frame,text="Course",font=("times now roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","FE", "SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3,padx=2,pady=10,sticky=W)

    #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame, textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-2021","2021-2022","2022-2023","2023-2024","2024-2025")
        year_combo.current(0)
        year_combo.grid(row=1, column=1,padx=2,pady=10,sticky=W)
    
    # Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

    #Class Student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Students Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)

    #student id
        #studentId_label=Label(class_student_frame, textvariable=self.var_std_id, text="Student ID:",font=("times new roman", 13, "bold"), bg="white")
        studentId_label=Label(class_student_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

    #student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,pady=5,padx=10,sticky=W)                             

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

    #Class division
        class_div_label=Label(class_student_frame,text="Section:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,pady=5,padx=10,sticky=W)

        # class_div_entry=ttk.Entry(class_student_frame, textvariable=self.var_div,  width=20, font=("times new roman", 13, "bold"))
        # class_div_entry.grid(row=1, column=1, padx=10,pady=5, sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div, font=("times new roman", 13, "bold"),state="readonly",width=18)
        div_combo["values"]=("A", "B", "C", "D", "E","F","G","H","I")
        div_combo.current(0)
        div_combo.grid(row=1, column=1,padx=10,pady=5,sticky=W)

   #Roll No
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,pady=5,padx=10,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

    #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,pady=5,padx=10,sticky=W)

        # gender_entry=ttk.Entry(class_student_frame, textvariable=self.var_gender,  width=20, font=("times new roman", 13, "bold"))
        # gender_entry.grid(row=2, column=1, padx=10,pady=5, sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Male","Femail","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1,padx=10,pady=5,sticky=W)

    #DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,pady=5,padx=10,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

    #Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,pady=5,padx=10,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

    #Phone No
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,pady=5,padx=10,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

    #Address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,pady=5,padx=10,sticky=W)

        address_entry=ttk.Entry(class_student_frame, textvariable=self.var_address, width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

    #Teacher name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,pady=5,padx=10,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

    # radio Button
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame, variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=6,column=0)

        # self.var_radio2=StringVar()
        radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn2.grid(row=6,column=1)

    #botton frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data, width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1=Frame(class_student_frame,bd=2, relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=34, font=("times new roman", 13,"bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn=Button(btn_frame1, text="Update Photo Sample",command=self.generate_dataset, width=34, font=("times new roman", 13,"bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1 )


    #Right label frame
        
        Right_frame=LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height= 580)


        img_right=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\love.jpg")
        img_right=img_right.resize((720,130),Image.ADAPTIVE)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl =Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0, width=720, height=130)


    ############################################# Searching System #######################################
        
        Search_frame=LabelFrame(Right_frame, bd=2,bg="white", relief=RIDGE, text="Search System", font=("times new roman",12, "bold"))
        Search_frame.place(x=5, y=135, width=710, height=70)
        
        search_label=Label(Search_frame, text="Search By:", font=("times new roman", 13, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, pady=5, padx=10, sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman", 13,"bold"), state="readonly",width=15)
        search_combo["values"]=("Select", "Roll-No", "Phone-No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1,padx=2,pady=10,sticky=W)

        # self.var_search=StringVar()
        search_entry=ttk.Entry(Search_frame,textvariable=self.var_search, width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10,pady=5, sticky=W)


        search_btn=Button(Search_frame, text="Search",command=self.search_data, width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showALL_btn=Button(Search_frame, text="Show All",command=self.fetch_data, width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        showALL_btn.grid(row=0, column=4, padx=4)  

        #####################    Table frame ################# scroll bar
        table_frame=Frame(Right_frame, bd=2,bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=250)

        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame, column=("dep", "course","year", "sem", "id", "name","div","roll","gender","dob","email", "phone" ,"address","teacher","photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student_Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text= "Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100) 
        self.student_table.column("photo",width=150)
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_coursor)
        self.fetch_data()


        ###########  Function Declation ########################

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            # messagebox.showinfo("success","welcomebro")
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Nadeem@786",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(  

                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            
                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                
   ####################  Fetch data ################
                
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Nadeem@786",database="face_recognizer")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
                            
  ################## get cursor data #####################
        
    def get_coursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


  ########### Update Function ###############
   
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if update:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Nadeem@786", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        """UPDATE student SET Name=%s, Dep=%s, Course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, 
                        Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s""",
                        (
                            self.var_std_name.get(),
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()
                        )
                    )
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                else:
                    if not update:
                        return
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
    
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Please select a student to delete" ,parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Are you sure you want to delete this student?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Nadeem@786", database="face_recognizer")
                    mycursor = conn.cursor() 
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Student details successfully deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 

    ######### Reset Data #########
    
    def reset_data(self):
        self.var_dep.set("Status"),
        self.var_std_name.set(""),
        self.var_course.set("Status"),
        self.var_year.set("Select Year")
        self.var_semester.set("Status"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Status"),
        self.var_roll.set(""),
        self.var_gender.set("Status"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

#***********************************************************************************************************************
     ########## Search Dat a#################
        
    def search_data(self):
        if self.var_search.get() == "" or self.var_searchTX.get() == "Select":
            messagebox.showerror("Error", "Select Combo option and enter entry box", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(user='root', password='Nadeem@786', host='localhost',
                                            database="face_recognizer", port=3306)
                my_cursor = conn.cursor()
                
                # First query
                sql = "SELECT   Dep, course, year, semester, Student_id, Name, Division,Roll, Gender, Dob,Email, Phone, Address,Teacher, PhotoSample FROM student WHERE Roll = %s"
                my_cursor.execute(sql, (self.var_search.get(),))
                rows = my_cursor.fetchall()
                
                # Checking if rows exist
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=i)
                else:
                    messagebox.showerror("Error", "Data Not Found", parent=self.root)
                
                conn.commit()
                conn.close()
                
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Database Error: {err}", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}", parent=self.root)

        #################Generating Data#############
        
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                
                conn = mysql.connector.connect(user='root', password='Nadeem@786',host='localhost',database='face_recognizer',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myreslut = mycursor.fetchall()
                id=0
                for x in myreslut:
                    id+=1

                mycursor.execute("update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s,Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s,PhotoSample=%s WHERE Student_id=%s",( 
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1   
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ====================part of opencv=======================

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        
                        face=cv2.resize(face_croped(my_frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 
  
  


#**************************************************************************************************************************
        
if __name__ == "__main__":

    root=Tk() 
    obj = Student(root) 
    root.mainloop()
