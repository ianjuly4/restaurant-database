from helpers import (
    exit_program,
    list_food_types,
    find_food_type_by_id,
    find_food_type_by_name,
    input_food_type,
    update_food_type,
    delete_food_type,
    #list_restaurants,
    #find_restaurant_by_name,
    #find_restaurant_by_id,
    #input_restaurant,
    #update_restaurant,
    #delete_restaurant,
    #list_restaurants_by_food_type
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_food_types()
        elif choice == "2":
            find_food_type_by_id()
        elif choice == "3":
            find_food_type_by_name()
        elif choice == "4":
            input_food_type()
        elif choice == "5":
            update_food_type()
        elif choice == "6":
            delete_food_type()
        elif choice == "7":
            list_restaurants()
        elif choice == "8":
            find_restaurant_by_name()
        elif choice == "9":
            find_restaurant_by_id()
        elif choice == "10":
            input_restaurant()
        elif choice == "11":
            update_restaurant()
        elif choice == "12":
            delete_restaurant()
        elif choice == "13":
            list_restaurants_by_food_type()
        else:
            print("Please pick a valid choice.")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all food types")
    print("2. Find food type by name")
    print("3. Find food type by id")
    print("4: Create food type")
    print("5: Update food type")
    print("6: Delete food type")
    print("7. List all restaurants")
    print("8. Find restaurant by name")
    print("9. Find restaurant by id")
    print("10: Create restaurant")
    print("11: Update restaurant")
    print("12: Delete restaurant")
    print("13: List all restaurants in a food type")


if __name__ == "__main__":
    main()