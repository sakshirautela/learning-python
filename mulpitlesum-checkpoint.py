def fun(*argv):
    sum=0
    for i in argv:
        sum+=i
    return sum
print(fun(34,45,55,66))

def fun(**kwargs):
    for key, val in kwargs.items():
        print(key, val)

fun(first='sakshi',last='rautela')