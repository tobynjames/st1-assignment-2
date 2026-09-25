SmartCare v0.4 - Domain Implementation Workbook

Week 7 student resource

# 1\. UML-to-Code Trace

| UML element | Python element | Implemented? | Notes |
| --- | --- | --- | --- |
|Patient|Patient Class|No|Stored in a list|
|Practitioner|Practitioner class|no|Also Stored in a list  |
|Appointments|Appointment Class  |No  |Stored as dictonary|
|Patient name |Atribute of patient class|yes|string|
|Practitioner name |Atribute of Practitioner class|yes|string|
|appointment date|atribute of appointment|no|stored as "date" key in appointment dictronary|
|book appointmnet|book_appointmnet()|no|method which created a new appoinmtment|
|add practitioner|add_practitioner|no|adds practitioner to system|
|add Patient|Patient|no|adds Patient to system|
|veiw appointments operation|veiw_appointments|no|displays all appointments  |

# 2\. Domain Invariants

| Class | Invariant / rule | How protected |
| --- | --- | --- |
|Patient|Name can't be null|Inputvalidation|
|practitioner|Name can't be null|Inputvalidation|
|Patient|DOB must be valid|Input validation with format|
|appointment|Must have one practitioer and patient|can't create if both feilds are null|
|appointment|Date must be valid and not in the past|Date/time validation|
|appointment|must not be doubble booked|compared with other appointments for the practitioner and patient|

# 3\. Composition / Inheritance Decisions

| Relationship | Decision | Rationale |
| --- | --- | --- |
|appopintment -> Patient|Composition  |appointments have patients  |
|appopintment -> practitioner|Composition  |appointments have practitioners  |
|Patient -> practitioner|associated  | they have a relationshiop but no inheritence between the two|
|User -> patient|inheritence|a base user class with name & DOB that is inherited by patient and practitioner  |

# 4\. AI Pair-Programming Record

| AI contribution | Conforms? | Decision | Reason | Verification |
| --- | --- | --- | --- | --- |
|Suggested Patient, Practitioner, and Appointment classes.|Yes| Implement |in scope|in uml diagram|
|Generated Python methods for booking appointments.|Yes  |Implement|in scope|tested|
|Suggested appointment validation rules.|  yes|Implement|in scope|tested|
|Suggested a database implementation.| no | ignore |in scope|to big for small project|
|Recommended inheritance from a Person superclass.| yes |Implement|in scope|in UML diagram|

# 5\. Updated UML

Insert updated UML only if implementation revealed a justified design change. Explain every change.

New UML in week 7 folder,

Structure is the same but I've updated the methods and attributes, as well as added text to relation lines to show that each appointment requires 1 practitoner and 1 patient,

Added basic info that Patients and practioers have to the user class, please note this class is ABSTRACT and can't be created on it's own