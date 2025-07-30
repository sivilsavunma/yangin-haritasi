import pandas as pd
import requests

# NASA Earthdata token (MAP_KEY)
token = "eyJ0eXAiOiJKV1QiLCJvcmlnaW4iOiJFYXJ0aGRhdGEgTG9naW4iLCJzaWciOiJlZGxqd3RwdWJrZXlfb3BzIiwiYWxnIjoiUlMyNTYifQ.eyJ0eXBlIjoiVXNlciIsInVpZCI6InNpdmlsc2F2dW5tYSIsImV4cCI6MTc1OTA2MTcyMiwiaWF0IjoxNzUzODc3NzIyLCJpc3MiOiJodHRwczovL3Vycy5lYXJ0aGRhdGEubmFzYS5nb3YiLCJpZGVudGl0eV9wcm92aWRlciI6ImVkbF9vcHMiLCJhY3IiOiJlZGwiLCJhc3N1cmFuY2VfbGV2ZWwiOjN9.CDYzPNnc_puHBW7PnVrDx9ucMgv2vqcZ_91fU_wP0UJ4OOdAjA3gjuPD9MZrOXLfhVOenu2VfJvTzEt9NQyICYoa6NMGW78eibzVYVQda3N3gGAPJHLhSyZxhVX_79N0gdOXl3QLVNGjUsYHaAzly6urqQRHlm2yG6tJ5vojiczNZVc-osJHVndRw22FYOLVwlKerOixG9gUGW5-xzyudlwICT6I3qGNy7CWmO5GJmzmN7qZYZ3kxmvKqe9FfNqe4H_gNVmiy8FsHbTMe3ZzEozOrNbbWsF3K-KWMIXLB0RwMF_D_lQ8DN2F24-fea6YHDYCqcvWTzlj9TV7X4IBaA"  # Örn: AAAAAA-XXXX-BBB-CCC-123456

url = f"https://firms.modaps.eosdis.nasa.gov/api/country/csv/{token}/viirs-snpp-nrt/TUR/1"
r = requests.get(url)

with open("veri.csv", "w", encoding="utf-8") as f:
    f.write(r.text)

df = pd.read_csv("veri.csv")
df = df[["latitude", "longitude", "acq_date", "acq_time", "brightness"]]
df.to_json("yanginlar.json", orient="records", indent=2, force_ascii=False)

print("✅ yanginlar.json dosyası güncellendi.")
