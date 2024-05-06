from models.food_type import Food_type
from models.restaurant import Restaurant

def exit_program():
    print("Goodbye!")
    exit()

def list_food_types():
    food_types = Food_type.get_all()
    for food_type in food_types:
        print(food_type)

def find_food_type_by_id():
    id_ = input("Enter the food type's id: ")
    food_type = Food_type.find_by_id(id_)
    print(food_type) if food_type else print(f'Food type {id_} not found')

def find_food_type_by_name():
    name = input("Enter the food type's name: ")
    food_type = Food_type.find_by_name(name)
    print(food_type) if food_type else print(
        f'Food type {name} not found')


def create_department():
    new = input("Enter a new food type: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)

    
    input_food_type,
    update_food_type,
    delete_food_type,
    list_restaurants,
    find_restaurant_by_name,
    find_restaurant_by_id,
    input_restaurant,
    update_restaurant,
    delete_restaurant,
    list_restaurants_by_food_type