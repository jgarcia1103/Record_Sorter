# I made this program to help myself and others organize their vinyl collections as a fun side project.

import os

# This function checks if the records.txt file exists. If it doesn't, it creates one for you to store your records.
def create_file_if_not_exists():   
    if not os.path.exists("records.txt"):
        with open("records.txt", 'w') as f:
            pass
        print("Records file created.")
    else:
        print("Records file already exists.")

# This function lets you add new records as you expand your collection by prompting you for the artist, album, and year of release. It saves your records for easy access.
def add_record():   
    while True:
        artist = input("Enter artist name (or type 'sort' to sort your records): ")
        
        if artist.lower() == "sort":
            view_records()
            break
       
        album = input("Enter album name: ")
        year = input("Enter year released: ")

        with open("records.txt", 'a') as f:
            f.write(f"{artist}|{album}|{year}\n")

        print(f'"{album}" by {artist} ({year}) added!')

# This function shows you which records are in your records.txt file and sorts them alphabetically by artist, then by year, and finally by album name for easy browsing.
def view_records():   
    with open("records.txt", 'r') as f:
        lines = f.readlines()

    if not lines:
        print("No records found.")
        return
    
    records = []
    for line in lines:
        parts = line.strip().split("|")
        records.append((parts[0], parts[1], parts[2]))

    records.sort(key=lambda r: (r[0].lower(), int(r[2]), r[1].lower()))

    print("\n--- Your Vinyl Collection ---")
    for artist, album, year in records:
        print(f"{artist} | {album} | {year}")
    print("-----------------------------")

# This function allows you to search your catalog of records by artists name for when your collection gets to big to easily browse :)
def search_by_artist():       
    search = input("Enter artist name to search: ")

    with open("records.txt", "r") as f:
        lines = f.readlines()

    results = []
    for line in lines:
        parts = line.strip().split("|")
        if parts[0].lower() == search.lower():
            results.append((parts[0], parts[1], parts[2]))

    if not results:
        print(f"No records found for '{search}'.")
        return
    
    results.sort(key=lambda r: (int(r[2]), r[1].lower()))

    print(f"\n--- Records by {search} ---")
    for artist, album, year in results:
        print(f"{artist} | {album} | {year}")
    print("-----------------------------")

# This function lets you delete records from your collection if you ever misplace a record or decide to part ways with one.
def delete_record():           
    with open("records.txt", "r") as f:
        lines = f.readlines()

    if not lines:
        print("No records to delete.")
        return
    records = []
    for line in lines:
        parts = line.strip().split("|")
        records.append((parts[0], parts[1], parts[2]))
    records.sort(key=lambda r: (r[0].lower(), int(r[2]), r[1].lower()))

    print("\n--- Select a Record to Delete ---")
    for i, (artist, album, year) in enumerate(records):
        print(f"{i + 1}. {artist} | {album} | {year}")
    
    choice = input("\nEnter the number of the record to delete (or 'cancel' to go back): ")

    if choice.lower() == "cancel":
        print("Cancelled.")
        return
    if not choice.isdigit() or not (1 <= int(choice) <= len(records)):
        print("Invalid choice.")
        return
    
    removed = records.pop(int(choice) - 1)

    with open("records.txt", "w") as f:
        for artist, album, year in records:
            f.write(f"{artist}|{album}|{year}\n")

    print(f"Deleted: {removed[1]} by {removed[0]} ({removed[2]})")

# This is the main menu function that ties everything together and allows you to navigate through the different features of the program.
def menu():               
    create_file_if_not_exists()
    while True:
        print("\n--- Vinyl Record Sorter ---")
        print("1. Add a record")
        print("2. Delete a record")
        print("3. Search by artist")
        print("4. View all records")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_record()
        elif choice == "2":
            delete_record()
        elif choice == "3":
            search_by_artist()
        elif choice == "4":
            view_records()
        elif choice == "5":
            print("Later!")
            break
        else:
            print("Invalid choice, try again.")

menu()