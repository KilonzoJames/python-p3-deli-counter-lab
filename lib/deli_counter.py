katz_deli = ["Jack"]

def line(my_list):
    if len(my_list)==0:
        print("The line is currently empty.")
    else:
        line_message = "The line is currently:"
        for idx, person in enumerate(my_list, start=1):
            line_message += f" {idx}. {person}"
        print(line_message)
print(line(katz_deli))

def take_a_number(my_list, element):
    my_list.append(element)
    position = len(my_list)
    print(f'Welcome, {element}. You are number {position} in line.')
print(take_a_number(katz_deli, 'Shelby'))

def now_serving(my_list):
    if len(my_list) == 0:
        print("There is nobody waiting to be served!")
    else:
        serving_person = my_list.pop(0)
        print(f"Currently serving {serving_person}.")
print(now_serving(katz_deli))
