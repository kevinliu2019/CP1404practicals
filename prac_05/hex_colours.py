CODE_TO_COlOUR = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                "DodgerBlue3": "#1874cd", "gray": "#bebebe",
                "aquamarine1": "#7fffd4", "OldLace": "#fdf5e6",
                "aquamarine4": "#458b74", "azure1": "#f0ffff",
                "azure2": "#e0eeee", "LightCoral": "#f08080", "MediumPurple": "#9370db",
                "beige": "#f5f5dc", "DarkSalmon": "#e9967a"}
print(CODE_TO_COlOUR)

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name,
                                             CODE_TO_COlOUR.get(colour_name)))
    colour_name = input("Enter a colour name: ")
