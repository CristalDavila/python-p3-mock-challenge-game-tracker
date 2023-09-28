class Game:
    

    def __init__(self, title):
        self.title = title
        

    @property
    def title(self):
        return self._title
        
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title)> 0 and not hasattr(self, "title"):
                self._title = title

    def results(self):
        results_list = []
        for result in Result.all:
            if isinstance(result, Result) and result.game is self:
                results_list.append(result)
        return results_list

    def players(self):
        players_list = []
        for result in self.results():
            if result.player not in players_list:
                players_list.append(result.player)
        return players_list
    

    def average_score(self, player):
        player_results = [result.score for result in player.results() if result.game is self]
        if player_results:
            return sum(player_results) /len(player_results)
        else:
            return 0

class Player:
    all = []

    def __init__(self, username):
        self.username = username

    @property
    def username(self):
            return self._username
        
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    def results(self):
        result_list = []
        for result in Result.all:
            if isinstance(result, Result)  and result.player is self:
                result_list.append(result)
        return result_list

    def games_played(self):
        games_played_list = []
        for result in self.results():
            if result.game not in games_played_list:
                games_played_list.append(result.game)
        return games_played_list
    

    def played_game(self, game):
        return any(result.game is game for result in self.results())


    def num_times_played(self, game):
        return sum(1 for result in self.results() if result.game is game)

class Result:
    all = []

    
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000 and not hasattr(self, "score"):
            self._score = score
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game

# game = Game("Skribbl.io")
# game_2 = Game("Scattegories")
# player = Player("Saaammmm")
# result_1 = Result(player, game, 2000)
# result_2 = Result(player, game, 3500)
# result_3 = Result(player, game_2, 19)

# print(result_1 in game.results())
# print(game.results())
# print(result_1)