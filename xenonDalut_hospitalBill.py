class Patient():
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Bill amount must be a number.")
        if value < 0:
            raise ValueError("Bill amount cannot be negative.")
        self._bill_amount = value

    def calculate_bill(self):
        return self.bill_amount

class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        discount = 0.2
        discounted_amount = self.bill_amount * (1 - discount)
        return discounted_amount

class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        discount = 0.15
        discounted_amount = self.bill_amount * (1 - discount)
        return discounted_amount

regular_patient = Patient("Khiane Lanz", 10000)
senior_patient = SeniorPatient("Senior Lanz", 10000)
philhealth_patient = PhilHealthPatient("PhilHealth Lanz", 10000)

print("Hospital Billing System\n--------------------")
print(f"Patient Name: {regular_patient.name}\nOriginal Bill Amount: {regular_patient.bill_amount}, Final Bill Amount: {regular_patient.calculate_bill()}")
print(f"Patient Name: {senior_patient.name}\nOriginal Bill Amount: {senior_patient.bill_amount}, Final Bill Amount: {senior_patient.calculate_bill()}")
print(f"Patient Name: {philhealth_patient.name}\nOriginal Bill Amount: {philhealth_patient.bill_amount}, Final Bill Amount: {philhealth_patient.calculate_bill()}")