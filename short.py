import requests

def shorten_url(long_url):
    if long_url == "":
        return "❌ Error: Please enter a URL"
    
    response = requests.get(f"https://tinyurl.com/api-create.php?url={long_url}")
    
    if response.status_code == 200:
        return response.text
    else:
        return "❌ Error: Could not shorten URL"

long_url = input("Enter the URL: ").strip()
short_url = shorten_url(long_url)

if "❌" in short_url:
    print(short_url)
else:
    print(f"✅ Your short URL is: {short_url}")

    with open("links.txt", "a") as file:
        file.write(short_url + "\n")
    print("📁 Link saved to links.txt!")