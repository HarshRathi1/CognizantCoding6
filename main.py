r1=int(input())
r2=int(input())
if r1>=r2 or r1<=0 or r2<=0:
   print("Provide valid input")
else:
      for i in range(r1, r2 + 1):
         for j in range(2, (i // 2)+1):
            if i % j == 0:
               break
         else:
            print(i)