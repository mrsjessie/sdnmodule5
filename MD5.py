import http.client
import mimetypes
conn = http.client.HTTPSConnection("deckofcardsapi.com")
payload = ''
headers = {
  'Cookie': '__cfduid=d4a82c304b518415294a50a94c0327fad1594056270'
}
conn.request("GET", "/api/deck/new/draw/?count=1&deck_count=1", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))