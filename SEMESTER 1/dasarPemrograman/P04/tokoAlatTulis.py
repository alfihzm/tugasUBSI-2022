kodeBarang = input("Masukkan kode barang [B01/B02/B03] : ");

print("=========TOKO ALAT TULIS=========");
if kodeBarang == "B01" :
    nama_brg = "Buku";
    harga_brg = 500;
    stock_brg = "200";
elif kodeBarang == "B02" :
    nama_brg = "Pensil";
    harga_brg = 4000;
    stock_brg = "18";
elif kodeBarang == "B03" :
    nama_brg = "Pensil";
    harga_brg = 2000;
    stock_brg = 57;
else :
    nama_brg = "Barang tidak ditemukan";
    harga_brg = 0;
    stock_brg = 0;

# Output dari Input
print("Nama Barang          :", nama_brg);
print("Harga Barang         :", harga_brg);
print("Stock Barang         :", stock_brg);

jumlahBeli = int(input("Masukkan Jumlah Beli : "));
print("----------------------------------")
print("Jumlah Beli          :", jumlahBeli, "Buah");
totalBeli = harga_brg * jumlahBeli
print("Harga Pembelian      : Rp", totalBeli);

print("==================================");
if totalBeli > 20000 :
    print("Bonus : Penghapus");
else :
    print("Bonus : Tidak Ada");

print("==================================");