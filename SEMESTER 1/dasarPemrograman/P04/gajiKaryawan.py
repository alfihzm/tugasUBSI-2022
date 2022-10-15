separator = "==========================================================";
gaji = 300000
comp = "PT. DINGIN DAMAI".center(60)
prog = "PROGRAM HITUNG GAJI KARYAWAN".center(60)

# User Input
karyawan = str(input("Masukkan Nama Anda : "));
gol = input("Masukkan Golongan Anda [GOL1 / GOL2 / GOL3] : ");
pend = input("Masukkan Pendidikan Terakhir Anda [SMA / D1 / D3 / S1] : ");
jam = int(input("Masukkan Jumlah Jam Kerja : "));

# Rumus Honor Lembur
if jam > 96 :
   lembur = (jam - 96);
   honor = lembur * 3500;
elif jam > 48 :
   lembur = (jam - 48);
   honor = lembur * 3500;
elif jam > 8 :
    lembur = (jam - 8);
    honor = lembur * 3500;
else :
    honor = 0;

# Rumus Golongan
if gol == "GOL3" or gol == "gol3" or gol == "3" :
    golGaji = gaji * 15/100;
elif gol == "GOL2" or gol == "gol2" or gol == "2" :
    golGaji = gaji * 10/100;
elif gol == "GOL1" or gol == "gol1" or gol == "1" :
    golGaji = gaji * 5/100;
else :
    golGaji = 0;
 
# Rumus Pendidikan
if pend == "S1" or pend == "s1" or pend == "4" :
    pendGaji = gaji * 30/100;
elif pend == "D3" or pend == "d3"  or pend == "3" :
    pendGaji = gaji * 20/100;
elif pend == "D1" or pend == "d1"  or pend == "2" :
    pendGaji = gaji * 5/100;
elif pend == "SMA" or pend == "sma"  or pend == "1" :
    pendGaji = gaji * 2.5/100;
else :
    pendGaji = 0;

# Output dari Input
print(separator)
print(prog);
print(comp);
print(separator)
print("Karyawan Yang Bernama    :", karyawan);
print(separator)
print("HONOR YANG DITERIMA".center(60));
print(" ");
print("Gaji Pokok               :", "Rp", gaji);
print("Tunjangan Jabatan        :", "Rp", int(golGaji));
print("Tunjangan Pendidikan     :", "Rp", int(pendGaji));
print("Honor Lembur             :", "Rp", honor);
print("----------------------------------------------------------");
print("TOTAL GAJI YANG DITERIMA :", "Rp", gaji + int(golGaji + pendGaji) + honor);
print(separator)
print(" ");