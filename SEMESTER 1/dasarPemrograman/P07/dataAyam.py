import pandas as pd;

sep1 = "=";
sep2 = "-";

print(sep1 * 46);
print("ALFIE'S FRIED CHICKEN".center(47));
print(sep1 * 46);
print("KODE", "JENIS POTONG".center(32), "HARGA");
print(sep2 * 45);
print("D ", "Dada ".center(30), "    Rp 2500");
print("P ", "Paha ".center(30), "    Rp 2000");
print("S ", "Sayap".center(30), "    Rp 1500");
print(sep1 * 46);

#Input User
banyakJenis= int(input("Berapa Jenis yang akan anda beli : "))
kodeAyam   = [];
banyakAyam = [];
jenisAyam  = [];
harga      = [];
jumlah     = [];

i = 0;
while i < banyakJenis :
    print("Menu Ke -", i + 1);
    kodeAyam.append(input("Kode Potong [D/P/S]  : "));
    banyakAyam.append(int(input("Banyak Potong        : ")));

    if kodeAyam[i] == "D" or kodeAyam[i] == "d" :
        jenisAyam.append("Dada ");
        harga.append("Rp 2,500");
        jumlah.append(banyakAyam[i]*int("2500"));
    
    elif kodeAyam[i] == "P" or kodeAyam[i] == "p" :
         jenisAyam.append("Paha ");
         harga.append("Rp 2,000");
         jumlah.append(banyakAyam[i]*int("2000"));
    
    elif kodeAyam[i] == "S" or kodeAyam[i] == "s" :
         jenisAyam.append("Sayap");
         harga.append("Rp 1,500");
         jumlah.append(banyakAyam[i]*int("1500"));

    else :
         jenisAyam.append("Kode Salah");
         harga.append("0");
         jumlah.append(banyakAyam[i]*int("0"));

    i = i + 1;


dataAyam = {
    "Kode Potong" : kodeAyam,
    "Jenis Potong" : jenisAyam,
    "Harga Satuan" : harga,
    "Banyak Beli" : banyakAyam,
    "Jumlah Harga" : jumlah
}

menu = pd.DataFrame(dataAyam);

print("========================= Struk Pembelian ==========================");
print(menu);
print("====================================================================");