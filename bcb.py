import time
import tkinter
from tkinter import *


BG_BLACK = "#ffffff"
BG_COLOR = "#000000"
TEXT_COLOR = "#000000"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
#Here defining bot-name
m1 = input("Enter AI name : ")
mn = {'ainame' : m1}
class ChatApplication:

    def __init__(self):
        
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=BG_BLACK,
                           text="Welcome, I am AI chatbot how can i help you", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=450, bg=BG_BLACK)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_BLACK, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.window, bg=BG_COLOR, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg=BG_BLACK, fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Enter", font="#ffffff", width=20, bg=BG_BLACK,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        
    def _on_enter_pressed(self, event):
        msg = (self.msg_entry.get()).lower()
        m = mn.get('ainame')

        self._insert_message(msg, "You", m)

    def _insert_message(self, msg, sender, receiver):
        if not msg:
            return
        m = mn.get('ainame')
        n = time.ctime()
        questions = {
            "hi": "hey",
            "how are you": "I am fine",
            "what is your name": f"my name is {m}",
            "how old are you": "I am just 1 day older",
            "what is time now": n
        }
        nt = " Result not found enter something else"
        if msg in questions :
            msg2 = f"{receiver}: {questions[msg]}\n\n"
        else  :
            msg2 = f"{receiver}: {nt}\n\n"
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
