class Player:
    def __init__(self, race, level):
        self.race = race
        self.level = level

class Guild:
    def __init__(self, master, members_number):
        self.master = master
        self.members_number = members_number
        self.marshals = []
        self.members = []

    def add_member(self, member):
        if len(self.members) < 200:
            self.members.append(member)
            return True
        return False

    def add_marshal(self, member):
        if len(self.marshals) < 2:
            self.marshals.append(member)
            return True
        return False

    def get_average_level(self):
        lvl = 0
        for i in self.members:
            lvl += i.level
        return lvl / len(self.members)

    def get_race_number(self, race):
        n = 0
        for i in self.members:
            if i.race == race:
                n += 1
        return n


yato = Player('warrior', 93)
lies = Player('assassin', 101)
Potter = Player('mage', 8)

Arcane = Guild('ash', 11)

Arcane.add_member(yato)
Arcane.add_member(lies)
Arcane.add_member(Potter)

print(Arcane.get_average_level())
print(Arcane.get_race_number('warrior'))