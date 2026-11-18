class RegularPatient:
    def __init__(self, PatientName, Originalbill, FinalBill):
        self._PatientName = PatientName
        self._Originalbill = Originalbill
        self._FinalBill = FinalBill

    @property
    def PatientName(self):
        return f"{self._PatientName}"

    @property
    def Originalbill(self):
        return f"{self._Originalbill:.2f}"

    @property
    def FinalBill(self):
        return f"{self._FinalBill:.2f}"
    
    @FinalBill.setter
    def FinalBill(self, new_finalbill):
        if new_finalbill == 0:
            self._FinalBill = self._Originalbill * .20

regular_patient = RegularPatient("Juan Dela Cruz", 15000.00, 15000.00)

FinalBill = regular_patient.FinalBill

print("---Hospital Billing System---")
print("Patient Name:", regular_patient.PatientName) 
print("Patient Type: Regular Patient")
print("Original Bill: ₱", regular_patient.Originalbill)
print("Final Bill:₱", regular_patient.FinalBill)



class SeniorPatient:
    def __init__(self, PatientName, Originalbill, FinalBill):
        self._PatientName = PatientName
        self._Originalbill = Originalbill
        self._FinalBill = FinalBill

    @property
    def PatientName(self):
        return f"{self._PatientName}"

    @property
    def Originalbill(self):
        return f"{self._Originalbill:.2f}"

    @property
    def FinalBill(self):
        return f"{self._FinalBill:.2f}"
    
    @FinalBill.setter
    def FinalBill(self, new_finalbill):
        if new_finalbill == 0:
            self._FinalBill = self._Originalbill - 3000

senior_patient = SeniorPatient("Mario Santos", 15000.00, 12000.00) 

final_bill = senior_patient.FinalBill

print("Patient Name:", senior_patient.PatientName) 
print("Patient Type: Senior Patient")
print("Original Bill:₱", senior_patient.Originalbill)
print("Final Bill: ₱", senior_patient.FinalBill)




class PhilHealthPatient:
    def __init__(self, PatientName, Originalbill, FinalBill):
        self._PatientName = PatientName
        self._Originalbill = Originalbill
        self._FinalBill = FinalBill

    @property
    def PatientName(self):
        return f"{self._PatientName}"

    @property
    def Originalbill(self):
        return f"{self._Originalbill:.2f}"

    @property
    def FinalBill(self):
        return f"{self._FinalBill:.2f}"
    
    @FinalBill.setter
    def FinalBill(self, new_finalbill):
        if new_finalbill == 0:
            self._FinalBill = self._Originalbill - 2250

phil_health_patient = PhilHealthPatient("Pedro Reyes", 15000.00, 12750.00)

final_bill = phil_health_patient.FinalBill

print("Patient Name:", phil_health_patient.PatientName) 
print("Patient Type: PhilHealth Patient")
print("Original Bill: ₱", phil_health_patient.Originalbill)
print("Final Bill: ₱", phil_health_patient.FinalBill)


                                  


                                  


                                  