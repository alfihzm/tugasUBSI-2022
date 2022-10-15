separator = "=======================================";
gajiPokok = 4200000;
tunjangan = gajiPokok * 20/100;
jamKerja = int(input("Masukkan Jumlah Jam Kerja : "));

if jamKerja > 200 :
    jamLembur = jamKerja - 200;
    bonus = jamLembur * 20000;
else :
    bonus = 0;

totalGaji = gajiPokok + tunjangan + bonus;
pajak = totalGaji * 10/100;

print(" ");
print(separator);
print("Jam Kerja Anda  :", jamKerja, "jam");
print(separator);
print("Gaji Pokok      : Rp", gajiPokok);
print("Tunjangan       : Rp", int(tunjangan));
print("Uang Lembur     : Rp", bonus);
print("Pajak 10%       : Rp", int(pajak));
print("---------------------------------------")
print("Total Gaji      : Rp", int(totalGaji));
print(separator);
print(" ");