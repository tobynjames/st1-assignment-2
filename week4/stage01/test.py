# SmartCare Community Clinic - Simple Demo

patients = []
practitioners = []
appointments = []

def add_patient():
    name = input("Enter patient name: ")
    patients.append(name)
    print("Patient added.\n")

def add_practitioner():
    name = input("Enter practitioner name: ")
    practitioners.append(name)
    print("Practitioner added.\n")

def book_appointment():
    patient = input("Patient name: ")
    practitioner = input("Practitioner name: ")
    date = input("Appointment date (DD/MM/YYYY): ")

    appointments.append({
        "patient": patient,
        "practitioner": practitioner,
        "date": date
    })

    print("Appointment booked.\n")

def view_appointments():
    print("\nAppointments")
    print("-" * 30)

    if len(appointments) == 0:
        print("No appointments found.")
    else:
        for appt in appointments:
            print(
                f"Patient: {appt['patient']} | "
                f"Practitioner: {appt['practitioner']} | "
                f"Date: {appt['date']}"
            )

    print()

while True:
    print("=== SmartCare Clinic ===")
    print("1. Add Patient")
    print("2. Add Practitioner")
    print("3. Book Appointment")
    print("4. View Appointments")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        add_practitioner()
    elif choice == "3":
        book_appointment()
    elif choice == "4":
        view_appointments()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.\n")
