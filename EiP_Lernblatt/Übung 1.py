
def pascalscheDreieck(tiefe):
    dreieck = []
    # Wir holen den Wert von links oben
    for m in range(tiefe):
        for i in range(len(dreieck[m])):
            if i - 1 >= 0:
                links = dreieck[m-1][i-1]
            else:
                links = 0  # Hier ist unsere "vorgestellte" 0! 👻

            # Wir holen den Wert von rechts oben
            if i < len(dreieck[m-1]):
                rechts = dreieck[m-1][i]
            else:
                rechts = 0  # Und hier die zweite 0! 👻

            dreieck[m][i] = links + rechts
    return dreieck
            

tiefe = int(input('Tiefe: '))
print(pascalscheDreieck(tiefe))


# Tiefe: 5
[
    [1],
    [1, 1], 
    [1, 2, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 0, 1]
 ]




















# def pascalscheDreieck(tiefe):
#     pos = 1
#     dreieck = [[1]* i  for i in range(1, tiefe + 1)]
#     for m in range(1, tiefe):
#         for i in range(1, len(dreieck[m-1])):
#             j = i-1
#             summe = dreieck[m-1][i] + dreieck[m-1][j]
#             dreieck[m][i] = summe

#     i = 1   
#     for zeile in dreieck:  
#         print(f"i: {i} = {zeile}")
#         i += 1


