from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import mysql.connector 
import os
import numpy as np

try:
    # Establish connection to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nadeem@786",
        database="face_recognizer"
    )
    # If the connection is successful, print a success message
    print("Connected to MySQL database!")
    # Don't forget to close the connection when done
    conn.close()
except Exception as e:
    # If there's an error, print the error message
    print("Error:", e)


class Train:

    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0") 
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white", fg="red")
        title_lbl.place(x=0,y=0,width=1530, height=45)

        img_top=Image.open(r"image\facial_recognition_action.jpg")
        img_top=img_top.resize((1530,325),Image.ADAPTIVE)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl =Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55, width=1530, height=325)

        b1_1=Button(self.root, text="TRAIN DATA",command=self.train_classifier ,cursor="hand2",font=("times new roman",30,"bold"),bg="red", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)

        img_bottom=Image.open(r"image\facialrecognition.png")
        img_bottom=img_bottom.resize((1530,325),Image.ADAPTIVE)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl =Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440, width=1530, height=325)

            ############ maain program ##############
        
    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

        ids = np.array(ids)

        # Train Classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.save("classifier.xml")

        messagebox.showinfo("Result", "Training dataset completed!!", parent=self.root)
        


if __name__ == "__main__":
    root=Tk() 
    obj = Train(root)
    root.mainloop()