from datetime import datetime

#Lists
appointments = [] 
patients = []
practitioners = []



# Base class
class Person:
        def __init__(self, name, dob, email):
                self.name = name
                self.dob = dob
                self.email = email

# sub classes
class Patient(Person):
        def __init__(self, patient_id, name, dob, email):
                super().__init__(name,dob,email)
                self.patient_id = patient_id

              
class Practitioner(Person):
        def __init__(self, practitioner_id, name, dob, email):
                super().__init__(name,dob,email)
                self.patient_id = practitioner_id

#Data validation (Not implimented for email)
def validate_name(name):
    return name.replace(" ", "").isalpha()

def validate_time(time):
    try:
        # %H checks for 24-hour format, %M checks for minutes
        datetime.strptime(time, "%H:%M")
        return True
    except ValueError:
        return False


def add_patient():
    patient_id = input("Patient ID: ")
    name = input("Name: ")
    dob = input("DOB: ")
    email = input("Email: ")

    if not validate_name(name):
        print("Name must contain letters only.")
        return

    patient = Patient(patient_id, name, dob, email)

    patients.append(patient)

    print("Patient added.")

def add_practitioner():
    practitioner_id = input("Practitioner ID: ")
    name = input("Name: ")
    dob = input("DOB: ")
    email = input("Email: ")

    if not validate_name(name):
            print("Name must contain letters only.")
            return

    practitioner = Practitioner(
    practitioner_id,
    name,
    dob,
    email
    )

    practitioners.append(practitioner)

    print("Practitioner added.")

#seach function for booking
def find_practitioner(practitioner_id):

    for practitioner in practitioners:
        if practitioner.practitioner_id == practitioner_id:
            return practitioner
    return None

def find_patient(patient_id):

    for patient in patients:
        if patient.patient_id == patient_id:
            return patient
    return None



def add_appointment():

    patient_id = input("Enter Patient ID: ")
    practitioner_id = input("Enter Practitioner ID: ")
    appointment_time = input("Enter appointment time HH:MM in 24 Hour Time:")

    if not validate_time(appointment_time):
           print("Time must be HH:MM format in 24 Hour Time")
           return
    patient = find_patient(patient_id)
    practitioner = find_practitioner(practitioner_id)

    if patient is None:
        print("Patient not found.")
        return

    if practitioner is None:
        print("Practitioner not found.")
        return

    # Run Book Appointment Function
    add_appointment(patient, practitioner, appointment_time)

#Grabs info from create_appointment's appointment dictornary and saves them to appointments array
def book_appointment(patient_name, practitioner_name, appointment_time): 
    if not patient_name: 
         print("Patient name must not be empty")
         return
    if not validate_name(patient_name): 
             print("Patient name must not have numbers")
             return
    if not practitioner_name: 
             print("Practitioner name must not be empty")
             return
    if not validate_name(practitioner_name): 
                print("Practitioner name must not have numbers")
                return
    if not appointment_time: 
                    print("Time is required")
                    return
    if not appointment_time: 
                        print("Time is required")
                        return
    if not validate_time(appointment_time): 
                            print("Time has to be in 24 hour format")
                            return
    appointment = { 
        "patient": patient_name, 
        "practitioner": practitioner_name, 
        "time": appointment_time 
    } 
    appointments.append(appointment) 
    print("Appointment booked successfully.")



#Lists all appointsments if there is any
def display_appointments(): 
    if not appointments: 
         print("No appointments recorded.") 
         return 
    print ("====Appointments====")
    for appointment in appointments: 
            print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}") 

while True:

    print("\n=== SmartCare ===")
    print("1. Add Patient")
    print("2. Add Practitioner")
    print("3. Add Appointment")
    print("4. View Appointments")
    print("5. Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        add_patient()
    
    elif choice == "2":
        add_practitioner()
    
    elif choice == "3":
        add_appointment()
    
    elif choice == "4":
        display_appointments()
    
    elif choice == "5":
        break

    else:
        print("Invalid option.")
