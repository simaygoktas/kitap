"""
Kitap Takip Uygulaması
----------------------
Amaç: Okunan/okunacak kitapları ekleyen, listeleyen, durumunu (okundu/okunmadı)
güncelleyen ve silen basit bir konsol uygulaması. Kitaplar 'kitaplar.json'
dosyasında saklanır; program kapanıp açılınca kayıtlar korunur.

Nasıl çalıştırılır:
- python3 kitap.py

İşlevler:
1. Kitapları Listele
2. Yeni Kitap Ekle (boş başlık/yazar kabul etmez)
3. Okundu/Okunmadı İşaretle
4. Kitap Sil
5. Çıkış (kayıtları dosyaya yazar)
"""

import json

DOSYA_ADI = "kitaplar.json"


def kitaplari_yukle():
    """
    Dosyadan kitap listesini okur ve döndürür.
    Dosya yoksa (FileNotFoundError) boş bir liste döndür.
    Dosya bozuksa (json.JSONDecodeError) yine boş liste döndürüp kullanıcıyı bilgilendirebilirsin.

    İpucu:
        with open(DOSYA_ADI, "r", encoding="utf-8") as f:
            return json.load(f)
    Bunu try-except FileNotFoundError içine al.
    """
    # TODO: dosyayı aç, json.load ile oku, hata durumunda [] döndür
    pass


def kitaplari_kaydet(kitaplar):
    """
    Verilen kitap listesini DOSYA_ADI dosyasına json olarak yazar.

    İpucu:
        with open(DOSYA_ADI, "w", encoding="utf-8") as f:
            json.dump(kitaplar, f, ensure_ascii=False, indent=2)
    """
    # TODO: dosyayı "w" modunda aç, json.dump ile yaz
    pass


def kitaplari_listele(kitaplar):
    """
    Kitapları numaralandırarak başlık — yazar [durum] biçiminde yazdırır.
    Liste boşsa "Henüz kayıtlı kitap yok." yazdırır.

    İpucu: enumerate(kitaplar, start=1) kullanarak numaraları otomatik üret.
    Her kitap bir dict: kitap["baslik"], kitap["yazar"], kitap["okundu"] (True/False)
    """
    # TODO: liste boşsa mesaj ver, değilse numaralandırarak yazdır
    pass


def kitap_ekle(kitaplar):
    """
    Kullanıcıdan başlık ve yazar alır. Boş girilirse "Başlık boş olamaz!" /
    benzer bir mesaj göster ve eklemeden çık.
    Yeni kitap: {"baslik": ..., "yazar": ..., "okundu": False}
    kitaplar listesine ekle, sonra kitaplari_kaydet(kitaplar) çağır.
    """
    # TODO: input al, strip() ile boşluk temizle, boşsa uyar ve dön
    # TODO: değilse dict oluştur, listeye ekle, kaydet, onay mesajı yazdır
    pass


def durum_degistir(kitaplar):
    """
    Önce listeyi göster. Kullanıcıdan numara al (try-except ValueError ile,
    sayı değilse "Lütfen bir sayı girin!" yazdır).
    Numara aralık dışındaysa "Geçersiz kitap numarası!" yazdır.
    Geçerliyse kitap["okundu"] değerini tersine çevir (True <-> False),
    kaydet ve onay mesajı yazdır.
    """
    # TODO
    pass


def kitap_sil(kitaplar):
    """
    durum_degistir ile aynı numara doğrulama mantığı.
    Geçerliyse kitaplar.pop(index) ile sil, kaydet, onay mesajı yazdır.
    """
    # TODO
    pass


def menu_goster():
    print("\n--- KİTAP TAKİP UYGULAMASI ---")
    print("1. Kitapları Listele")
    print("2. Yeni Kitap Ekle")
    print("3. Okundu/Okunmadı İşaretle")
    print("4. Kitap Sil")
    print("5. Çıkış")


def main():
    print("Kitap Takip Uygulamasına Hoş Geldiniz!")
    kitaplar = kitaplari_yukle()
    # TODO: kitaplar boşsa "Kayıt dosyası bulunamadı..." mesajı,
    #       doluysa "Kitaplar başarıyla yüklendi." mesajı yazdırabilirsin.

    while True:
        menu_goster()
        secim = input("Seçiminiz (1-5): ")

        if secim == "1":
            kitaplari_listele(kitaplar)
        elif secim == "2":
            kitap_ekle(kitaplar)
        elif secim == "3":
            durum_degistir(kitaplar)
        elif secim == "4":
            kitap_sil(kitaplar)
        elif secim == "5":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen 1-5 arası bir değer girin.")


if __name__ == "__main__":
    main()