class BMI_Calculator:
    def __init__(self, weight_kg, height_m):
        self.weight_kg = weight_kg
        self.height_m = height_m

    @property
    def weight(self):
        return self.weight_kg

    @property
    def height(self):
        return self.height_m

    def calculate_bmi(self):
        bmi = self.weight_kg / (self.height_m ** 2)
        return bmi

# Contoh penggunaan kelas BMI_Calculator
weight = float(input("Masukkan berat badan (kg): "))
height = float(input("Masukkan tinggi badan (meter): "))

person = BMI_Calculator(weight, height)
print("Berat Badan:", person.weight, "kg")
print("Tinggi Badan:", person.height, "meter")
print("BMI:", person.calculate_bmi())
