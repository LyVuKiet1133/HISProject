from datetime import datetime


class Patient():
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    @classmethod
    def random_patient(cls):
        current_time = datetime.now()
        first_name = "LVK"
        last_name = current_time.strftime("%d%m%Y%H")
        address = "Suối Tre"
        return cls(first_name, last_name, address)


if __name__ == "__main__":
    patient = Patient.random_patient()
    print(patient.first_name + patient.last_name + patient.address)
