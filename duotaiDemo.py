class animal():
    def run(self):
        print("Animal is running")

class cat(animal):
    def run(self):
        print("cat is running")
    def run_two_times(self,animal):
        animal.run()
        animal.run()

oneCat=cat()
oneCat.run()
print(isinstance(oneCat,cat))
print(dir(animal))
