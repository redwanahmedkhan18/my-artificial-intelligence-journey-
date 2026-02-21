class Player:
    team_run = 0   

    def __init__(self, name):
        self.name = name
        self.run = 0

    def hit_one(self):
        self.run += 1
        Player.team_run += 1

    def no_ball(self):
        Player.team_run += 1   # extra run

    def wide_ball(self):
        Player.team_run += 1   # extra run

    def bye(self):
        Player.team_run += 2   # extra runs

    def two_run(self):
        self.run += 2
        Player.team_run += 2

    def three_run(self):
        self.run += 3
        Player.team_run += 3

    def four_run(self):
        self.run += 4
        Player.team_run += 4

    def six_run(self):
        self.run += 6
        Player.team_run += 6

    def show_player_run(self):
        print(f"{self.name} run: {self.run}")

    @classmethod
    def show_team_run(cls):
        print(f"Team run: {cls.team_run}")



Player1=Player("Adnan")
Player1.six_run()
Player1.no_ball()
Player1.wide_ball()
Player1.six_run()
Player1.two_run()
Player1.three_run()
Player1.four_run()
Player1.six_run()
Player1.six_run()
Player1.four_run()
Player1.two_run()
Player1.six_run()

print(f"{Player1.name} run: {Player1.run}")

Player2=Player("Rafsan")
Player2.no_ball()
Player2.four_run()
Player2.no_ball()
Player2.six_run()
Player2.four_run()
Player2.six_run()
Player2.no_ball()
Player2.three_run()
Player2.three_run()
Player2.six_run()
Player2.six_run()
Player2.six_run()
Player2.six_run()
print(f"{Player2.name} run: {Player2.run}")
print(f"Team run: {Player.team_run}")
