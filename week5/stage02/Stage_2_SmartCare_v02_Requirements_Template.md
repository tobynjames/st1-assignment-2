SmartCare v0.2 - Requirements Specification Template

# 1\. Problem and Scope
SmartCare's current system has a mix of physical and digital records causing duplicate bookings and is overall difficult to use - the problem is to create a simple booking system that is centralized so info is added and found in one place
It needs to be small and maintainable


# 2\. Stakeholders

| Stakeholder | Need | Evidence |
| --- | --- | --- |
|Staff|Easy to use system with Bookings all in one place|Client Briefing  |
|Patients|Reliable bookings with practitioners|Client Briefing  |
|Management|Small Manageble system  |Client Briefing  |
|Practitioners|Reliable system that dosn't cause scheduling conflicts| Client Briefing |
|  |  |  |

# 3\. Functional Requirements

FR-01: Search Function for patient information

FR-02: Record and display Full appointment history

FR-03: Record and display appointment status

FR-04: Booking function

FR-05: Scedualing conflict detection

FR-06: Information is stored at one database so all info is in one place

FR-07: Creation of new patients

FR-08: Creation of new practitioners

FR-09: Filter options for searching patients and practitioners

FR-10: Update booking function

FR-11: delete booking function

FR-12: recurring booking function

# 4\. Non-Functional Requirements

NFR-01: System must be easy to use for all staff

NFR-02: Search features must be fast

NFR-03: Filters must be clear to find

NFR-04: System must be maintainable

NFR-05: Bookings must be reliable

NFR-06: Data must be secure

# 5\. User Stories

US-01: As a STAFF MEMBER, I want FILTER BOOKINGS BY PRACTITIONER, so that I CAN SEE THEIR AVALIBILITY.

US-02: As a STAFF MEMBER, I want CANCLE A BOOKING, so that THERE'S A FREE SPACE

US-03: As a PRACTIONER, I want VEIW MY SCEDUAL, so that I CAN PLAN MY DAY.

US-04: As a PATIENT, I want MY BOOKINGS TO HAVE NO CONFLICT, so that I CAN ATTEND THEM WITH NO DISRUPTIONS.

US-05: As a STAFF MEMBER, I want TO MAKE A NEW PATIENT ENTRY, so that I CAN BOOK THEM WITH A PRATICTIONER.

US-06: As a PATIENT, I want TO REQUEST AN UPDATE TO MY BOOKING, so that I CAN SCHEDUAL IT AROUND MY DAY AFTER THE FACT.

# 6\. Acceptance Criteria

Feature: Canceling bookings

- Sinario: Paitent asks's staff to cancel a booking

- GIVEN I Have a booking that I can no longer need to attend

- WHEN  I request for the booking to be cancled

- THEN A staff memeber will cancle the booking

Feature: Updating Bookings

- Sinario: Paitent asks's staff to update a booking

- GIVEN  I Have a booking that I can no longer attend today

- WHEN   I ask a staff memeber for help with updating the booking

- THEN I get given other options for the booking & it is updated to one of thoes


Feature: Filtering by Practioner

- Sinario: Staff member needs to veiw Practioners schedual for the day

- GIVEN  I've been asked to check on a Practioners schedual

- WHEN   I filter by date & the practioner

- THEN I can see all their bookings for a particualr day


# 7\. Assumptions and Open Questions
Copilot limmited it's assumptions and took only info implied from the breif
Copilot had the following open questions

Appointment History
- What historical information must be retained?
- How long should history be stored?
- Should status changes be recorded in history?


Users and Access
- Which staff roles will use the system?
- Are different permissions required?
- Who can create, edit, or delete records?


Reporting and Search
- What patient search capabilities are required?
- What appointment reports are needed?
- Should management have summary views?


Data Migration
- Must existing spreadsheet data be imported?
- Must paper records be digitised?
- What level of historical data should be migrated?



# 8\. AI Requirements Review Record

| AI suggestion | Evidence? | Decision | Reason | Verification |
| --- | --- | --- | --- | --- |
|Duplicate bookings managment|Staff report duplicate bookings|Implement|To avoid scedualing conflits|Verified|
|Provide a centralised patient record|Staff report difficulty finding patient information|Implement|Efficency|Verified|
|Standardise appointment status management|Staff report inconsistent appointment status|Implement|Consistancy|Verified|
|Maintain appointment history|Staff report limited appointment history.|Implement|Allow access to previous appointments |Verified|
|  |  |  |  |  |