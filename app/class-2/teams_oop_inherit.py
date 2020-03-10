

class Team():
    var1 = "Something"

    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return f"<Team {self.city} {self.name}>"

    def __repr__(self):
        return f"<Team {self.city} {self.name}>"

    @property
    def full_name(self):
        return f"{self.city} {self.name}"

    def advertise(self):
        print(f"HELLO PLEASE COME TO {self.city.upper()} TO SEE OUR GAMES!")

    @staticmethod
    def advertise_generically():
        print("HELLO PLEASE COME TO OUR GAMES!")

class BaseballTeam(Team):
    def __init__(self, name, city, league):
        super().__init__(name, city)
        self.league = league

    def advertise(self):
        print(f"WE'RE THE BEST IN THE {self.league} LEAGUE")

if __name__ == "__main__":
    team = Team("Terriers", "Hometown")

    baseball_team = BaseballTeam("Yankees", "New York", "American")

    breakpoint()
