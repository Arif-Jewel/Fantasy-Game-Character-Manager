import json

characters = []

def add_character():
    name = input("Enter character name: ")
    race = input("Enter race (Elf, Dwarf, Human): ")
    role = input("Enter role (Warrior, Mage): ")
    skill_level = int(input("Enter skill level (1-5): "))
    wealth = int(input("Enter wealth in gold coins: "))

    character = {
        "name": name,
        "race": race,
        "role": role,
        "skill_level": skill_level,
        "wealth": wealth
    }
    characters.append(character)
    print(f"{name} added successfully!\n")

def list_characters():
    if not characters:
        print("No characters available.\n")
        return

    for char in characters:
        print(f"Name: {char['name']}, Race: {char['race']}, Role: {char['role']}, "
              f"Skill: {char['skill_level']}, Wealth: {char['wealth']} gold coins")
    print()

def search_character():
    name = input("Enter character name to search: ")
    found = [char for char in characters if char["name"].lower() == name.lower()]
    
    if found:
        for char in found:
            print(f"Found - Name: {char['name']}, Race: {char['race']}, Role: {char['role']}, "
                  f"Skill: {char['skill_level']}, Wealth: {char['wealth']} gold coins\n")
    else:
        print("Character not found.\n")

def calculate_total_wealth():
    total_wealth = sum(char["wealth"] for char in characters)
    print(f"Total wealth of all characters: {total_wealth} gold coins\n")

def save_to_file():
    with open("characters.json", "w") as f:
        json.dump(characters, f, indent=4)
    print("Characters saved successfully!\n")

def load_from_file():
    global characters
    try:
        with open("characters.json", "r") as f:
            characters = json.load(f)
        print("Characters loaded successfully!\n")
    except FileNotFoundError:
        print("No saved character file found.\n")

def main():
    while True:
        print("Fantasy Game Character Manager")
        print("1. Add Character")
        print("2. List Characters")
        print("3. Search Character")
        print("4. Calculate Total Wealth")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_character()
        elif choice == "2":
            list_characters()
        elif choice == "3":
            search_character()
        elif choice == "4":
            calculate_total_wealth()
        elif choice == "5":
            save_to_file()
        elif choice == "6":
            load_from_file()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
