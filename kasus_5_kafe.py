class MenuItem:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama 
        self.harga = harga 

class PesananKafe:
    def __init__(self, customer):
        self.customer = customer
        self.order = []

    def tambahkan_item(self, item, jumlah):
        self.order.append((item, jumlah))

    def hitung_total_item(self):
        total = 0
        for item, jumlah in self.order:
            total += jumlah
        return total

    def hitung_subtotal(self):
        subtotal = 0
        for item, jumlah in self.order:
            subtotal += item.harga * jumlah
        return subtotal 

    def hitung_diskon(self):
        subtotal = self.hitung_subtotal()
        if subtotal >= 60000:
            return subtotal * 0.10
        return 0

    def hitung_pajak(self):
        subtotal_setelah_diskon = (
            self.hitung_subtotal() - self.hitung_diskon()
        )
        return subtotal_setelah_diskon * 0.10 

    def hitung_total_bayar(self):
        return(
            self.hitung_subtotal()
            - self.hitung_diskon() 
            + self.hitung_pajak()
        )

    def cetak_struk(self):
        print("\n=== STRUK PESANAN KAFE ===")
        print(f"Pelanggan: {self.customer}")

        for nomor, (item, jumlah) in enumerate(self.order, start=1):
            total_item = item.harga * jumlah
            print(f"{nomor}. {item.nama}")
            print(
                f"  {jumlah} x Rp{item.harga:,.0f}"
                f" = Rp{total_item:,.0f}"
            )

        print("-" * 30)
        print(f"Total item : {self.hitung_total_item()}")
        print(f"Subtotal   : Rp{self.hitung_subtotal():,.0f}".replace(",", "."))
        print(f"Diskon 10% : Rp{self.hitung_diskon():,.0f}".replace(",", "."))
        print(f"Pajak 10%  : Rp{self.hitung_pajak():,.0f}".replace(",", "."))
        print(f"Total bayar: Rp{self.hitung_total_bayar():,.0f}".replace(",", "."))
        print("=" * 30)

def tampilkan_menu(menu_kafe):
    print("\n===KAFE KOMA KOPI===")
    print("Daftar Menu:")

    for item in menu_kafe:
        harga = f"{item.harga:,.0f}".replace(",",".")
        print(f"{item.kode} - {item.nama} (Rp{harga})")

def main():
    menu_kafe = [
        MenuItem("K01", "Kopi Susu Aren", 18000),
        MenuItem("k02", "Matcha Latee", 22000),
        MenuItem("K03", "Toast Cokelat Keju", 15000), 
        MenuItem("K04", "Kentang Goreng", 14000)
    ]

    tampilkan_menu(menu_kafe)

    nama = input("\nNama pelanggan: ").strip()
    while not nama:
        print("Nama pelanggan tidak boleh kosong.")
        nama = input("Nama pelanggan: ").strip()

    pesanan = PesananKafe(nama)

    while True:
        kode = input("\nKode menu: ").strip().upper()

        item_dipilih = None
        for item in menu_kafe:
            if item.kode == kode:
                item_dipilih = item
                break

        if item_dipilih is None:
            print("Kode menu tidak ditemukan.")
            continue

        while True:
            try:
                jumlah = int(input("Jumlah pesanan: "))
                if jumlah > 0:
                    break
                print("Jumlah harus lebih dari 0.")
            except ValueError:
                print("Jumlah harus berupa bilangan bulat.")

        pesanan.tambahkan_item(item_dipilih, jumlah)
        print("Menu berhasil ditambahkan.")

        while True:
            confirm = input(
                "Apakah ada menu yang ingin ditambahkan (y/n)?"
            ).strip().lower()

            if confirm in ("y", "n"):
                break
            print("Masukkan pilihan y atau n.")

        if confirm == "n":
            break

    if pesanan.order:
        pesanan.cetak_struk()
    else:
        print("Tidak ada pesanan.")

if __name__ == "__main__":
    main()