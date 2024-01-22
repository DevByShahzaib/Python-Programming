import os

class Finder:
    def scan(self,path):
        for entry in os.scandir(path):
            if entry.is_file():
                if entry.name.endswith(".txt"):
                    print(entry.name)
            else:
                    self.scan(entry)
fin = Finder()
fin.scan('C:\Users\Dell Latitude E6440\Desktop\python from chapter#07')