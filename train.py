from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np




class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")#Size of window setting
        self.root.title("Attendance Management System Using Face Recognition")# Title

        title_lbl=Label(self.root,text="TRAIN DATASET",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1531,height=45)

        img_top=Image.open(r"college_images\pu.jpg")
        #img_top=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1500,height=300)
        
        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=350,width=1500,height=60)

        img_buttom=Image.open(r"college_images\pu.jpg")
        #img_buttom=img_top.resize((1530,325),Image.ANTIALIAS)
        self.photoimg_buttom=ImageTk.PhotoImage(img_buttom)
        f_lb2=Label(self.root,image=self.photoimg_buttom)
        f_lb2.place(x=0,y=440,width=1500,height=300)

    #tain data function

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')#convert gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids)

        #train the classifier data & save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!")



       


if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()