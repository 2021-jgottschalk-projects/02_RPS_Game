game_summary = []

win = 0
lose = 0
tie = 0

for item in range(0, 5):
    result = input("choose result: ")

    outcome = "Round {}: {}".format(item, result)

    if result == "win":
        win += 1
    elif result == "lose":
        lose += 1
    else:
        tie += 1

    game_summary.append(outcome)

games_played = win + lose + tie

# **** Calculate Game Stats ******
percent_win = win / games_played * 100
percent_lose = lose / games_played * 100
percent_tie = tie / games_played * 100

print()
print("***** Game Summary *******")
for game in game_summary:
    print(game)

print()

# displays game stats with % values to the nearest whole number
print("******* Game Statistics ********")
print("Win: {}, ({:.0f}%)\nLoss: {}, ({:.0f}%)\nTie: {}, ({:.0f}%)".format(win, percent_win, lose, percent_lose, tie,
                                                                           percent_tie))
