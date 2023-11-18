#after method refesh a window afetr a certaion time frame and also call a menthod after that time frame
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    #check timer text
    canvas.itemconfig(timer_text,text="00:00")
    #title reset
    title_label.config(text="Timer")
    #reset check mark
    check_mark.config(text="")
    global reps
    reps=0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN * 60
    short_break_sec=SHORT_BREAK_MIN * 60
    long_break_min=LONG_BREAK_MIN * 60
    
    
    if reps%8==0:
        count_down(long_break_min)
        title_label.config(text="Break",fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        title_label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="work",fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}" #Dynamic Typing
    
        
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0 :
       timer= window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        work_session=math.floor(reps/2)
        for _ in range(work_session):
            mark+="✔"
        check_mark.config(text=mark)




# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("pamodaro")
window.config(padx=100,pady=50,bg=YELLOW,highlightthickness=0) #to modify



title_label=Label(text="Timer",font=(FONT_NAME,50),fg=GREEN)
title_label.grid(column=1,row=0)


canvas=Canvas(width=200,height=224,bg=YELLOW)
tomato_img=PhotoImage(file="tomato.png") #inser the image 
canvas.create_image(102,112,image=tomato_img)#Add the image 
timer_text=canvas.create_text(100,112,text="00:00",fill="white",font=(FONT_NAME,35,"bold")) #text visible on the image
canvas.grid(column=1,row=1)



start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",highlightthickness=0, command=reset_timer)
reset_button.grid(column=2,row=2)

check_mark=Label(bg=YELLOW)
check_mark.grid(column=1,row=3)



window.mainloop()