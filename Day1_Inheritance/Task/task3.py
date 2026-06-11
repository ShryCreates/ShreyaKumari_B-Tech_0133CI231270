class School:
    def infrastructure(self):
        print("School is an infrastructure")
        
class Department(School):
    def department_name(self):
        print("CSIT dept")
        
class Classroom(Department):
    def total_students(self):
        print("Total student is 60")
        
c=Classroom()
c.infrastructure()
c.department_name()
c.total_students()                        