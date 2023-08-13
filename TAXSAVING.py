# cook your dish here
T = int(input())
for i in range(T):
    X,Y = map(int,input().split(" "))
    if X>Y:
        res = X-Y
        print(res)
    else:
        print("0")