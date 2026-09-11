Assignment 2 Case Study

Stage 2 Tutorial From Problems to Requirements

Week 5 | 60 minutes

# Learning goals

-   Analyse stakeholders.
-   Distinguish functional and non-functional requirements.
-   Recognise ambiguity and unsupported requirements.
-   Define scope.
-   Develop user stories and acceptance criteria.
-   Critique AI-generated requirements.

# Activity 1 - Stakeholder Map

| Stakeholder | Need | Potential conflict |
| --- | --- | --- |
|Staff|Easy to use system with Bookings all in one place|previous bookings|
|Patients|Reliable bookings with practitioners|Priority of bookings|
|Management|Small Manageble system |Staff want more features|
|Practitioners|Reliable system that dosn't cause scheduling conflicts|allocation of bookings when practioner is sick|
|  |  |  |

# Activity 2 - Functional or Non-Functional?

x Functional □ Non-functional The system shall allow staff to cancel an appointment.

□ Functional x Non-functional The system should remain responsive for the course-scale dataset.

x Functional □ Non-functional The system shall retain cancelled appointments.

x Functional □ Non-functional Core business logic should be independently testable.

x Functional □ Non-functional The system shall search for a patient by ID.

# Activity 3 - Repair Ambiguous Requirements

The system should be easy to use.

Problem:System is currently hard to use  Clarification question: Who are the main users?

Patient search should be fast.

Problem: System is slow Clarification question: how fast do you want search results

The system should securely manage data.

Problem: Data is not stored securely Clarification question: Who should and shouldn't have access to data

Appointments should normally be easy to cancel.

Problem: Cancling appointments easaly Clarification question: What are our time frames for full canclation? 

# Activity 4 - AI Requirements Audit

Classify each suggestion: Confirmed / Assumption requiring validation / Unsupported / Out of scope.

| AI suggestion | Classification | Evidence / reason |
| --- | --- | --- |
| Patients receive SMS reminders. |Requiring Validation|Out Of Scope|
| Facial recognition login. |Requiring Validation|Out Of Scope|
| Receptionists create appointments. |Confirmed|In Scope|
| Online payment. |Requiring Validation|Out Of Scope|
| Practitioners view schedules. |Confirmed|In Scope|
| AI recommends treatments. |Requiring Validation|Out Of Scope|
| Cancelled appointments remain in history. |Confirmed|In Scope|

# Exit question

Why is 'AI suggested it' not sufficient evidence for a requirement?

AI offten takes into account information from it's learning model that isn't appliciable to your question
It can easly add requirements to a project that were not requested and are not needed + it's designed to output a large volume of responce so it's bound to add extra unneeded items