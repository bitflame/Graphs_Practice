def tennis_score(score, player1_name, player2_name):
    points = {0: 'Love', 1: 'Fifteen', 2: 'Thirty', 3: 'Fourty'}
    scores = list(score.split(":"))
    player1_score = int(scores[0])
    player2_score = int(scores[1])
    if player1_score > 1 + player2_score and player1_score > 4:
        return "Game {player1_name}"
    elif player2_score > 1 + player1_score and player2_score > 4:
        return "Game {player2_name}"
    elif player1_score == player2_score and player1_score > 4:
        return "Deuce"
    else:
        return "".join(points[player1_score]+" "+points[player2_score])


print(f'Test 1- 1:0, Micha, Tim. Expected output: Fifteen Love. Actual output: {tennis_score("1:0", "Micha", "Tim")}')

def extract_points(score):
    values = score.strip().split(":")
    if len(values)!=2:
        raise ValueError("illegal format -- scofre has not "+
                         "format <points>:<points>, e.\,g. 7:6")
    score1 = int(values[0])
    score2 = int(values[1])
    if score1 < 0 or score2 < 0:
        raise ValueError("points must be > 0")
    if (score1 > 4 or score2 > 4) and abs(score1-score2)>2:
        raise ValueError("point difference must be < 3, "+
                         "otherwise invalid score")
    return score1, score2
