# from tkinter import*
# from tkinter import ttk
# from PIL import Image, ImageTk
# import os
# from student import Student
# import cv2
# import webbrowser


# class Helps:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1530x790+0+0") 
#         self.root.title("Exit Window")

# # This part is image labels setting start 
#         # first header image  
#         img=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\banner1.jpg")
#         img=img.resize((1530,230),Image.ADAPTIVE)
#         self.photoimg=ImageTk.PhotoImage(img)

#         # set image as lable
#         f_lb1 = Label(self.root,image=self.photoimg)
#         f_lb1.place(x=0,y=0,width=1530,height=230)

#         # backgorund image 
#         bg1=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\bg2.jpg")
#         bg1=bg1.resize((1530,710),Image.ADAPTIVE)
#         self.photobg1=ImageTk.PhotoImage(bg1)

#         # set image as lable
#         bg_img = Label(self.root,image=self.photobg1)
#         bg_img.place(x=0,y=150,width=1530,height=710)


#         #title section
#         title_lb1 = Label(bg_img,text="Help & Support",font=("verdana",20,"bold"),bg="navyblue",fg="white")
#         title_lb1.place(x=0,y=0,width=1530,height=50)

#         # Create buttons below the section 
#         # ------------------------------------------------------------------------------------------------------------------- 
#         # student button 1
#         std_img_btn=Image.open(r"image\web.png")
#         std_img_btn=std_img_btn.resize((180,180),Image.ADAPTIVE)
#         self.std_img1=ImageTk.PhotoImage(std_img_btn)

#         std_b1 = Button(bg_img,command=self.website,image=self.std_img1,cursor="hand2")
#         std_b1.place(x=210,y=160,width=180,height=180)

#         std_b1_1 = Button(bg_img,command=self.website,text="Website",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
#         std_b1_1.place(x=210,y=340,width=180,height=45)

#         # Detect Face  button 2
#         det_img_btn=Image.open(r"image\fb.png")
#         det_img_btn=det_img_btn.resize((180,180),Image.ADAPTIVE)
#         self.det_img1=ImageTk.PhotoImage(det_img_btn)

#         det_b1 = Button(bg_img,command=self.facebook,image=self.det_img1,cursor="hand2",)
#         det_b1.place(x=440,y=160,width=180,height=180)

#         det_b1_1 = Button(bg_img,command=self.facebook,text="Facebook",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
#         det_b1_1.place(x=440,y=340,width=180,height=45)

#          # Attendance System  button 3
#         att_img_btn=Image.open(r"image\yt.png")
#         att_img_btn=att_img_btn.resize((180,180),Image.ADAPTIVE)
#         self.att_img1=ImageTk.PhotoImage(att_img_btn)

#         att_b1 = Button(bg_img,command=self.youtube,image=self.att_img1,cursor="hand2",)
#         att_b1.place(x=670,y=160,width=180,height=180)

#         att_b1_1 = Button(bg_img,command=self.youtube,text="Youtube",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
#         att_b1_1.place(x=670,y=340,width=180,height=45)

#         # Help  Support  button 4
#         hlp_img_btn=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\gmail.png")
#         hlp_img_btn=hlp_img_btn.resize((180,180),Image.ADAPTIVE)
#         self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

#         hlp_b1 = Button(bg_img,command=self.gmail,image=self.hlp_img1,cursor="hand2",)
#         hlp_b1.place(x=900,y=160,width=180,height=180)

#         hlp_b1_1 = Button(bg_img,command=self.gmail,text="Gmail",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
#         hlp_b1_1.place(x=900,y=340,width=180,height=45)

#         # Help  Support  button 5
#         llis_img_btn=Image.open(r"image\linkedin.png")
#         llis_img_btn=llis_img_btn.resize((180,180),Image.ADAPTIVE)
#         self.llis_img1=ImageTk.PhotoImage(llis_img_btn)

#         llis_b1 = Button(bg_img,command=self.linkedin,image=self.llis_img1,cursor="hand2",)
#         llis_b1.place(x=1130,y=160,width=180,height=180)

#         llis_b1_1 = Button(bg_img,command=self.linkedin,text="Linkedin",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
#         llis_b1_1.place(x=1130,y=340,width=180,height=45)


#         # create function for button 
    
    
#     def website(self):
#         self.new = 1
#         self.url = "https://github.com/MdnadeemSarwar"
#         webbrowser.open(self.url,new=self.new)
    
#     def facebook(self):
#         self.new = 1
#         self.url = "https://www.facebook.com/nadeem.sarwar.79069/"
#         webbrowser.open(self.url,new=self.new)
    
#     def youtube(self):
#         self.new = 1
#         self.url = "https://www.youtube.com/@Careerhelpline"
#         webbrowser.open(self.url,new=self.new)
    
#     def gmail(self):
#         self.new = 1
#         self.url = "https://www.gmail.com"
#         webbrowser.open(self.url,new=self.new)
    
#     def linkedin(self):
#         self.new = 1
#         self.url = "https://www.linkedin.com/in/md-nadeem-sarwar-b564b919b/"
#         webbrowser.open(self.url,new=self.new)


# if __name__ == "__main__":
#    root=Tk()
#    obj = Helps(root)
#    root.mainloop()

