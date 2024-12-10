class TampilkanData:
    @staticmethod
    def tampilkan_daftar(daftar_mahasiswa):
        if not daftar_mahasiswa:
            print("Tidak ada data mahasiswa. ")
        else:
            for mahasiswa in daftar_mahasiswa:
                print(mahasiswa)

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print(mahasiswa)
        else:
            print("Mahasiswa tidak ditemukan. ")