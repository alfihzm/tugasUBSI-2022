# Latihan 2
name = input("Masukkan nama anda    : ");
toyCode = input("Masukkan Kode Mainan  : ");
price = int(input("Masukkan Harga Mainan : "));
amount = int(input("Masukkan Jumlah Beli  : "));
priceAmt = price * amount

price = f"Harga       : Rp {int(price):,}"
priceAmt = f"Total Harga : Rp {int(priceAmt):,}"

print("=" * 25);
print("Nama        :", name);
print("Kode Mainan :", toyCode);
print(price)
print("Jumlah Beli :", amount, "Buah");
print("=" * 25);
print(priceAmt);

if priceAmt > "50,000" :
    print("Bonus voucher!");
else :
    print("Tidak ada bonus");
print("=" * 25);