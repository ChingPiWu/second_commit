import requests
from bs4 import BeautifulSoup
import pandas as pd

# 12 星座對應網址
base_url = "https://www.elle.com/tw/starsigns/"
zodiac_signs = {
    "處女座": "virgo-today/",
    "牡羊座": "aries-today/",
    "金牛座": "taurus-today/",
    "雙子座": "gemini-today/",
    "巨蟹座": "cancer-today/",
    "獅子座": "leo-today/",
    "天秤座": "libra-today/",
    "天蠍座": "scorpio-today/",
    "射手座": "sagittarius-today/",
    "摩羯座": "capricorn-today/",
    "水瓶座": "aquarius-today/",
    "雙魚座": "pisces-today/",
}

# 儲存所有星座的結果
zodiac_data = []

for sign, path in zodiac_signs.items():
    url = base_url + path
    response = requests.get(url)

    if response.status_code != 200:
        print(f"❌ 無法獲取 {sign} 的運勢，狀態碼: {response.status_code}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    topic_elements = soup.find_all("div", class_="article-body-content article-body standard-body-content css-1rvjbpv et2g3wt6")

    for topic_element in topic_elements:
        statements = topic_element.find_all('ul', class_="css-18lcivh emevuu60")
        for statement in statements:
            # 依句號分割，讓短評逐行儲存
            sentences = statement.text.split("開運方位")[0].split(" ")
            for sentence in sentences:
                if sentence.strip():  # 避免空白行
                    zodiac_data.append({"星座": sign, "短評": sentence.strip() + "。"})  # 重新加上句號

# 轉為 DataFrame
df = pd.DataFrame(zodiac_data)

# 儲存成 CSV 檔案
df.to_csv("horoscope.csv", index=False, encoding="utf-8-sig")

print("✅ 已成功爬取並儲存 12 星座的運勢到 horoscope.csv！")
