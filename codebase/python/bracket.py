#Working with creating bracket classes and subclasses... this might not end up being necessary in the long run


class Bracket:
    def __init__(self, regions):
        self.north = [region for region in regions if region=="north"][0]
        self.east = [region for region in regions if region=="east"][0]
        self.west = [region for region in regions if region=="west"][0]
        self.midwest = [region for region in regions if region=="midwest"][0]
        

class Region:
    def __init__(self, region_name, teams):
        self.name = region_name

        matchup_nums = [1,16,8,9,5,12,4,13,6,11,3,14,7,10,2,15] 
        matchups = []
        for m_num in matchup_nums:
            try:
                matchups.append([team for team in teams if team.ranking == m_num][0])
            except:
                matchups.append(m_num)
        self.matchups = matchups

    def get_games(self):
        matchups = self.matchups
        games = []
        for match in range(0,len(matchups),2):
            games.append((matchups[match],matchups[match+1]))
        return games


class Team:
    def __init__(self, team_name, ranking, region):
        self.name = team_name
        self.ranking = ranking
        self.region = region
