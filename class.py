class employee:
    def __init__(self, name, idno):
        self.name=name
        self.idno=idno
    def show(self):
        return f"name: {self.name}, id number {self.idno}"
class manager(employee):
    def __init__(self, name, idno, depart):
        super().__init__(name, idno)
        self.depart = depart
    def show(self):
        return super().show() + f"manager of {self.depart}"
class intern(employee):
    def __init__(self, name, idno, period):
        super().__init__(name, idno)
        self.period = period
    def show(self):
        return super().show() + f"is here for {self.period} months"
    
employees=[
    manager("James nandi", 2745365, "finance"),
    intern("George Njoroge", 3790876, 6)
]
for emp in employees:
    print(emp.show())