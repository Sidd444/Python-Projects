from tkinter import *
from tkinter import messagebox

def click(event):
    global sc_value
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            sc_value.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            sc_value.set("")
    elif text == "C":
        sc_value.set("")
    else:
        if text == '×':
            text = '*'
        elif text == '÷':
            text = '/'
        sc_value.set(sc_value.get() + text)

window = Tk()
window.title("🧮 Siddharth's Tkinter Calculator")
window.geometry("400x500")
window.configure(bg="dimgray")

sc_value = StringVar()
sc_value.set("")
screen = Entry(window, textvar=sc_value, font="calibiri 20 bold", bg="darkslategray", fg="white", bd=5, relief="sunken")
screen.pack(fill=BOTH, ipadx=8, pady=10, padx=10)

button_frame = Frame(window, bg="black")
button_frame.pack()

number_bg = "green"
symbol_bg = "blue"
button_fg = "white"
on_off_bg = "red"
button_width = 5
button_height = 2

buttons = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "×"],
    ["C", "0", "=", "÷"]
]

for row_idx, row in enumerate(buttons):
    for col_idx, button in enumerate(row):
        if button.isdigit():
            bg_color = number_bg
        elif button in ["+", "-", "×", "÷", "="]:
            bg_color = symbol_bg
        elif button == "C":
            bg_color = on_off_bg
        else:
            bg_color = "gray"

        btn = Button(button_frame,text=button,font="calibiri 15 bold",width=button_width,height=button_height,bg=bg_color,fg=button_fg,relief="raised",bd=3)
        btn.grid(row=row_idx, column=col_idx, padx=5, pady=5)

        if button not in ["ON", "OFF"]:
            btn.bind("<Button-1>", click)

footer = Label(window, text="🧮 Siddharth's Tkinter Calculator", font="calibiri 15 bold", fg="white", bg="dimgray")
footer.pack(pady=10)

mainloop()
