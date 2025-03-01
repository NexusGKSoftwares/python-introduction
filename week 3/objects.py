from classes  import Department, Doctor, Hospital, Patient, Person, Employee, Manager, Developer, QA_Engineer, Project_Manager, Team_Leader 

# adding objects to our classes from models.py 
person = Person('John', 'Doe', 30)
employee = Employee('Jane', 'Doe', 25, 'Software Engineer')
manager = Manager('Bob', 'Smith', 40, 'Project Manager')
developer = Developer('Alice', 'Johnson', 28, 'Software Developer')
qa_engineer = QA_Engineer('Mike', 'Williams', 35, 'QA Engineer ')
project_manager = Project_Manager('Emily', 'Davis', 32, 'Project Manager')
team_leader = Team_Leader('David', 'Taylor', 38, 'Team Leader')

# objects of hospital management system 
hospital = Hospital("ABC Hospital", "123 Main St")
patient = Patient("John Doe", 30, "123-456-7890", "123 Main St", "Diabetes", "Dr. Smith", 101, 1, "General Ward", "2022-01-01", "2022-01-15", "Di abetes", "Insulin Therapy")
doctor = Doctor("Dr. Smith", 40, "987-654-3210", " 456 Elm St", "Cardiology", "Cardiology Department", "ABC Hospital", 202, 2, "ICU")
department = Department("Cardiology Department", "456 Elm St", "Dr. Smith", 202 , 2, "ICU") 
