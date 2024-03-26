from algo import *

class CircleButton(tk.Canvas):
    def __init__(self, parent, color, name, text=2,radius=50):
        super().__init__(parent, width=radius*2, height=radius*2, bd=0, highlightthickness=0, name=name)
        self.parent = parent
        self.create_oval(0, 0, radius*2, radius*2, fill=color, outline=color)
        self.text_id = self.create_text(radius, radius, text=text, font=("Arial", 20, "bold"), fill="white")
        self.bind("<ButtonPress-1>", self.on_button_click)

    def update_text(self, new_text):
        self.itemconfig(self.text_id, text=new_text)

    def get_element(self):
        return int(self.itemcget(self.text_id, 'text'))
    
    def clear(self):
        self.update_text(0)
    
    def add_element(self, e=1):
        lst_number = self.get_element()
        self.update_text(lst_number+e)

    def on_button_click(self, event):
        widget_name = str(event.widget)
        lst_number = self.get_element()
        if lst_number > 0 and widget_name.split('.')[1]=='player':
            start(widget_name)