#%%

# puanlarının max'ını buldurduğumda, çıkan puanın hangi
# takıma ait olduğunu nasıl otomatik buldururum?

import random


def points(won,draw,lost):
    return (won * 3 + draw + lost * 0)


random.seed(1)
team_A =  {
    "name" : "team A",
    "win" : random.randrange(15,26), #btw 15-25
    "draw" : random.randrange(3,7), # btw 3-6
}
team_A ["lose"] =  30 - (team_A["win"] + team_A["draw"])

team_B =  {
    "name" : "team B",
    "win" : random.randrange(15,26), #btw 15-25
    "draw" : random.randrange(3,7), # btw 3-6
}
team_B ["lose"] =  30 - (team_B["win"] + team_B["draw"])

team_C =  {
    "name" : "team C",
    "win" : random.randrange(15,26), #btw 15-25
    "draw" : random.randrange(3,7), # btw 3-6
}
team_C ["lose"] =  30 - (team_C["win"] + team_C["draw"])

team_A["points"] = points(team_A["win"],team_A["draw"],team_A ["lose"])
team_B["points"] = points(team_B["win"],team_B["draw"],team_B ["lose"])
team_C["points"] = points(team_C["win"],team_C["draw"],team_C ["lose"])

# teams = [team_A , team_B, team_C] # listeyi dict'ten oluşturamıyon

teams = {
        "team A" : team_A,
        "team B" : team_B,
        "team C" : team_C
}

print(teams)
print("***")
print(teams["team A"])
print("***")
print(teams["team A"]["points"]) # oha işe yarıyo
print("devamm**************")
#
# # işe yaramıyor
# for team in teams[:]: 
#     for points in team["points"]:
#         print(points)
# 


# """
# for tms in teams.values():
#     for pts in tms.values():
#         print(pts["points"])
# """

for key in teams:
    print(teams[key]["name"], "'s point is:",teams[key]["points"],)

winner_team = "N/A"
winner_point = -1

for key in teams:
    if(teams[key]["points"] > winner_point):
        winner_team = teams[key]["name"]
        winner_point = teams[key]["points"]

print("champ of leauge is: {var1}\nchamp's point is: {var2}".format(var1 = winner_team, var2 = winner_point))






# %%
