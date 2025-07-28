# stok_takip_sistemi

Basit ama işlevsel bir stok yönetim sistemi. Python ve MSSQL kullanarak ürünlerin takibini sağlamak için geliştirildi.

## Özellikler

- Ürün ekleme
- Ürün silme
- Ürün güncelleme
- Ürün listeleme
- MSSQL veritabanı bağlantısı (pyodbc ile)

## Kullanılan Teknolojiler

- Python 3.10
- MSSQL Server
- pyodbc

## Kurulum ve Kullanım

1. MSSQL Server'da `StokDB` veritabanını oluştur.
2. `Urunler` tablosunu aşağıdaki gibi oluştur:

```sql
CREATE TABLE Urunler (
  UrunID INT PRIMARY KEY IDENTITY(1,1),
  UrunAdi NVARCHAR(100),
  StokAdedi INT,
  Fiyat FLOAT
);

