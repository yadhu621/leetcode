competitions = [
  ["HTML", "Java"],
  ["Java", "Python"],
  ["Python", "HTML"],
  ["C#", "Python"],
  ["Java", "C#"],
  ["C#", "HTML"],
  ["SQL", "C#"],
  ["HTML", "SQL"],
  ["SQL", "Python"],
  ["SQL", "Java"]
]

results = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1]

# 1 

def tournamentWinner(competitions, results):
  
  scores = {}
  
  for i in range(len(competitions)):
    
    hometeam = competitions[i][0]
    awayteam = competitions[i][1]

    if results[i]:
      scores[hometeam] = scores.get(hometeam, 0) + 3
    else:
      scores[awayteam] = scores.get(awayteam, 0) + 3

  highest_score = 0

  for team, score in scores.items():
    if score > highest_score:
      highest_score += score
      highest_scoring_team = team

  return highest_scoring_team
  
# tournamentWinner(competitions=competitions, results=results)
print(tournamentWinner(competitions=competitions, results=results))