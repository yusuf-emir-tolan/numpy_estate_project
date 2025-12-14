*AI-Powered Real Estate Analysis System / Yapay Zeka Destekli Emlak Analizi*

**Language / Dil:**
[🇺🇸 English](#-english) | [🇹🇷 Türkçe](#-türkçe)

---
🇺🇸 English

Project Overview
This project is a data analysis simulation developed using **Python** and **NumPy**. It generates and analyzes 1,000 synthetic real estate records using **vectorized operations** (without any `for` loops) to ensure high performance.

Key Features
* **Data Generation:** Randomly generated data for m², number of rooms, and district codes using `np.random`.
* **Price Algorithm:** A custom logic calculates house prices based on features using matrix operations.
* **Statistical Analysis:** Calculates Mean, Median, and Standard Deviation to understand market trends.
* **Smart Filtering:** Uses **Boolean Masking** to identify "Opportunity Houses" (houses in the city center with a price below the average).

Tech Stack
* **Python 3.x**
* **NumPy** (Data Manipulation, Statistics, Filtering)

How to Run
1.  Clone the repository.
2.  Install the required library:
    ```bash
    pip install numpy
    ```
3.  Run the script:
    ```bash
    python emlak_projesi.py
     ```

---

🇹🇷 Türkçe

Proje Hakkında
Bu proje, **Python** ve **NumPy** kütüphanesi kullanılarak geliştirilmiş sanal bir veri analizi simülasyonudur. For döngüleri kullanılmadan, tamamen **vektörel işlemlerle** (Vectorization) 1000 adet emlak verisi üretilip analiz edilmiştir.

Neler Yapıldı?
* **Veri Üretimi:** 1000 adet evin m², oda sayısı ve semt bilgileri `np.random` ile rastgele üretildi.
* **Fiyat Algoritması:** Her evin fiyatı; metrekare, oda sayısı ve semt çarpanlarına göre matematiksel formülle hesaplandı.
* **İstatistiksel Analiz:** Pazar durumunu anlamak için Ortalama, Medyan ve Standart Sapma hesaplandı.
* **Akıllı Filtreleme:** NumPy **Maskeleme (Boolean Indexing)** yöntemi kullanılarak "Merkezde bulunan ve Ortalamanın altında fiyata sahip" kelepir evler tespit edildi.

Kullanılan Teknolojiler
* **Python 3.x**
* **NumPy** (Veri Üretimi, Manipülasyon, İstatistik)

Nasıl Çalıştırılır?
1.  Projeyi indirin.
2.  Gerekli kütüphaneyi yükleyin:
    ```bash
    pip install numpy
    ```
3.  Kodu çalıştırın:
    ```bash
    python emlak_projesi.py
    ```

---
*Developed for self-improvement as part of the Python & AI Bootcamp / Python & AI Bootcamp kapsamında kendimi geliştirmek için geliştirilmiştir.*


