N=int(input("Количество моменты времени в общем и целом: "))
S = []
D = []

print("Введите массив спроса: ")
for i in range(N):
    S.append(int(input()))

print("Введите массив предложения: ")
for i in range(N):
    D.append(int(input()))

c = 0

for i in range(N):
    if S[i] == D[i]:
        c += 1

print("Количество моментов времени, когда рынок находился в равновесии: ", c)