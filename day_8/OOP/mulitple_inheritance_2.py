class FirstTerm:
    def __init__(self, csc103, eng101, math147, phy111):
        self.csc103 = csc103
        self.eng101 = eng101
        self.math147 = math147
        self.phy111 = phy111

    def first_term_result(self):
        return (self.csc103 * 0.20 + self.eng101 * 0.20 + self.math147 * 0.20 + self.phy111 * 0.20)


class MidTerm(FirstTerm):
    def __init__(self, ft_marks, csc103, eng101, math147, phy111):
        super().__init__(*ft_marks)
        self.mid_csc103 = csc103
        self.mid_eng101 = eng101
        self.mid_math147 = math147
        self.mid_phy111 = phy111

    def mid_term_result(self):
        return (self.mid_csc103 * 0.20 + self.mid_eng101 * 0.20 +
                self.mid_math147 * 0.20 + self.mid_phy111 * 0.20)


class FinalTerm(MidTerm):
    def __init__(self, ft_marks, mt_marks, csc103, eng101, math147, phy111):
        super().__init__(ft_marks, *mt_marks)
        self.final_csc103 = csc103
        self.final_eng101 = eng101
        self.final_math147 = math147
        self.final_phy111 = phy111

    def final_term_result(self):
        return (self.final_csc103 * 0.35 + self.final_eng101 * 0.35 +
                self.final_math147 * 0.35 + self.final_phy111 * 0.35)


class FinalResult(FinalTerm):

    def calculate_final_result(self):
        total = ((self.first_term_result() +
                 self.mid_term_result() +
                 self.final_term_result())+25)/3

        print(f"Final Marks: {total:.2f}")

        self.calculate_cgpa(total)

    def calculate_cgpa(self, marks):
        if marks >= 90 and marks <= 100:
            cgpa = 4.00
        elif marks >= 87 and marks < 90:
            cgpa = 3.75
        elif marks >= 84 and marks < 87:
            cgpa = 3.40
        elif marks >= 80 and marks < 84:
            cgpa = 3.10
        elif marks >= 75 and marks < 80:
            cgpa = 2.75
        elif marks >= 70 and marks < 75:
            cgpa = 2.40
        elif marks >= 65 and marks < 70:
            cgpa = 2.10
        elif marks >= 60 and marks < 65:
            cgpa = 1.75
        elif marks >= 50 and marks < 60:
            cgpa = 1.40
        elif marks >= 40 and marks < 50:
            cgpa = 1.10
        else:
            cgpa = 0.00

        print(f"Final CGPA: {cgpa}")


ft = (85, 90, 80, 75)
mt = (82, 88, 79, 85)
final = (88, 92, 85, 90)

student1 = FinalResult(ft, mt, *final)
student1.calculate_final_result()
