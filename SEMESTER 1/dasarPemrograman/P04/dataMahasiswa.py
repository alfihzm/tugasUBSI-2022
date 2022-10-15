nama = input("Masukkan Nama Anda : ");
nis = input("Masukkan NIS Anda : ");
prodi = input("Masukkan Prodi Anda [SI/SIA] : ");

print("=======================================");

print("Nama Mahasiswa :", nama);
print("NIS            :", nis);
print("Program Studi  :", prodi);

if prodi == "SIA" or prodi == "sia" :
    print("=============================================================");
    print("Kode Jurusan".ljust(20), "Nama Prodi".center(10), "Harga".rjust(25));
    print("=============================================================");
    print("SIA".ljust(20), "Sistem Informasi Akuntansi".center(10), "2.000.000".rjust(13));
    print("=============================================================");

elif prodi == "SI" or prodi == "si" :
    print("=============================================================");
    print("Kode Jurusan".ljust(20), "Nama Prodi".center(10), "Harga".rjust(15));
    print("=============================================================");
    print("SI".ljust(20), "Sistem Informasi".center(10), "2.400.000".rjust(13));
    print("=============================================================");

else : 
    print("=============================================================");
    print("Kode Jurusan".ljust(20), "Nama Prodi".center(10), "Harga".rjust(15));
    print("=============================================================");
    print(prodi.ljust(20), "-".center(1), "-".rjust(20));
    print("=============================================================");