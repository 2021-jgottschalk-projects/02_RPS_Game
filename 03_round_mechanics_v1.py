# functions go here


# checks that a number is an
# integer more than zero
def int_check(num_to_check):

    try:
        response = int(num_to_check)

        if response <= 0:
            response = "not ok"

    except ValueError:
        response = "not ok"

    return response


# Main routine goes here
mode = ""
num_rounds = ""

# ask for number of rounds and check that it
# is either <enter> or an integer more than 0
valid_rounds = False
while not valid_rounds:
    num_rounds = input("Number of rounds (press "
                       "<enter> for infinite mode)? ")

    if num_rounds == "":
        # Set rounds to arbitrary number.  We will
        # increase this each round in infinite mode
        # (see later code)
        num_rounds = 99
        mode = "infinite"
        valid_rounds = True
    else:
        num_rounds = int_check(num_rounds)
        if num_rounds == "not ok":
            # if answer is invalid, go back to start of loop
            continue
        else:
            valid_rounds = True

# Initialise round counter (and win / loss counters)
rounds_played = 0

# Loop game for # of rounds
# (or until exit code is received)
for item in range(0, num_rounds):

    # Add 1 to rounds played
    rounds_played += 1

    # Add 1 to number of rounds each time so
    # that game continues until exit code is entered.
    if mode == "infinite":
        num_rounds += 1

    print("Round {}".format(rounds_played))

    # Get user choice
    choice = input("Choice")
    print(choice)

    # end loop if exit code chosen
    if choice == "xxx":
        break
