word = input("File?: ").casefold().strip()

if word.endswith(".gif"):
    print("image/gif")
elif word.endswith(".jpeg") or word.endswith(".jpg"):
    print("image/jpeg")
elif word.endswith(".png"):
    print("image.png")
elif word.endswith(".pdf"):
    print("document.pdf")
elif word.endswith(".txt"):
    print("text/plain")
elif word.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")

