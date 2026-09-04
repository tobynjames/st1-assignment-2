from datetime import datetime
appointments = [] 

continue_request = "y"

print("Welcome to SmartCare: The Clinical Appointment Booking System!") 


def create_apppointments():
    patient = input("Enter patient name: ")

    practitioner = input("Enter practitioner name: ")
    appointment_time = input("Enter appointment time HH:MM in 24 Hour Time:")

    # Run Book Appointment Function
    book_appointment(patient, practitioner, appointment_time)

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

#Checks if name is valid
def validate_name(name):
    return name.replace(" ", "").isalpha()

def validate_time(time):
    try:
        # %H checks for 24-hour format, %M checks for minutes
        datetime.strptime(time, "%H:%M")
        return True
    except ValueError:
        return False

#Lists all appointsments if there is any
def display_appointments(): 
    if not appointments: 
         print("No appointments recorded.") 
         return 
    print ("====Appointments====")
    for appointment in appointments: 
            print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}") 

while continue_request == "y":
    create_apppointments()
    continue_request = input("Do you want to add another appointment, type Y for yes")
display_appointments()
exit

