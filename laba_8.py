FirstArr = []

N = int(input("Введи количество, которое хочешь вводить "))

for i in range(N):
    FirstArr.append(float(input("Введи своё число")))

m = int(input("Введи своё m"))
if 1<=m<=N:
    s = sum(FirstArr[:m])
    maxS = s

    for i in range(m , N):
        s = s - FirstArr[i-m] + FirstArr[i]

        if s > maxS:
            maxS = s

    print(f"Максимальная сумма у тебя будет {maxS}")

else:
    print("введи нормальное m ")


