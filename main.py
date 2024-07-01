import requests
from send_email import send_email

api_key = "c9871065896a4b9088bf2da6b916d4de"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-06-01&sortBy=publishedAt&apiKey=" \
      "c9871065896a4b9088bf2da6b916d4de"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

message_content = ""

# Access the article titles and descriptions
for article in content["articles"]:
    if article["title"] is not None:
        message_content = message_content + f"""
        {article["title"]}
        {article["description"]}
    
    """
message_content = message_content.encode("utf-8")
send_email(message_content)


