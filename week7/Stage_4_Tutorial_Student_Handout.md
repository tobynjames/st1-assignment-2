Assignment 2 – Case Study

Stage 4 Tutorial Activities

Object-Oriented Design Decisions

Week 7 | 60 minutes

# Activity 1 - Encapsulation Review

| Class | Protected state / invariant | Public operations |
| --- | --- | --- |
| Patient |Unique Patient ID, Name cannot be null, date of birth must be valid|register_patient(), update_details()|
| Practitioner |Unique Patient ID, Name cannot be null, specialty must be valid|get_schedule()|
| Appointment |required at least one practitioner and patiend, valid time, not doubble booked|book_appointment(), cancle_appointment()|

# Activity 2 - Composition or Inheritance?

Appointment and Patient -> Associated Reason: every appointment requires at least one patient

Appointment and Practitioner -> Associated Reason: every appointment requires at least one Practitioner

Doctor and Practitioner (hypothetical) -> Inheritence both would inherit from a user class, but also doctor and practitioner would share many atributes

Clinic and Appointment -> Accociated Reason: Clinics have appointments

# Activity 3 - Responsibility Allocation

Who decides whether SCHEDULED can become CANCELLED? - Admin's of the system

Who validates a patient name? - Admin's of the system

Should Appointment execute SQL? Why? - no a seprate class should be made to edit SQL database

Should the UI decide whether a status transition is legal? no, the code running the database should do this, and the UI should only display options & not directly affect the database classes

# Activity 4 - AI Code Critique

AI generates an Appointment class with public status mutation, SQL inside cancel(), a NotificationManager dependency and inheritance from PatientRecord. Identify at least five design problems and corrections.

1. Notofication depency, if notofications are down we still want the appointments to function
2. public status mutation, we want things to have a public get but a private set so statuses should be visible but not directly editable outside normal means
3. Appointments include patients which are linked to their record but the appointment class will not need to inherit anyhting directly from the PatientRecord class
4. SQL should be edited and controlled by a diffrent class / system
5. Don't generate the class with AI, request suggestions and create it yourself

# Exit question

Why can code be object-oriented syntactically but still have poor object-oriented design?

OOP works well when everything in segmented but connected correctly, having one class, handel two jobs or adding to many dependencys starts to turn OOP back into a single file like code structure, 

Some good guide lines include

ENCAPSULATION
Keep related state and behaviour together; protect invariants.

INFORMATION HIDING
Not every attribute should be changed freely; internal representation may change without breaking clients.

PUBLIC INTERFACE
Expose purposeful operations. Good interfaces reduce coupling.