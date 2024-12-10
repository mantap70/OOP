class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def __str__(self):
        return f"NIM: {self.nim}, Nama: {self.nama}, Jurusan: {self.jurusan}"
    

class DataMahasiswa:
    def __init__(self):
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)
        print(f"Mahasiswa {mahasiswa.nama} berhasil ditambahkan. ")
    
    def hapus_mahasiswa(self, nim):
        for mahasiswa in self.daftar_mahasiswa:
            if mahasiswa.nim == nim:
                self.daftar_mahasiswa.remove(mahasiswa)
                print(f"Mahasiswa dengan NIM {nim} berhasil dihapus. ")
                return
        print(f"Mahasiswa dengan NIM {nim} tidak ditemukan")

    def cari_mahasiswa(self, nim):
        for mahasiswa in self.daftar_mahasiswa:
            if mahasiswa.nim == nim:
                return mahasiswa
        return None