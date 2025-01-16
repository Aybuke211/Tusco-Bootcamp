import os

class Market:
    def __init__(self):
        self.filename = "product.txt"
        # Dosya mevcut değilse oluştur
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                pass

    def __del__(self):
        print("Program sonlandı ve dosya kapatıldı.")

    def list_products(self):
        """Dosyadaki tüm ürünleri listeleyen metot"""
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                if not lines:
                    print("\nHiçbir ürün bulunamadı.\n")
                else:
                    print("\n*** ÜRÜNLER ***")
                    for index, line in enumerate(lines, start=1):
                        try:
                            name, category, price, stock = line.strip().split(",")
                            print(f"{index}) Ad: {name}, Kategori: {category}, Fiyat: {price}, Stok: {stock}")
                        except ValueError:
                            print(f"Satır {index} format hatası içeriyor: {line.strip()}")
        except Exception as e:
            print("Hata: ", e)

    def add_product(self):
        """Yeni bir ürün ekleyen metot"""
        try:
            name = input("\nÜrün adını girin: ").strip()
            category = input("Kategori girin: ").strip()
            price = input("Fiyat girin: ").strip()
            stock = input("Stok miktarını girin: ").strip()

            if not name or not category or not price or not stock:
                print("Tüm alanlar doldurulmalıdır!")
                return

            with open(self.filename, "a") as file:
                file.write(f"{name},{category},{price},{stock}\n")
            print(f"\n{name} isimli ürün eklendi.\n")
        except Exception as e:
            print("Hata: ", e)

    def delete_product(self):
        """Bir ürünü silen metot"""
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

            if not lines:
                print("\nHiçbir ürün bulunamadı.\n")
                return

            self.list_products()

            choice = input("\nSilmek istediğiniz ürün numarasını girin: ").strip()
            if not choice.isdigit():
                print("Lütfen geçerli bir sayı girin.")
                return

            choice = int(choice)
            if 1 <= choice <= len(lines):
                removed_product = lines.pop(choice - 1)

                with open(self.filename, "w") as file:
                    file.writelines(lines)

                name, category, price, stock = removed_product.strip().split(",")
                print(f"\n{name} isimli ürün silindi.\n")
            else:
                print("Geçersiz bir numara girdiniz.")

        except Exception as e:
            print("Hata: ", e)


def menu():
    market = Market()
    while True:
        print("\n*** MENÜ ***")
        print("1) ÜRÜNLERİ LİSTELE")
        print("2) ÜRÜN EKLE")
        print("3) ÜRÜN SİL")
        print("4) ÇIKIŞ")

        choice = input("\nSeçiminizi yapın (1-4): ").strip()

        if choice == "1":
            market.list_products()
        elif choice == "2":
            market.add_product()
        elif choice == "3":
            market.delete_product()
        elif choice == "4":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    menu()