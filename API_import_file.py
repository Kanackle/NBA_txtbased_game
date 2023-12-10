from nba_api.stats.endpoints import playercareerstats, playerdashboardbyteamperformance, commonteamroster, teamdetails
from nba_api.stats.static import players, teams
import random

#in a list of dictionaries that each contain multiple key value pairs, 
#where each dictionary has the same key but different values 
#how can I return the value of first key from each dictionary?
allTeamsDetails = teams.get_teams()
allTeamsID = [d.get('id') for d in allTeamsDetails]
print(allTeamsID)

# for i in range(len(allTeamsID)):
#     print(teams.find_team_name_by_id(allTeamsID[i]))

# for j in range(3):
#     nbaTeam = commonteamroster.CommonTeamRoster(allTeamsID[j])
#     nbaTeamRoster = nbaTeam.get_data_frames()[0]
#     print(nbaTeamRoster)

#Find Stephen Curry's player ID (201939)
#sCurry = players.find_players_by_full_name('Curry')
curryCareer = playercareerstats.PlayerCareerStats(player_id=201939)
#Take the average of  3P FG% of the last 3 years
lastThreeYearsStats = curryCareer.get_data_frames()[0].iloc[-4:-1]
print(lastThreeYearsStats)
#Average FG% of last 3 years
lastThreeYearsFG = round(lastThreeYearsStats['FG_PCT'].mean(),3)
#lastThreeYearsFG = round(curryCareer.get_data_frames()[0].iloc[-4:-1,'FG_PCT'].mean(),3)
print(f"POTATO {lastThreeYearsFG}")
#Average 3FG% of last 3 years
lastThreeYearsFG3 = round(lastThreeYearsStats['FG3_PCT'].mean(),3)
#Average FT% of last 3 years
lastThreeYearsFT = round(lastThreeYearsStats['FT_PCT'].mean(),3)
#Convert to string
convertToStr = str(lastThreeYearsFG3)
FG3A = lastThreeYearsStats['FG3A'].sum()
FGA = lastThreeYearsStats['FGA'].sum()
FTAperGame = round(round(lastThreeYearsStats['FTA'].sum()) / (round(lastThreeYearsStats['GP'].sum())))
FG3ratio = round(FG3A/FGA,3)
#print(FG3ratio)
#print(lastThreeYearsFG)
#print("Stephen Curry's 3P% for the last 3 years is " + convertToStr)

#Keep track of shots MADE
#FGMshots = 0
#FG3Mshots = 0

################################################
#Generate a simulation of 10 games
for w in range(10):
    #Keep track of shots MADE
    FGMshots = 0
    FG3Mshots = 0
    FTMshots = 0
    #Introduce a hot streak by inflating percentages if/when a player makes multiple shots in a row
    hotStreak = 0
    fakeFGM = lastThreeYearsFG
    fakeFG3M = lastThreeYearsFG3
    #Generate random number of shots taken, then determine the ratio of 2 point shots and 3 point shots ATTEMPTED
    randShots = random.randrange(10,20)
    FGAshots = round(randShots*(1-FG3ratio))
    FG3Ashots = round(randShots*FG3ratio)
    for x in range(FGAshots):
        randFG = random.random()
        if randFG <= lastThreeYearsFG:
            FGMshots += 1
            hotStreak += 1
            # print(f"HOTSTREAK = {hotStreak}")
            if hotStreak >= 3:
                fakeFGM = fakeFGM + round(hotStreak*0.015)
                # print(f"how big is it? {fakeFGM}")
        else:
            hotStreak = 0
            fakeFGM = lastThreeYearsFG
    hotStreak = 0  
    for y in range(FG3Ashots):
        randFG3 = random.random()
        if randFG3 <= lastThreeYearsFG3:
            FG3Mshots += 1
            hotStreak += 1
            # print(f"HOTSTREAK = {hotStreak}")
            if hotStreak >= 3:
                fakeFG3M = fakeFG3M + round(hotStreak*0.025)
                # print(f"how big is it? {fakeFG3M}")
        else:
            hotStreak = 0
            fakeFG3M = lastThreeYearsFG3
    hotStreak = 0
    for z in range(FTAperGame):
        randFT = random.random()
        if randFT <= lastThreeYearsFT:
            FTMshots += 1
    #Keep track of TOTAL POINTS
    FGpoints = FGMshots * 2
    FG3points = FG3Mshots * 3
    totalPoints = FGpoints + FG3points + FTMshots
    print(f"Game {w+1}: Stephen Curry shot {FGMshots} of {FGAshots} and {FG3Mshots} of {FG3Ashots} from downtown plus {FTMshots} free throws for {totalPoints} points")    
 #print(randShots,FGAshots,FGMshots, FG3Ashots, FG3Mshots)

#print(FGpoints, FG3points, totalPoints)
#Find stats for player ID 203999 (Nikola Jokic)
#career = playercareerstats.PlayerCareerStats(player_id='203999')
#print(career.get_data_frames()[0])