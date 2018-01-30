n=int(input("enter the number"))
rev=0;
temp=n;
while(temp>0):
    rev=rev*10
    rev=rev+temp%10
    temp=temp//10
    if (rev==n):
        print(n,"is palindrome")
    else:
            print(n,"is not palindrome")
