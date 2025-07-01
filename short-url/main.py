import pyshorteners

long_url = "https://www.google.com/"
short_url = pyshorteners.Shortener().tinyurl.short(long_url)

print(short_url)
