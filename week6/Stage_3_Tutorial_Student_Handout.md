Assignment 2-Case Study

Stage 3 Tutorial Activities

From Requirements to Domain Models

Week 6 | 60 minutes

# Candidate Concepts

| Candidate | Class? | Reason |
| --- | --- | --- |
| Patient |Yes|Has relationship with other classes & has multible values within eg; ID, Name & DOB|
| Practitioner |Yes|Has relationship with other classes & has multible values within eg; ID, Name & DOB|
| Appointment |Yes|Has relationship with other classes & has values eg ; Date & time|
| Name |No|Simple value that can go into a class but not a class itself|
| Clinic |Yes |assuming this means the clinic as a whole, it will have everythingn grouped under it|
| Database |No|Part of infrastructure|
| Cancellation |No|This is a state of the appoinment class|
| Status |No|this is also a state of the appointment class|

# CRC Cards

## Patient

| Responsibilities | Collaborators |
| --- | --- |
|Basic Validation|Appointmets|
|  |  |

## Practitioner

| Responsibilities | Collaborators |
| --- | --- |
|basic validation|Appointmets|
|  |  |

## Appointment

| Responsibilities | Collaborators |
| --- | --- |
|Store time,date and patient / practioner info|Practitioners and Patients|
|  |  |

# Relationship Reasoning

Patient to Appointment: which relationship and why?
Each appointment has exactly one Patient and one practitioner as without one there can be no appointment

Practitioner to Appointment: what multiplicity?
Practitioner 0{Appointments}*

Should Appointment inherit from Patient?
Appointments should have patients as a value, but won't need to enherit all patient values so no

Does Clinic need to own every object?
Yes, for all systems to oporate under the clinic app

# AI Model Critique

Critique AI proposals: PatientManager, PractitionerManager, AppointmentManager, ClinicController, NotificationManager, ScheduleEngine.

The AI made many suggestions for these classess, but ultimatly added to many additional varibles that increased the complexitiy of the system alot, and which sits outside the scope of the clinic app