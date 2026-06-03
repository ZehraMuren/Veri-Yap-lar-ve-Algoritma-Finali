# Başlangıçta izlemek istediğimiz 3 diziyi sırayla kuyruğa ekliyoruz
# İlk eklediğimiz dizi sıranın en önünde olacak (FIFO mantığı)
dizi_kuyrugu = ["Weak Hero Class 1", "Taxi Driver", "Twinkling Watermelon"]
maksimum_kapasite = 5

# while True döngüsü biz 3'e basıp çıkana kadar menüyü sürekli döndürür
while True:
    print("\n---  DİZİ İZLEME SIRASI ---")
    print("1 - Listeye Yeni Dizi Ekle (Sıranın Sonuna)")
    print("2 - Sıradaki İlk Diziyi İzle (Sıranın Önünden Çıkar)")
    print("3 - Listeden Çık")
    
    secim = input("Yapmak istediğiniz işlemi seçin (1,2,3): ")
    
    if secim == "1":
        # Listedeki dizi sayısı kapasiteye (5) ulaştıysa uyar
        if len(dizi_kuyrugu) == maksimum_kapasite:
            print(" İzleme listesi çok uzadı! Önce listedekileri bitir.")
        else:
            yeni_dizi = input("Eklenecek dizinin adını yazın: ")
            dizi_kuyrugu.append(yeni_dizi)
            print(f" '{yeni_dizi}' sıranın sonuna eklendi.")
            print(f"Güncel İzleme Sırası: {dizi_kuyrugu}")
            
    elif secim == "2":
        # Listede hiç dizi kalmadıysa uyar
        if (dizi_kuyrugu) == 0:
            print(" İzleyecek dizi kalmadı! Liste bomboş.")
        else:
            # pop(0) sayesinde listenin EN ÖNÜNDEKİ (yani ilk gelen) dizi çıkar
            izlenen_dizi = dizi_kuyrugu.pop(0)
            print(f" Şu an izlenen dizi: {izlenen_dizi} (İlk sıradaydı ve bitti!)")
            print(f"Kalan İzleme Sırası: {dizi_kuyrugu}")
            
    elif secim == "3":
        print("İzleme listesinden çıkıldı. Keyifli seyirler!")
         # while döngüsünü sonlandırır
        
    else:
        print("Geçersiz tuşlama yaptınız, tekrar deneyin.")