ip = int(input())

print("Pattern 1")
for i in range(ip):
    for j in range(ip):
        print(f"{i}{j}", end=" ")
    print()

print("\n" + "=" * 40)

print("Pattern 2")
for i in range(ip):
    for j in range(1, ip, 2):
        print(f"{i}{j}", end=" ")
    print()

print("\n" + "=" * 40)

print("Pattern 3")
for i in range(ip):
    for j in range(ip, -1, -1):
        print(f"{i}{j}", end=" ")
    print()

print("\n" + "=" * 40)

print("Pattern 4")
for i in range(ip):
    for j in range(ip):
        print("*", end="")
    print()

print("\n" + "=" * 40)

print("Pattern 5")
for i in range(1, ip + 1):
    for j in range(ip):
        print(i, end="")
    print()

print("\n" + "=" * 40)

print("Pattern 6")
for i in range(ip):
    for j in range(1, ip + 1):
        print(j, end="")
    print()

print("\n" + "=" * 40)

print("Pattern 7")
for i in range(1, ip + 1):
    for j in range(i):
        print(i, end="")
    print()

print("\n" + "=" * 40)

print("Pattern 8")
for i in range(1, ip + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\n" + "=" * 40)

print("Pattern 9")
for i in range(1, ip + 1):
    for j in range(i):
        print("*", end="")
    print()

print("\n" + "=" * 40)

print("Pattern 10")
for i in range(1, ip + 1):
    for j in range(ip - i + 1):
        print(i, end="")
    print()

print("\n" + "=" * 40)

print("Pattern 11")
for i in range(ip, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\n" + "=" * 40)

print("Pattern 12")
for i in range(ip, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print("\n" + "=" * 40)

print("Pattern 13")
for i in range(ip, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

print("\n" + "=" * 40)

print("Pattern 14")
for i in range(1, ip + 1):
    print(" " * (ip - i) + "*" * i)

print("\n" + "=" * 40)

print("Pattern 15")
for i in range(ip, 0, -1):
    print(" " * (ip - i) + "*" * i)

print("\n" + "=" * 40)

print("Pattern 16")
for i in range(1, ip):
    print(" " * (ip - i) + "* " * i)

for i in range(ip, 0, -1):
    print(" " * (ip - i) + "* " * i)

print("\n" + "=" * 40)

print("Pattern 17")
for i in range(1, ip + 1):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()

print("\n" + "=" * 40)

print("Pattern 18")
for i in range(1, ip + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

print("\n" + "=" * 40)


print("Pattern 19")
ch = 65
for i in range(ip):
    for j in range(ip):
        print(chr(ch), end=" ")
        ch += 1
    print()

print("\n" + "=" * 40)

print("Pattern 20")
for i in range(1, ip + 1):
    print("*" * (2 * i - 1))

print("\n" + "=" * 40)

print("Pattern 21")
for i in range(1, ip + 1):
    for j in range(i):
        if i % 2 == 0:
            print("$", end="")
        else:
            print("#", end="")
    print()

print("\n" + "=" * 40)

print("Pattern 22")
for i in range(1, ip + 1):
    for j in range(1, i + 1):
        if j % 2 == 0:
            print("$", end="")
        else:
            print("#", end="")
    print()

print("\n" + "=" * 40)

print("Pattern 23")
for i in range(1, ip + 1):
    for j in range(1, ip + 1):
        if i == 1 or i == ip or j == 1 or j == ip:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\n" + "=" * 40)

print("Pattern 24")
for i in range(1, ip + 1):
    for j in range(1, ip + 1):
        if j == 1 or j == ip or i == j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\n" + "=" * 40)

print("Pattern 25")
for i in range(1, ip + 1):
    for j in range(1, ip + 1):
        if i == j or i + j == ip + 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\n" + "=" * 40)

print("Pattern 26")
for i in range(1, ip + 1):
    for j in range(1, ip + 1):
        if (i == 1 or i == ip or j == 1 or j == ip or
                i == j or i + j == ip + 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()