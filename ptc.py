import math
import os
import random
import re
import sys
from collections import Counter
def isValid(s):
    # Write your code here
    dit = Counter(s)
    cont = Counter(dit.values())
    if len(cont) == 1:
        return 'YES'
    elif len(cont) > 2:
        return 'NO'
    else:
        mx = max(cont.values())
        v1, v2 = cont.keys()
        if (mx == len(dit)-1):
            if(abs(v1 - v2) == 1):
                return 'YES'
            elif (min(v1, v2) == 1):
                if cont[1] == 1:
                    return 'YES'
                else:
                    return 'NO'
            else:
                return 'NO'
        else:
            return 'NO'
                  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = isValid(s)
    fptr.write(result + '\n')
    fptr.close()