'''
1. Fullname and Email

Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:

Form the fullname by simply joining the first and last name together, separated by a space.
Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.
Examples
emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")
emp_1.fullname ➞ "John Smith"

emp_2.email ➞ "mary.sue@company.com"

emp_3.firstname ➞ "Antony"
'''

class Employee:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
		self.fullname = self.firstname + " " + self.lastname
		self.email = (self.firstname + "." + self.lastname + "@company.com").lower()

# *************************************************************

'''
2. Which Function Returns the Larger Number?

Your function will be passed two functions, f and g, that don't take any parameters. Your function has to call them, and return a string which indicates which function returned the larger number.

If f returns the larger number, return the string f.
If g returns the larger number, return the string g.
If the functions return the same number, return the string neither.
Examples
which_is_larger(lambda: 5, lambda: 10) ➞ "g"

which_is_larger(lambda: 25,  lambda: 25) ➞ "neither"

which_is_larger(lambda: 505050, lambda: 5050) ➞ "f"
'''

def which_is_larger(f, g):
	if f() == g(): 
		return "neither"
	return "f" if f() > g() else "g"
	
# *************************************************************
