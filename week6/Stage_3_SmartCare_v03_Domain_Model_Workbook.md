SmartCare v0.3 - Domain Model Workbook

Week 6 student resource

# Requirement-to-Concept Trace

| Requirement | Concept | State/behaviour | Decision |
| --- | --- | --- | --- |
|Appointments|Bookings, timeslot, calendar event|Confirmed/cancled|Implement doubble booking check|
|Patients|Health Record, Identity like name and DOB|Active|Encrypt information, store behind passwords|
|Practioners|Avalibility|Avalible or not|Same as Patients|
|Filters|Simple search query|Applied or not applied|Can be simple as scale of the clinic is small|

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

## Optional class (Filter)

| Responsibilities | Collaborators |
| --- | --- |
|Have diffrent options for filtering data|Practitioners, Patients & appointments|
|  |  |

# UML Class Diagram

Insert/draw UML here. Include defensible relationships and multiplicities.
IMAGE IN WEEK 6 FOLDER

# Design Rationale

Explain class selection, responsibility allocation and key relationships.

Our core entitys are the 3 classes Patient, Practioner & appointment
We also have a utility class like the filter which interacts with these classes

Practioner and Patient have their responcibiltys to Validate their information such as name and DOB

Our key relationship is that every appointment must have 1 patient and 1 practioner

# AI Design Review Record

| AI suggestion | Evidence | Decision | Reason | Model change |
| --- | --- | --- | --- | --- |
|Virtual Consoltations|Healthcare systems have started doing this in modern times|No|Out of scope for small local clinic|Update appointment class to have two subclasses|
|Electronic health Records|Real world Medical systems have privacy laws governing them|Yes|If this system was real this would be a legal requirement|Database system added to store and encript patient data|
|Automated wait list|In the real world appointmets are often cancled last minute with empty slots not being auto filled|No|Out of scope for such a small clinic|Add an automated auto boking system that moves appointments when slots become free|
|  |  |  |  |  |
|  |  |  |  |  |