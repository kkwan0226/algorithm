from timeit import default_timer as timer
from datetime import timedelta

## import ###################################
from collections import Counter
#############################################

def solution(participant, completion):
    return list(Counter(participant) - Counter(completion))[0]

if __name__=="__main__":
    ## Test Case ############################################
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    #########################################################

    start = timer()
    print('answer: ', solution(participant, completion))
    end = timer()
    print('time: ', timedelta(seconds=end-start))