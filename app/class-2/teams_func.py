
# example teams.py (functional approach)

def advertise(my_team):
    print(f"HEY COME TO {my_team['city'].upper()} TO SEE OUR GAMES!!!")

def full_name(my_team):
    return f"{my_team['city']} {my_team['name']}"

if __name__ == "__main__":
    teams = [
        {"city": "New York", "name": "Yankees"},
        {"city": "New York", "name": "Mets"},
        {"city": "Boston", "name": "Red Sox"},
        {"city": "New Haven", "name": "Ravens"},
        {"city": "Washington", "name": "Nationals"}
    ]

    for team in teams:
        print("-------")
        print(full_name(team))
        advertise(team)
