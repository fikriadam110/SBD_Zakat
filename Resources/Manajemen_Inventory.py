from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector as mysql
import datetime
import os
from os import sys


from Setting import SettingTheme


class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root_settings = SettingTheme()
        self.root.geometry("1200x740")
        self.root.resizable(True, True)
        self.root.overrideredirect(True)
        self.root.configure(bg='#F9ECE0')
        self.root.option_add("*TCombobox*Listbox*Background", "#FFFFFF")
        self.root.option_add("*TCombobox*Listbox*Foreground", "#F4963F")
        self.root.bind('<Escape>', self.closeEsc)
        self.root.attributes("-topmost", True)

        os.chdir(os.path.join(sys.path[0],))


        ## Header window ##
        self.x = None
        self.y = None
        self.frm_header = Frame(self.root, bg="#277454", relief='raised', height=35)
        self.frm_header.pack(side=TOP, fill=BOTH)
        self.frm_header.bind('<ButtonPress-1>', self.mouse_down)
        self.frm_header.bind('<B1-Motion>', self.mouseDrag)
        self.frm_header.bind('<ButtonRelease-1>', self.mouse_up)
        self.frm_header.bind('<Map>', self.frmMappedRoot)

        self.lbl_header_emoji = Label(self.frm_header, font=("Lucida Sans",18), text="📋")
        self.lbl_header_emoji.configure(bg='#277454', fg='#FFFFFF')
        self.lbl_header_emoji.pack(side=LEFT, anchor=NW)

        self.lbl_header = Label(self.frm_header, font=("Lucida Sans",16,'bold'), text="Mari Kita Zakat")
        self.lbl_header.configure(bg='#277454', fg='#FFFFFF')
        self.lbl_header.pack(side=LEFT, anchor=SW)

        self.btn_close = Button(self.frm_header, width=3, height=1, command=lambda: [self.close()])
        self.btn_close.configure(font=('Lucida Sans',10,'bold'),text='X',bg='#43e33d', fg='#E60707', activebackground='#E60707', activeforeground='#FFFFFF')
        self.btn_close.pack(side=RIGHT, anchor=NE, fill=None, expand=False)

        self.btn_min = Button(self.frm_header, width=3, height=1, command=lambda: [self.minimizeRoot()])
        self.btn_min.configure(font=('Lucida Sans',10,'bold'),text='—',bg='#43e33d', fg='#FFFFFF', activebackground='#FFFFFF', activeforeground='#545454')
        self.btn_min.pack(side=RIGHT, anchor=NE, fill=None, expand=False)

        
        ## Body window ##

        # Frame filter
        # self.frm_filter = LabelFrame(self.root,relief='groove', bg="#f08726", height=200,width=300)
        # self.frm_filter.place(x=20,y=50)
        
        # self.lbl_filter = Label(self.root,font=("Lucida Sans",15,'bold underline'),fg='#FFFFFF',bg='#f08726',text=" Filter*                             ").place(x=27,y=60)
        # self.lbl_cari = Label(self.root,font=("Lucida Sans",13,'bold'),fg='#FFFFFF',bg='#f08726',text="Cari").place(x=30,y=100)
        # self.lbl_tbl_kategori = Label(self.root,font=("Lucida Sans",13,'bold'),fg='#FFFFFF',bg='#f08726',text="Kategori").place(x=30,y=140)

        # self.txt_cari = Entry(self.root,width=17,font=("Lucida Sans",11))
        # self.txt_cari.place(x=130,y=103)

        # self.lst_tbl_kategori = ['Semua', 'Dapur', 'Elektronik', 'Fashion', 'Perawatan Tubuh', 'Alat Tulis Kantor']
        # self.cmb_tbl_kategori = ttk.Combobox(self.root, style="TCombobox", state="readonly", font=("Lucida Sans",11,'bold'), value=self.lst_tbl_kategori, width=14)
        # self.cmb_tbl_kategori.set(self.lst_tbl_kategori[0])
        # self.cmb_tbl_kategori.place(x=130,y=140)


        #Frame olah data
        self.frm_olah_data = LabelFrame(self.root,relief='groove', bg="#277454", height=200,width=350)
        self.frm_olah_data.place(x=50,y=300)

        self.img_logo = ImageTk.PhotoImage(Image.open("Gambar/ZakatologyLogo.png").resize((300,300), Image.ANTIALIAS))
        self.lbl_img_logo = Label(self.root, image=self.img_logo, bg='#F9ECE0', borderwidth=0).place(x=530,y=180)

        self.lbl_welcome = Label(self.root,font=("Lucida Sans",15),fg='#277454',bg='#F9ECE0',text="Welcome to Zakatology!").place(x=500,y=100)
        # self.lbl_qty = Label(self.root,font=("Lucida Sans",15,'bold'),fg1='#FFFFFF',bg='#f08726',text="Qty").place(x=70,y=220)

        # self.txt_qty = Entry(self.root,width=17,font=("Lucida Sans",11))
        # self.txt_qty.place(x=130,y=320)

        # self.txt_harga = Entry(self.root,width=17,font=("Lucida Sans",11))
        # self.txt_harga.place(x=180,y=430)

        # self.lst_kategori = ['Zakat', 'Zakat', 'Zakat', 'Zakat', 'Zakat']
        # self.cmb_kategori = ttk.Combobox(self.root, style="TCombobox", state="readonly", font=("Lucida Sans",12,'bold'), value=self.lst_kategori, width=14)
        # self.cmb_kategori.set("Pilih Jenis Zakat")
        # self.cmb_kategori.place(x=180,y=385)

        self.btn_tambah = ttk.Button(self.root,style="TButton",text='Tambah',width=10)
        self.btn_tambah.place(x=190,y=460)

        # self.btn_edit = ttk.Button(self.root,style="TButton",text='Edit',width=10)
        # self.btn_edit.place(x=300,y=330)

        # self.btn_hapus = ttk.Button(self.root,style="TButton",text='Hapus',width=10)
        # self.btn_hapus.place(x=300,y=330)

        # self.img_recycle = ImageTk.PhotoImage(Image.open("Resources/Gambar/recycle.png").resize((30,30), Image.ANTIALIAS))
        # self.img_recycle_orange = ImageTk.PhotoImage(Image.open("Resources/Gambar/recycleOrange.png").resize((30,30), Image.ANTIALIAS))
        # self.btn_recycle = ttk.Button(self.root,style="TButton",image=self.img_recycle,width=10)
        # self.btn_recycle.place(x=890,y=110)
        # self.btn_recycle.bind("<Enter>", self.onHover)
        # self.btn_recycle.bind("<Leave>", self.offHover)

        
        

        # self.tabelInventory()


    # Menunjukkan tabel dari database
    # def tabelInventory(self):
    #     self.frm_tabel = Frame(self.root, bg='#277454', borderwidth=0)
    #     self.frm_tabel.place(x=20,y=260)

    #     self.scrollTree = ttk.Scrollbar(self.frm_tabel, style="TScrollbar", orient='vertical')
        
    #     self.cols = ('ID Barang','Nama','Kategori','Qty','Harga')
    #     self.listBox = ttk.Treeview(self.frm_tabel, style="listBox.Treeview", columns=self.cols, show='headings', yscrollcommand=self.scrollTree.set,height=20)
    #     self.listBox.pack(side=LEFT, fill=Y)

    #     self.scrollTree.config(command=self.listBox.yview)
    #     self.scrollTree.pack(side=RIGHT, fill=Y)

    #     for self.col in self.cols:
    #         self.listBox.heading(self.col, text=self.col)
    #         self.listBox.column('ID Barang', minwidth=0, width=130, stretch=NO, anchor = CENTER)
    #         self.listBox.column('Nama', minwidth=0, width=310, stretch=NO, anchor = W)
    #         self.listBox.column('Kategori', minwidth=0, width=200, stretch=NO, anchor = W)
    #         self.listBox.column('Qty', minwidth=0, width=100, stretch=NO, anchor = CENTER)
    #         self.listBox.column('Harga', minwidth=0, width=200, stretch=NO, anchor = W)

    #     self.conn = mysql.connect(user="root", password="", database='db_Sahabat_Masyarakat', host="localhost", port='3306')
    #     self.c = self.conn.cursor()

    #     self.c.execute("""SELECT CONCAT(prefix,a.id_barang) as ID, a.nama, kategori, qty, harga
	#                         from tb_inventory A
	#                         inner join tb_detail_barang B on a.nama = b.nama and a.id_barang = b.id_barang
	# 	                        where a.status_data = %s and b.status_data = %s""",
    #     ('Aktif','Aktif'))
    #     self.record = self.c.fetchall()
    #     self.conn.commit()
    #     # print(type(self.record))
    #     # print(self.record[0])
        
    #     for i, (id_barang,nama,kategori,qty,harga) in enumerate(self.record, start=1):
    #         self.listBox.insert("", "end", values=(id_barang,nama,kategori,qty,"Rp {:,},-".format(harga)), tags=('ganjil',))
    #         self.conn.close()
        
    #     # print(self.txt_nama)

    #     self.listBox.bind('<ButtonRelease-1>',self.GetValue)


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
        self.top.destroy()

    def closeEsc(self,e):
        self.root.destroy()
        self.top.destroy()


    # Untuk menggerakkan header (frame) window
    def mouse_down(self, e):
        self.x = e.x
        self.y = e.y

    def mouse_up(self, e):
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

    
    def onHover(self, e):
        self.btn_recycle.configure(image=self.img_recycle_orange)
    
    def offHover(self, e):
        self.btn_recycle.configure(image=self.img_recycle)


    # Untuk mengambil nilai pada saat tabel di klick
    def GetValue(self, e):
        self.txt_nama.delete(0, END)
        self.txt_qty.delete(0, END)
        self.txt_harga.delete(0, END)
        rowID = self.listBox.selection()[0]
        select = self.listBox.set(rowID)

        self.id_barang_temp = ''.join(select['ID Barang'])
        self.id_barang = int(self.id_barang_temp[4:])

        self.txt_nama.insert(0,select['Nama'])
        self.txt_qty.insert(0,select['Qty'])
        self.txt_harga.insert(0,select['Harga'])
        self.nama = (select['Nama'])
        self.qty = (select['Qty'])
        
        self.kategori_temp = ''.join(select['Kategori'])
        # self.kategori_brg = str(self.kategori_temp[:3])
        if self.kategori_temp == self.lst_kategori[0]:
            self.kategori = self.lst_kategori[0]
        elif self.kategori_temp == self.lst_kategori[1]:
            self.kategori = self.lst_kategori[1]
        elif self.kategori_temp == self.lst_kategori[2]:
            self.kategori = self.lst_kategori[2]
        elif self.kategori_temp == self.lst_kategori[3]:
            self.kategori = self.lst_kategori[3]
        elif self.kategori_temp == self.lst_kategori[4]:
            self.kategori = self.lst_kategori[4]
        elif self.kategori_temp == self.lst_kategori[5]:
            self.kategori = self.lst_kategori[5]
        self.cmb_kategori.set(self.kategori)

        self.harga_temp = self.txt_harga.get()
        self.harga_temp = (select['Harga'])
        self.harga = str(self.harga_temp.replace(",","")[3:][:-1])
        self.txt_harga.delete(0, END)
        self.txt_harga.insert(0, self.harga)

        print(self.id_barang)
        print(self.nama)
        print(self.kategori)
        print(self.qty)
        print(self.harga)



if __name__ == "__main__":
    main = MainWindow()
    main.root.mainloop()
