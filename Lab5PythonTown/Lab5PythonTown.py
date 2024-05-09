from Lab5PythonTownLib import Town

arr_towns = []
cnt_towns = int(input("Введіть кількість міст: "))
for _ in range(cnt_towns):
        town = Town()
        town.name = input("Введіть назву міста: ")
        town.country = input("Введіть назву країни: ")
        town.region = input("Введіть назву регіону: ")
        town.population = int(input("Введіть кількість населення: "))
        town.year_income = float(input("Введіть річний дохід: "))
        town.square = float(input("Введіть площу, кв. км: "))
        town.has_port = input("Чи є у місті порт? (y-так, n-ні): ").lower() == 'y'
        town.has_airport = input("Чи є у місті аеропорт? (y-так, n-ні): ").lower() == 'y'
        arr_towns.append(town)

for t in arr_towns:
        print(f"\nДані про місто {t.name}")
        print(f"Країна: {t.country}")
        print(f"Регіон: {t.region}")
        print(f"Кількість населення: {t.population}")
        print(f"Річний дохід: {t.year_income:.2f}")
        print(f"Площа: {t.square:.3f}")
        print("У місті є порт" if t.has_port else "У місті нема порту")
        print("У місті є аеропорт" if t.has_airport else "У місті нема аеропорту")
        print(f"Середній річний дохід на одного громадянина: {t.year_income_per_inhabitant:.2f}")
