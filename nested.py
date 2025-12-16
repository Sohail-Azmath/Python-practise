def f():
    print("inside f")
    def g():
        print("inside g")
    g()

f()
# g()


def f():
    print("inside f")
    def g():
        print("inside g")
        f()
    g()

f()
