#Function with Outputs

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't enter valid inputs."
    formatted_f_name = (f_name.title())
    formatted_l_name = (l_name.title())
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("ChArLoTTe", "mCkNIght"))

