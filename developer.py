from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
import os
import webbrowser

class Developer:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0") 
        self.root.title("face Recognition")
        
# This part is image labels setting start 
        # first header image  
        img=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\coding.jpg")
        img=img.resize((1530,230),Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1530,height=230)

        # backgorund image 
        bg1=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\developer.jpg")
        bg1=bg1.resize((1530,710),Image.ADAPTIVE)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=145,width=1530,height=710)


        #title section
        title_lb1 = Label(bg_img,text="Developer",font=("verdana",20,"bold"),bg="navyblue",fg="white")
        title_lb1.place(x=0,y=0,width=1530,height=50)


        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        
        att_img_btn=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\Photo.png")
        att_img_btn=att_img_btn.resize((250,250),Image.ADAPTIVE)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,image=self.att_img1,cursor="hand2",command=self.linkedin)
        att_b1.place(x=350,y=120,width=250,height=250)

        att_b1_1 = Button(bg_img,text="Software Developer",command=self.linkedin,cursor="hand2",font=("tahoma",10,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=350,y=370,width=250,height=50)


        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=600,y=120,width=550,height=300)
        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Developer",font=("verdana",10,"bold"),fg="navyblue")
        right_frame.place(x=7,y=7,width=510,height=280)

        #label Name
        name_label=Label(right_frame,text="Name:",font=("verdana",12),bg="white")
        name_label.grid(row=0,column=0,padx=5,pady=12)
        #Name
        name=Label(right_frame,text="Md Nadeem Sarwar",font=("verdana",12,"bold"),bg="white", fg="navyblue",)
        name.grid(row=0,column=1,padx=5,pady=12,sticky=W)
        
        #label ID
        idstd_label=Label(right_frame,text="Course:",font=("verdana",12),bg="white")
        idstd_label.grid(row=1,column=0,padx=5,pady=12)
        #ID
        idstd=Label(right_frame,text="Btech(CSE)",font=("verdana",12,"bold"),bg="white", fg="navyblue",)
        idstd.grid(row=1,column=1,padx=5,pady=12,sticky=W)

        #label class
        classStd_label=Label(right_frame,text="Roll No:",font=("verdana",12),bg="white")
        classStd_label.grid(row=2,column=0,padx=5,pady=12)
        #class
        classStd=Label(right_frame,text="20SCSE1010767",font=("verdana",12,"bold"),bg="white",fg="navyblue",)
        classStd.grid(row=2,column=1,padx=5,pady=12,sticky=W)

        #label phone
        phone_label=Label(right_frame,text="Phone No:",font=("verdana",12),bg="white")
        phone_label.grid(row=3,column=0,padx=5,pady=12)
        #phone
        phone=Label(right_frame,text="85400003089",font=("verdana",12,"bold"),bg="white",fg="navyblue",)
        phone.grid(row=3,column=1,padx=5,pady=12,sticky=W)

        #label email
        email_label=Label(right_frame,text="Email:",font=("verdana",12),bg="white")
        email_label.grid(row=4,column=0,padx=5,pady=12)
        #email
        email=Label(right_frame,text="nadeemsarwar11612@gmail.com",font=("verdana",12,"bold"),bg="white",fg="navyblue",)
        email.grid(row=4,column=1,padx=5,pady=12,sticky=W)


    def linkedin(self):
        self.new = 1
        self.url = "https://www.linkedin.com/in/md-nadeem-sarwar-b564b919b/"
        webbrowser.open(self.url,new=self.new)


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()