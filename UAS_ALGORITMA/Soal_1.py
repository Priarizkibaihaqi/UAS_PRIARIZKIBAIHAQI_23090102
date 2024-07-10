def input_mahasiswa():
    data_mahasiswa = []
    while True:
        nim = input("Masukan NIM: ")
        nama = input("Masukan Nama: ")
        data_mahasiswa.append({'NIM': nim, 'Nama': nama})
        
        tambah_lagi = input("Ingin tambah lagi (yaa/tidak)? ").lower()
        if tambah_lagi != 'yaa':
            break

    print("nData Mahasiswa:")
    for mahasiswa in data_mahasiswa: 
        print(f"NIM: {mahasiswa['NIM']}, Nama: {mahasiswa['Nama']}")


#Memanggil fungsi untuk Menjalankan program 
input_mahasiswa()