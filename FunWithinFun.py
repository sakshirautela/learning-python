def fun():
    """ fun in fun"""
    s="hello world"
    def fun2():
        print(s)

    fun2()
fun()

def sun(a: int):
    def sun2(b : int):
        return a+b
print(sun(3)(4))
