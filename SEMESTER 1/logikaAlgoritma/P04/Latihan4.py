gajiPokok = 5000000
barang = int(input("Masukkan Jumlah Barang : "));
harga = int(input("Masukkan Harga Barang / Satuan : "));

if barang > 100 :
    omset = harga * barang
    bonusJual = omset * 20/100
    bonusGaji = gajiPokok + bonusJual
else :
    omset = harga * barang
    bonusJual = omset * 10/100
    bonusGaji = gajiPokok + bonusJual

print(" ");
print("======================================");
print("Banyak Produk Terjual    :", barang, "barang");
print("Harga Satuan             : Rp", harga);
print("Bonus                    : Rp", int(bonusJual));
print("======================================");
print("Total Bonus + Gaji Pokok : Rp", int(bonusGaji))
print("======================================");
print(" ");