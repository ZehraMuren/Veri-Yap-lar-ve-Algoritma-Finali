# 1. ADIM: Günlük dizi izlenme sayıları listesi
izlenmeler = [2, 1, 5, 1, 3, 2]

# 2. ADIM: İlk 3 günün toplamını alıp "en büyük" kabul ediyoruz (2 + 1 + 5)
su_anki_toplam = izlenmeler[0] + izlenmeler[1] + izlenmeler[2]
en_buyuk_toplam = su_anki_toplam

# 3. ADIM: Pencereyi el ile sağa kaydırıyoruz (Gireni ekle, çıkanı çıkar!)
# 1. Kaydırma: 2 çıktı, 1 girdi
su_anki_toplam = su_anki_toplam - izlenmeler[0] + izlenmeler[3]
if su_anki_toplam > en_buyuk_toplam: en_buyuk_toplam = su_anki_toplam

# 2. Kaydırma: 1 çıktı, 3 girdi
su_anki_toplam = su_anki_toplam - izlenmeler[1] + izlenmeler[4]
if su_anki_toplam > en_buyuk_toplam: en_buyuk_toplam = su_anki_toplam

# 3. Kaydırma: 5 çıktı, 2 girdi
su_anki_toplam = su_anki_toplam - izlenmeler[2] + izlenmeler[5]
if su_anki_toplam > en_buyuk_toplam: en_buyuk_toplam = su_anki_toplam

# 4. ADIM: En yüksek ardışık 3 günlük sonucu ekrana yazdırıyoruz
print("En yüksek 3 günlük toplam izlenme:", en_buyuk_toplam)