CREATE DATABASE IF NOT EXISTS db_Sahabat_Masyarakat

use db_sahabat_masyarakat

-- ============================================================ --
-- 							Buat Tabel							--
-- ============================================================ --

CREATE TABLE IF NOT EXISTS tb_Inventory (
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


CREATE TABLE IF NOT EXISTS tb_Detail_Barang (
        id_barang INT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
        nama VARCHAR(255) NOT NULL,
        kategori VARCHAR(255) NOT NULL,
        dibuat DATETIME NULL,
        diubah DATETIME NULL,
        status_data VARCHAR(255) NULL,
        PRIMARY KEY (id_barang),
        INDEX (nama, kategori)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1


CREATE TABLE IF NOT EXISTS tb_User (
        username VARCHAR(255) PRIMARY KEY,
        password VARCHAR(255) NOT NULL,
        dibuat DATETIME NULL,
        diubah DATETIME NULL,
        status_data VARCHAR(255) NULL
         )


CREATE TABLE IF NOT EXISTS tb_Riwayat_Pembelian (
        id_struk INT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
        nama VARCHAR(255) NOT NULL,
        qty INT(4) NOT NULL,
        total INT(9) NOT NULL,
        dibuat DATETIME NULL,
        diubah DATETIME NULL,
        status_data VARCHAR(255) NULL,
        PRIMARY KEY (id_struk)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1


CREATE TABLE IF NOT EXISTS tb_Tabungan (
        id_tabungan INT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
        pemasukkan INT(9) NOT NULL,
        saldo_toko INT(12) NOT NULL,
        dibuat DATETIME NULL,
        diubah DATETIME NULL,
        status_data VARCHAR(255) NULL,
        PRIMARY KEY(id_tabungan),
        INDEX (pemasukkan, saldo_toko)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1


CREATE TABLE IF NOT EXISTS tb_Log_Data (
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


-- ============================================================ --
-- 							Input Data							--
-- ============================================================ --

insert into tb_detail_barang (nama,kategori,dibuat,status_data)
	values
		('Pulpen', 'Alat Tulis Kantor', now(), 'Aktif'),
		('Pensil', 'Alat Tulis Kantor', now(), 'Aktif'),
		('Penggaris', 'Alat Tulis Kantor', now(), 'Aktif'),
		('Penghapus', 'Alat Tulis Kantor', now(), 'Aktif'),
		('Rautan', 'Alat Tulis Kantor', now(), 'Aktif'),
		('Tip-X', 'Alat Tulis Kantor', now(), 'Aktif'),
		('Correction Tape', 'Alat Tulis Kantor', now(), 'Aktif'),
		('Lem Kertas', 'Alat Tulis Kantor', now(), 'Aktif')


insert into tb_inventory (nama,qty,harga,dibuat,status_data)
	values
		('Pulpen', 40, 2500, now(), 'Aktif'),
		('Pensil', 40, 2500, now(), 'Aktif'),
		('Penggaris', 30, 4000, now(), 'Aktif'),
		('Penghapus', 35, 2000, now(), 'Aktif'),
		('Rautan', 15, 3500, now(), 'Aktif'),
		('Tip-X', 20, 7000, now(), 'Aktif'),
		('Correction Tape', 20, 14000, now(), 'Aktif'),
		('Lem Kertas', 20, 4000, now(), 'Aktif')


-- ============================================================ --
-- 							Lihat Tabel							--
-- ============================================================ --

select * from tb_inventory

select * from tb_detail_barang

select * from tb_user

select * from tb_riwayat_pembelian

select * from tb_tabungan

select * from tb_log_data


-- ============================================================ --
-- 						 Mengosongkan Tabel 					--
-- ============================================================ --

truncate table tb_inventory

truncate table tb_detail_barang

truncate table tb_user

truncate table tb_riwayat_pembelian

truncate table tb_tabungan

truncate table tb_log_data


-- ============================================================ --
-- 					Menghapus Database/Tabel					--
-- ============================================================ --

drop database db_sahabat_masyarakat

drop table tb_inventory

drop table tb_detail_barang

drop table tb_user

drop table tb_riwayat_pembelian

drop table tb_tabungan

drop table tb_log_data


-- ============================================================ --
-- 					  View Tabel Dalam Program					--
-- ============================================================ --

-- Tabel pada manajemen inventory
select concat(prefix,a.id_barang) as Id, a.nama, kategori, qty, harga
	from tb_inventory A
	inner join tb_detail_barang B on a.nama = b.nama and a.id_barang = b.id_barang
		where a.status_data = 'Aktif' and b.status_data = 'Aktif'

-- Tabel pada kasir
SELECT a.nama, kategori, harga
    from tb_inventory A
	inner join tb_detail_barang B on a.nama = b.nama and a.id_barang = b.id_barang
        where a.status_data = 'Aktif' and b.status_data = 'Aktif'

-- Tabel pada recycle bin
select concat(prefix,a.id_barang) as Id, a.nama, kategori, qty, harga
	from tb_inventory A
	inner join tb_detail_barang B on a.nama = b.nama and a.id_barang = b.id_barang
		where a.status_data = 'Aktif' and b.status_data = 'Aktif'
		
