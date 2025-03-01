class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

class Manager(Employee):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department
        
class Developer(Manager):
    def __init__(self, name, age, employee_id, department, programming_languages):
        super().__init__(name, age, employee_id, department)
        self.programming_languages = programming_languages
        
class QA_Engineer(Manager):
    def __init__(self, name, age, employee_id, department, testing_tools):
        super().__init__(name, age, employee_id, department)
        self.testing_tools = testing_tools

class Project_Manager(Manager):
    def __init__(self, name, age, employee_id, department, project_name):
        super().__init__(name, age, employee_id, department)
        self.project_name = project_name

class Team_Lead(Manager):
    def __init__(self, name, age, employee_id, department, team_members):
        super().__init__(name, age, employee_id, department)
        self.team_members = team_members
        
        
        
        
# classes for hospital management system
class Hospital:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
class Patient(Hospital):
    def __init__(self, name, age, contact_number, address, medical_history, doctor_name, room_number, bed_number, ward, admission_date, discharge_date, diagnosis, treatment):
        self.name = name
        self.age = age
        self.contact_number = contact_number
        self.address = address
        self.medical_history = medical_history
        self.doctor_name = doctor_name
        self.room_number = room_number
        self.bed_number = bed_number
        self.ward = ward
        self.admission_date = admission_date
        self.discharge_date = discharge_date
        self.diagnosis = diagnosis
        self.treatment = treatment
        
class Doctor(Hospital):
    def __init__(self, name, age, contact_number, address, specialization, department, hospital_name, room_number, bed_number, ward):
        self.name = name
        self.age = age 
        self.contact_number = contact_number
        self.address = address
        self.specialization = specialization
        self.department = department
        self.hospital_name = hospital_name
        self.room_number = room_number
        self.bed_number = bed_number
        self.ward = ward

class Department(Hospital):
    def __init__(self, name, address, doctor_name, room_number , bed_number, ward):
        self.name = name
        self.address = address
        self.doctor_name = doctor_name
        self.room_number = room_number
        self.bed_number = bed_number
        self.ward = ward
        



