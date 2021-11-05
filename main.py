import pyshorteners

link = input("Вставьте ссылку : ")

shortener = pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print(x)