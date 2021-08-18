# pastecord
Api wrapper for pastecord.com

# usage
Create a new pastecord document:
```py
from pastecord import create_document

document = create_document('print("Hello World!")')
print(document)
# Document('wivewoniki')
print(document.url)
# https://pastecord.com/wivewoniki
print(document.read())
# print("Hello World!")
```
Save a pastecord document:
```py
from pastecord import Document

d = Document('https://pastecord.com/wivewoniki')
d.save('document.txt')
```