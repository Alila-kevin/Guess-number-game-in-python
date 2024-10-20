class student:
    def __init__(self):
        self.name = "James Ngali"
        self.adm = "T5457U"
        self.idno = 3456890
        self.year =2019
        self.lap = self.laptop()
    
    def show(self):
        print(self.name, self.adm, self.idno, self.year)
        self.lap.show()
    
    class laptop:
        def __init__(self):
            self.ram ='8 GB'
            self.cpu ='i5'
            self.brand ='HP/DELL/Lenevo'
        def show(self):
            print(self.ram, self.cpu, self.brand)
class almin(student):
    def __init__(self, name, adm, idno, year):
        super().__init__(name, adm, idno, year)
        self.fy = 2024
    def show(self):
        print(self.fy)
        return self.super().show()           

#s1=student("Trend anode", "35343R", 53535353, 2019)
a1=almin
a1.show()