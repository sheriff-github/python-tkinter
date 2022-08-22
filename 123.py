from tkinter import *

def save():
    e1_save=e1.get()
    e2_save=e2.get()
    print('USER DATA\n')
    print(e1_save,'\t',e2_save)
    file=open('sample1.txt','w')
    file.write(e1_save)
    file.write(e2_save)
    file.close()


    

window=Tk()
window.minsize(width=1500,height=900)
window.title('MY FIRST PROJECT')
l1=Label(window,text='ENTER YOUR NAME',font=('bold',15))
l1.place(x=500,y=100)
l2=Label(window,text='ENTER YOUR ADDRESS',font=('bold',15))
l2.place(x=450,y=200)

e1=Entry(window,width=30,bd=1,font='bold 25')
e1.place(x=700,y=100)
e2=Entry(window,width=30,bd=1,font='bold 25')
e2.place(x=700,y=200)
b1=Button(window,text='ENTER',bg='white',width=8,height=2,command=save)
b1.place(x=700,y=300)

b2=Button(window,text='EXIT',width=100,height=3,command=window.destroy,bg='light green',fg='black')
b2.place(x=300,y=400)
window.mainloop()
