# This is a collection of five madlibs program programmed in python3 by Monney Joshua


print("\nMADLIBS PROGRAM\n")


# Input any word that comes into your head(you are restricted to enter a specific word class) to make it more
# interesting

def campus_tour():  # This is a campus tour madlib,I've never went to a campus tour in person but only the virtual ones
    adj1 = input("adjective: ")
    noun1 = input("noun: ")
    verb1 = input("verb(past): ")
    adverb1 = input("adverb: ")
    adj2 = input("adjective: ")
    noun2 = input("noun: ")
    adj3 = input("adjective: ")
    adj4 = input("adjective: ")
    adj5 = input("adjective: ")
    verb2 = input("verb: ")
    adverb2 = input("adverb: ")
    verb3 = input("verb(past): ")
    adj6 = input("adjective: ")

    print("\nTHE CAMPUS TOUR\n")
    print(f"Today I went to the campus tour.I saw a(n) {adj1} {noun1} at the north side of the campus.\n"
          f"The touring bus {verb1} {adverb1} through the inner roads that led to the {adj2} {noun2}.\n"
          f"I got some brochures of the college which was so {adj3}.The people in charge of the campus tour\n"
          f" were so {adj4} that they gave me some snacks to enjoy.The college was very {adj5}\n"
          f"Afterwards,I had to {verb2} {adverb2} to catch the bus.When I got home I {verb3} with my mom\n"
          f"about the {adj6} day at the campus.\n")


def chess_masters():  # This is about a chess fiction which came up during my drafting
    verb1 = input("verb: ")
    adj1 = input("adjective: ")
    noun1 = input("noun: ")
    adj2 = input("adjective: ")
    adv1 = input("adverb: ")
    adj3 = input("adjective: ")

    print("\nTHE CHESS MASTER\n")
    print(f"The day I saw the chess queen {verb1} was one of the {adj1} days in my life.\n"
          f"After I saw that,the chess master played chess on his brother's {noun1} and then checkmate his brother's\n"
          f"{adj2} king which was made out of old ceramic.Later that day,I saw the chess master stalemate {adv1}\n"
          f"in front of an audience which was so {adj3}.\n")


def google_trip():  # The google madlib is very interesting
    friends_name = input("friends's name: ")
    vehicle = input("vehicle: ")
    adj1 = input("adjective: ")
    adj2 = input("adjective: ")
    adj3 = input("adjective: ")
    noun = input("noun: ")
    verb2 = input("verb(past): ")
    place = input("place: ")
    verb3 = input("verb: ")

    print("\nTHE GOOGLE VISIT\n")
    print(f"Last month,I went to the Google company with {friends_name}.We traveled by {vehicle}.Finally we arrived\n"
          f"and it was very {adj1}.I wish it had been more {adj2},but it wasn't anyway.We visited their {adj3}\n"
          f"server room called Google {noun}.{friends_name} nearly fainted when we entered their cafeteria.\n"
          f"Later,we went to their apartments and {verb2}.Next year,I want to go to {place},where we can {verb3}.\n")


def video_games():  # A talk about video games
    noun1 = input("noun(plural): ")
    verb1 = input("verb( -ing): ")
    noun2 = input("noun(plural): ")
    noun3 = input("noun: ")
    adj = input("adjectives: ")

    print("\nVIDEO GAMES ARE AMAZING\n")
    print(f"When I go to game centres with my {noun1} there are lots of games to play.In a car racing game you need\n"
          f"to beat every computerized vehicle that you are {verb1} against.There are a whole lot of other games.\n"
          f"When you play some games you win {noun2} for certain scores.Once you're done you can cash in your tickets\n"
          f"to get a big {noun3}.You can save your progress for another time.So far I have had a lot of fun every time\n"
          f"I've been to these {adj} game centres.\n")


def the_labyrinth():  # A bit like the greek story of a guy who met a beast in a maze
    adj1 = input("adjective: ")
    adj2 = input("adjective: ")
    adj3 = input("adjective: ")
    noun1 = input("noun: ")
    adj4 = input("adjective: ")
    adj5 = input("adjective: ")
    noun2 = input("noun: ")
    verb1 = input("verb: ")
    noun3 = input("noun: ")
    adj6 = input("adjective: ")
    verb2 = input("verb: ")
    adj7 = input("adjective: ")
    adj8 = input("adjective: ")

    print("\nTHE LABYRINTH\n")
    print(f"I walk through the maze.I take out my {adj1} map.There's a {adj2} beast with a {adj3} {noun1} in his\n"
          f"mouth standing right in front of me in the {adj4} recesses. I gaze at his {adj5} {noun2}.A sudden sound \n"
          f"awakes me from my daydream! A dragon {verb1} in front of my head with a flaming nose.I remember I have a\n"
          f"packet of {noun3} that makes me go into a deep slumber.I return back to that maze again this time that\n"
          f"{adj6} beast charging on me.I {verb2} away through the {adj7} labyrinth.I meet my parents at the outside.\n"
          f"Phew! It's being a(n) {adj8} day in the maze\n")


campus_tour()
chess_masters()
google_trip()
video_games()
the_labyrinth()
play_again = input("\nPlay again Y/N: ")  # This is a play again command,you can play again or terminate the program
if play_again.lower() == "y":
    campus_tour()
    chess_masters()
    google_trip()
    video_games()
    the_labyrinth()
else:
    quit()
