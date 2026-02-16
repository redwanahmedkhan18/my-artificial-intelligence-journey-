from abc import ABC,abstractmethod

class Result(ABC):
    @abstractmethod
    def final_result(self):
        pass


class Semester_Final_Result(Result):
    def __init__(self,number1,number2):
        super().__init__()
        self.n1=number1
        self.n2=number2
    def final_result(self):
        print(f"Final marks:{(self.n1+self.n2)/2}")


rs=Semester_Final_Result(89,92)
rs.final_result()