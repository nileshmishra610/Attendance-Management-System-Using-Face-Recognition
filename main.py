from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendanceDetails import AttendanceDatils


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")#Size of window setting
        self.root.title("Attendance Management System Using Face Recognition")# Title

        img=Image.open(r"college_images\pu.jpg")
       # img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        img1=Image.open(r"college_images\download.jpeg")
       # img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl1=Label(self.root,image=self.photoimg1)
        f_lbl1.place(x=430,y=0,width=500,height=130)

        img2=Image.open(r"college_images\pu.jpg")
       # img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl2=Label(self.root,image=self.photoimg2)
        f_lbl2.place(x=900,y=0,width=500,height=130)


        # backgroung image
        img3=Image.open(r"college_images\bg.jpg")
       # img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM USING FACE RECOGNITION..       ",font=("times new roman",25,"bold"),bg="black",fg="pink")
        title_lbl.place(x=0,y=0,width=1531,height=45)


        #add student details buttton
        img4=Image.open(r"college_images\student.png")
       # img4=img3.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=90,width=180,height=180)
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="pink")
        b1_1.place(x=150,y=270,width=180,height=35)


        #attendxance
        img5=Image.open(r"college_images\student.png")
       # img4=img3.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=460,y=90,width=180,height=180)
        b2_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="black",fg="pink")
        b2_1.place(x=460,y=270,width=180,height=35)


         #attendxance details
        img6=Image.open(r"college_images\student.png")
       # img4=img3.resize((180,180),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b3.place(x=760,y=90,width=180,height=180)
        b3_1=Button(bg_img,text="Attendance Details",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="black",fg="pink")
        b3_1.place(x=760,y=270,width=180,height=35)

         #Help
        img7=Image.open(r"college_images\help.jpeg")
       # img4=img7.resize((180,180),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b4=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b4.place(x=1060,y=90,width=180,height=180)
        b4_1=Button(bg_img,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="pink")
        b4_1.place(x=1060,y=270,width=180,height=35)


         #Train
        img8=Image.open(r"college_images\train.jpeg")
       # img4=img3.resize((180,180),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=150,y=340,width=180,height=180)
        b5_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="black",fg="pink")
        b5_1.place(x=150,y=520,width=180,height=35)


        #Photo
        img9=Image.open(r"college_images\student.png")
        #img4=img3.resize((180,180),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=460,y=340,width=180,height=180)
        b6_1=Button(bg_img,text="Photo",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="black",fg="pink")
        b6_1.place(x=460,y=520,width=180,height=35)


         #Developer
        img10=Image.open(r"college_images\student.png")
       # img4=img3.resize((180,180),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        b7=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b7.place(x=760,y=340,width=180,height=180)
        b7_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="pink")
        b7_1.place(x=760,y=520,width=180,height=35)

         #Exit
        img11=Image.open(r"college_images\student.png")
       # img4=img7.resize((180,180),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        b8=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b8.place(x=1060,y=340,width=180,height=180)
        b8_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="pink")
        b8_1.place(x=1060,y=520,width=180,height=35)


    def open_img(self):
        os.startfile("data")


        #button Function

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
        self.app=AttendanceDatils(self.new_window)











if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()