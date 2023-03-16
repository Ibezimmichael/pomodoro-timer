from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW)
    check_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}.{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
            check_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 132, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=1, column=1)

start_button = Button(text="Start", fg=RED, bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="reset", fg=RED, bg=YELLOW, highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)
check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)
window.mainloop()

