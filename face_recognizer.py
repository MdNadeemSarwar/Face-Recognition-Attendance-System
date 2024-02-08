from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import mysql.connector 
import cv2
import numpy as np
from time import strftime
from datetime import datetime
from sys import path

class Face_Recognition:

    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0") 
        self.root.title("face Recognition")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white", fg="red")
        title_lbl.place(x=0,y=0,width=1530, height=45)
        #ist image
        img_top=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\det2.jpg")
        img_top=img_top.resize((650,700),Image.ADAPTIVE)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl =Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55, width=650, height=700)
        #2nd Image
        img_bottom=Image.open(r"C:\Users\caree\Desktop\Face Reco\image\image.jpg")
        img_bottom=img_bottom.resize((950,700),Image.ADAPTIVE)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl =Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55, width=950, height=700)

        b1_1=Button(f_lbl, text="Face Recognition",command=self.face_recog, cursor="hand2",font=("times new roman",18,"bold"),bg="white", fg="red")
        b1_1.place(x=365, y=620, width=200, height=40)

        # #=====================Attendance===================
        
    def mark_attendance(self,i,n,r):
        with open("attendance.csv","r+",newline="\n") as f:
            myDatalist=f.readlines()
            name_list=[]
            for line in myDatalist:
                entry=line.split((","))
                name_list.append(entry[0])

            if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")


        #================face recognition==================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="Nadeem@786", database="face_recognizer",port=3306)
                cursor = conn.cursor()
                cursor.execute("select Student_id from student where Student_id="+str(id))
                i=cursor.fetchone()
                # i="+".join(i)
                if i is not None:
                    i = "+".join(i)


                cursor.execute("select Roll from student where Student_id="+str(id))
                r=cursor.fetchone()
                # r="+".join(r)
                if r is not None:
                    r = "+".join(r)


                cursor.execute("select Name from student where Student_id="+str(id))
                n=cursor.fetchone()
                # n="+".join(n)
                if n is not None:
                    n = "+".join(n)
                    
              
                if confidence > 77:
                    cv2.putText(img,f"Student_id:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Roll:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    self.mark_attendance(i,n,r)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]  
                
            return coord 


        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            
            cv2.imshow("Welcome To Face Recognition",img)

            # Press 'q' to exit the loop and close the window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        videoCap.release()
        cv2.destroyAllWindows()
        print("Window closed")

if __name__ == "__main__":
    root=Tk() 
    obj=Face_Recognition(root)
    root.mainloop()