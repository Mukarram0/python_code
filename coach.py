coach=input("select coach: sleeper, ac, general, luxury: ").lower()
match coach:
    case 'sleeper':
        print("cheap and comfortable")
    case"ac":
        print(" ac conditioned coach and better comfort with space")
    case 'general':
        print("very cheap")
    case 'luxury':
        print("free food , full Ac conditioned room, lots of spaces, private chamber")
    case _:
        print("invalid choice ")
