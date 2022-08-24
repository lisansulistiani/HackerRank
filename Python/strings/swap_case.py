def swap_case(s):
    string_out = ""
    for item in list(s):
        if(item.islower()):
            string_out+=item.upper()
        else:
            string_out+=item.lower()
    return string_out

