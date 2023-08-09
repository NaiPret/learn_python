ga = 1
while (ga <= 36):
    cho = 1
    while (cho <= 36):
        if ((ga + cho == 36) and (2 * ga + 4 * cho == 100)):
            print("Số gà của bài toán là:", ga)
            print("Số chó của bài toán là:", cho)
            break
        cho += 1
    ga += 1
