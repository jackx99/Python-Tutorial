# Hello Guys
# Today Lesson is Inheritance and Polymorphism. These are pillars of Object Oriented Programming.
# What is inheritance? It allows the class to extend its definition without making any physical changes to the existing class.
# Any new class created from the existing class is called a subclass or derived class; existing classes are called superclasses or base classes.
# It enables a subclass to inherit features from its superclass.
# A call to the constructor of superclass must be the first statement. So you pass super().init(parameters) with parameters if any.
# What is Polymorphism? It treats an object of a subclass as an object of its superclass. In other words, a reference variable of a superclass
# type can point to an object of its subclass.
# It also means associating multiple meanings with the same method name.

"""
In this exercise, you will design various classes and write a program to computerize the billing system of a hospital.

a. Design the class Doctor, inherited from the class Person, with an additional data member to store a doctor's specialty.
Add appropriate constructors and methods to initialize, access, and manipulate the data members.

b. Design the class Bill with data members to store a patient's ID and the patient's hospital charges such as pharmacy
for medicine, the doctor's fee, and the room charges. Add appropriate constructors and methods to initialize, access, and
manipulate the data members.

c. Design the class Patient, inherited from the class Person, with additional data members to store a patient's ID, age,
data of birth, attending physician's name, the date when the patient was admitted in the hospital, and the date when the patient
was discharged from the hospital. (Use the class Date to store the date of birth, admit name, discharge date, and the class Doctor 
to store the attending physician's name.) Add appropriate constructors and methods to initialize, access, and manipulate the data
members.

Write a program to test your classes.
"""

# Let's Start
# First we need to create a base class named Person
# Create a class Date for later use
class Person:
    __first_name = None
    __last_name = None

    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
    
    def set_name(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
    
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def __str__(self):
        return f'{self.__first_name} {self.__last_name}'  # Here we use f-strings only available python 3
        # Its easier to comprehend the statement. We only interpolate the value in around with braces in this string value

class Date:
    __month, __day, __year = None, None, None # We can declare variables in single statement by separating it with commas.

    def __init__(self, month, day, year):
        self.__month = month
        self.__day = day
        self.__year = year
    
    def set_date(self, month, day, year):
        self.__month = month
        self.__day = day
        self.__year = year
    
    def get_month(self):
        return self.__month 

    def get_day(self):
        return self.__day
    
    def get_year(self):
        return self.__year
    
    def __str__(self):
        return f'{self.__month} - {self.__day} - {self.__year}'

# In this exercise, you will design various classes and write a program to computerize the billing system of a hospital.

# a. Design the class Doctor, inherited from the class Person, with an additional data member to store a doctor's specialty.
# Add appropriate constructors and methods to initialize, access, and manipulate the data members.
class Doctor(Person):
    __specialty = None

    def __init__(self, specialty):
        self.__specialty = specialty
    
    def set_specialty(self, specialty):
        self.__specialty = specialty
    
    def get_specialty(self):
        return self.__specialty
    
    def __str__(self):
        return f'The doctor\'s specialty {self.__specialty}'


# b. Design the class Bill with data members to store a patient's ID and the patient's hospital charges such as pharmacy
# charges for medicine, the doctor's fee, and the room charges. Add appropriate constructors and methods to initialize, access, and
# manipulate the data members.
class Bill:
    __patientID = None
    __pharmacy_charges = None
    __doctor_fee = None
    __room_charges = None
    
    def __init__(self, patientID, pharmacy_charges, doctor_fee, room_charges):
        self.__patientID = patientID
        self.__pharmacy_charges = pharmacy_charges
        self.__doctor_fee = doctor_fee
        self.__room_charges = room_charges

    def set_bill(self, patientID, pharmacy_charges, doctor_fee, room_charges):
        self.__patientID = patientID
        self.__pharmacy_charges = pharmacy_charges
        self.__doctor_fee = doctor_fee
        self.__room_charges = room_charges

    def get_patient_id(self):
        return self.__patientID
    
    def get_pharmacy_charges(self):
        return self.__pharmacy_charges
    
    def get_doctor_fee(self):
        return self.__doctor_fee
    
    def get_room_charges(self):
        return self.__room_charges
    
    def __str__(self):
        return f'**Bill** \n Patient id: {self.__patientID} \n Pharmacy charges {self.__pharmacy_charges}, \n Doctor fee {self.__doctor_fee}, \n Room charges {self.__room_charges}'
    

# c. Design the class Patient, inherited from the class Person, with additional data members to store a patient's ID, age,
# date of birth, attending physician's name, the date when the patient was admitted in the hospital, and the date when the patient
# was discharged from the hospital. (Use the class Date to store the date of birth, admit date, discharge date, and the class Doctor 
# to store the attending physician's name.) Add appropriate constructors and methods to initialize, access, and manipulate the data
# members.
class Patient(Person):
    __patientID = None
    __age = None
    __date_of_birth = None # Use date
    __attending_physician_name = None # Use class Doctor
    __date_patient_admitted = None # Use date
    __date_patient_discharged = None # Use date

    def __init__(self, patientID, first_name, last_name, age, date_of_birth, 
    attending_physician_name, date_patient_admitted, date_patient_discharged):
        super().__init__(first_name, last_name)
        self.__patientID = patientID
        self.__age = age
        self.__date_of_birth = date_of_birth
        self.__attending_physician_name = attending_physician_name
        self.__date_patient_admitted = date_patient_admitted
        self.__date_patient_discharged = date_patient_discharged

    def setPatient(self, patientID, first_name, last_name, age, date_of_birth,
    attending_physician_name, date_patient_admitted, date_patient_discharged):
        self.__patientID = patientID
        self.set_name(first_name, last_name)
        self.__age = age
        self.__date_of_birth = date_of_birth
        self.__attending_physician_name = attending_physician_name
        self.__date_patient_admitted = date_patient_admitted
        self.__date_patient_discharged = date_patient_discharged

    def get_patient_id(self):
        return self.__patientID
    
    def get_age(self):
        return self.__age
    
    def get_date_birth(self):
        return self.__date_of_birth

    def get_attending_physician_name(self):
        return self.__attending_physician_name

    def get_date_patient_admitted(self):
        return self.__date_patient_admitted

    def get_date_patient_discharged(self):
        return self.__date_patient_discharged
    
    def __str__(self):
        return f'**Patient** Patient Id: {self.__patientID}, First name: {self.get_first_name()}, Last name: {self.get_last_name()}, Age: {self.__age}, Date of birth: {self.__date_of_birth}, Attending physician name: {self.__attending_physician_name}, Date admitted: {self.__date_patient_admitted}, Date discharged: {self.__date_patient_discharged}'
        

# Write a program to test your classes.
doctor = Doctor(specialty="Cardiologists")
doctor.set_name(first_name="Kelly", last_name="Hunter")
patient = Patient(patientID=39340889, first_name='Stella', last_name='Krawczyk', age=67, date_of_birth=Date(3, 18, 1953), attending_physician_name=f'{doctor.get_first_name()} {doctor.get_last_name()}', date_patient_admitted=Date(1, 16, 2020), date_patient_discharged=Date(3, 23, 2020))
print(patient)
bill = Bill(patientID=39340889, pharmacy_charges='$123', doctor_fee='$1024', room_charges='$500')
print(bill)
# Adding the parameter name is optional
# You can see it easily to understand you have passed in each parameter.
