print("输入数字：")
N = int(input())
count = 0
n = N
while n != 0:
    n = (n - 1) & n
    count += 1
print(N, "的二进制形式含有", count, "个 1")
