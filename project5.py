from customtkinter import *


class MainWindow(CTk):
    def __init__(self):

        self.chat_text=CTkScrollableFrame(self)
        self.chat_text.plac(x=0,y=30)
        self.message_input = CtkEntry(self,placeholder_text="Message")
        self.message_input.place(x=0,y=250)
        self.send_button = CTk(self, text=">")



        super().__init__()
        self.geometry('400x300')

        self.frame = CTkFrame(self, width=200, height=self.winfo_height())
        self.frame.pack_propagate(False)
        self.frame.configure(width=0)
        self.frame.place(x=0, y=0)
        self.is_show_menu = False
        self.frame_width = 0

        self.label = CTkLabel(self.frame, text="Ваше ім'я")
        self.label.pack(pady=30)
        self.entry=CTkEntry(self.frame)
        self.entry.pack()

        self.btn = CTkButton(self, text='☰', command=self.toggle_show_menu, width=30)
        self.btn.place(x=0, y=0)
        self.menu_show_speed = 20

        self.adaptive_ui()

    def toggle_show_menu(self):
        if self.is_show_menu:
            self.is_show_menu = False
            self.close_menu()
        else:
            self.is_show_menu = True
            self.show_menu()




    def show_menu(self):
        if self.frame_width <= 200:
            self.frame_width += self.menu_show_speed
            self.frame.configure(width=self.frame_width, height=self.winfo_height())
            if self.frame_width >= 30:
                self.btn.configure(width=self.frame_width, text='☰')
        if self.is_show_menu:
            self.after(20, self.show_menu)

    def close_menu(self):
        if self.frame_width >= 0:
            self.frame_width -= self.menu_show_speed
            self.frame.configure(width=self.frame_width)
            if self.frame_width >= 30:
                self.btn.configure(width=self.frame_width, text='☰')
        if not self.is_show_menu:
            self.after(20, self.close_menu)

    def adaptive_ui(self):

        self.after(20, self.adaptive_ui)


win = MainWindow()
win.mainloop()