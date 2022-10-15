from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
check = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    main_label.config(text="Title", fg=GREEN)
    done_label.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        long_break_sec = LONG_BREAK_MIN * 60
        main_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif REPS % 2 == 0:
        short_break_sec = SHORT_BREAK_MIN * 60
        main_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        work_sec = WORK_MIN * 60
        main_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(int(count) / 60)
    count_sec = int(count) % 60
    if count_sec == 0:
        count_sec = "00"
    elif int(count_sec) < 10 and int(count_sec) != 0:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    if count_min == 0 and count_sec == "00" and REPS < 8:
        if REPS % 2 != 0:
            global check
            check += 1
            done_label.config(text="✔" * check)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

# main label
main_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
main_label.grid(row=0, column=1)

# button start
button_start = Button(text="Start", command=start_timer, bg=GREEN, fg=RED, highlightthickness=0)
button_start['font'] = FONT_NAME
button_start.grid(row=2, column=0)

# button reset
button_reset = Button(text="Reset", command=reset_timer, bg=GREEN, fg=RED, highlightthickness=0)
button_reset['font'] = FONT_NAME
button_reset.grid(row=2, column=3)

# label ✔
done_label = Label(font=(FONT_NAME, 13, "bold"), bg=YELLOW, fg=GREEN)
done_label.grid(row=3, column=1)

window.mainloop()
