from __future__ import division


# Set up the player object and the needed stats
class Player(object):
    def __init__(self, name, pos, gp, goals, assists, img):
        '''
        __init__ assigns param values to variables to construct the format for players data
        '''
        self.name = name
        self.position = pos
        self.games_played = gp
        self.goals = goals
        self.assists = assists
        self.points = int(self.goals + self.assists)
        self.goals_per_game = round(self.goals / self.games_played, 3)
        self.assists_per_game = round(self.assists / self.games_played, 3)
        self.points_per_game = round(self.points / self.games_played, 3)
        self.img = img


# Create player instances
class PlayerData(object):
    def __init__(self):
        '''
        __init__ sets private variables to an instance of Player by passing Params to player class
        These are private to keep the data from being easily changed. 
        '''
        self.__gretzkey = Player("Wayne Gretzkey", "Forward", 1487, 894, 1963, '../img/gretzkey.jpg')
        self.__messier = Player("Mark Messier", "Forward", 1756, 694, 1193, '../img/messier.jpg')
        self.__jagr = Player("Jaromir Jagr", "Forward", 1629, 749, 1119, '../img/jagr.jpg')
        self.__howe = Player("Gordie Howe", "Forward", 1767, 801, 1049, '../img/howe.jpg')
        self.__francis = Player("Ron Francis", "Forward", 1731, 549, 1249, '../img/francis.jpg')
        # self.__players is used to structure links. The full name is used for display, last name for get data
        self.__players = [["Wayne Gretzkey", "gretzkey"], ["Mark Messier", "messier"], ["Jaromir Jagr", "jagr"],["Gordie Howe", "howe"], ["Ron Francis", "francis"]]

    # Set up getters for data and return player data
    @property
    def gretzkey(self):
        '''
        Getter returns the player data for Gretzkey
        '''
        return self.__gretzkey

    @property
    def messier(self):
        '''
        Getter returns the player data for Messier
        '''
        return self.__messier

    @property
    def jagr(self):
        '''
        Getter returns the player data for Jagr
        '''
        return self.__jagr

    @property
    def howe(self):
        '''
        Getter returns the player data for Howe
        '''
        return self.__howe

    @property
    def francis(self):
        '''
        Getter returns the player data for Francis
        '''
        return self.__francis

    # Getter used to return __players array
    @property
    def player_list(self):
        '''
        Getter returns the player data for __players
        '''
        return self.__players

    def player_data(self, player):
        '''
        player_data contains the logic for which data to return. An instance of PlayerData is created, the player param is assigned to
         p, and name is set to the lowercase of p.

         Then name is run through if/elif to determine what to return. If name doesn't match any of the data false is returned and an
         error page is displayed.
        '''
        # set p to player param
        p = player
        # ensure that p is passed in all lowercase
        name = p.lower()
        # check if name is equal to...
        if name == "gretzkey":
            # Assign player_info to value of players getter
            player_info = self.gretzkey
            # return player_info
            return player_info
        elif name == "messier":
            # Assign player_info to value of players getter
            player_info = self.messier
            # return player_info
            return player_info
        elif name == "jagr":
            # Assign player_info to value of players getter
            player_info = self.jagr
            # return player_info
            return player_info
        elif name == "howe":
            # Assign player_info to value of players getter
            player_info = self.howe
            # return player_info
            return player_info
        elif name == "francis":
            # Assign player_info to value of players getter
            player_info = self.francis
            # return player_info
            return player_info
        # If no match is found than return false
        else:
            return False



