K = int(input("Введите число K от 1 до 365: "))
day_of_week = (K + 1) % 7
if day_of_week == 0:
    day_of_week = 7
print("Номер дня недели:", day_of_week)