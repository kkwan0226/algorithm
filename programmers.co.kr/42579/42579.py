from timeit import default_timer as timer
from datetime import timedelta

from collections import defaultdict
from operator import itemgetter

def solution(genres, plays):
    answer = list()

    sum_plays = defaultdict(int)
    for genre, play in zip(genres, plays):
        sum_plays[genre] += play
    sum_plays = sorted(sum_plays.items(), key=lambda x: x[1], reverse=True)

    preprocessing = [[] for _ in range(len(sum_plays))]
    idx = [i for i in range(len(genres))]
    for idx, genre, play in zip(idx, genres, plays):
        for count_play_idx, count_play in enumerate(sum_plays):
            if count_play[0] == genre :
                preprocessing[count_play_idx].append({'idx': idx, 'play': play})
    
    for order in range(len(sum_plays)):
        preprocessing[order]= sorted(preprocessing[order], key=itemgetter('play'), reverse=True)
        if len(preprocessing[order]) == 1:
            answer.append(preprocessing[order][0]['idx'])
        else:
            answer.append(preprocessing[order][0]['idx'])
            answer.append(preprocessing[order][1]['idx'])
    
    return answer

if __name__=="__main__":
    ## Test Case #############################################
    genres = ["classic", "pop", "classic", "classic", "pop"]	
    plays = [500, 600, 150, 800, 2500]
    ##########################################################

    start = timer()
    print('answer: ', solution(genres, plays))
    end = timer()
    print('time: ', timedelta(seconds=end-start))