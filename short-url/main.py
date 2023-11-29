import pyshorteners

long_url = "https://www.google.com/"
tyni_url = pyshorteners.Shortener().tinyurl.short(long_url)

print(tyni_url)