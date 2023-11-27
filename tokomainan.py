 # membuat kelas mainan
class Mainan:
    def __init__(self, nama, tipe):
        self.nama = nama
        self.tipe = tipe

# membuat kelas mainan yg disewa yang mengambil atribut dari kelas mainan
# di kelas ini atribut pembedanya harga_beli
class  mainanygdisewa(Mainan):
    def __init__(self, nama, tipe, harga_beli):
        super().__init__(nama, tipe)
        self.harga_beli = harga_beli


# membuat kelas mainanygdijusl yang mengambil atribut atribut dari kelas kamera
# di kelas ini atribut pembedanya harga_jual
class mainanygdijual(Mainan):
    def __init__(self, nama, tipe, harga_jual):
        super().__init__(nama, tipe)
        self.harga_jual = harga_jual

# membuat kelas pelanggan
# dimana pelanggan dapat membeli kamera dan juga menyewa
class Pelanggan:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        self.mainan_disewa = []
        self.mainan_dibeli = []
    
    # membuat fungsi sewa_kamera
    def sewa_mainan(self, mainan, tanggal_sewa, durasi_sewa):
        penyewaan = Penyewaan(self, mainan, tanggal_sewa, durasi_sewa)
        self.mainan_disewa.append(penyewaan)
        return penyewaan

    # membuat fungsi beli_mainan
    def beli_mainan(self, mainan, jumlah, tanggal_penjualan):
        penjualan = Penjualan(self, mainan, jumlah, tanggal_penjualan)
        self.mainan_dibeli.append(penjualan)
        return penjualan

# membuat kelas Penyewaan
class Penyewaan:
    def __init__(self, pelanggan, mainan, tanggal_sewa, durasi_sewa):
        self.pelanggan = pelanggan
        self.mainan = mainan
        self.tanggal_sewa = tanggal_sewa
        self.durasi_sewa = durasi_sewa

# membuat kelas Penjualan
class Penjualan:
    def __init__(self, pelanggan, mainan, jumlah, tanggal_penjualan):
        self.pelanggan = pelanggan
        self.mainan = mainan
        self.jumlah = jumlah
        self.tanggal_penjualan = tanggal_penjualan

# Contoh implementasi program di atas
mainan_jeep_disewa = mainanygdisewa("Mobil Aki Anak Model Jeep", "Mobil Aki Anak Model Bmw", 50000)
mainan_RC_dijual = mainanygdijual("RC Car Jeep", "RC Mobil VW Kodok", 250000)

pelanggan_1 = Pelanggan("Agil", "Jl. Raya Citraland No. 123")
pelanggan_2 = Pelanggan("Rafli", "Jl. Wonokromo SS No. 45")

penyewaan_1 = pelanggan_1.sewa_mainan(mainan_jeep_disewa, "31-10-2023", 2)
penyewaan_2 = pelanggan_2.sewa_mainan(mainan_RC_dijual, "31-10-2023", 3)

penjualan_1 = pelanggan_1.beli_mainan(mainan_jeep_disewa, 2, "31-10-2023")
penjualan_2 = pelanggan_2.beli_mainan(mainan_RC_dijual, 3, "31-10-2023") 

# Menampilkan informasi penyewaan
print("Informasi Penyewaan:")
for penyewaan in pelanggan_1.mainan_disewa:
    print(f"{pelanggan_1.nama} menyewa {penyewaan.mainan.nama} pada tanggal : {penyewaan.tanggal_sewa} selama {penyewaan.durasi_sewa} jam dengan total biaya penyewaan {penyewaan.durasi_sewa*mainan_jeep_disewa.harga_beli}")

for penyewaan in pelanggan_2.mainan_disewa:
    print(f"{pelanggan_2.nama} menyewa {penyewaan.mainan.nama} pada tanggal : {penyewaan.tanggal_sewa} selama {penyewaan.durasi_sewa} jam dengan total biaya penyewaan {penyewaan.durasi_sewa*mainan_RC_dijual.harga_jual}")

