from urllib.parse import quote_plus

def google_link(kereses: str) -> str:
    kodolt = quote_plus(kereses)
    return f"https://www.google.com/search?q={kodolt}"

szoveg = input("Kérdezz bármit: ")
link = google_link(szoveg)

print("Generált link:")
print(link)
