n = int(input("Sonlarni kiriting: "))
juft_sonlar = []
for i in range(1, n + 1):
    son = int(input(f"{i}-sonni kiriting: "))
    if son % 2 == 0:
        juft_sonlar.append(son)
print("Juft sonlar:")
for juft_son in juft_sonlar:
    print(juft_son)