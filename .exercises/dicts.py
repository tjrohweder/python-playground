registrations = []

while True:
    name = input("Enter name (or type 'exit' to finish): ")
    if name.lower() == 'exit':
        break

    age = int(input("Enter age: "))
    city = input("Enter city: ")

    person = {
        "name": name,
        "age": age,
        "city": city
    }

    registrations.append(person)

print(f"\nTotal people registered: {len(registrations)}")

unique_cities = set()
for person in registrations:
    unique_cities.add(person["city"])

print("Unique cities:")
for city in unique_cities:
    print("-", city)

search = input("\nEnter a name to search (or press Enter to skip): ")
if search:
    found = False
    for person in registrations:
        if person["name"].lower() == search.lower():
            print(f"{person['name']} is {person['age']} years old and lives in {person['city']}.")
            found = True
            break
    if not found:
        print("Person not found.")
