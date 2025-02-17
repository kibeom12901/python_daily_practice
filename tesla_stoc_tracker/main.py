import requests
import yfinance as yf

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "44d73a8697264dc59847e82bddf6d6cc"

tesla = yf.Ticker(STOCK_NAME)
hist = tesla.history(period="5d") 

if len(hist) < 3:
    print("Not enough data to calculate percentage change.")
    exit()

print(hist)


yesterday_close = hist['Close'].iloc[-2]
day_before_yesterday_close = hist['Close'].iloc[-3]

price_difference = abs(yesterday_close - day_before_yesterday_close)

percentage_difference = (price_difference / day_before_yesterday_close) * 100
print(f"📈 Tesla Stock Change: {percentage_difference:.2f}%")

if percentage_difference > 5:
    print("🚀 Get News!")
    news_params = {
            "apiKey": NEWS_API_KEY,
            "q": COMPANY_NAME,
            "searchIn": "title,description",
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 3
        }

    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    news_data = response.json()

    articles = news_data.get("articles", [])[:3]  

    messages = [
        f"TSLA: {'🔺' if yesterday_close > day_before_yesterday_close else '🔻'}{percentage_difference:.2f}%\n"
        f"Headline: {article['title']}\n"
        f"Brief: {article['description']}\n"
        f"Read more: {article['url']}"
        for article in articles
    ]

for message in messages:
    print(message)

