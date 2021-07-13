from timeit import default_timer as timer
from datetime import timedelta

from collections import Counter

def solution(clothes):
    clothes_case = list()
    for idx, case in clothes:
        clothes_case.append(case)

    total = 1    
    for idx in list(Counter(clothes_case).values()):
        total = total * (idx+1)
    
    return total - 1

if __name__=="__main__":
    ## Test Case ######################################################################################
    clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
    #[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    ###################################################################################################

    start = timer()
    print('answer: ', solution(clothes))
    end = timer()
    print('time: ', timedelta(seconds=end-start))