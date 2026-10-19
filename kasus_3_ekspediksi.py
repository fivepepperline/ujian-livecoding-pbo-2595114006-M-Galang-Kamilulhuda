class PkaetEkspedisi:
    def __init__(self, nomor_resi, pengirim, layanan, berat, nilai_barang):
        self.nomor_resi = nomor_resi
        self.pengirim = pengirim
        self.layanan = layanan 
        self.berat = berat
        self.nilai_barang = nilai_barang

    def hitung_ongkos_dasar(self):
        if self.layanan == "Reguler":
            tarif = 10000
        else:
            tarif = 18000

        return tarif * self.berat

    def hitung_surcharge(self):
        if self.berat > 10:
            return 20000
        return 0 

    def hitung_asuransi(self):
        if self.nilai_barang >= 1000000:
            return self.nilai_barang * 0.10
        return 0 

    def hitung_total_ongkos(self):
        return (
            self.hitung_ongkos_dasar()
            + self.hitung_surcharge()
            + self.hitung_asuransi
        )

    def cetak_resi(self):
        print("\n=== RESI PENGIRIMAN ===")
        print(f"Nomor Resi        : {self.nomor_resi}")
        print(f"pengirim          : {self.pengirim}")
        print(f"Layanan           : {self.layanan}")
        print(f"Berat             : {self.berat:g} Kg")
        print(f"Tarif dasar       : Rp{self.hitung_ongkos_dasar():,.0f}".replace(",", "."))
        print(f"Heavy Surcharge   : Rp{self.hitung_surcharge():,.0f}".replace(",", "."))
        print(f"Biaya Asuransi    : Rp{self.hitung_asuransi():,.0f}".replace(",", "."))
        print(f'Total Ongkos      : Rp{self.hitung_total_ongkos():,.0f}'.replace(",", "."))
        print("=" * 30)

def main():
    print("=== EKSPEDISI NUSANTARA LOGISTIK ===")

    nomor_resi = input("Nomor Resi: ").strip()
    pengirim = input("Nama Pengirim: ").strip()

    while True:
        layanan = input("Jenis Layanan (Reguler/Ekspress): ").strip().title()
        if layanan in ("Reguler", "Ekspress"):
            break
        print("Layanan tidak valid. Pilih Reguler atau Express.")

    while True:
        try:
            berat = float(input("Berat Paket (Kg): "))
            if berat > 0:
                break
            print("Berat paket harus lebih dari 0.")

        except ValueError:
            print("Berat harus berupa angka.")

    while True:
        try:
            nilai_barang = float(input("Nilai barang (Rp): "))
            if nilai_barang > 0:
                break 
            print("Nilai barang harus lebih dari 0.")

        except ValueError:
            print("Nilai barang harus berupa angka.")

    paket = PkaetEkspedisi(
        nomor_resi,
        pengirim, 
        layanan,
        berat,
        nilai_barang
    )

    paket.cetak_resi()

if __name__ == "__main__":
    main()