from csv import DictReader
import random
from tkinter import *
from datetime import datetime
import os



os.chdir('E:/COMPLETED_ SCRIPTS/DeeQuotes')

f = open('success.csv', 'r')
r = DictReader(f)
thoughts_l = []
writer_l = []

for row in r:
        thoughts_l.append(row['QUOTE'])
        writer_l.append(row['AUTHOR'])

rand_int = random.randint(0,len(thoughts_l)-1)

thought_for_the_day = thoughts_l[rand_int]




c = 1
thought = []
temp = ''
for i in thought_for_the_day.split():       
        temp += ' '+i
        if c == 5:
                thought.append(temp)
                temp = ''
                c = 0
        c+=1



thought.append(temp)
thought.append(f'- {writer_l[rand_int]}')







win = Tk()
win.geometry('550x400+260+140')
win.resizable(0,0)
win.title('Thought Of The Day')
                

good_morning_img = PhotoImage(file='resources/g_morning.png')
good_afternoon_img = PhotoImage(file='resources/g_after.png')
good_evening_img = PhotoImage(file='resources/g_evening.png')

if len(thought) > 6:
        win.geometry('550x450+260+140')
if len(thought) > 8:
        win.geometry('550x500+260+130')
if len(thought) > 10:
        win.geometry('550x550+260+120')
if len(thought) > 12:
        win.geometry('550x620+260+100')

t = datetime.now().strftime('%H  hours and %M minutes')          
o= t.split()
if int(o[0]) < 12:
        cur_img = good_morning_img
elif int(o[0]) > 12 and int(o[0]) < 17 :
        cur_img = good_afternoon_img
else:
        cur_img = good_evening_img

Label(win, image=cur_img).pack()

t_img = PhotoImage(file='resources/t_img.png')
Label(win, image=t_img).pack(side=LEFT)

thought = '\n'.join(thought)

Label(win, text=thought,font=('Segoe Script',13)).place(x=150,y=230)

win.mainloop()



