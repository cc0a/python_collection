def spam1():  # Inside spam1 we cannot refer to vars y and z

    def spam2():  # Inside spam2 two we can refer to var x

        def spam3():  # Inside spam3 we can refer to vars both x and y
            z = " even more spam"
            z += y
            print("In spam3, locals are {}".format(locals()))
            return z

        y = " more" + x  # y must exist before spam3 is called
        y = " more spam"  # do not combine these assignments
        y += spam3()
        print("In spam2, locals are {}".format(locals()))
        return y

    x = "spam"  # x must exist before spam2 is called
    x += spam2()  # do not combine these assignments
    print("In spam1, locals are {}".format(locals()))
    return x


print(spam1())
print(locals())
print(globals())

