import pandas as pd
import requests

# NASA Earthdata token
token = "774af2fc620e960355a4c57bc9b4b528"
url = f"https://firms.modaps.eosdis.nasa.gov/api/country/csv/{token}/viirs-snpp-nrt/TUR/1"

r = requests.get(url)
with open("veri.csv", "w", encoding="utf-8") as f:
    f.write(r.text)

df = pd.read_csv("veri.csv")

# 🔁 İlk 5 sütunu al ve yeniden adlandır (garanti çözüm)
df = df.iloc[:, :5]
df.columns = ["latitude", "longitude", "acq_date", "acq_time", "bright_ti4"]

df.to_json("yanginlar.json", orient="records", indent=2, force_ascii=False)

print("✅ yanginlar.json dosyası güncellendi.")
