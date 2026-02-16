class Overloading:

    def operations(self,*args):
        print(sum(args))



s1=Overloading()


s1.operations(1,2)
s1.operations(1,2,3,4,5)
