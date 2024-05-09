from Lab5PythonCountryLib import Country


arr_countries = []
cnt_countries = int(input("Введіть кількість кїаїн: "))
for _ in range(cnt_countries):
        country = Country()
        country.Name = input("Введіть назву країни: ")
        country.Capital = input("Введіть назву столиці: ")
        country.Population = int(input("Введіть кількість населення: "))
        country.Area = float(input("Введіть площу країни, кв. км: "))
        country.Language = input("Введіть мову(-и) країни: ")
        is_un_member = input("Чи є країна членом ООН? (y-так, n-ні): ").lower()
        country.IsUNMember = is_un_member == 'y'
        country.DevelopmentLevel = input("Рівень розвитку країни: ")
        arr_countries.append(country)
    
for country in arr_countries:
        print()
        print(" ")
        print("Дані про країну", country.Name)
        print()
        print("Столиця:", country.Capital)
        print("Кількість населення:", country.Population)
        print("Площа:", "{:.3f}".format(country.Area))
        print("Мова(-и):", country.Language)
        print("Країна є членом ООН" if country.IsUNMember else "Країна не є членом ООН")
        print("Рівень розвитку:", country.DevelopmentLevel)
        print("Густина населення:", "{:.2f}".format(country.PopulationDensity))

