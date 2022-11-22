from atmFunction import atmFungsi
from atmFunction import dataNasabah
from datetime import date
import os

def atmBahasaIndonesia() :
    minSetorTunai = 50000;
    maxTarikTunai = 1000000;
    pecahanSatu = [50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000, 550000, 600000, 650000, 700000, 750000, 800000, 850000, 900000, 950000, 1000000];
    pecahanDua = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000];

    def menuUtama():
        # Menu Utama User;
        print("[1] Setor Tunai");
        print("[2] Tarik Tunai");
        print("[3] Informasi Saldo");
        print("[4] Transfer");
        print("[5] Keluar");

    def setorTunai(atmFunction):
        try:
            os.system("cls"); # clear
            while True:
                setorTunai = int(input("Masukkan jumlah uang yang ingin disetor : Rp "));
                if setorTunai < minSetorTunai:
                    print("Minimal saldo setor Rp 50.000");
                    continue;
                else:
                    atmFunction.setSaldo(atmFunction.cekSaldo() + setorTunai);
                    infoSaldo = f"saldo anda sekarang : Rp {int(atmFunction.cekSaldo()):,}";
                    os.system("cls"); # clear
                    print("Setor tunai berhasil,", infoSaldo);
                    break;
        except:
            print("Jumlah salah, silahkan masukkan kembali jumlahnya.");

    # Receipt harus dibenerin

    def tarikTunai(atmFunction):
        while True:
            try:
                os.system("cls"); # clear
                while True:
                    tarikTunai = int(input("Masukkan jumlah uang yang ingin diambil : Rp "));
                    jumlah = f"{int(tarikTunai):,}"
                    if tarikTunai < minSetorTunai:
                        os.system("cls"); # clear
                        print("Minimal tarik tunai Rp 50.000");
                        continue;
                    elif tarikTunai > maxTarikTunai:
                        os.system("cls"); # clear
                        print("Maksimal tarik tunai Rp 1.000.000");
                        continue;
                    elif tarikTunai not in pecahanSatu and pecahanDua:
                        print("Hanya pecahan Rp 50.000 dan Rp 100.000.");
                    else:
                        if (atmFunction.cekSaldo() < tarikTunai):
                            print("Saldo anda tidak cukup.");
                        else:
                            os.system("cls"); # clear
                            atmFunction.setSaldo(atmFunction.cekSaldo() - tarikTunai);
                            while True:
                                try:
                                    inputPecahan = int(input("Pecahan Rp 50.000 [1] atau Rp 100.000 [2]? : "));
                                    if inputPecahan == 1:
                                        if tarikTunai >= 50001 and tarikTunai <= 99999:
                                            atmFunction.setSaldo(atmFunction.cekSaldo() + tarikTunai);
                                            print("Kesalahan.");
                                            return;
                                        elif tarikTunai not in pecahanSatu:
                                            atmFunction.setSaldo(atmFunction.cekSaldo() + tarikTunai);
                                            print("Kesalahan.");
                                            return;
                                        else:
                                            os.system("cls") # clear
                                            tarikBerhasil = "Tarik tunai berhasil, silahkan ambil uang anda.";
                                            print(tarikBerhasil);
                                            while True:
                                                tanggal = date.today();
                                                userReceipt = input("Apakah anda ingin mencetak resi? [Y] / [N] : ");
                                                if userReceipt == "Y" or userReceipt == "y" or userReceipt == "1":
                                                    os.system("cls"); # clear
                                                    print("============================");
                                                    print("BANK POP".center(27));
                                                    print("CABANG POHON".center(27));
                                                    print("============================");
                                                    print(tanggal);
                                                    print("============================");
                                                    print("Tarik Tunai");
                                                    print(f"NO. REK     : {atmFunction.cekNoRekening()}");
                                                    print(f"REKENING    : TABUNGAN");
                                                    print(f"JUMLAH      : Rp",jumlah);
                                                    print(f"SISA SALDO  : Rp {int(atmFunction.cekSaldo()):,}");
                                                    print("============================");
                                                    print("SIMPAN RESI INI SEBAGAI".center(27));
                                                    print("BUKTI YANG SAH".center(27));
                                                    print("============================");
                                                    print("Terimakasih telah menggunakan jasa Bank POP :)");
                                                    os._exit(0);
                                                elif userReceipt == "N" or userReceipt == "n" or userReceipt == "2":
                                                    os.system("cls"); # clear
                                                    print("Terimakasih telah menggunakan jasa Bank POP :)");
                                                    os._exit(0);
                                                else:
                                                    print("Input salah.");

                                    elif inputPecahan == 2:
                                        if tarikTunai == 50000:
                                            os.system("cls"); # clear
                                            print("Gimana ceritanya tarik tunai Rp 50.000 jadi pecahan Rp 100.000? :)")
                                            continue;
                                        elif tarikTunai >= 50001 and tarikTunai <= 99999:
                                            atmFunction.setSaldo(atmFunction.cekSaldo() + tarikTunai);
                                            print("Kesalahan.");
                                            return;
                                        elif tarikTunai not in pecahanDua:
                                            atmFunction.setSaldo(atmFunction.cekSaldo() + tarikTunai);
                                            print("Kesalahan.");
                                            return;
                                        else:
                                            atmFunction.setSaldo(atmFunction.cekSaldo() + tarikTunai);
                                            print("Saat ini tidak tersedia untuk Rp 100.000.");
                                        return;
                                    else:
                                        os.system("cls"); # clear
                                        print("Input salah.");
                                except:
                                    os.system("cls"); # clear
                                    print("Pecahan uang salah");
            except:
                print("Input salah.");

    def cekSaldo(atmFunction):
        os.system("cls"); # clear
        infoSaldo = f"Saldo anda sekarang : Rp {atmFunction.cekSaldo():,}";
        print(infoSaldo);

        akunNasabah = dataNasabah("","","");

        ## List Pengguna Bank POP
        listAkunNasabah = [];
        listAkunNasabah.append(dataNasabah("1379708899", "Muan", "Paharani"));
        listAkunNasabah.append(dataNasabah("1725964330", "Freddy", "Karbo"));
        listAkunNasabah.append(dataNasabah("1250248833", "Entis", "Sutrisna"));
        listAkunNasabah.append(dataNasabah("1853039966", "Joseph", "Mansoer"));
        listAkunNasabah.append(dataNasabah("1992842233", "Norman", "Komarudin"));

    def transfer(atmFunction):
        os.system("cls"); # clear
        while True:
            try:
                rekeningTujuan = input("Masukkan nomor rekening tujuan : ");
                cekNasabah = [holder for holder in listAkunPengguna if holder.noRekening == rekeningTujuan];
                if rekeningTujuan == inputNomorRekening:
                    os.system("cls") #clear
                    print("Tidak bisa transfer ke rekening sendiri.");
                    continue;
                elif (len(cekNasabah) > 0):
                    nominalTransfer = int(input("Masukkan jumlah nominal transfer : "));
                    jumlahTransfer = f"{int(nominalTransfer):,}"
                    tanggal = date.today();

                    if (atmFunction.cekSaldo() < nominalTransfer):
                        print("Saldo anda tidak cukup.")
                    else:
                        os.system("cls"); # clear
                        infoNominal = input(f"Anda akan mentransfer uang sejumlah Rp {(nominalTransfer):,} ke rekening ({rekeningTujuan}) Apakah benar? [Y] / [N] : ");
                        print(infoNominal);

                        while True:
                            try:
                                if infoNominal == "Y" or infoNominal == "y" or infoNominal == "1":    
                                    os.system("cls"); # clear
                                    atmFunction.setSaldo(atmFunction.cekSaldo() - nominalTransfer);
                                    while True:
                                        os.system("cls"); # clear
                                        print("Transfer berhasil.");
                                        while True:
                                            nextOption = input("Apakah anda ingin mencetak resi? [Y] / [N] : ");
                                            if nextOption == "Y" or nextOption == "y" or nextOption == "1":
                                                os.system("cls"); # clear
                                                print("============================");
                                                print("BANK POP".center(27));
                                                print("CABANG POHON".center(27));
                                                print("============================");
                                                print(tanggal);
                                                print("============================");
                                                print("Transfer");
                                                print(f"NO. REK     : {atmFunction.cekNoRekening()}");
                                                print(f"REKENING    : TABUNGAN");
                                                print(f"JUMLAH      : Rp", jumlahTransfer);
                                                print(f"KE REK.     :", rekeningTujuan);
                                                print("============================");
                                                print("SIMPAN RESI INI SEBAGAI".center(27));
                                                print("BUKTI YANG SAH".center(27));
                                                print("============================");
                                                print("Terimakasih telah menggunakan jasa Bank POP :)");
                                                os._exit(0);
                                            elif nextOption == "N" or nextOption == "n" or nextOption == "2":
                                                os.system("cls"); # clear
                                                print("Terimakasih telah menggunakan jasa Bank POP :)");
                                                os._exit(0);
                                            else:
                                                print("Input salah.");
                                else:
                                    os.system("cls"); # clear
                                    print("Transaksi gagal.");
                                    return;
                            except:
                                print("Transaksi gagal.");
                else:
                    os.system("cls") #clear
                    print("Nomor nasabah tidak dikenal.");
            except:
                print("Kesalahan.");

    if __name__ == "__main__" :
        akunUser = atmFungsi("","","","","");

        ## List Pengguna Bank POP
        listAkunPengguna = [];
        listAkunPengguna.append(atmFungsi("1379708899", 582492, "Muan", "Paharani", 5500000));
        listAkunPengguna.append(atmFungsi("1725964330", 512253, "Freddy", "Karbo", 1500000));
        listAkunPengguna.append(atmFungsi("1250248833", 185247, "Entis", "Sutrisna", 9650000));
        listAkunPengguna.append(atmFungsi("1853039966", 124578, "Joseph", "Mansoer", 4300000));
        listAkunPengguna.append(atmFungsi("1992842233", 525392, "Norman", "Komarudin", 8700000));

        # Input User
        ## Input Rekening Pengguna
        while True:
            try:
                inputNomorRekening = input("Masukkan nomor rekening anda : ");
                cekDebit = [holder for holder in listAkunPengguna if holder.noRekening == inputNomorRekening];
                if(len(cekDebit) > 0):
                    akunUser = cekDebit[0];
                    break;
                else:
                    print("Nomor akun tidak dikenal, silahkan input kembali nomor akun anda : ");
            except:
                print("Nomor akun tidak dikenal, silahkan input kembali nomor akun anda : ");

        ## Input PIN Pengguna
        count = 1;
        while count <= 3:
            try:
                userPin = int(input("Masukkan PIN anda            : ").strip());
                if akunUser.cekPin() == userPin:
                    os.system("cls"); # clear
                    break;
                else:
                    if akunUser.cekPin() != userPin:
                        if count == 1:
                            os.system("cls"); # clear
                            count += 1;
                            print("PIN salah, silahkan masukkan kembali PIN anda. Tersisa : 2 kali.");
                        else:
                            if akunUser.cekPin() == userPin:
                                os.system("cls"); # clear
                                break;
                            else:
                                if akunUser.cekPin() != userPin:
                                    if count == 2:
                                        os.system("cls"); # clear
                                        count += 1;
                                        print("PIN salah, silahkan masukkan kembali PIN anda. Tersisa : 1 kali.");
                                    else:
                                        if akunUser.cekPin() == userPin:
                                            os.system("cls"); # clear
                                            break;
                                        else:
                                            if akunUser.cekPin() != userPin:
                                                if count == 3:
                                                    os.system("cls"); # clear
                                                    print("Sesi berakhir. Silahkan coba beberapa sesaat lagi.");
                                                    os._exit(0);
                                                else:
                                                    os.system("cls"); # clear
                                                    break;
                    else:
                        break;
            except:
                print("PIN salah, silahkan masukkan kembali PIN anda.");

        ## Opsi printOut atmProgram
        print("Selamat Datang,", akunUser.cekNamaDepan(), akunUser.cekNamaBelakang());

    def userMenu():
        while True:
            menuUtama();
            try:
                opsi = int(input("Masukkan Pilihan Menu : "));
            except:
                print("Pilihan salah, masukkan ulang.");
            if (opsi == 1):
                setorTunai(akunUser);
            elif (opsi == 2):
                tarikTunai(akunUser);
            elif (opsi == 3):
                cekSaldo(akunUser);
            elif (opsi == 4):
                transfer(akunUser);
            elif (opsi == 5):
                os.system("cls"); # clear
                break;
            else:
                os.system("cls"); # clear
                print("Input yang anda masukkan salah");
        print("Terimakasih telah menggunakan jasa Bank POP :)");
        os._exit(0);
        
    userMenu();

def menuUtama():
    print("Selamat datang di menu utama POP");
    print("[1] Bahasa Indonesia.");
    print("[2] English.");
    while True:
        langMenu = int(input("Silahkan pilih bahasa. Please choose your language : "))

        if langMenu == 1 or langMenu == "1":
            os.system("cls") #clear
            atmBahasaIndonesia();
        else:
            print("Bahasa belum tersedia. Language is not available");
    
menuUtama();
