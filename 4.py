class EmailAlreadyExistsException(Exception):
    pass


class Employee:

    def __init__(self, name, daily_salary, email=None):
        self.name = name
        self.daily_salary = daily_salary
        self.email = email
        if email is not None:
            self.save_email()

    def work(self) -> str:
        return "I come to the office."

    def __str__(self) -> str:
        return f"Employee: {self.name}, Email: {self.email}"

    def __lt__(self, other):
        return self.daily_salary < other.daily_salary

    def __gt__(self, other):
        return self.daily_salary > other.daily_salary

    def __eq__(self, other):
        return self.daily_salary == other.daily_salary

    def check_salary(self, days):
        return self.daily_salary * days

    def save_email(self):
        if self.email is None:
            return
        with open("emails.csv", "w") as file:
            file.write(f"{self.email}")

    def validate_email(self, email):
        if not email:
            raise ValueError("Email address cannot be empty")
        with open('emails.csv', 'r') as file:
            existing_emails = file.readlines()
            if email in existing_emails:
                raise EmailAlreadyExistsException("Email already exists")


class Recruiter(Employee):
    def work(self) -> str:
        return "I come to the office and start to hiring."

    def __str__(self) -> str:
        return f"Recruiter: {self.name}"


class Developer(Employee):

    def __init__(self, name, daily_salary, tech_stack):
        super().__init__(name, daily_salary)
        self.tech_stack = tech_stack

    def work(self) -> str:
        return "I come to the office and start to coding."

    def __str__(self) -> str:
        return f"Developer: {self.name}, Daily Salary: {self.daily_salary}, Tech Stack: {self.tech_stack}"

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __add__(self, other):
        name = self.name + ' ' + other.name
        tech_stack = list(set(self.tech_stack + other.tech_stack))
        daily_salary = max(self.daily_salary, other.daily_salary)
        return Developer(name, daily_salary, tech_stack)


try:
    employee1 = Employee("Dima", 400, "dima@gmail.com")
    print(employee1)
    employee1.save_email()
    print("Email saved successfully!")
except EmailAlreadyExistsException as e:
    print(e)

employee2 = Employee("Anton", 350, "Anton@gmail.com")
print(employee2)
employee2.save_email()
print("Email saved successfully!")

try:
    employee3 = Employee("Nika", 150, "dima@gmail.com")
except EmailAlreadyExistsException as e:
    print(e)

try:
    employee4 = Employee("Eva", 200, "")
except ValueError as e:
    print(e)
