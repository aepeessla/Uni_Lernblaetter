text = str(input("text: "))
text = text.split()
print(text)

und = ["und", '&']

for i in range(len(text)):
    if '\\' in text[i] :
        text[i] = f'${text[i]}$'
    if text[i] in und[0]:
        text[i] = und[1]
    
text = " ".join(text)
print(text)