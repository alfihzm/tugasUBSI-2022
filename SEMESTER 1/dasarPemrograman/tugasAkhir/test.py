while True:
    try:
        angka = int(input("Masukkan angka : "));
        if angka == int(angka):
            print("Input yang anda masukkan benar.");
            break;
    except:
        print("Input yang anda masukkan salah.");