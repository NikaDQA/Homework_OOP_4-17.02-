class EmailAlreadyExistsException(Exception):
    pass


class Employee:
    def __init__(self, name, daily_salary, email=None):
        self.name = name
        self.daily_salary = daily_salary
        self.email = email
        if email is not None:
            self.validate_email(email)
            self.save_email()

    def work(self) -> str:
        return "I come to the office."

    def check_salary(self, days):
        return self.daily_salary * days

    def __str__(self) -> str:
        return f"Employee: {self.name}, Email: {self.email}"

    def __eq__(self, other):
        return self.daily_salary == other.daily_salary

    def __lt__(self, other):
        return self.daily_salary < other.daily_salary

    def save_email(self):
        if self.email is None:
            return
        with open('emails.csv', 'a') as file:
            file.write(f"{self.email}\n")

    def validate_email(self, email):
        if not email:
            raise ValueError("Email address cannot be empty")
        with open('emails.csv', 'r') as file:
            existing_emails = file.readlines()
            existing_emails = [existing_email.strip() for existing_email in existing_emails]
            if email in existing_emails:
                raise EmailAlreadyExistsException("Email already exists")


try:
    employee1 = Employee("Dima", 400, "Dima@example.com")
    print(employee1)
    print("Email saved successfully!")
except EmailAlreadyExistsException as e:
    print(e)

employee2 = Employee("Anton", 300, "Anton@example.com")
print(employee2)
print("Email saved successfully!")

try:
    employee3 = Employee("Dima", 450, "Dima@example.com")
except EmailAlreadyExistsException as e:
    print(e)

try:
    employee4 = Employee("Nika", 200, "")
except ValueError as e:
    print(e)
