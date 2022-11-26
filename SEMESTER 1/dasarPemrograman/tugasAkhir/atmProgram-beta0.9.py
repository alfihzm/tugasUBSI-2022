from atmFunction import atmFungsi
from datetime import date
from colorama import Fore
import time
import os
import random

def atmBahasaIndonesia() :
    minSetorTunai = 50000;
    maxTarikTunai = 1000000;
    pecahanSatu = [50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000, 550000, 600000, 650000, 700000, 750000, 800000, 850000, 900000, 950000, 1000000];
    pecahanDua = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000];
    tokenListrik = ["9824 1245 4924 2952", "1247 3822 5835 9242", "2194 4592 2945 9445", "3482 2493 2918 9634", "5382 4020 3850 1835", "4382 5860 5920 1940", "7323 6942 1294 5393"];

    def randomToken():
        randomToken = random.randrange(len(tokenListrik));
        randomNum = tokenListrik[randomToken]
        print("Kode token anda adalah : " + str(randomNum));

    def menuUtama():
        # Menu Utama User;
        print(Fore.RED + "==========================");
        print("|        POP BANK        |");
        print("==========================");
        print("| [1] SETOR TUNAI        |");
        print("| [2] TARIK TUNAI        |");
        print("| [3] INFORMASI SALDO    |");
        print(Fore.LIGHTWHITE_EX + "| [4] TRANSFER           |");
        print("| [5] PEMBAYARAN TAGIHAN |");
        print("|                        |");
        print("| [0] KELUAR             |");
        print("==========================");

    def setorTunai(atmFunction):
        print(Fore.LIGHTGREEN_EX);
        os.system("cls"); # clear
        print("======================================");
        print("|             SETOR TUNAI            |");
        print("======================================");
        print("| [1] Rp 50.000     [4] Rp 500.000   |");
        print("| [2] Rp 100.000    [5] Rp 800.000   |");
        print("| [3] Rp 250.000    [6] Rp 1.000.000 |");
        print("|                                    |");
        print("| [9] Input jumlah nominal lain.     |");
        print("| [0] KEMBALI                        |");
        print("======================================");
        while True:
            try:
                setorTunai = int(input("Masukkan nominal di atas : "));
                while True:
                    try:
                        if setorTunai == 1:
                            atmFunction.setSaldo(atmFunction.cekSaldo() + 50000);
                            infoSaldo = f"saldo anda sekarang : Rp {int(atmFunction.cekSaldo()):,}";
                            os.system("cls"); # clear
                            print("Setor tunai berhasil,", infoSaldo);
                            return;
                        elif setorTunai == 2:
                            atmFunction.setSaldo(atmFunction.cekSaldo() + 100000);
                            infoSaldo = f"saldo anda sekarang : Rp {int(atmFunction.cekSaldo()):,}";
                            os.system("cls"); # clear
                            print("Setor tunai berhasil,", infoSaldo);
                            return;
                        elif setorTunai == 3:
                            atmFunction.setSaldo(atmFunction.cekSaldo() + 250000);
                            infoSaldo = f"saldo anda sekarang : Rp {int(atmFunction.cekSaldo()):,}";
                            os.system("cls"); # clear
                            print("Setor tunai berhasil,", infoSaldo);
                            return;
                        elif setorTunai == 4:
                            atmFunction.setSaldo(atmFunction.cekSaldo() + 500000);
                            infoSaldo = f"saldo anda sekarang : Rp {int(atmFunction.cekSaldo()):,}";
                            os.system("cls"); # clear
                            print("Setor tunai berhasil,", infoSaldo);
                            return;
                        elif setorTunai == 5:
                            atmFunction.setSaldo(atmFunction.cekSaldo() + 800000);
                            infoSaldo = f"saldo anda sekarang : Rp {int(atmFunction.cekSaldo()):,}";
                            os.system("cls"); # clear
                            print("Setor tunai berhasil,", infoSaldo);
                            return;
                        elif setorTunai == 6:
                            atmFunction.setSaldo(atmFunction.cekSaldo() + 1000000);
                            infoSaldo = f"saldo anda sekarang : Rp {int(atmFunction.cekSaldo()):,}";
                            os.system("cls"); # clear
                            print("Setor tunai berhasil,", infoSaldo);
                            return;
                        elif setorTunai == 9:
                            while True:
                                customSetor = int(input("Masukkan jumlah nominal yang ingin disetor : Rp "));
                                if customSetor == customSetor:
                                    if customSetor < minSetorTunai:
                                        os.system("cls"); #clear
                                        print("Minimal saldo setor Rp 50.000");
                                        continue;
                                    else:
                                        os.system("cls"); # clear
                                        atmFunction.setSaldo(atmFunction.cekSaldo() + customSetor);
                                        infoSaldo = f"saldo anda sekarang : Rp {int(atmFunction.cekSaldo()):,}";
                                        print("Setor tunai berhasil,", infoSaldo);
                                        return;
                                else:
                                    print("Nominal yang anda masukkan salah.");
                        elif setorTunai == 0:
                            os.system("cls"); #clear
                            return;
                        else:
                            os.system("cls"); #clear
                            print("Input yang anda masukkan salah.");
                            return;
                    except:
                        print("input salah, silahkan masukkan kembali.");
            except:
                print("Input yang anda masukkan salah. Silahkan coba lagi.");
    # Receipt harus dibenerin

    def tarikTunai(atmFunction):
        print(Fore.LIGHTYELLOW_EX);
        os.system("cls") #clear
        waktu = time.strftime("%H:%M");
        tanggal = date.today();
        print("======================================");
        print("|             TARIK TUNAI            |");
        print("======================================");
        print("| [1] Rp 50.000     [4] Rp 500.000   |");
        print("| [2] Rp 100.000    [5] Rp 800.000   |");
        print("| [3] Rp 250.000    [6] Rp 1.000.000 |");
        print("|                                    |");
        print("| [9] Input jumlah nominal lain.     |");
        print("| [0] KEMBALI                        |");
        print("======================================");
        while True:
            try:
                nominalWithdraw = int(input("Masukkan nominal di atas : "));
                if nominalWithdraw == 1:
                    while True:
                        inputPecahan = int(input("Pecahan Rp 50.000 [1] atau Rp 100.000 [2]? : "));
                        if inputPecahan == 1:
                            jumlah = f"{int(50000):,}"
                            if (atmFunction.cekSaldo() < 50000):
                                os.system("cls") #clear
                                print("Saldo anda tidak cukup.");
                                return;
                            else:
                                os.system("cls") #clear
                                print("Transaksi berhasil.");
                                atmFunction.setSaldo(atmFunction.cekSaldo() - 50000);
                                while True:
                                    userReceipt = input("Apakah anda ingin mencetak resi? [Y] / [N] : ");
                                    if userReceipt == "Y" or userReceipt == "y" or userReceipt == "1":
                                        os.system("cls"); # clear
                                        print("===============================");
                                        print("|           BANK POP          |");
                                        print("|         CABANG POHON        |");
                                        print("===============================");
                                        print(f"| {tanggal}            {waktu} |");
                                        print("===============================");
                                        print("| Tarik Tunai                 |");
                                        print(f"| NO. REK     : {atmFunction.cekNoRekening()}    |");
                                        print(f"| REKENING    : TABUNGAN      |");
                                        print(f"| JUMLAH      : Rp {jumlah}     |");
                                        print(f"| SISA SALDO  : Rp {int(atmFunction.cekSaldo()):,}  |");
                                        print("===============================");
                                        print("|   SIMPAN RESI INI SEBAGAI   |");
                                        print("|       BUKTI YANG SAH        |");
                                        print("===============================");
                                        print(Fore.LIGHTBLUE_EX);
                                        print("Terimakasih telah menggunakan jasa Bank POP :)");
                                        os._exit(0);
                                    elif userReceipt == "N" or userReceipt == "n" or userReceipt == "2":
                                        os.system("cls"); # clear
                                        print(Fore.LIGHTBLUE_EX);
                                        print("Terimakasih telah menggunakan jasa Bank POP :)");
                                        os._exit(0);
                                    else:
                                        print("Input salah.");
                        elif inputPecahan == 2:
                            print("Gimana ceritanya tarik tunai Rp 50.000 jadi pecahan Rp 100.000? :)")
                            continue;
                        else:
                            print("Input pecahan salah");
                
                elif nominalWithdraw == 2:
                    while True:
                        inputPecahan = int(input("Pecahan Rp 50.000 [1] atau Rp 100.000 [2]? : "));
                        if inputPecahan == 1:
                            jumlah = f"{int(100000):,}"
                            if (atmFunction.cekSaldo() < 100000):
                                os.system("cls") #clear
                                print("Saldo anda tidak cukup.");
                                return;
                            else:
                                os.system("cls") #clear
                                print("Transaksi berhasil.");
                                atmFunction.setSaldo(atmFunction.cekSaldo() - 100000);
                                while True:
                                    userReceipt = input("Apakah anda ingin mencetak resi? [Y] / [N] : ");
                                    if userReceipt == "Y" or userReceipt == "y" or userReceipt == "1":
                                        os.system("cls"); # clear
                                        print("===============================");
                                        print("|           BANK POP          |");
                                        print("|         CABANG POHON        |");
                                        print("===============================");
                                        print(f"| {tanggal}            {waktu} |");
                                        print("===============================");
                                        print("| Tarik Tunai                 |");
                                        print(f"| NO. REK     : {atmFunction.cekNoRekening()}    |");
                                        print(f"| REKENING    : TABUNGAN      |");
                                        print(f"| JUMLAH      : Rp {jumlah}    |");
                                        print(f"| SISA SALDO  : Rp {int(atmFunction.cekSaldo()):,}  |");
                                        print("===============================");
                                        print("|   SIMPAN RESI INI SEBAGAI   |");
                                        print("|       BUKTI YANG SAH        |");
                                        print("===============================");
                                        print(Fore.LIGHTBLUE_EX);
                                        print("Terimakasih telah menggunakan jasa Bank POP :)");
                                        os._exit(0);
                                    elif userReceipt == "N" or userReceipt == "n" or userReceipt == "2":
                                        os.system("cls"); # clear
                                        print(Fore.LIGHTBLUE_EX);
                                        print("Terimakasih telah menggunakan jasa Bank POP :)");
                                        os._exit(0);
                                    else:
                                        print("Input salah.");
                        elif inputPecahan == 2:
                            os.system("cls"); #clear
                            print("Saat ini tidak tersedia untuk pecahan Rp 100.000")
                            return
                        else:
                            print("Input pecahan salah");
                
                elif nominalWithdraw == 3:
                    while True:
                        inputPecahan = int(input("Pecahan Rp 50.000 [1] atau Rp 100.000 [2]? : "));
                        if inputPecahan == 1:
                            jumlah = f"{int(250000):,}"
                            if (atmFunction.cekSaldo() < 250000):
                                os.system("cls") #clear
                                print("Saldo anda tidak cukup.");
                                return;
                            else:
                                os.system("cls") #clear
                                print("Transaksi berhasil.");
                                atmFunction.setSaldo(atmFunction.cekSaldo() - 250000);
                                while True:
                                    userReceipt = input("Apakah anda ingin mencetak resi? [Y] / [N] : ");
                                    if userReceipt == "Y" or userReceipt == "y" or userReceipt == "1":
                                        os.system("cls"); # clear
                                        print("===============================");
                                        print("|           BANK POP          |");
                                        print("|         CABANG POHON        |");
                                        print("===============================");
                                        print(f"| {tanggal}            {waktu} |");
                                        print("===============================");
                                        print("| Tarik Tunai                 |");
                                        print(f"| NO. REK     : {atmFunction.cekNoRekening()}    |");
                                        print(f"| REKENING    : TABUNGAN      |");
                                        print(f"| JUMLAH      : Rp {jumlah}    |");
                                        print(f"| SISA SALDO  : Rp {int(atmFunction.cekSaldo()):,}  |");
                                        print("===============================");
                                        print("|   SIMPAN RESI INI SEBAGAI   |");
                                        print("|       BUKTI YANG SAH        |");
                                        print("===============================");
                                        print(Fore.LIGHTBLUE_EX);
                                        print("Terimakasih telah menggunakan jasa Bank POP :)");
                                        os._exit(0);
                                    elif userReceipt == "N" or userReceipt == "n" or userReceipt == "2":
                                        os.system("cls"); # clear
                                        print(Fore.LIGHTBLUE_EX);
                                        print("Terimakasih telah menggunakan jasa Bank POP :)");
                                        os._exit(0);
                                    else:
                                        print("Input salah.");
                        elif inputPecahan == 2:
                            os.system("cls"); #clear
                            print("Saat ini tidak tersedia untuk pecahan Rp 100.000")
                            return
                        else:
                            print("Input pecahan salah");

                elif nominalWithdraw == 4:
                    while True:
                        inputPecahan = int(input("Pecahan Rp 50.000 [1] atau Rp 100.000 [2]? : "));
                        if inputPecahan == 1:
                            jumlah = f"{int(500000):,}"
                            if (atmFunction.cekSaldo() < 500000):
                                os.system("cls") #clear
                                print("Saldo anda tidak cukup.");
                                return;
                            else:
                                os.system("cls") #clear
                                print("Transaksi berhasil.");
                                atmFunction.setSaldo(atmFunction.cekSaldo() - 500000);
                                while True:
                                    userReceipt = input("Apakah anda ingin mencetak resi? [Y] / [N] : ");
                                    if userReceipt == "Y" or userReceipt == "y" or userReceipt == "1":
                                        os.system("cls"); # clear
                                        print("===============================");
                                        print("|           BANK POP          |");
                                        print("|         CABANG POHON        |");
                                        print("===============================");
                                        print(f"| {tanggal}            {waktu} |");
                                        print("===============================");
                                        print("| Tarik Tunai                 |");
                                        print(f"| NO. REK     : {atmFunction.cekNoRekening()}    |");
                                        print(f"| REKENING    : TABUNGAN      |");
                                        print(f"| JUMLAH      : Rp {jumlah}    |");
                                        print(f"| SISA SALDO  : Rp {int(atmFunction.cekSaldo()):,}  |");
                                        print("===============================");
                                        print("|   SIMPAN RESI INI SEBAGAI   |");
                                        print("|       BUKTI YANG SAH        |");
                                        print("===============================");
                                        print(Fore.LIGHTBLUE_EX);
                                        print("Terimakasih telah menggunakan jasa Bank POP :)");
                                        os._exit(0);
                                    elif userReceipt == "N" or userReceipt == "n" or userReceipt == "2":
                                        os.system("cls"); # clear
                                        print(Fore.LIGHTBLUE_EX);
                                        print("Terimakasih telah menggunakan jasa Bank POP :)");
                                        os._exit(0);
                                    else:
                                        print("Input salah.");
                        elif inputPecahan == 2:
                            os.system("cls"); #clear
                            print("Saat ini tidak tersedia untuk pecahan Rp 100.000")
                            return
                        else:
                            print("Input pecahan salah");
                
                elif nominalWithdraw == 5:
                    while True:
                        inputPecahan = int(input("Pecahan Rp 50.000 [1] atau Rp 100.000 [2]? : "));
                        if inputPecahan == 1:
                            jumlah = f"{int(800000):,}"
                            if (atmFunction.cekSaldo() < 800000):
                                os.system("cls") #clear
                                print("Saldo anda tidak cukup.");
                                return;
                            else:
                                os.system("cls") #clear
                                print("Transaksi berhasil.");
                                atmFunction.setSaldo(atmFunction.cekSaldo() - 800000);
                                while True:
                                    userReceipt = input("Apakah anda ingin mencetak resi? [Y] / [N] : ");
                                    if userReceipt == "Y" or userReceipt == "y" or userReceipt == "1":
                                        os.system("cls"); # clear
                                        print("===============================");
                                        print("|           BANK POP          |");
                                        print("|         CABANG POHON        |");
                                        print("===============================");
                                        print(f"| {tanggal}            {waktu} |");
                                        print("===============================");
                                        print("| Tarik Tunai                 |");
                                        print(f"| NO. REK     : {atmFunction.cekNoRekening()}    |");
                                        print(f"| REKENING    : TABUNGAN      |");
                                        print(f"| JUMLAH      : Rp {jumlah}    |");
                                        print(f"| SISA SALDO  : Rp {int(atmFunction.cekSaldo()):,}  |");
                                        print("===============================");
                                        print("|   SIMPAN RESI INI SEBAGAI   |");
                                        print("|       BUKTI YANG SAH        |");
                                        print("===============================");
                                        print(Fore.LIGHTBLUE_EX);
                                        print("Terimakasih telah menggunakan jasa Bank POP :)");
                                        os._exit(0);
                                    elif userReceipt == "N" or userReceipt == "n" or userReceipt == "2":
                                        os.system("cls"); # clear
                                        print(Fore.LIGHTBLUE_EX);
                                        print("Terimakasih telah menggunakan jasa Bank POP :)");
                                        os._exit(0);
                                    else:
                                        print("Input salah.");
                        elif inputPecahan == 2:
                            os.system("cls"); #clear
                            print("Saat ini tidak tersedia untuk pecahan Rp 100.000")
                            return
                        else:
                            print("Input pecahan salah");

                elif nominalWithdraw == 6:
                    while True:
                        inputPecahan = int(input("Pecahan Rp 50.000 [1] atau Rp 100.000 [2]? : "));
                        if inputPecahan == 1:
                            jumlah = f"{int(1000000):,}"
                            if (atmFunction.cekSaldo() < 1000000):
                                os.system("cls") #clear
                                print("Saldo anda tidak cukup.");
                                return;
                            else:
                                os.system("cls") #clear
                                print("Transaksi berhasil.");
                                atmFunction.setSaldo(atmFunction.cekSaldo() - 1000000);
                                while True:
                                    userReceipt = input("Apakah anda ingin mencetak resi? [Y] / [N] : ");
                                    if userReceipt == "Y" or userReceipt == "y" or userReceipt == "1":
                                        os.system("cls"); # clear
                                        print("===============================");
                                        print("|           BANK POP          |");
                                        print("|         CABANG POHON        |");
                                        print("===============================");
                                        print(f"| {tanggal}            {waktu} |");
                                        print("===============================");
                                        print("| Tarik Tunai                 |");
                                        print(f"| NO. REK     : {atmFunction.cekNoRekening()}    |");
                                        print(f"| REKENING    : TABUNGAN      |");
                                        print(f"| JUMLAH      : Rp {jumlah}  |");
                                        print(f"| SISA SALDO  : Rp {int(atmFunction.cekSaldo()):,}  |");
                                        print("===============================");
                                        print("|   SIMPAN RESI INI SEBAGAI   |");
                                        print("|       BUKTI YANG SAH        |");
                                        print("===============================");
                                        print(Fore.LIGHTBLUE_EX);
                                        print("Terimakasih telah menggunakan jasa Bank POP :)");
                                        os._exit(0);
                                    elif userReceipt == "N" or userReceipt == "n" or userReceipt == "2":
                                        os.system("cls"); # clear
                                        print(Fore.LIGHTBLUE_EX);
                                        print("Terimakasih telah menggunakan jasa Bank POP :)");
                                        os._exit(0);
                                    else:
                                        print("Input salah.");
                        elif inputPecahan == 2:
                            os.system("cls"); #clear
                            print("Saat ini tidak tersedia untuk pecahan Rp 100.000")
                            return
                        else:
                            print("Input pecahan salah");

                elif nominalWithdraw == 9:
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
                                                            userReceipt = input("Apakah anda ingin mencetak resi? [Y] / [N] : ");
                                                            if userReceipt == "Y" or userReceipt == "y" or userReceipt == "1":
                                                                os.system("cls"); # clear
                                                                print("===============================");
                                                                print("|           BANK POP          |");
                                                                print("|         CABANG POHON        |");
                                                                print("===============================");
                                                                print(f"| {tanggal}            {waktu} |");
                                                                print("===============================");
                                                                print("| Tarik Tunai                 |");
                                                                print(f"| NO. REK     : {atmFunction.cekNoRekening()}    |");
                                                                print(f"| REKENING    : TABUNGAN      |");
                                                                print(f"| JUMLAH      : Rp {jumlah}    |");
                                                                print(f"| SISA SALDO  : {int(atmFunction.cekSaldo()):,}     |");
                                                                print("===============================");
                                                                print("|   SIMPAN RESI INI SEBAGAI   |");
                                                                print("|       BUKTI YANG SAH        |");
                                                                print("===============================");
                                                                print(Fore.LIGHTBLUE_EX);
                                                                print("Terimakasih telah menggunakan jasa Bank POP :)");
                                                                os._exit(0);
                                                            elif userReceipt == "N" or userReceipt == "n" or userReceipt == "2":
                                                                os.system("cls"); # clear
                                                                print(Fore.LIGHTBLUE_EX);
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
                
                elif nominalWithdraw == 0:
                    os.system("cls"); #clear
                    return;
                
                else:
                    print("Nominal yang anda masukkan salah.");
            except:
                print("Input yang anda masukkan salah.")

    def cekSaldo(atmFunction):
        print(Fore.MAGENTA);
        os.system("cls"); # clear
        infoSaldo = f"Saldo anda sekarang : Rp {atmFunction.cekSaldo():,}";
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-");
        print("",infoSaldo);
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-");

    def transfer(atmFunction):
        print(Fore.LIGHTYELLOW_EX);
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
                                            waktu = time.strftime("%H:%M");
                                            tanggal = date.today();
                                            nextOption = input("Apakah anda ingin mencetak resi? [Y] / [N] : ");
                                            if nextOption == "Y" or nextOption == "y" or nextOption == "1":
                                                os.system("cls"); # clear
                                                print("===============================");
                                                print("|           BANK POP          |");
                                                print("|         CABANG POHON        |");
                                                print("===============================");
                                                print(f"| {tanggal}            {waktu} |");
                                                print("===============================");
                                                print("| Transfer                    |");
                                                print(f"| NO. REK     : {atmFunction.cekNoRekening()}    |");
                                                print(f"| REKENING    : TABUNGAN      |");
                                                print(f"| JUMLAH      : Rp {jumlahTransfer}    |");
                                                print(f"| KE REK.     : {rekeningTujuan}    |");
                                                print("===============================");
                                                print("|   SIMPAN RESI INI SEBAGAI   |");
                                                print("|       BUKTI YANG SAH        |");
                                                print("===============================");
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

    def pembayaran(atmFunction):
        print(Fore.LIGHTGREEN_EX);
        os.system("cls"); #clear
        print("==========================");
        print("|       PEMBAYARAN       |");
        print("==========================");
        print("| [1] TOKEN PLN          |");
        print("| [2] LISTRIK PRABAYAR   |");
        print("| [3] PULSA HP           |");
        print("| [4] E-COMMERCE         |");
        print("|                        |")
        print("| [0] KEMBALI            |");
        print("==========================");
        while True:
            try:
                inputBayar = int(input("Masukkan menu pembayaran : "));
                if inputBayar == 1:
                    while True:
                        try:
                            akunPelanggan = input("Masukkan nomor pelanggan : ");
                            cekAkun = [holder for holder in listAkunPengguna if holder.noPelanggan == akunPelanggan];
                            if(len(cekAkun) > 0):
                                os.system("cls") #clear
                                print("======================================");
                                print("|             TOKEN PLN              |");
                                print("======================================");
                                print("| [1] Rp 20.000     [4] Rp 250.000   |");
                                print("| [2] Rp 50.000     [5] Rp 500.000   |");
                                print("| [3] Rp 100.000    [6] Rp 1.000.000 |");
                                print("|                                    |");
                                print("| [0] KEMBALI                        |");
                                print("======================================");
                                while True:
                                    beliListrik = int(input("Masukkan nominal token di atas : "));
                                    try:
                                        if beliListrik == 1:
                                            os.system("cls");
                                            showHarga = input("Harga token Rp 22.000. Ingin melanjutkan transaksi? [Y] / [N] : ");
                                            if showHarga == "Y" or showHarga == "y" or showHarga == "1":
                                                os.system("cls");
                                                print("Transaksi berhasil.");
                                                atmFunction.setSaldo(atmFunction.cekSaldo() - 22000);
                                                randomToken();
                                                break;
                                            elif showHarga == "N" or showHarga == "n" or showHarga == "2":
                                                os.system("cls"); #clear
                                                print("Transaksi dibatalkan.");
                                                return;
                                            else:
                                                print("Input yang anda masukkan salah.");
                                        elif beliListrik == 2:
                                            os.system("cls");
                                            showHarga = input("Harga token Rp 52.000. Ingin melanjutkan transaksi? [Y] / [N] : ");
                                            if showHarga == "Y" or showHarga == "y" or showHarga == "1":
                                                os.system("cls");
                                                print("Transaksi berhasil.");
                                                atmFunction.setSaldo(atmFunction.cekSaldo() - 52000);
                                                randomToken();
                                                break;
                                            elif showHarga == "N" or showHarga == "n" or showHarga == "2":
                                                os.system("cls"); #clear
                                                print("Transaksi dibatalkan.");
                                                return;
                                            else:
                                                print("Input yang anda masukkan salah.");
                                        elif beliListrik == 3:
                                            os.system("cls");
                                            showHarga = input("Harga token Rp 102.500. Ingin melanjutkan transaksi? [Y] / [N] : ");
                                            if showHarga == "Y" or showHarga == "y" or showHarga == "1":
                                                os.system("cls");
                                                print("Transaksi berhasil.");
                                                atmFunction.setSaldo(atmFunction.cekSaldo() - 102500);
                                                randomToken();
                                                break;
                                            elif showHarga == "N" or showHarga == "n" or showHarga == "2":
                                                os.system("cls"); #clear
                                                print("Transaksi dibatalkan.");
                                                return;
                                            else:
                                                print("Input yang anda masukkan salah.");
                                        elif beliListrik == 4:
                                            os.system("cls");
                                            showHarga = input("Harga token Rp 252.500. Ingin melanjutkan transaksi? [Y] / [N] : ");
                                            if showHarga == "Y" or showHarga == "y" or showHarga == "1":
                                                os.system("cls");
                                                print("Transaksi berhasil.");
                                                atmFunction.setSaldo(atmFunction.cekSaldo() - 252500);
                                                randomToken();
                                                break;
                                            elif showHarga == "N" or showHarga == "n" or showHarga == "2":
                                                os.system("cls"); #clear
                                                print("Transaksi dibatalkan.");
                                                return;
                                            else:
                                                print("Input yang anda masukkan salah.");
                                        elif beliListrik == 5:
                                            os.system("cls");
                                            showHarga = input("Harga token Rp 504.000. Ingin melanjutkan transaksi? [Y] / [N] : ");
                                            if showHarga == "Y" or showHarga == "y" or showHarga == "1":
                                                os.system("cls");
                                                print("Transaksi berhasil.");
                                                atmFunction.setSaldo(atmFunction.cekSaldo() - 504000);
                                                randomToken();
                                                break;
                                            elif showHarga == "N" or showHarga == "n" or showHarga == "2":
                                                os.system("cls"); #clear
                                                print("Transaksi dibatalkan.");
                                                return;
                                            else:
                                                print("Input yang anda masukkan salah.");
                                        elif beliListrik == 6:
                                            os.system("cls");
                                            showHarga = input("Harga token Rp 1.005.000. Ingin melanjutkan transaksi? [Y] / [N] : ");
                                            if showHarga == "Y" or showHarga == "y" or showHarga == "1":
                                                os.system("cls");
                                                print("Transaksi berhasil.");
                                                atmFunction.setSaldo(atmFunction.cekSaldo() - 1005000);
                                                randomToken();
                                                break;
                                            elif showHarga == "N" or showHarga == "n" or showHarga == "2":
                                                os.system("cls"); #clear
                                                print("Transaksi dibatalkan.");
                                                return;
                                            else:
                                                print("Input yang anda masukkan salah.");
                                        elif beliListrik == 0:
                                            os.system("cls"); #clear
                                            print("Transaksi dibatalkan");
                                            return;
                                        else:
                                            print("Input nominal salah.");
                                    except:
                                        print("Input yang anda masukkan salah.");
                                
                                while True:
                                    try:
                                        nextOption = input("Apakah anda ingin melanjutkan transaksi? [Y] / [N] : ");
                                        if nextOption == "Y" or nextOption ==  "y" or nextOption == "1":
                                            os.system("cls"); #clear
                                            return;
                                        elif nextOption == "N" or nextOption ==  "n" or nextOption == "2":
                                            os.system("cls"); #clear
                                            print("Terimakasih telah menggunakan jasa Bank POP :)");
                                            os._exit(0);
                                        else:
                                            print("Input yang anda masukkan salah.");
                                    except:
                                        print("Input yang anda masukkan salah.");
                            else:
                                print("Data yang anda masukkan salah.");
                        except:
                            os.system("cls"); #clear
                            print("Data yang anda masukkan salah.");
                elif inputBayar == 2:
                    os.system("cls") #clear
                    print("Belum tersedia.");
                    break;
                elif inputBayar == 3:
                    print(Fore.MAGENTA);
                    os.system("cls"); #clear
                    print("==================");
                    print("|      PULSA     |");
                    print("==================");
                    print("| [1] TELKOMSEL  |");
                    print("| [2] XL         |");
                    print("|                |");
                    print("| [0] KEMBALI    |");
                    print("==================");
                    while True:
                        try:
                            inputProvider = int(input("Masukkan provider di atas : "));
                            if inputProvider == 1:
                                os.system("cls"); #clear
                                while True:
                                    try:
                                        pulsaINT = int(input("Masukkan nomor HP anda 0821 "));
                                        pulsaSTR = str(pulsaINT);
                                        if len(pulsaSTR) < 8:
                                            print("Nomor yang anda masukkan kurang dari 12.");
                                            continue;
                                        elif len(pulsaSTR) > 8:
                                            print("Nomor yang anda masukkan lebih dari 12.");
                                            continue;
                                        elif len(pulsaSTR) == 8:
                                            os.system("cls"); #clear
                                            print(Fore.RED);
                                            print("======================================");
                                            print("|              TELKOMSEL             |");
                                            print("======================================");
                                            print("| [1] Rp 5.000       [4] Rp 20.000   |");
                                            print("| [2] Rp 10.000      [5] Rp 50.000   |");
                                            print("| [3] Rp 15.000      [6] Rp 100.000  |");
                                            print("|                                    |");
                                            print("| [0] KEMBALI                        |");
                                            print("======================================");
                                            while True:
                                                nominalPulsa = int(input("Masukkan nominal di atas : "));
                                                try:
                                                    if nominalPulsa == 1:
                                                        os.system("cls"); #clear
                                                        while True:
                                                            transaksiHP = input("Harga pulsa Rp 7.000, ingin melanjutkan transaksi? [Y] / [N] : ");
                                                            if transaksiHP == "Y" or transaksiHP == "y" or transaksiHP == "1":
                                                                os.system("cls"); #clear
                                                                atmFunction.setSaldo(atmFunction.cekSaldo() - 7000);
                                                                while True:
                                                                    nextTr = input("Transaksi Berhasil. Ingin melanjutkan transaksi? [Y] / [N] : ");
                                                                    if nextTr == "Y" or nextTr == "y" or nextTr == "1":
                                                                        os.system("cls"); #clear
                                                                        return;
                                                                    elif nextTr == "N" or nextTr == "n" or nextTr == "2":
                                                                        os.system("cls"); #clear
                                                                        print("Terimakasih telah menggunakan jasa Bank POP :)");
                                                                        os._exit(0);
                                                                    else:
                                                                        print("Input yang anda masukkan salah");
                                                            elif transaksiHP == "N" or transaksiHP == "n" or transaksiHP == "2":
                                                                os.system("cls"); #clear
                                                                print("Transaksi dibatalkan.");
                                                                return;
                                                            else:
                                                                print("Input yang anda masukkan salah.");

                                                    elif nominalPulsa == 2:
                                                        os.system("cls"); #clear
                                                        while True:
                                                            transaksiHP = input("Harga pulsa Rp 12.000, ingin melanjutkan transaksi? [Y] / [N] : ");
                                                            if transaksiHP == "Y" or transaksiHP == "y" or transaksiHP == "1":
                                                                os.system("cls"); #clear
                                                                atmFunction.setSaldo(atmFunction.cekSaldo() - 12000);
                                                                while True:
                                                                    nextTr = input("Transaksi Berhasil. Ingin melanjutkan transaksi? [Y] / [N] : ");
                                                                    if nextTr == "Y" or nextTr == "y" or nextTr == "1":
                                                                        os.system("cls"); #clear
                                                                        return;
                                                                    elif nextTr == "N" or nextTr == "n" or nextTr == "2":
                                                                        os.system("cls"); #clear
                                                                        print("Terimakasih telah menggunakan jasa Bank POP :)");
                                                                        os._exit(0);
                                                                    else:
                                                                        print("Input yang anda masukkan salah");
                                                            elif transaksiHP == "N" or transaksiHP == "n" or transaksiHP == "2":
                                                                os.system("cls"); #clear
                                                                print("Transaksi dibatalkan.");
                                                                return;
                                                            else:
                                                                print("Input yang anda masukkan salah.");

                                                    elif nominalPulsa == 3:
                                                        os.system("cls"); #clear
                                                        while True:
                                                            transaksiHP = input("Harga pulsa Rp 17.000, ingin melanjutkan transaksi? [Y] / [N] : ");
                                                            if transaksiHP == "Y" or transaksiHP == "y" or transaksiHP == "1":
                                                                os.system("cls"); #clear
                                                                atmFunction.setSaldo(atmFunction.cekSaldo() - 17000);
                                                                while True:
                                                                    nextTr = input("Transaksi Berhasil. Ingin melanjutkan transaksi? [Y] / [N] : ");
                                                                    if nextTr == "Y" or nextTr == "y" or nextTr == "1":
                                                                        os.system("cls"); #clear
                                                                        return;
                                                                    elif nextTr == "N" or nextTr == "n" or nextTr == "2":
                                                                        os.system("cls"); #clear
                                                                        print("Terimakasih telah menggunakan jasa Bank POP :)");
                                                                        os._exit(0);
                                                                    else:
                                                                        print("Input yang anda masukkan salah");
                                                            elif transaksiHP == "N" or transaksiHP == "n" or transaksiHP == "2":
                                                                os.system("cls"); #clear
                                                                print("Transaksi dibatalkan.");
                                                                return;
                                                            else:
                                                                print("Input yang anda masukkan salah.");

                                                    elif nominalPulsa == 4:
                                                        os.system("cls"); #clear
                                                        while True:
                                                            transaksiHP = input("Harga pulsa Rp 21.500, ingin melanjutkan transaksi? [Y] / [N] : ");
                                                            if transaksiHP == "Y" or transaksiHP == "y" or transaksiHP == "1":
                                                                os.system("cls"); #clear
                                                                atmFunction.setSaldo(atmFunction.cekSaldo() - 21500);
                                                                while True:
                                                                    nextTr = input("Transaksi Berhasil. Ingin melanjutkan transaksi? [Y] / [N] : ");
                                                                    if nextTr == "Y" or nextTr == "y" or nextTr == "1":
                                                                        os.system("cls"); #clear
                                                                        return;
                                                                    elif nextTr == "N" or nextTr == "n" or nextTr == "2":
                                                                        os.system("cls"); #clear
                                                                        print("Terimakasih telah menggunakan jasa Bank POP :)");
                                                                        os._exit(0);
                                                                    else:
                                                                        print("Input yang anda masukkan salah");
                                                            elif transaksiHP == "N" or transaksiHP == "n" or transaksiHP == "2":
                                                                os.system("cls"); #clear
                                                                print("Transaksi dibatalkan.");
                                                                return;
                                                            else:
                                                                print("Input yang anda masukkan salah.");

                                                    elif nominalPulsa == 5:
                                                        os.system("cls"); #clear
                                                        while True:
                                                            transaksiHP = input("Harga pulsa Rp 51.500, ingin melanjutkan transaksi? [Y] / [N] : ");
                                                            if transaksiHP == "Y" or transaksiHP == "y" or transaksiHP == "1":
                                                                os.system("cls"); #clear
                                                                atmFunction.setSaldo(atmFunction.cekSaldo() - 51500);
                                                                while True:
                                                                    nextTr = input("Transaksi Berhasil. Ingin melanjutkan transaksi? [Y] / [N] : ");
                                                                    if nextTr == "Y" or nextTr == "y" or nextTr == "1":
                                                                        os.system("cls"); #clear
                                                                        return;
                                                                    elif nextTr == "N" or nextTr == "n" or nextTr == "2":
                                                                        os.system("cls"); #clear
                                                                        print("Terimakasih telah menggunakan jasa Bank POP :)");
                                                                        os._exit(0);
                                                                    else:
                                                                        print("Input yang anda masukkan salah");
                                                            elif transaksiHP == "N" or transaksiHP == "n" or transaksiHP == "2":
                                                                os.system("cls"); #clear
                                                                print("Transaksi dibatalkan.");
                                                                return;
                                                            else:
                                                                print("Input yang anda masukkan salah.");
                                                    
                                                    elif nominalPulsa == 6:
                                                        os.system("cls"); #clear
                                                        while True:
                                                            transaksiHP = input("Harga pulsa Rp 101.500, ingin melanjutkan transaksi? [Y] / [N] : ");
                                                            if transaksiHP == "Y" or transaksiHP == "y" or transaksiHP == "1":
                                                                os.system("cls"); #clear
                                                                atmFunction.setSaldo(atmFunction.cekSaldo() - 101500);
                                                                while True:
                                                                    nextTr = input("Transaksi Berhasil. Ingin melanjutkan transaksi? [Y] / [N] : ");
                                                                    if nextTr == "Y" or nextTr == "y" or nextTr == "1":
                                                                        os.system("cls"); #clear
                                                                        return;
                                                                    elif nextTr == "N" or nextTr == "n" or nextTr == "2":
                                                                        os.system("cls"); #clear
                                                                        print("Terimakasih telah menggunakan jasa Bank POP :)");
                                                                        os._exit(0);
                                                                    else:
                                                                        print("Input yang anda masukkan salah");
                                                            elif transaksiHP == "N" or transaksiHP == "n" or transaksiHP == "2":
                                                                os.system("cls"); #clear
                                                                print("Transaksi dibatalkan.");
                                                                return;
                                                            else:
                                                                print("Input yang anda masukkan salah.");
                                                    elif nominalPulsa == 0:
                                                        os.system("cls"); #clear
                                                        return;           
                                                    else:
                                                        print("Nominal yang anda masukkan salah.");
                                                except:
                                                    print("Jumlah salah.")
                                        else:
                                            print("Nomor yang anda masukkan salah.");
                                    except:
                                        print("Nomor Invalid.");
                            elif inputProvider == 2:
                                os.system("cls"); #clear
                                print("Segera hadir.");
                                return;
                            elif inputProvider == 0:
                                os.system("cls"); #clear
                                return;
                            else:
                                print("Input yang anda masukkan salah.");
                                continue;
                        except:
                            print("Input yang anda masukkan salah.");
                elif inputBayar == 4:
                    os.system("cls"); #clear
                    print("==================");
                    print("|   E-COMMERCE   |");
                    print("==================");
                    print("| [1] TokoPaEdi  |");
                    print("| [2] Sheepi     |");
                    print("| [3] Lupabapak  |");
                    print("|                |");
                    print("| [0] KEMBALI    |");
                    print("==================");
                    while True:
                        try:
                            tokoOnline = int(input("Masukkan toko di atas : "));
                            if tokoOnline == 1:
                                os.system("cls"); #clear
                                print("Segera hadir.");
                                return;
                            elif tokoOnline == 2:
                                os.system("cls"); #clear
                                print("Segera hadir.");
                                return;
                            elif tokoOnline == 3:
                                os.system("cls"); #clear
                                print("Segera hadir.");
                                return;
                            elif tokoOnline == 0:
                                os.system("cls"); #clear
                                return;
                            else:
                                print("Input yang anda masukkan salah.");
                        except:
                            print("Input yang anda masukkan salah.")
                elif inputBayar == 0:
                    os.system("cls"); #clear
                    return;
                else:
                    os.system("cls");
                    print("Input yang anda masukkan salah.");
                    return;
            except:
                print("Input yang anda masukkan salah.");

    if __name__ == "__main__" :
        akunUser = atmFungsi("","","","","","");

        ## List Pengguna Bank POP
        ## List Nasabah
        listAkunPengguna = [];
        listAkunPengguna.append(atmFungsi("1379708899", "123456789", 582492, "ALFIE", "HAMZAMI", 5500000));
        listAkunPengguna.append(atmFungsi("1725964330", "123654789", 512253, "RYAN", "HIDAYAH", 1500000));
        listAkunPengguna.append(atmFungsi("1250248833", "135792468", 132433, "REFY", "SAPUTRI", 9650000));
        listAkunPengguna.append(atmFungsi("1992842233", "987654321", 345453, "ARIF", "HIDAYAT", 8700000));
        listAkunPengguna.append(atmFungsi("1853039966", "246813579", 125578, "JOSEPH", "MANSOER", 4300000));

        # Input User
        ## Input Rekening Pengguna
        while True:
            try:
                inputNomorRekening = input(Fore.YELLOW + "Masukkan nomor rekening anda : ");
                cekDebit = [holder for holder in listAkunPengguna if holder.noRekening == inputNomorRekening];
                if(len(cekDebit) > 0):
                    akunUser = cekDebit[0];
                    break;
                else:
                    print(Fore.LIGHTYELLOW_EX + "Nomor akun tidak dikenal, silahkan input kembali nomor akun anda.");
            except:
                print(Fore.RED + "Nomor akun tidak dikenal, silahkan input kembali nomor akun anda.");

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
                            print(Fore.LIGHTYELLOW_EX + "PIN salah, silahkan masukkan kembali PIN anda. Tersisa : 2 kali.");
                        else:
                            if akunUser.cekPin() == userPin:
                                os.system("cls"); # clear
                                break;
                            else:
                                if akunUser.cekPin() != userPin:
                                    if count == 2:
                                        os.system("cls"); # clear
                                        count += 1;
                                        print(Fore.RED + "PIN salah, silahkan masukkan kembali PIN anda. Tersisa : 1 kali.");
                                    else:
                                        if akunUser.cekPin() == userPin:
                                            os.system("cls"); # clear
                                            break;
                                        else:
                                            if akunUser.cekPin() != userPin:
                                                if count == 3:
                                                    os.system("cls"); # clear
                                                    print(Fore.RED + "Sesi berakhir. Silahkan coba beberapa sesaat lagi.");
                                                    os._exit(0);
                                                else:
                                                    os.system("cls"); # clear
                                                    break;
                    else:
                        break;
            except:
                print("Format hanya angka! Masukkan kembali PIN anda.");

        ## Opsi printOut atmProgram
        print(Fore.BLUE + "Selamat Datang,", akunUser.cekNamaDepan(), akunUser.cekNamaBelakang());

    def userMenu():
        while True:
            menuUtama();
            try:
                opsi = int(input("Masukkan Pilihan Menu : "));
                if (opsi == 1):
                    setorTunai(akunUser);
                elif (opsi == 2):
                    tarikTunai(akunUser);
                elif (opsi == 3):
                    cekSaldo(akunUser);
                elif (opsi == 4):
                    transfer(akunUser);
                elif (opsi == 5):
                    pembayaran(akunUser);
                elif (opsi == 0):
                    os.system("cls"); # clear
                    print(Fore.BLUE + "Terimakasih telah menggunakan jasa Bank POP :)");
                    os._exit(0);
                else:
                    os.system("cls"); # clear
                    print(Fore.RED + "Menu tidak tersedia.");
            except:
                os.system("cls"); #clear
                print(Fore.RED + "Format yang anda masukkan salah. Silahkan masukkan kembali.");
        
    userMenu();

def mainMenu():
    print(Fore.MAGENTA + "Selamat datang di menu utama POP");
    print(Fore.LIGHTYELLOW_EX + "[1] " + Fore.RED + "Bahasa " + Fore.LIGHTWHITE_EX + "Indonesia");
    print(Fore.LIGHTYELLOW_EX + "[2] " + Fore.BLUE + "English");
    while True:
        print(Fore.LIGHTRED_EX);
        langMenu = input("Silahkan pilih bahasa. Please choose your language : ")
        try:
            if langMenu == 1 or langMenu == "1":
                os.system("cls") #clear
                atmBahasaIndonesia();
            else:
                print("Bahasa belum tersedia. Language is not available");
        except:
            print("Menu yang anda masukkan salah, silahkan coba lagi. Wrong input, please try again.");
mainMenu();