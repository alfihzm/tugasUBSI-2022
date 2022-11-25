import pandas as pd
#variable yang berulang menggunakan List/Matriks

listNIM = [];
listNama = [];
listUTS = [];
listUAS = [];
listTotal = [];

loop = int(input("Masukkan jumlah data : "));
for i in range(loop) :
    print("Data Ke -", i + 1);
    listNIM.append(input("Masukkan NIM : "));
    listNama.append(input("Nama : "));
    listUTS.append(int(input("Nilai UTS : ")));
    listUAS.append(int(input("Nilai UAS : ")));

#process
for i in range(loop) :
    listTotal.append((listUAS[i] + listUTS[i])/2);

guest = {
    "NIM" : listNIM,
    "Nama Lengkap" : listNama,
    "Nilai UTS" : listUTS,
    "Nilai UAS" : listUAS,
    "Rata-rata" : listTotal
}
guestData = pd.DataFrame(guest);

#print
print("================== DATA NILAI ==================");
print(guestData);
print("================================================");