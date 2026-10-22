class Player:
  def __init__(self, name: str, position: str):
    self.name = name
    self.position = position


class Team:
  def __init__(self, name: str):
    self.name = name
    self.players = []

  def add_player(self, player: Player):
    self.players.append(player)


player_one = Player("Alex", "Forward")
player_two = Player("Sam", "Goalkeeper")

red_team = Team("Red Dragons")

red_team.add_player(player_one)
red_team.add_player(player_two)

print(red_team.name)
for player in red_team.players:
  print(player.name, player.position)
