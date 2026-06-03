# 1. ADIM: Ağacın sırasını oluşturmak için standart sınıf yapısı
class KitapSırası:
    def __init__(self, sayfa_sayisi):
        self.sayfa = sayfa_sayisi
        self.sol = None   # Kendinden küçük sayfalı kitaplar için sol taraf
        self.sag = None   # Kendinden büyük sayfalı kitaplar için sağ taraf

# ---- 2. ADIM: AĞACI KENDİMİZ KURUYORUZ ----
# Sayfa sayılarına göre dengeli bir kitaplık ağacı kurduk
ana_kok = KitapSırası(250)
ana_kok.sol = KitapSırası(180)
ana_kok.sag = KitapSırası(400)
ana_kok.sag.sol = KitapSırası(320)
ana_kok.sag.sag = KitapSırası(500)

# ---- 3. ADIM: WHILE DÖNGÜSÜ İLE ARAMA YAPMA ----
aranan_kitap = 320
su_anki_durum = ana_kok
bulundu_mu = False

print(f" Arama Başlıyor: {aranan_kitap} sayfalık kitap aranıyor...\n")

# Ağaçta aşağı doğru indikçe döngü çalışır
while su_anki_durum is not None:
    print(f" Şu an {su_anki_durum.sayfa} sayfalık kitaba bakılıyor...")
    
    # Kitabı bulursak döngüyü kırıyoruz
    if aranan_kitap == su_anki_durum.sayfa:
        bulundu_mu = True
        print(" Eşleşme yakalandı!")
        break # OLMAZSA SONSUZ DÖNGÜYE GİRER 
        
    # Aranan kitap sayfası kökten büyükse SAĞA gidiyoruz
    elif aranan_kitap > su_anki_durum.sayfa:
        print(f"   {aranan_kitap} > {su_anki_durum.sayfa} olduğu için SAĞA gidiyoruz.")
        su_anki_durum = su_anki_durum.sag
        
    # Aranan kitap sayfası kökten küçükse SOLA gidiyoruz
    else:
        print(f"   {aranan_kitap} < {su_anki_durum.sayfa} olduğu için SOLA gidiyoruz.")
        su_anki_durum = su_anki_durum.sol
        
    # BULUNMUYORSA DÖNGÜ BİTİRİLMELİ
    if su_anki_durum is None:
        break

print("\n--- ARAMA SONUCU ---")
if bulundu_mu == True:
    print(f" Başarılı! {aranan_kitap} sayfalık kitap sırada bulundu.")
else:
    print(f" Başarısız {aranan_kitap} sayfalık kitap bu sırada yok.")