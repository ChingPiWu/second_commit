import requests
import pandas as pd

# 取得天氣預報的 JSON 資料
url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-71FAB6CC-5683-4756-828C-3D18328A4195&locationName=&elementName="
response = requests.get(url)

# 檢查請求是否成功
if response.status_code == 200:
    data_json = response.json()  # 轉換成 JSON 格式

    # 確認 JSON 結構
    if "records" in data_json and "location" in data_json["records"]:
        location_data = data_json["records"]["location"]
        
        weather_data = []  # 用來存放所有縣市的天氣資訊
        
        for location in location_data:
            city = location["locationName"]  # 縣市名稱
            wx8 = location["weatherElement"][0]["time"][0]["parameter"]["parameterName"]  # 天氣現象
            maxt8 = location["weatherElement"][1]["time"][0]["parameter"]["parameterName"]  # 最高溫
            mint8 = location["weatherElement"][2]["time"][0]["parameter"]["parameterName"]  # 最低溫
            ci8 = location["weatherElement"][3]["time"][0]["parameter"]["parameterName"]  # 舒適度
            pop8 = location["weatherElement"][4]["time"][0]["parameter"]["parameterName"]  # 降雨機率

            # 儲存到列表
            weather_data.append({
                "縣市": city,
                "天氣現象": wx8,
                # "最高溫(°C)": maxt8,
                # "最低溫(°C)": mint8,
                "舒適度": ci8,
                "降雨機率(%)": "降雨機率"+pop8+"%",
            })

        # 轉為 DataFrame
        df = pd.DataFrame(weather_data)

        # 存成 CSV 檔案
        df.to_csv("weather.csv", index=False, encoding="utf-8-sig")

        print("✅ 已成功爬取並儲存天氣預報到 weather.csv！")
    else:
        print("❌ JSON 結構不符合預期")
else:
    print(f"❌ 無法獲取天氣數據，HTTP 狀態碼: {response.status_code}")
