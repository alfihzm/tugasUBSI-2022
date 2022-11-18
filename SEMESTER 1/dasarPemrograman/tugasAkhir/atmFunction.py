class atmFungsi :
    def __init__(self, noRekening, pin, namaDepan, namaBelakang, saldo):
        self.noRekening   = noRekening;
        self.pin          = pin;
        self.namaDepan    = namaDepan;
        self.namaBelakang = namaBelakang;
        self.saldo        = saldo;

    ## Get Data
    def cekNoRekening(self):
        return self.noRekening;
    def cekPin(self):
        return self.pin;
    def cekNamaDepan(self):
        return self.namaDepan;
    def cekNamaBelakang(self):
        return self.namaBelakang;
    def cekSaldo(self):
        return self.saldo;

    ## Set Data
    def setNoRekening(self, newVal):
        self.noRekening = newVal;
    def setPin(self, newVal):
        self.pin = newVal
    def setNamaDepan(self, newVal):
        self.namaDepan = newVal;
    def setNamaBelakang(self, newVal):
        self.namaBelakang = newVal;
    def setSaldo(self, newVal):
        self.saldo = newVal;
