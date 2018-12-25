import base64

with open("lake copy.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print str
