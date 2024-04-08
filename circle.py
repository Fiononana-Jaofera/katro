from algo import *

class CircleButton(tk.Canvas):
    def __init__(self, parent, color, name, bg, text=2,radius=40):
        super().__init__(parent, width=radius*2, height=radius*2, bd=0, highlightthickness=0, name=name, bg=bg, cursor="hand2")
        self.color = color
        self.parent = parent
        self.oval_id =self.create_oval(0, 0, radius*2, radius*2, fill=self.color, outline=self.color)
        self.text_id = self.create_text(radius, radius, text=text, font=("Arial", 15, "bold"), fill="white")
        self.bind("<ButtonPress-1>", self.on_button_click)
        self.bind("<ButtonRelease-1>", self.on_button_release)

    def update_text(self, new_text):
        self.itemconfig(self.text_id, text=new_text)

    def get_element(self):
        return int(self.itemcget(self.text_id, 'text'))
    
    def clear(self):
        self.update_text(0)
    
    def add_element(self, e=1):
        lst_number = self.get_element()
        self.update_text(lst_number+e)

    def on_button_release(self, event):
        self.itemconfig(self.oval_id, fill=self.color)
        self.itemconfig(self.text_id, fill='white')

    def on_button_click(self, event):
        widget_name = str(event.widget)
        lst_number = self.get_element()
        if lst_number > 0 and widget_name.split('.')[1]=='player':
            start(widget_name)
            self.itemconfig(self.oval_id, fill='white')
            self.itemconfig(self.text_id, fill=self.color)
