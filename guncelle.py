import pandas as pd
import requests

# NASA Earthdata token (MAP_KEY)
token = "774af2fc620e960355a4c57bc9b4b528"

# Türkiye VIIRS verisini indir
url = f"https://firms.modaps.eosdis.nasa.gov/api/country/csv/{token}/viirs-snpp-nrt/TUR/1"
r = requests.get(url)

# Veriyi kaydet
with open("veri.csv", "w", encoding="utf-8") as f:
    f.write(r.text)

# Veriyi oku
df = pd.read_csv("veri.csv")

# Gerekli sütunlar varsa al, yoksa hata ver
istenen_sutunlar = ["latitude", "longitude", "acq_date", "acq_time", "bright_ti4"]
mevcut_sutunlar = df.columns.str.lower().tolist()

# Küçük harfe çevirerek kontrol et (bazı dosyalarda büyük harf olabilir)
if all(sutun in mevcut_sutunlar for sutun in istenen_sutunlar):
    # Sütun adlarını normalize et
    df.columns = [c.lower() for c in df.columns]
    df = df[istenen_sutunlar]
    df.to_json("yanginlar.json", orient="records", indent=2, force_ascii=False)
    print("✅ yanginlar.json başarıyla güncellendi.")
else:
    print("🚫 Gerekli sütunlar eksik! Mevcut sütunlar:", df.columns.tolist())
