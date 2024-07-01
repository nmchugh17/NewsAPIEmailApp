import requests
from send_email import send_email

topic = "tesla"
api_key = "c9871065896a4b9088bf2da6b916d4de"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-06-01&" \
      "sortBy=publishedAt&" \
      "apiKey=c9871065896a4b9088bf2da6b916d4de&" \
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

message_content = "Subject: Today's news" + "\n"

# Access the article titles and descriptions
for article in content["articles"][:20]:
    if article["title"] is not None:
        message_content = message_content + article["title"] + "\n" \
                          + article["description"] \
                          + "\n" + article["url"] + 2*"\n"

message_content = message_content.encode("utf-8")
send_email(message_content)


