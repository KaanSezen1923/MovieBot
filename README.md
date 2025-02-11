# 🎬 MovieBot - Film Öneri Sohbet Botu

**MovieBot**, kullanıcıların tercihlerine göre film önerileri sunan bir AI sohbet botudur. Langflow API ve Streamlit ile entegre edilmiştir.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)

## 🌟 Özellikler
- Doğal dilde film öneri sorguları
- Langflow API entegrasyonu
- Kullanıcı dostu Streamlit arayüzü
- Çevresel değişkenlerle güvenli yapılandırma

## 🛠️ Kurulum
1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/KaanSezen1923/moviebot.git
   cd moviebot
   ```

2. Sanal ortam oluşturun ve bağımlılıkları yükleyin:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   pip install -r requirements.txt
   ```

3. `.env` dosyası oluşturun:
   ```ini
   APPLICATION_TOKEN="langflow_application_token_icin_deger"
   ```

## 🔑 Gereksinimler
- Python 3.9+
- [Langflow](https://langflow.org/) API erişimi
- Geçerli bir `APPLICATION_TOKEN`

## 🚀 Kullanım
1. Streamlit ile uygulamayı başlatın:
   ```bash
   streamlit run app.py
   ```

2. Açılan web arayüzüne film tercihlerinizi yazın:
   ```
   "1980'lerden bilim kurgu filmleri önerir misin?"
   "En iyi romantik komediler hangileri?"
   ```

## 📂 Proje Yapısı
```
moviebot/
├── app.py            # Ana uygulama dosyası
├── .env              # Çevresel değişkenler
├── requirements.txt  # Bağımlılıklar
└── README.md
```

## 🤝 Katkıda Bulunma
1. Fork oluşturun
2. Yeni branch açın: `git checkout -b feature/yeni-özellik`
3. Değişiklikleri commit edin: `git commit -m 'Yeni özellik eklendi'`
4. Push işlemi: `git push origin feature/yeni-özellik`
5. Pull Request oluşturun

## 📜 Lisans
MIT Lisansı - Detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

> **Not:** Langflow API bağlantısı için geçerli bir `APPLICATION_TOKEN` gereklidir. Token almak için [Langflow](https://langflow.org/)'u ziyaret edin.
