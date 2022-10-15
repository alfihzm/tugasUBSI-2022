budget = int(input("Masukkan Budget Uang : "));
telur = 26000;
ongkos = 3500;
berat_telur = int(input("Masukkan Berat Telur yang Ingin dibeli : "));
angkot = int(input("Masukkan Berapa kali transport : "))
sisa_uang = budget - (telur * berat_telur) - (angkot * ongkos)

print("Sisa Uang Ibu Adalah : Rp", sisa_uang);