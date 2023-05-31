class Employee:
    def __init__(self):
        self.salary=1000
        self.id="1234bvd"
    def deatail(self):
        print(f"id of employee:{self.id}")#inside instance method
obj=Employee()
print(f"salary of employee:{obj.salary}")#outside instance method call
obj.deatail()#method calling