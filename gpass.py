#المكاتب 
import random
import numpy as np
from tkinter import *
#الحروف والأرقام الرموز 
num=np.array([0,1,2,3,4,5,6,7,8,9])
letters=np.array(['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'])
symbol=np.array(['_','/','+','[]','[',']','<','>','{','}','(',')'])

#هنا تكمن صفحة كلمة السر الثانية
def passwordpage2():
  root2=Tk()
  root2.geometry("2000x2000")
  root2.title("tiki tiki")
  textpass2=Label(root2,text="enter password two",font=("CaskaydiaMono NF",50))
  textpass2.place(x=550,y=300)
  pass2=Entry(root2,font=("CaskaydiaMono NF",50))
  pass2.place(x=550,y=400)
  #من هنا يمكنة التحقق من كلمة السر في الصفحة الثانية
  def passwordget2():
      password2=pass2.get()
      if password2=="Codari404soft404":
        root2.destroy()  
        def passwordroom1():
         #هنا الصفحة التي توجد فيها الباسوردات
  
         passroompage1=Tk()
         passroompage1.geometry("2000x2000")
         passtext=Label(passroompage1,text="tab to any password",font=("CaskaydiaMono NF",50))
         passtext.place(x=550,y=50)
         #من هنا اذا تمضغط الزر يغير الكتابة
         def v():
          passtext.config(text="wew")
          #من هنا يمكنك اضافة الباسوردات يمنكن تعديلهامن كيت هب
         passbutton1=Button(passroompage1,text="pass1",font=("CaskaydiaMono NF",50),command=v)
         passbutton1.place(x=550,y=250,width=750)
         passroompage1.mainloop()
        start=Tk()
        start.title("start")
        start.geometry("2000x2000")
        passwordsbut1=Button(start,text="passwords",width=20,height=2,font=("CaskaydiaMono NF",50),command=passwordroom1)
        passwordsbut1.place(x=550,y=200)
        start.mainloop()
        
        but2=Button(root2,text="GO",font=("CaskaydiaMono NF",50),command=passwordget2)
        but2.place(x=400,y=500,width=787)
        root2.mainloop()
  but1=Button(root2,text=("hi"),width=70,height=5,command=passwordget2)
  but1.place(x=550,y=600)
 
#هنا التحقق من الباسورد الاول
def passwordget1():
  password1=pass1.get()
  if password1=="Essa@42561M1234":
   root.destroy()
   passwordpage2()
 
 #هنا الصفحة التي يوجد فيها الباسورد الاول 
root=Tk()
root.geometry("2000x2000")

textpass1=Label(root,text="enter password one",font=("CaskaydiaMono NF",50))
textpass1.place(x=550,y=100)
pass1=Entry(root,font=("CaskaydiaMono NF",50))
pass1.place(x=550,y=200)
but1=Button(root,text="GO",font=("CaskaydiaMono NF",50),command=passwordget1)
but1.place(x=550,y=500,width=787)
root.mainloop()

c=int(input("enter your password range(num only):"))
all=np.concatenate([num,letters,symbol])
password="".join(random.choice(all)for i in range(c))
