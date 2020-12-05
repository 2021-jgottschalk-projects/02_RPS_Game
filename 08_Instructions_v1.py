

# Functions go here...
def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


def instructions():
    print()
    print("**** How to Play ****")
    print()
    print("Choose either a number of rounds or "
          "press <enter> for infinite mode")
    print()
    print("Then for each round, choose from rock \n"
          "/ paper / scissors (or xxx to quit)")
    print("You can type r / p / s / x if you \n"
          "don't want to type the entire word.")
    print()
    print("The rules are...\n"
          "- Rock beats scissor\n"
          "- Scissors beats paper\n"
          "- Paper beats rock")
    print()
    print("*** Have fun ***")
    print()
    return ""


# Main Routine goes here...
yes_no_list = ["yes", "no"]
played_before = choice_checker("Have you played the "
                               "game before? ", yes_no_list,
                               "Please type yes / no")

if played_before == "no":
    instructions()

print("Program continues")
