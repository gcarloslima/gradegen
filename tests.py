for h in range(0, 20):
    for i in range(0, 5):
        print('-')
        for j in range(0, 4 - i):
            print(f"{i * 20 + (j * 20) + h} - {i * 20 + ((j + 1) * 20) + h}")