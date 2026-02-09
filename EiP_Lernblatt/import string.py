import string as s

text = 'ein Test, ein Test! ein Beispiel'

sonderzeichen = s.punctuation
zahlen = s.digits

for symbol in sonderzeichen:
    text = text.replace(symbol, "")

for zahl in zahlen:
    text = text.replace(zahl, "")

text_lst = text.lower().split()

print(f"text_lst: {text_lst}")



wörter_einmalig = set(text_lst) #das ist nur damit wir jedes Wort einmal haben ! Somit können wir einfacher die Häufigkeit berechnen
print(f"wörter_einmalig: {wörter_einmalig}")


wort_häufigkeit = {}
for wort in wörter_einmalig:
    häufigkeit = text.count(text)
    wort_häufigkeit[wort] = häufigkeit
print(f"wort_häufigkeit: {wort_häufigkeit}")



gruppe = {}
for wort in text_lst:
    if len(wort) not in gruppe:
        gruppe[len(wort)] = [wort]
    else: 
        gruppe[len(wort)].append(wort)


print(f"gruppe: {gruppe}")

