from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Technique")
window.config(padx=100, pady=60, bg=YELLOW)
#window.wm_attributes('-transparentcolor', GREEN)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
t_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=t_image)
canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 35, 'bold'), fill='white' )
canvas.grid(column=1, row=1)

timer = Label(text='Timer', font=(FONT_NAME, 55, 'bold'), bg=YELLOW, fg=GREEN, highlightthickness=0)
timer.grid(column=1, row=0)

start = Button(text='Start', highlightthickness=0)
start.grid(column=0, row=2)

reset = Button(text='Reset', highlightthickness=0)
reset.grid(column=2, row=2)

done = Label(text='✅', fg='green', bg=YELLOW, highlightthickness=0)
done.grid(column=1, row=3)

window.mainloop()

