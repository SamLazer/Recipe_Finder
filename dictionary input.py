# **** recipe search using dictionaries ****
# program takes input for 3 food items at a time. It will ask you if you would like to add three more food items.
# It concatenates the strings you write and uses them to search allrecipes.com

# import web browser
import webbrowser

# declare empty lists
food_name_1 = []

# question to add food list entry function


def food_input():
    add_entry = input("Would you like to make some food? type yes or no:")
    # question loop
    while add_entry == 'yes':
        # food 1 entry to list
        food_1 = input("enter a type of food item #1 ")
        food_name_1.append(food_1)
        # food 2 entry to list
        food_2 = input("enter a type of food item #2 ")
        food_name_1.append(food_2)
        # food 3 on entry to list
        food_3 = input("enter a type of food item #3 ")
        food_name_1.append(food_3)
        # add new entry or break loop
        add_entry = input("Would you like to add another set of items for another dish? type yes or no: ")

        if add_entry == 'no':
            break
    sorted(food_name_1)

    # join list
    food_name_join = ' '.join(food_name_1)

    # all recipes search items
    webbrowser.open('http://allrecipes.com/search/results/?wt=' + food_name_join + '&sort=re')

# call function


food_input()




























