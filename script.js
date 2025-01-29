// 解析 URL 查詢參數
const urlParams = new URLSearchParams(window.location.search);

// 取得並解碼用戶資料
const name = decodeURIComponent(urlParams.get('name') || '訪客');
const age = decodeURIComponent(urlParams.get('age') || '未知');
const constellation = decodeURIComponent(urlParams.get('constellation') || '未知');
const location = decodeURIComponent(urlParams.get('location') || '未知');

// 顯示用戶資料
document.getElementById('userName').textContent = name;
document.getElementById('userAge').textContent = age;
document.getElementById('userConstellation').textContent = constellation;
document.getElementById('userLocation').textContent = location;

// 假資料模擬（可根據星座及地點填寫）
const weatherData = {
  "台北市": { status: "晴天", temperature: "25°C" },
  "高雄市": { status: "多雲", temperature: "28°C" },
  "台中市": { status: "陰天", temperature: "24°C" }
};

const horoscopeData = {
  "白羊座": { luckyColor: "紅色", message: "今天適合積極行動，機會在你手中。" },
  "金牛座": { luckyColor: "綠色", message: "穩健是今天的關鍵字，保持冷靜。" },
  "雙魚座": { luckyColor: "藍色", message: "保持開放心態，會有驚喜的發展！" }
};

const outfitSuggestions = {
  "紅色": "紅色上衣搭配牛仔褲，增強行動力。",
  "綠色": "穿著綠色系衣物，適合休閒與放鬆。",
  "藍色": "藍色襯衫搭配卡其褲，展現優雅氣質。"
};

// 設定天氣資訊
const weather = weatherData[location] || { status: "未知", temperature: "N/A" };
document.getElementById('weatherLocation').textContent = location;
document.getElementById('weatherStatus').textContent = weather.status;
document.getElementById('temperature').textContent = weather.temperature;

// 設定星座運勢
const horoscope = horoscopeData[constellation] || { luckyColor: "黑色", message: "今天要保持耐心，靜觀其變。" };
document.getElementById('luckyColor').textContent = horoscope.luckyColor;
document.getElementById('horoscopeMessage').textContent = horoscope.message;

// 設定服裝搭配
document.getElementById('outfitSuggestion').textContent = outfitSuggestions[horoscope.luckyColor] || "穿著舒適，保持自信！";
