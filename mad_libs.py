def mad_libs():
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")

    mad_lib = f"The {adjective} {noun} {verb} to the {place}."
    print(mad_lib)

mad_libs()
