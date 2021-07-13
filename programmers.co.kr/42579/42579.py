from timeit import default_timer as timer
from datetime import timedelta

def solution(genres, plays):
    answer = []
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