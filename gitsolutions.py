'''
def gcd(a,b):
    if a>b:
        if(a%b==0):
            print('gcd=',b)
        else:
            c=a%b
            return gcd(b,c)
    elif b>a:
        if(b%a==0):
            print('gcd=',a)
        else:
            c = b % a
            return gcd(a,c)
    else:
        print('gcd=',a)
gcd(14,9)

def is_power(a,b):
    if a%b==0:
        c=a/b
        i=0
        d=b
        while i<c:
            if c>d:
                d=b*d
                if c==d:
                    return True
                    break
            else:
                return False
                break
            i=i+1
    else:
        return False
a=is_power(8,3)
print(a)

def factI(n):
    fac=1
    for i in range(1,n+1):
        fac=fac*i
    return fac
def factR(n):
    result=1
    if n==0:
        return 1
    elif n<0:
        return False

    elif n>0:
       result=n*factR(n-1)

    return result

a=factR(0)
print(a)

binary = input()
decimal = 0
l = len(binary)


for x in binary:
    l = l - 1
    decimal += pow(2, l) * int(x)

print(decimal)

def sumDigit(n):
    try:
        if any(char.isdigit() for char in n):

            return True
        else:
            raise ValueError
    except:
        return False
a=sumDigit('hdddrdtr')
print(a)

def findAnEven(l):
    count=0
    try:
        for i in range(0,len(l)):
            if l[i]%2==0:
                return l[i]
                count=1
        if count == 0:
            raise ValueError
    except ValueError:
        print("no even value")

result=findAnEven([1,3,7])
print(result)

def isPalindrome(s):
    ls=list(s)
    bs=ls[::-1]
    print(bs)
    b="".join(bs)
    if(s==b):
        return True
    else:
        return False
a=isPalindrome('abab')
print(a)



def eval_loop():
    i = 1
    while i > 0:

        n = input()
        if n == 'done':
            i=0
            break
        else:
            out = eval(n)
        print(out)
a = eval_loop()
print(a)



def newtonsq(a):
    x=int(input('assume nearby no'))
    y=(x+a/x)/2
    print(y)
ans=newtonsq(16)
print(ans)

'''