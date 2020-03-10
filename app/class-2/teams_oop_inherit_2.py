


def enlarge_again():
    print("DOING SOME STUFF")

class Team():
    def __init__(self, city, name, players):
        self.city = city
        self.name = name
        self.players = players

    @property
    def full_name(self):
        """
        Prints the full team name, including the city.
        """
        return f"{self.city} {self.name}"

    def count_players(self):
        """
        Count the number of players on a team.
        """
        return len(self.players)

    def advertise(self):
        print(f"HEY COME TO {self.city} TO SEE OUR GAMES!!!!!")

class BaseballTeam(Team):
    def __init__(self, city, name, players, starting_pitcher):
        super().__init__(city, name, players)
        self.starting_pitcher = starting_pitcher

    def advertise(self):
        print(f"HEY COME TO {self.city} TO SEE OUR BASEBALL GAMES!!!!! TO SEE OUR STARTING PITCHER {self.starting_pitcher}")

if __name__ == "__main__":

    #team = {"city": "New York", "name": "Yankees", "players": ["A"]}
    #team2 = {"city": "New York", "name": "Mets", "players": ["B", "C"]}
    #team3 = {"city": "Boston", "name": "Red Socks", "players": ["D", "E", "F"]}

    team = Team("New York", "Giants", [])
    print(team.name)
    #print(team.full_name())
    print(team.full_name)
    print(team.count_players())
    team.advertise()

    baseball_team = BaseballTeam("New York", "Yankees", [], "John Snow")
    print(baseball_team.full_name)
    print(baseball_team.starting_pitcher)
    baseball_team.advertise()
