shape_to_score = {'X': 1, 'Y': 2, 'Z':3, 'rock': 1, 'paper': 2, 'scissors':3}
outcome_decider = {'AX': 'draw', 'AY': 'won', 'AZ':'lose','BX':'lose'
    ,'BY':'draw','BZ':'won','CX':'won','CY':'lose','CZ':'draw'}
outcome_to_score = {'lose': 0, 'draw': 3, 'won':6, 'X': 0, 'Y': 3, 'Z':6}
shape_decider = {'AX': 'scissors', 'AY': 'rock', 'AZ':'paper','BX':'rock'
    ,'BY':'paper','BZ':'scissors','CX':'paper','CY':'scissors','CZ':'rock'}

score = 0
score_second = 0
for i in open('day2_data.txt').read().splitlines():
    opponent_play, your_play = i.split(' ')

    # 2A
    score+=shape_to_score[your_play]
    score+=outcome_to_score[outcome_decider[opponent_play+your_play]]

    # 2B
    score_second+=shape_to_score[shape_decider[opponent_play+your_play]]
    score_second+=outcome_to_score[your_play]

print("2a):",score)
print("2b):",score_second)


