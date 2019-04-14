class A:

    def __init__(self, a):
        self.a = a
        
    def add_a(self, b):
        self.z = self.a + b
        return self.z, self.a


aa = A(10)
print(aa.add_a(10))
