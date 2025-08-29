def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))

# multiple returns on the same function.
def format_name_v2(f_name, l_name):
    # check they are no t empty
    if f_name == "" or l_name == "":
        return "You dini not provide valid input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name_v2(input("What is your first name? "), input("What is your last name? ")))