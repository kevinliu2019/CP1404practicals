import wikipedia

print("What do you want to search on Wikipedia?")
search_input_one = input("")
for i in search_input_one:
    if search_input_one is None:
        break
    elif search_input_one == "Monty":
        print("Disambiguation!")
    else:
        search_output_one = wikipedia.search(search_input_one)
        print(search_output_one)
        print("Please chose:")
        search_input_two = input("")
        search_output_two = wikipedia.summary(search_input_two)
        search_output_three = wikipedia.page(search_input_two)
        search_output_four = search_output_three.title
        search_output_five = search_output_three.url
        search_output_six = search_output_three.content
        print(search_output_two)
        print(search_output_three)
        print(search_output_four)
        print(search_output_five)
        print(search_output_six)
    print("What do you want to continue to search on Wikipedia?")
    search_input_one = input("")
