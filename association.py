class Doctor:
  def __init__(self, name: str, field: str):
    self.name = name
    self.field = field


class Patient:
  def __init__(self, name: str):
    self.name = name
    self.doctors = []

  def consult(self, doctor: Doctor):
    self.doctors.append(doctor)


doctor_smith = Doctor("Dr. Smith", "Cardiology")
doctor_jones = Doctor("Dr. Jones", "Neurology")

patient_alice = Patient("Alice")
patient_bob = Patient("Bob")

patient_alice.consult(doctor_smith)
patient_alice.consult(doctor_jones)
patient_bob.consult(doctor_smith)

print(patient_alice.name)
for doc in patient_alice.doctors:
  print(doc.name)
