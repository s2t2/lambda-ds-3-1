

class Team():

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

if __name__ == "__main__":
    team = Team("Terriers", "Hometown")
    print(team.full_name)

    team2 = Team("Yankees", "New York")
    print(team2.full_name)
