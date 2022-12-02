shape_to_score = {'A': 1, 'B': 2, 'C':3, 'X': 1, 'Y': 2, 'Z':3}
outcome_decider = {'AX': 'draw', 'AY': 'won', 'AZ':'lose','BX':'lose'
    ,'BY':'draw','BZ':'won','CX':'won','CY':'lose','CZ':'draw'}
outcome_to_score = {'lose': 0, 'draw': 3, 'won':6}

score = 0
score_second = 0
for i in open('day2_data.txt').read().splitlines():
    opponent_play, your_play = i.split(' ')
    score+=shape_to_score[your_play]
    score+=outcome_to_score[outcome_decider[opponent_play+your_play]]



print("Your score:",score)

