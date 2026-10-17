import urllib.request, json

url = "https://gutendex.com/books/?search=Webster%27s%20Unabridged%20Dictionary"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req, timeout=12) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        print("Total found:", data.get("count", 0))
        for b in data.get("results", [])[:12]:
            print(f"ID: {b['id']} | Title: {b['title']}")
except Exception as e:
    print("Error:", e)
