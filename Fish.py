class Fish():
    def __init__(self,location,fins=True):
        self.location=location
        self.fins=fins
    def swim(self):
        print(f'The Fish can swim now')
rohu=Fish('River')

print(rohu.location)
print(rohu.fins)
rohu.swim()

'''class Fish():
    def __init__(self,location,fins=True):
        print(self.location=location)
        self.fins=fins'''