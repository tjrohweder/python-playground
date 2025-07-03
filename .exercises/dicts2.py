registrations = []

while len(registrations) <= 3:
    name = input("Step 1 - Provide the user name( or 'exit' to finish): ")
    if name.lower() == 'exit':
        break

    age = int(input("Step 2 - Provide the user age: "))
    city = input("Step 3 - Provide user location(city): ")

    people = {
        "name": name.lower(),
        "age": age,
        "city": city.lower()
    }

    registrations.append(people)

print(f"Number of people registered is {len(registrations)}")
