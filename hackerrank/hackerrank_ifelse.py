n=int(input())
if n%2!=0:
    print("weird")
elif n%2==0 and n in range(2,5):
    print("not weird")
elif n%2==0 and n in range(6,20):
    print("weird")
elif n%2==0 and n in range(20,100):
    print("not weird")