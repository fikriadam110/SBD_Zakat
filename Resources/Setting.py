from tkinter import *
from tkinter import ttk



class SettingTheme:
    def __init__(self):
        self.theme = ttk.Style()
        self.theme.theme_use('clam')
        self.theme.configure("listBox.Treeview.Heading", font=('Lucida Sans', 10,'bold'), foreground="#FFFFFF", background="#FF7A00")
        self.theme.configure("listBox.Treeview.Heading", borderwidth=1,bordercolor="#393939",lightcolor="#FF7A00",darkcolor="#FF7A00")
        self.theme.configure("listBox.Treeview", fieldbackground="#D0D0D0", activebackground="#F4963F")
        self.theme.map("listBox.Treeview", background=[('selected', '#277454')], foreground=[('selected','#FFFFFF')])

        self.theme.configure("TCombobox", arrowcolor='#43e33d')
        self.theme.map("TCombobox", background=[('readonly','#43e33d')], foreground=[('readonly','#FFFFFF')])
        self.theme.map("TCombobox", bordercolor=[('readonly','#43e33d')], darkcolor=[('readonly','#43e33d')], lightcolor=[('readonly','#43e33d')])
        self.theme.map("TCombobox", fieldbackground=[('readonly','#43e33d')])
        self.theme.map("TCombobox", selectbackground=[('readonly','#43e33d')], selectforeground=[('readonly','#FFFFFF')])

        self.theme.configure("TScrollbar", troughcolor='#008BD0', background='#F4963F', bordercolor='#393939', darkcolor='#393939', lightcolor='#393939', arrowcolor='#393939')
        self.theme.map("TScrollbar", background=[('active','#F4963F'), ('disabled','#F4963F')])

        self.theme.configure("TButton",background='#277454',foreground='#FFFFFF')
        self.theme.configure("TButton",bordercolor='#277454',lightcolor='#393939',darkcolor='#393939')
        self.theme.configure("TButton",font=("Lucida Sans",11,'bold'))
        self.theme.map("TButton", foreground=[('active', '#F4963F')])

        self.theme.configure("Login.TButton",background='#42A079',foreground='#FFFFFF')
        self.theme.configure("Login.TButton",bordercolor='#0B5B3A',lightcolor='#0B5B3A',darkcolor='#0B5B3A')
        self.theme.configure("Login.TButton",font=("Lucida Sans",13))
        self.theme.map("Login.TButton", foreground=[('active', '#42A079')])

        self.theme.configure("Kasir.TButton",background='#277454',foreground='#FFFFFF')
        self.theme.configure("Kasir.TButton",bordercolor='#393939',lightcolor='#393939',darkcolor='#393939')
        self.theme.configure("Kasir.TButton",font=("Lucida Sans",10,'bold'))
        self.theme.map("Kasir.TButton", foreground=[('active', '#F4963F')])

        self.theme.configure("Item", focuscolor="#F4963F")
        # self.theme.tag_configure("selectedRow", background="#F4963F", foreground="#FFFFFF")
        


        
