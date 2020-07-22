words=['oklo','uncle','jaleebi','Apple'
       ,'gun','door','ned','fruits',
           'apple', 'Orange', 'Grape','Item' 

       ]
def Slider():
    global count,sliderWords
    text="Welcome to Master your Typing game"
    if(count >=len(text)):
        count=0
        sliderWords=''
    sliderWords += text[count]
    count += 1
    fontL.configure(text=sliderWords)
    fontL.after(160,Slider)
    
def time():
    global timeleft,score,miss
    if(timeleft>0):
        timeleft -=1
        timerCount.configure(text=timeleft)
        timerCount.after(1000,time)
    else:
        details.configure(text="Hit = {} | Miss = {} | Total Score={}".format(score,miss,score-miss))
        nof = messagebox.askretrycancel("PopUp","For playing again click retry")
        if nof==True:
            score=0
            timeleft=60
            miss=0
            timerCount.configure(text=timeleft)
            word.configure(text=words[0])
            scoreCount.configure(text=score)
            
def start(e):
    global score,miss
    if timeleft == 60:
        time()
        
    details.configure(text="")
    if(box.get() == word['text']):
        score +=1
        scoreCount.configure(text=score)
    else:
        miss +=1
    random.shuffle(words)
    word.configure(text=words[0])
    #print(box.get())
    box.delete(0,END)



from tkinter import *
import random
from tkinter import messagebox
root = Tk()
root.geometry('800x600+280+50')
root.configure(bg='sky blue')
root.title('Master Your Typing')
root.iconbitmap('1.ico')

##VARIABLES##
score=0
timeleft=60
count=0
sliderWords=''
miss=0

fontL = Label(root, text="",font=('arial',24,'bold'),bg="sky blue",fg='green',width=40)
fontL.place(x=10,y=10)
Slider()

random.shuffle(words)
word = Label(root, text=words[0],font=('arial',38,'bold'),bg="sky blue")
word.place(x=350,y=200)

box= Entry(root,font=('arial',24,'bold'),bd=8,justify='center')
box.place(x=240,y=300)
box.focus_set()

Score = Label(root, text="Your Score",font=('arial',22,'bold'),bg="sky blue",fg="brown")
Score.place(x=10,y=100)

scoreCount = Label(root, text=score,font=('arial',24,'bold'),bg="sky blue",fg="brown")
scoreCount.place(x=60,y=140)

timer = Label(root, text="Time Left",font=('arial',22,'bold'),bg="sky blue",fg="brown")
timer.place(x=600,y=100)

timerCount = Label(root, text=timeleft,font=('arial',22,'bold'),bg="sky blue",fg="brown")
timerCount.place(x=660,y=140)

details = Label(root, text="Type word and hit enter button",font=('arial',24,'bold'),bg="sky blue",fg="grey")
details.place(x=180,y=450)

root.bind('<Return>',start)
 

root.mainloop()
