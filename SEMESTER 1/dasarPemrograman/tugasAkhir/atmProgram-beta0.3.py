from atmFunction import atmFungsi
import os

userOption = ["Y", "N"];
minSetorTunai = 50000;
minTarikTunai = 50000;
maxTarikTunai = 10000000;
pecahanUang = [50000, 100000]

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
            setorTunai = int(input("Masukkan jumlah uang yang ingin disetor : "));
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

def tarikTunai(atmFunction):
    try:
        os.system("cls"); # clear
        while True:
            tarikTunai = int(input("Masukkan jumlah uang yang ingin diambil : Rp "));
            if tarikTunai < minSetorTunai:
                os.system("cls"); # clear
                print("Minimal tarik tunai Rp 50.000");
                continue;
            elif tarikTunai > maxTarikTunai:
                os.system("cls"); # clear
                print("Maksimal tarik tunai Rp 10.000.000");
                continue;
            else:
                if (atmFunction.cekSaldo() < tarikTunai):
                    print("Saldo anda tidak cukup.");
                else:
                    os.system("cls"); # clear
                    atmFunction.setSaldo(atmFunction.cekSaldo() - tarikTunai);
                    while True:
                        inputPecahan = int(input("Pecahan Rp 50.000 [1] atau Rp 100.000 [2]? : "));
                        if inputPecahan == 1:
                            print("Tarik tunai berhasil, silahkan ambil uang anda.")
                            return;
                        elif inputPecahan == 2:
                            if tarikTunai == 50000:
                                os.system("cls"); # clear
                                print("Gimana ceritanya tarik tunai Rp 50.000 jadi pecahan Rp 100.000? :)")
                                continue;
                            else:
                                atmFunction.setSaldo(atmFunction.cekSaldo() + tarikTunai);
                                print("Saat ini tidak tersedia untuk Rp 100.000.")
                            return;
                        else:
                            print("Pecahan uang salah");
    except:
        print("Jumlah salah, silahkan masukkan kembali jumlahnya.");

def cekSaldo(atmFunction):
    os.system("cls"); # clear
    infoSaldo = f"Saldo anda sekarang : Rp {atmFunction.cekSaldo():,}";
    print(infoSaldo);

def transfer(atmFunction):
    os.system("cls"); # clear
    rekeningTujuan = int(input("Masukkan nomor rekening tujuan : "));
    if (atmFunction.cekNoRekening() == rekeningTujuan):
        print("Rekening tidak ditemukan.");
    else:
        nominalTransfer = int(input("Masukkan jumlah nominal transfer : "));

        if (atmFunction.cekSaldo() < nominalTransfer):
            print("Saldo anda tidak cukup.")
        else:
            os.system("cls"); # clear
            infoNominal = input(f"Anda akan mentransfer uang sejumlah Rp {(nominalTransfer):,} ke rekening {rekeningTujuan} Apakah benar? [Y] / [N] : ");
            print(infoNominal);

            while True:
                try:
                    if infoNominal == userOption[0]:    
                        os.system("cls"); # clear
                        atmFunction.setSaldo(atmFunction.cekSaldo() - nominalTransfer);
                        transactionSuccess = input("Transfer berhasil. \nIngin melanjutkan transaksi? [Y] / [N] : ");
                        print(transactionSuccess);

                        while True:
                            if transactionSuccess == userOption[0]:
                                os.system("cls"); # clear
                                return;
                            elif transactionSuccess == userOption[1]:
                                os.system("cls"); # clear
                                print("Terimakasih telah menggunakan jasa Bank POP :)");
                                os._exit(0);
                    else:
                        print("Transaksi gagal.");
                except:
                    print("Transaksi gagal.");
                break;
            
if __name__ == "__main__" :
    akunUser = atmFungsi("","","","","");

    ## List Pengguna Bank POP
    listAkunPengguna = [];
    listAkunPengguna.append(atmFungsi("1056295728275628", 582492, "Muan", "Paharani", 5500000));
    listAkunPengguna.append(atmFungsi("1056493759284669", 185247, "Entis", "Sutrisna", 9650000));
    listAkunPengguna.append(atmFungsi("1056385275058334", 124578, "Joshua", "Hasanuddin", 4300000));
    listAkunPengguna.append(atmFungsi("1056219483055822", 512253, "Freddy", "Karbo", 1500000));
    listAkunPengguna.append(atmFungsi("1056492482852238", 525392, "Norman", "Komarudin", 8700000));

    # Input User
    ## Input Rekening Pengguna
    while True:
        try:
            inputNomorRekening = input("Masukkan Nomor Rekening Anda : ");
            cekDebit = [holders for holders in listAkunPengguna if holders.noRekening == inputNomorRekening];
            if(len(cekDebit) > 0):
                akunUser = cekDebit[0];
                break;
            else:
                print("Nomor akun tidak dikenal, silahkan input kembali nomor akun anda : ");
        except:
            print("Nomor akun tidak dikenal, silahkan input kembali nomor akun anda : ");

    ## Input PIN Pengguna
    while True:
        try:
            userPin = int(input("Masukkan PIN anda            : ").strip());
            if akunUser.cekPin() == userPin:
                break;
            else:
                print("PIN salah, silahkan masukkan kembali PIN anda.");
        except:
            print("PIN salah, silahkan masukkan kembali PIN anda.");

    ## Opsi printOut atmProgram
    os.system("cls"); # clear
    print("Selamat Datang,", akunUser.cekNamaDepan(), akunUser.cekNamaBelakang());
    opsi = 0;

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
            opsi == 0;
    print("Terimakasih telah menggunakan jasa Bank POP :)");

userMenu();