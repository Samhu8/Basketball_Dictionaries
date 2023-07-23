
#  Challenge 1: Update the Constructor
# Update the constructor to accept a dictionary with a single player's
# information instead of individual arguments for the attributes.

class Player:
    def __init__(self,player_dict):
        self.player_dict = player_dict

    @classmethod
    def get_team(cls,team_list):
        new_group =[]
        for player in team_list:
            player = Player(player)
            new_group.append(player)


# Challenge 2: Create instances using individual player dictionaries.
"""
Given these variables, create Player instances for each of the following dictionaries.
Be sure to instantiate these outside the class definition, in the outer scope.
"""

kevin = {
    "name":"Kevin Durant",
    "age":34,
    "position":"small forward",
    "team":"Brooklyn Nets"
}
jason = {
    "name":"Jason Tatum",
    "age":24,
    "position":"small forward",
    "team":"Boston Celtics"
}
kyrie = {
    "name":"Kyrie Irving",
    "age":32,
    "position":"Point Guard",
    "team":"Brooklyn Nets"
}

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

# Challenge 3: Make a list of Player instances from a list of dictionaries
"""
Finally, given the example list of players at the top of this module (the one with many players)
write a for loop that will populate an empty list with Player objects from the original list of dictionaries.
"""

players = [
    {
    	"name": "Kevin Durant",
    	"age":34,
    	"position": "small forward",
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum",
    	"age":24,
    	"position": "small forward",
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving",
    	"age":32, "position": "Point Guard",
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard",
    	"age":33, "position": "Point Guard",
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid",
    	"age":32, "position": "Power Foward",
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "",
    	"age":16,
    	"position": "P",
    	"team": "en"
    }
]



new_team =[]
for player in players:
    player = Player(player)
    new_team.append(player)

print(new_team)