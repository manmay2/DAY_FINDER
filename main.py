from tkinter import *
from tkinter import messagebox
import pyttsx3
def sub():
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-60)
    name=var.get()
    y=gen.get()
    if(y==0):
        say='a very charming welcome, to our Day finder app, mister ',name,'!'
        engine.say(say)
        engine.say("Please enter any date")
        engine.runAndWait()
    elif(y==1):
        say='a very charming welcome, to our Day finder app, miss ',name,'!'
        engine.say(say)
        engine.say("Please enter any date")
        engine.runAndWait()
    radio1.destroy()
    radio2.destroy()
    lbl.destroy()
    lbl1.destroy()
    ent.destroy()
    btn.destroy()
def destroy():
    win.destroy()
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-60)
    engine.say("thanks a lot for using our application!!!!!Bye , see you soon")
    engine.runAndWait()
def day_finder(inp):
    inp=inp.lower()
    if('-' in inp):
        day=inp.split('-')[0]
        month=inp.split('-')[1]
        year=inp.split('-')[2]
    elif(' ' in inp):
        day=inp.split(' ')[0]
        month=inp.split(' ')[1]
        year=inp.split(' ')[2]
    elif('/' in inp):
        day=inp.split('/')[0]
        month=inp.split('/')[1]
        year=inp.split('/')[2]
    def leap_year(year):
        if(year%100==0 and year%400==0):
            return True
        elif(year%100==0 and year%400!=0):
            return False
        elif(year%4==0):
            return True
        else:
            return False
    def get_key(val):
        for key, value in d_week.items():
            if val == value:
                return key
    def cent_get_code(cent):
        t_centuries=(6,4,2,0)
        r=cent%400
        if(r==0):
            return t_centuries[0]
        elif(r==100):
            return t_centuries[1]
        elif(r==200):
            return t_centuries[2]
        elif(r==300):
            return t_centuries[3]
    d_month={"january":1,"february":4,"march":4,"april":0,"may":2,"june":5,"july":0,"august":3,"september":6,"october":1,"november":4,"december":6}
    d_week={'Sunday':0,'Monday':1,'Tuesday':2,'Wednesday':3,'Thrusday':4,'Friday':5,'Saturday':6}
    d_month_s={'01':1,"02":4,"03":4,"04":0,"05":2,"06":5,"07":0,"08":3,"09":6,"10":1,"11":4,"12":6}
    if((month[0]) in '0123456789'):
        cent=(int(year)//400)*400
        cent_p=int(year)%400
        if((leap_year(int(year)) is True) and (month=='01' or month=='02')):
            find=((int(day)+int(d_month_s[month])+cent_get_code(cent)+cent_p+(cent_p//4)-1)%7)-1
        else:
            find=((int(day)+int(d_month_s[month])+cent_get_code(cent)+cent_p+(cent_p//4))%7)-1

    elif(month[0].isalpha()):
        cent=(int(year)//400)*400
        cent_p=int(year)%400
        if((leap_year(int(year)) is True) and (month=='january' or month=='february')):
            find=((int(day)+int(d_month[month])+cent_get_code(cent)+cent_p+(cent_p//4)-1)%7)-1
        else:
            find=((int(day)+int(d_month[month])+cent_get_code(cent)+cent_p+(cent_p//4))%7)-1
    if(find<0 and find!=-7):
        find=7+find
    return get_key(find)
    
#print(day_finder(input("[*] ENTER A DATE (in DD-MM-YYYY / DD MONTH YYYYY) : ")))

def day_find():
    inp=var1.get()
    if(inp==''):
        engine=pyttsx3.init()
        rate=engine.getProperty('rate')
        engine.setProperty('rate',rate-60)
        engine.say("Sorry, you haven't entered a date...please try giving a valid date")
    else:
        res=day_finder(inp)
        messagebox.showinfo("Success",res)
        engine=pyttsx3.init()
        rate=engine.getProperty('rate')
        engine.setProperty('rate',rate-60)
        say="The day of",inp,"is",res
        engine.say(say)
        engine.runAndWait()
def disable_event():
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-60)
    engine.say("Sorry ! The cancel button is disabled!! Please hit the Exit button for exiting the application!!")
    engine.runAndWait()
win=Tk()
var1=StringVar()
win.title('DAY_FINDER')
win.minsize(width=840,height=500)
win.maxsize(width=840,height=200)
lbl2=Label(win,text="Please Enter any Date : ",bg='#29bf1b',fg='black',height='2',width='32',font=('Times New Roman',16,'bold','italic'))
lbl2.place(x=8,y=64)
ent2=Entry(win,bg='#4c1a5c',fg='#f2973d',textvariable=var1,width='32',font=('Arial 20'))
ent2.place(x=400,y=68)
btn2=Button(win,text='FIND_DAY',bg='#bcbf1b',command=day_find,height='2',width='12',font=('Times New Roman',24,'bold','italic','underline'))
btn2.place(x=140,y=280)
label=Label(win,text= 'WELCOME TO DAY_FINDER',font=('Times New Roman',24,'bold','italic','underline'),bg='#6f7a72',fg='#5c0c69')
label.place(x=200,y=4)
var=StringVar()
lbl1=Label(win,text="Please Enter your name : ",bg='#bf1b8e',fg='black',height='3',width='32',font=('Times New Roman',16,'bold','italic'))
lbl1.place(x=8,y=64)
ent=Entry(win,bg='white',fg='#5c0c69',textvariable=var,width='32',font=('Arial 20'))
ent.place(x=400,y=68)
gen=IntVar()
lbl=Label(win,text="Please select your gender : ",bg='#78bf1b',fg='black',height='2',width='32',font=('Times New Roman',16,'bold','italic'))
lbl.place(x=8,y=160)
radio1=Radiobutton(win,text='Male',value=0,variable=gen,bg='#831bbf')
radio1.place(x=410,y=170,height='40',width='80')
radio2=Radiobutton(win,text='Female',value=1,variable=gen,bg='#1bbf86')
radio2.place(x=500,y=170,height='40',width='80')
btn=Button(win,text='SUBMIT',bg='#bcbf1b',command=sub,height='2',width='12',font=('Times New Roman',24,'bold','italic','underline'))
btn.place(x=140,y=280)
btn3=Button(win,text='EXIT',bg='#bcbf1b',command=destroy,height='2',width='8',font=('Times New Roman',24,'bold','italic','underline'))
btn3.place(x=500,y=280)
win.configure(bg='#6f7a72')
win.protocol("WM_DELETE_WINDOW", disable_event)
win.mainloop()
