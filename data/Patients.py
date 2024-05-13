from datetime import datetime


class Patient():
    def __init__(self, **kwargs):
        self.patientId = None
        self.first_name = None
        self.last_name = None
        self.address = None
        self.sdt = None
        self.dob = None
        self.srcFullName = None
        self.district = None
        self.ward = None
        self.ethnic = None
        self.nationality = None
        self.occupation = None
        self.insCardNo = None
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def random_patient(cls):
        current_time = datetime.now()
        first_name = current_time.strftime("%d%m%Y%H%M%S")
        last_name = "LVK"
        address = "Suối Tre"
        return cls(first_name=first_name, last_name=last_name, address=address)


if __name__ == "__main__":
    patient = Patient.random_patient()
    print(patient.first_name + patient.last_name + patient.address + patient.sdt)
