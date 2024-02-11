class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        temp = []
        temp.append(celsius + 273.15)
        temp.append(celsius * 1.80 + 32.00)
        return temp
