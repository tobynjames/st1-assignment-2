The following is a comparison between the AI version of the app copilot generated

=== Appointment Booking ===
Enter patient name: Dave
Enter practitioner name: Chan
Enter appointment time: Half Past Rad

Appointment Saved:
Patient: Dave
Practitioner: Chan
Time: Half Past Rad

And the version I made ( Note this is export from after I added time validation, the table below was made before I added that)

Welcome to SmartCare: The Clinical Appointment Booking System!
Enter patient name: David123
Enter practitioner name: Bob
Enter appointment time HH:MM in 24 Hour Time:12:20
Patient name must not have numbers
Do you want to add another appointment, type Y for yesy
Enter patient name: David
Enter practitioner name: bob
Enter appointment time HH:MM in 24 Hour Time:12:30
Do you want to add another appointment, type Y for yesy
Enter patient name: Mark
Enter practitioner name: Smith
Enter appointment time HH:MM in 24 Hour Time:4:30
Do you want to add another appointment, type Y for yesn
====Appointments====
Patient: David | Practitioner: bob | Time: 12:30
Patient: Mark | Practitioner: Smith | Time: 4:30


| Question                     | Human Version                                          | AI Version                           |
| ---------------------------- | ------------------------------------------------------ | ------------------------------------ |
| Easy to understand?          | Yes, I've got good code flow and a good amount of comments. | Still a good flow, but with fewer comments. |
| Runs successfully?           | Runs                                                   | Runs                                 |
| Uses only required features? | Has extra features I added.                            | Has only the required features.      |
| Adds assumptions?            | Assumes there are no time input issues.                | Assumes there are no input issues.   |
| Handles errors?              | Has input validation (except for time input).          | Has no input validation.             |
| Could I explain it?          | Yes                                                    | Yes                                  |