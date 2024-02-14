def format_name(f_name,l_name): #parameters
    fullname = f_name.title() + " " + l_name.title()
    return f"{fullname}"
    
newname = format_name("AnGEla","ANGELA") #arguments
print(newname)