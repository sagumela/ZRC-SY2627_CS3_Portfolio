

class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_bill_amount(self):
        return self.bill_amount

    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount

    def calculate_bill(self):
        return self.bill_amount



class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.bill_amount * 0.8



class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.bill_amount * 0.85


regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)

patients = [regular_patient, senior_patient, philhealth_patient]


for patient in patients:
    print(f"Patient Name: {patient.get_name()}")
    print(f"Original Bill Amount: {patient.get_bill_amount()}")
    print(f"Bill Amount: {patient.calculate_bill()}")
    print()
