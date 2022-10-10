def interpolationLagr(x, mas, f):
    sum = 1
    sum1 = 0
    flag = 0
    for j in range(0, len(mas)):
        for i in range(0, len(mas)):
            if i != j:
                sum *= (x - mas[i]) / (mas[j] - mas[i])

        flag += 1

        sum *= f(mas[j])
        sum1 += sum
        sum = 1



    return sum1
