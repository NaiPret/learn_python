for ga in range(1, 36):
    for cho in range(1, 36):
        if ((ga + cho == 36) and (2 * ga + 4 * cho == 100)):
            print("Số gà của bài toán là:", ga)
            print("Số chó của bài toán là:", cho)
            break
