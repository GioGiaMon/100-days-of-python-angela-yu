# PAUSE 1
# Create a function called format_name() that takes two inputs: f_name and `l_name'.
def format_name(f_name, l_name):
    # Use the title() function to modify the f_name and l_name parameters into Title Case.
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    # print(f"{formatted_f_name} {formatted_l_name}")
    return f"{formatted_f_name} {formatted_l_name}"

formatted_name = format_name("ANGEla", "yU")
print(f"{formatted_name}")
