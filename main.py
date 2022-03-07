from tkinter import *
import math as m

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
clock = None

# ---------------------------- TIMER RESET ------------------------------- # 
def re_set():
    global rep
    window.after_cancel(clock)
    timer.config(text='Timer', fg=GREEN)
    canvas.itemconfig(time_text, text=f'00:00')
    done.config(text='')
    rep = 0




# ---------------------------- TIMER MECHANISM ------------------------------- #

def set_timer():
    global rep
    rep += 1
    work_sec = WORK_MIN * 60
    sh_sec = SHORT_BREAK_MIN * 60
    lg_sec = LONG_BREAK_MIN * 60

    if rep % 8 == 0:
        count_down(lg_sec)
        timer.config(text='Break', fg=RED)
    elif rep % 2 == 0:
        count_down(sh_sec)
        timer.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text='Work', fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global clock
    mint = m.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f'0{sec}'

    canvas.itemconfig(time_text, text=f'{mint}:{sec}')
    if count > 0:
        clock = window.after(1000, count_down, count-1)
    else:
        set_timer()
        mark = ''
        for _ in range(m.floor(rep/2)):
            mark += '✅'
        done.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Technique")
window.config(padx=100, pady=60, bg=YELLOW)
#window.wm_attributes('-transparentcolor', GREEN)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
t_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=t_image)
time_text = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 35, 'bold'), fill='white' )
canvas.grid(column=1, row=1)

timer = Label(text='Timer', font=(FONT_NAME, 55, 'bold'), bg=YELLOW, fg=GREEN, highlightthickness=0)
timer.grid(column=1, row=0)

start = Button(text='Start', highlightthickness=0, command=set_timer)
start.grid(column=0, row=2)

reset = Button(text='Reset', highlightthickness=0, command=re_set)
reset.grid(column=2, row=2)

done = Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
done.grid(column=1, row=3)

window.mainloop()

