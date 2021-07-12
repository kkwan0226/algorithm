from timeit import default_timer as timer
from datetime import timedelta

def solution(pphone_book):
    answer = True
    return answer

if __name__=="__main__":
    ## Test Case ############################################
    phone_book = ["119", "97674223", "1195524421"]	
    #########################################################

    start = timer()
    print('answer: ', solution(phone_book))
    end = timer()
    print('time: ', timedelta(seconds=end-start))