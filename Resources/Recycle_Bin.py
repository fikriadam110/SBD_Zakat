from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import datetime
import mysql.connector as mysql

from Setting import SettingTheme


# Membuat database dan tabel jika belum ada
def createDatabase():
    conn = mysql.connect(user="root", password="", host="localhost", port='3306')
    c = conn.cursor()

    c.execute("CREATE DATABASE IF NOT EXISTS db_Sahabat_Masyarakat")
    conn.commit()

    conn.close()

def createTable():
    conn = mysql.connect(user="root", password="", database='db_Sahabat_Masyarakat', host="localhost", port='3306')
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS tb_Inventory (
        prefix VARCHAR(4) NOT NULL DEFAULT 'ITM-',
        id_barang INT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
        nama VARCHAR(255) NOT NULL,
        qty INT(4) UNSIGNED,
        harga INT(9) UNSIGNED,
        dibuat DATETIME NULL,
        diubah DATETIME NULL,
        status_data VARCHAR(255) NULL,
        PRIMARY KEY (id_barang),
        UNIQUE KEY (prefix, id_barang),
        UNIQUE KEY (nama),
        INDEX (nama, harga)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1
        """)
    conn.commit()

    c.execute("""CREATE TABLE IF NOT EXISTS tb_Detail_Barang (
        id_barang INT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
        nama VARCHAR(255) NOT NULL,
        kategori VARCHAR(255) NOT NULL,
        dibuat DATETIME NULL,
        diubah DATETIME NULL,
        status_data VARCHAR(255) NULL,
        PRIMARY KEY (id_barang),
        INDEX (nama, kategori)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1
    """)

    c.execute("""CREATE TABLE IF NOT EXISTS tb_User (
        username VARCHAR(255) PRIMARY KEY,
        password VARCHAR(255) NOT NULL,
        dibuat DATETIME NULL,
        diubah DATETIME NULL,
        status_data VARCHAR(255) NULL
         )
    """)
    conn.commit()

    c.execute("""CREATE TABLE IF NOT EXISTS tb_Riwayat_Pembelian (
        id_struk INT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
        nama VARCHAR(255) NOT NULL,
        qty INT(4) NOT NULL,
        total INT(9) NOT NULL,
        dibuat DATETIME NULL,
        diubah DATETIME NULL,
        status_data VARCHAR(255) NULL,
        PRIMARY KEY (id_struk)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1
    """)
    conn.commit()

    c.execute("""CREATE TABLE IF NOT EXISTS tb_Tabungan (
        id_tabungan INT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
        pemasukkan INT(9) NOT NULL,
        saldo_toko INT(12) NOT NULL,
        dibuat DATETIME NULL,
        diubah DATETIME NULL,
        status_data VARCHAR(255) NULL,
        PRIMARY KEY(id_tabungan),
        INDEX (pemasukkan, saldo_toko)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1
    """) 
    conn.commit()

    c.execute("""CREATE TABLE IF NOT EXISTS tb_Log_Data (
        id_log INT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
        user VARCHAR(255) NOT NULL,
        aksi VARCHAR(255) NOT NULL,
        tabel VARCHAR(255) NOT NULL,
        dibuat DATETIME NULL,
        diubah DATETIME NULL,
        status_data VARCHAR(255) NULL,
        PRIMARY KEY(id_log),
        INDEX (user, aksi, tabel)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1
    """)
    conn.commit()

    conn.close()


class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1000x440")
        self.root_settings = SettingTheme()
        self.root.resizable(True, True)
        self.root.overrideredirect(True)
        self.root.configure(bg='#eb8f3b')
        self.root.option_add("*TCombobox*Listbox*Background", "#FFFFFF")
        self.root.option_add("*TCombobox*Listbox*Foreground", "#F4963F")
        self.root.bind('<Escape>', self.closeEsc)


        ## Header window ##
        self.x = None
        self.y = None
        self.frm_header = Frame(self.root, bg="#ff6f00", relief='raised', height=35)
        self.frm_header.pack(side=TOP, fill=BOTH)
        self.frm_header.bind('<ButtonPress-1>', self.mouse_down)
        self.frm_header.bind('<B1-Motion>', self.mouseDrag)
        self.frm_header.bind('<ButtonRelease-1>', self.mouse_up)
        self.frm_header.bind('<Map>', self.frmMappedRoot)


        self.img_header_emoji = ImageTk.PhotoImage(Image.open("Resources/Gambar/recycle.png").resize((25,25), Image.ANTIALIAS))
        self.lbl_header_emoji = Label(self.frm_header, image=self.img_header_emoji, borderwidth=0, bg='#FF7A00')
        self.lbl_header_emoji.configure(bg='#ff6f00', fg='#FFFFFF')
        self.lbl_header_emoji.pack(side=LEFT, anchor=W)

        self.lbl_header = Label(self.frm_header, font=("Lucida Sans",16,'bold'), text="Recycle Bin")
        self.lbl_header.configure(bg='#ff6f00', fg='#FFFFFF')
        self.lbl_header.pack(side=LEFT, anchor=SW)

        self.btn_close = Button(self.frm_header, width=3, height=1, command=lambda: [self.close()])
        self.btn_close.configure(font=('Lucida Sans',10,'bold'),text='X',bg='#FF7A00', fg='#E60707', activebackground='#E60707', activeforeground='#FFFFFF')
        self.btn_close.pack(side=RIGHT, anchor=NE, fill=None, expand=False)

        self.btn_min = Button(self.frm_header, width=3, height=1, command=lambda: [self.minimizeRoot()])
        self.btn_min.configure(font=('Lucida Sans',10,'bold'),text='—',bg='#FF7A00', fg='#FFFFFF', activebackground='#FFFFFF', activeforeground='#FF7A00')
        self.btn_min.pack(side=RIGHT, anchor=NE, fill=None, expand=False)
    
        
        ## Body window ##
        self.lbl_cari = Label(self.root, font=("Lucida Sans",15,'bold'),fg='#FFFFFF',bg='#eb8f3b',text="Cari").place(x=20,y=45)

        self.txt_cari = Entry(self.root, font=("Lucida Sans",11))
        self.txt_cari.place(x=100,y=48)

        self.lst_tbl_kategori = ['Semua', 'Dapur', 'Elektronik', 'Fashion', 'Perawatan Tubuh', 'Alat Tulis Kantor']
        self.cmb_tbl_kategori = ttk.Combobox(self.root, style="TCombobox", state="readonly", font=("Lucida Sans",11,'bold'), value=self.lst_tbl_kategori, width=17)
        self.cmb_tbl_kategori.set(self.lst_tbl_kategori[0])
        self.cmb_tbl_kategori.place(x=100,y=83)

        self.btn_kembali = ttk.Button(self.root,style="TButton",text='Kembali',width=10)
        self.btn_kembali.place(x=700,y=60)

        self.btn_pulihkan = ttk.Button(self.root,style="TButton",text='Pulihkan',width=10)
        self.btn_pulihkan.place(x=830,y=60)

        self.tabelRecycleBin()


    # Menunjukkan tabel dari database
    def tabelRecycleBin(self):
        self.frm_tabel = Frame(self.root, bg='#75B4E7', borderwidth=0)
        self.frm_tabel.place(x=20,y=130)

        self.scrollTree = ttk.Scrollbar(self.frm_tabel, style="TScrollbar", orient='vertical')
        
        self.cols = ('ID Barang','Nama','Kategori','Qty','Harga')
        self.listBox = ttk.Treeview(self.frm_tabel, style="listBox.Treeview", columns=self.cols, show='headings', yscrollcommand=self.scrollTree.set,height=13)
        self.listBox.pack(side=LEFT, fill=Y)

        self.scrollTree.config(command=self.listBox.yview)
        self.scrollTree.pack(side=RIGHT, fill=Y)

        for self.col in self.cols:
            self.listBox.heading(self.col, text=self.col)
            self.listBox.column('ID Barang', minwidth=0, width=130, stretch=NO, anchor = CENTER)
            self.listBox.column('Nama', minwidth=0, width=410, stretch=NO, anchor = W)
            self.listBox.column('Kategori', minwidth=0, width=150, stretch=NO, anchor = W)
            self.listBox.column('Qty', minwidth=0, width=100, stretch=NO, anchor = CENTER)
            self.listBox.column('Harga', minwidth=0, width=150, stretch=NO, anchor = W)

        self.conn = mysql.connect(user="root", password="", database='db_Sahabat_Masyarakat', host="localhost", port='3306')
        self.c = self.conn.cursor()

        self.c.execute("""SELECT CONCAT(prefix,a.id_barang) as ID, a.nama, kategori, qty, harga
	                        from tb_inventory A
	                        inner join tb_detail_barang B on a.nama = b.nama and a.id_barang = b.id_barang
		                        where a.status_data = %s and b.status_data = %s""",
        ('Tidak Aktif','Tidak Aktif'))
        self.record = self.c.fetchall()
        self.conn.commit()
        # print(type(self.record))
        # print(self.record[0])
        
        for i, (id_barang,nama,kategori,qty,harga) in enumerate(self.record, start=1):
            self.listBox.insert("", "end", values=(id_barang,nama,kategori,qty,"Rp {:,},00-".format(harga)), tags=('ganjil',))
            self.conn.close()
        
        # print(self.txt_nama)

        self.listBox.bind('<ButtonRelease-1>',self.GetValue)

    
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
        self.harga = str(self.harga_temp.replace(",","")[3:][:-3])
        self.txt_harga.delete(0, END)
        self.txt_harga.insert(0, self.harga)

        # print(self.id_barang)
        # print(self.nama)
        # print(self.kategori)
        # print(self.qty)
        # print(self.harga)


if __name__ == "__main__":
    createDatabase()
    createTable()
    main = MainWindow()
    main.root.mainloop()
    
