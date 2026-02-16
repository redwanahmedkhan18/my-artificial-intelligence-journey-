class Personal:
    def __init__(self,name,age,phone_number,address,salary):
        self.name=name
        self.age=age
        self.__phone_number=phone_number
        self.__address=address
        self.__salary=salary


    def update_information(self,phone_number,address,salary):
            self.__phone_number=phone_number
            self.__address=address
            self.__salary=salary
            if len(str(phone_number))!=11:
                raise ValueError("Phone number must be 11 digits. Please enter a valid phone number.")
            else:               
                self.__phone_number=phone_number
            if salary <0:
                raise ValueError("Salary cannot be negative. Please enter a valid salary.")
            else:
                self.__salary=salary

    def view_information(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Phone Number:{self.__phone_number}")
        print(f"Address:{self.__address}")
        print(f"Salary:{self.__salary}")
    
personal1=Personal("John",30,12345678901,"123 Main St",50000)
personal1.view_information()
personal1.update_information(10987654321,"456 Elm St",60000)
personal1.view_information()        