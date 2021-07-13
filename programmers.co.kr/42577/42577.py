from timeit import default_timer as timer
from datetime import timedelta

from collections import defaultdict

def solution(phone_book):
    count = defaultdict(int)
    for idx, phone_num in enumerate(phone_book):
        for idx_in in range(len(phone_num)):
            count[phone_num[:idx_in+1]]+=1
    
    for idx in range(len(phone_book)):
        if count[phone_book[idx]] > 1: return False
    return True

if __name__=="__main__":
    ## Test Case ############################################
    phone_book = ["12","123","1235","567","88"]
    # ["119", "97674223", "1195524421"]	
    #########################################################

    start = timer()
    print('answer: ', solution(phone_book))
    end = timer()
    print('time: ', timedelta(seconds=end-start))
