from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from os import sys
import mysql.connector as mysql
import datetime
import os


from Resources.Setting import SettingTheme


# Membuat database dan tabel jika belum ada
# def createDatabase():
#     conn = mysql.connect(user="root", password="", host="localhost", port='3306')
#     c = conn.cursor()

#     c.execute("CREATE DATABASE IF NOT EXISTS db_Sahabat_Masyarakat")
#     conn.commit()

#     conn.close()

# def createTable():
#     conn = mysql.connect(user="root", password="", database='db_Sahabat_Masyarakat', host="localhost", port='3306')
#     c = conn.cursor()

#     c.execute("""CREATE TABLE IF NOT EXISTS tb_Inventory (
#         prefix VARCHAR(4) NOT NULL DEFAULT 'ITM-',
#         id_barang INT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
#         nama VARCHAR(255) NOT NULL,
#         qty INT(4) UNSIGNED,
#         harga INT(9) UNSIGNED,
#         dibuat DATETIME NULL,
#         diubah DATETIME NULL,
#         status_data VARCHAR(255) NULL,
#         PRIMARY KEY (id_barang),
#         UNIQUE KEY (prefix, id_barang),
#         UNIQUE KEY (nama),
#         INDEX (nama, harga)
#         ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1
#         """)
#     conn.commit()

#     c.execute("""CREATE TABLE IF NOT EXISTS tb_Detail_Barang (
#         id_barang INT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
#         nama VARCHAR(255) NOT NULL,
#         kategori VARCHAR(255) NOT NULL,
#         dibuat DATETIME NULL,
#         diubah DATETIME NULL,
#         status_data VARCHAR(255) NULL,
#         PRIMARY KEY (id_barang),
#         INDEX (nama, kategori)
#         ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1
#     """)

#     c.execute("""CREATE TABLE IF NOT EXISTS tb_User (
#         username VARCHAR(255) PRIMARY KEY,
#         password VARCHAR(255) NOT NULL,
#         dibuat DATETIME NULL,
#         diubah DATETIME NULL,
#         status_data VARCHAR(255) NULL
#          )
#     """)
#     conn.commit()

#     c.execute("""CREATE TABLE IF NOT EXISTS tb_Riwayat_Pembelian (
#         id_struk INT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
#         nama VARCHAR(255) NOT NULL,
#         qty INT(4) NOT NULL,
#         total INT(9) NOT NULL,
#         dibuat DATETIME NULL,
#         diubah DATETIME NULL,
#         status_data VARCHAR(255) NULL,
#         PRIMARY KEY (id_struk)
#         ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1
#     """)
#     conn.commit()

#     c.execute("""CREATE TABLE IF NOT EXISTS tb_Tabungan (
#         id_tabungan INT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
#         pemasukkan INT(9) NOT NULL,
#         saldo_toko INT(12) NOT NULL,
#         dibuat DATETIME NULL,
#         diubah DATETIME NULL,
#         status_data VARCHAR(255) NULL,
#         PRIMARY KEY(id_tabungan),
#         INDEX (pemasukkan, saldo_toko)
#         ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1
#     """) 
#     conn.commit()

#     c.execute("""CREATE TABLE IF NOT EXISTS tb_Log_Data (
#         id_log INT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
#         user VARCHAR(255) NOT NULL,
#         aksi VARCHAR(255) NOT NULL,
#         tabel VARCHAR(255) NOT NULL,
#         dibuat DATETIME NULL,
#         diubah DATETIME NULL,
#         status_data VARCHAR(255) NULL,
#         PRIMARY KEY(id_log),
#         INDEX (user, aksi, tabel)
#         ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1
#     """)
#     conn.commit()

#     conn.close()


# def opens(filename):
#     os.chdir(os.path.join(sys.path[0],))
#     os.system('python '+filename)
    

class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root_settings = SettingTheme()
        self.root.geometry("480x740")
        self.root.resizable(True, True)
        self.root.overrideredirect(True)
        self.root.configure(bg='#F9ECE0')
        self.root.option_add("*TCombobox*Listbox*Background", "#FFFFFF")
        self.root.option_add("*TCombobox*Listbox*Foreground", "#F4963F")
        self.root.bind('<Escape>', self.closeEsc)
        self.root.attributes("-topmost", True)


        ## Header window ##
        self.x = None
        self.y = None
        self.frm_header = Frame(self.root, bg="#277454", relief='raised', height=35)
        self.frm_header.pack(side=TOP, fill=BOTH)
        self.frm_header.bind('<ButtonPress-1>', self.mouseDown)
        self.frm_header.bind('<B1-Motion>', self.mouseDrag)
        self.frm_header.bind('<ButtonRelease-1>', self.mouseUp)
        self.frm_header.bind('<Map>', self.frmMappedRoot)

        # self.img_header_emoji = ImageTk.PhotoImage(Image.open("Resources/Gambar/Loginlogo.png").resize((25,25), Image.ANTIALIAS))
        # self.lbl_header_emoji = Label(self.frm_header, image=self.img_header_emoji, borderwidth=0, bg='#277454')
        # self.lbl_header_emoji.pack(side=LEFT, anchor=W)

        self.lbl_header = Label(self.frm_header, font=("Lucida Sans",18,'bold'), text="Zakatologi")
        self.lbl_header.configure(bg='#277454', fg='#FFFFFF')
        self.lbl_header.pack(side=LEFT, anchor=SW)

        self.btn_close = Button(self.frm_header, width=3, height=1, command=lambda: [self.close()])
        self.btn_close.configure(font=('Lucida Sans',10,'bold'),text='X',bg='#277454', fg='#E60707', activebackground='#E60707', activeforeground='#FFFFFF')
        self.btn_close.pack(side=RIGHT, anchor=NE, fill=None, expand=False)

        self.btn_min = Button(self.frm_header, width=3, height=1, command=lambda: [self.minimizeRoot()])
        self.btn_min.configure(font=('Lucida Sans',10,'bold'),text='—',bg='#277454', fg='#FFFFFF', activebackground='#FFFFFF', activeforeground='#545454')
        self.btn_min.pack(side=RIGHT, anchor=NE, fill=None, expand=False)



        self.img_logo = ImageTk.PhotoImage(Image.open("Resources/Gambar/ZakatologyLogo.png").resize((240,240), Image.ANTIALIAS))
        self.lbl_img_logo = Label(self.root, image=self.img_logo, bg='#F9ECE0', borderwidth=0).place(x=120,y=60)

        self.frm_sign_up = Frame(self.root, background='#42A079', borderwidth=0, relief=GROOVE, width=390,height=290)
        self.frm_sign_up.place(x=45,y=330)

        self.lbl_sign_up = Label(self.root, font=('Lucida Sans',28),bg="#42A079",fg="#FFFFFF",text="Sign Up").place(x=168,y=340)

        self.img_user = ImageTk.PhotoImage(Image.open("Resources/Gambar/Loginlogo.png").resize((40,40), Image.ANTIALIAS))
        self.lbl_img_user = Label(self.root, image=self.img_user, bg='#42A079', borderwidth=0).place(x=90,y=410)

        self.img_pass = ImageTk.PhotoImage(Image.open("Resources/Gambar/passwordlogo.png").resize((40,40), Image.ANTIALIAS))
        self.lbl_img_pass = Label(self.root, image=self.img_pass, bg='#42A079', borderwidth=0).place(x=90,y=470)

        self.frm_txt_user = Frame(self.root, width=210, height=30,bg='#FFFFFF').place(x=157,y=415)
        self.txt_user = Entry(self.frm_txt_user,bg='#FFFFFF',width=20,font=('Lucida Sans',12),borderwidth=0)
        self.txt_user.place(x=160,y=420)

        self.frm_txt_pass = Frame(self.root, width=210, height=30,bg='#FFFFFF').place(x=157 ,y=475)
        self.txt_pass = Entry(self.frm_txt_user,bg='#FFFFFF',width=20,font=('Lucida Sans',12),borderwidth=0)
        self.txt_pass.place(x=160,y=480)

        self.btn_sign_up = ttk.Button(self.root,style="Login.TButton", text="Sign Up", width=8, command=lambda: [])
        self.btn_sign_up.place(x=190,y=540)

        self.lbl_login_below1 = Label(self.root, font=('Lucida Sans',13),bg="#F9ECE0",fg="#000000",text="Already have an account? Login below!").place(x=77,y=635)
        self.lbl_btn_login = Label(self.root, font=('Lucida Sans',16),bg="#F9ECE0",fg="#3F9672",text="Login").place(x=208,y=670)

       


    # Fungsi header window
    def frmMappedRoot(self, e):
        self.root.update_idletasks()
        self.root.overrideredirect(True)
        self.root.state('normal')

    def frmMappedTop(self, e):
        self.top.update_idletasks()
        self.top.overrideredirect(True)
        self.top.state('normal')

    def minimizeRoot(self):
        self.root.update_idletasks()
        self.root.overrideredirect(False)
        self.root.state('iconic')

    def minimizeTop(self):
        self.top.update_idletasks()
        self.top.overrideredirect(False)
        self.top.state('iconic')

    def close(self):
        self.root.destroy()
        self.top.destroy

    def closeEsc(self,e):
        self.root.destroy()
        self.top.destroy()


    # Untuk menggerakkan header (frame) window
    def mouseDown(self, e):
        self.x = e.x
        self.y = e.y

    def mouseUp(self, e):
        self.x = None
        self.y = None

    def mouseDrag(self, e):
        try:
            self.deltax = e.x - self.x
            self.deltay = e.y - self.y
            self.x0 = self.root.winfo_x() + self.deltax
            self.y0 = self.root.winfo_y() + self.deltay
            self.root.geometry("+%s+%s" % (self.x0, self.y0))

            self.x0 = self.top.winfo_x() + self.deltax
            self.y0 = self.top.winfo_y() + self.deltay
            self.top.geometry("+%s+%s" % (self.x0, self.y0))
        except:
            pass


if __name__ == "__main__":
    # createDatabase()
    # createTable()
    main = MainWindow()
    main.root.mainloop()