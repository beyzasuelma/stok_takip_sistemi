import pyodbc

# MSSQL bağlantısı
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=BEYZASU\\SQLEXPRESS;"
    "Database=StokDB;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

# Ürün ekleme
def urun_ekle(urun_adi, stok_adedi, fiyat):
    sorgu = "INSERT INTO Urunler (UrunAdi, StokAdedi, Fiyat) VALUES (?, ?, ?)"
    cursor.execute(sorgu, (urun_adi, stok_adedi, fiyat))
    conn.commit()
    print(f"{urun_adi} başarıyla eklendi!")

# Ürün listeleme
def urun_listele():
    sorgu = "SELECT * FROM Urunler"
    cursor.execute(sorgu)
    urunler = cursor.fetchall()
    print("\n--- Ürün Listesi ---")
    for urun in urunler:
        print(f"ID: {urun.UrunID} | Ad: {urun.UrunAdi} | Stok: {urun.StokAdedi} | Fiyat: {urun.Fiyat}₺")

# Ürün silme
def urun_sil(urun_id):
    sorgu = "DELETE FROM Urunler WHERE UrunID = ?"
    cursor.execute(sorgu, (urun_id,))
    conn.commit()
    print(f"ID {urun_id} olan ürün silindi.")

# Ürün güncelleme
def urun_guncelle(urun_id, yeni_ad, yeni_stok, yeni_fiyat):
    sorgu = "UPDATE Urunler SET UrunAdi = ?, StokAdedi = ?, Fiyat = ? WHERE UrunID = ?"
    cursor.execute(sorgu, (yeni_ad, yeni_stok, yeni_fiyat, urun_id))
    conn.commit()
    print(f"ID {urun_id} olan ürün güncellendi.")

# Ana çalıştırma bloğu
if __name__ == "__main__":
    # Test örnekleri (dilersen yorum satırlarını kaldırıp deneyebilirsin)
    # urun_ekle("Şampuan", 50, 29.90)
    # urun_ekle("Saç Spreyi", 40, 89.50)
    # urun_ekle("El Kremi", 60, 22.75)

    # urun_listele()
    # urun_sil(1)
    # urun_guncelle(2, "Yeni Şampuan", 100, 39.90)

    conn.close()
