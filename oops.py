class Employee:
    company = "google"

    def getsalary(self):
        print(f"Salary for this employee working in {self.salary}")

    def __init__(self, name, branch, rollNo, salary):
        self.name = name
        self.branch = branch
        self.rollNo = rollNo
        self.salary = salary
        print(
            f"My name is {self.name}\nBranch : {self.branch}\nRollNo : {self.rollNo}")

    @staticmethod
    def office(amt):
        print(f"Office pays you : {amt}")


obj = Employee("parshant", "CSE", 2101140, 50000)
obj.getsalary()
obj.office(10000)
