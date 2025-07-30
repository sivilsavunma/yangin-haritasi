import pandas as pd
import requests

# NASA Earthdata token (MAP_KEY)
token = "BURAYA_KENDİ_TOKENİNİ_YAZ"  # Örn: AAAAAA-XXXX-BBB-CCC-123456

url = f"https://firms.modaps.eosdis.nasa.gov/api/country/csv/{token}/viirs-snpp-nrt/TUR/1"
r = requests.get(url)

with open("veri.csv", "w", encoding="utf-8") as f:
    f.write(r.text)

df = pd.read_csv("veri.csv")
df = df[["latitude", "longitude", "acq_date", "acq_time", "brightness"]]
df.to_json("yanginlar.json", orient="records", indent=2, force_ascii=False)

print("✅ yanginlar.json dosyası güncellendi.")
