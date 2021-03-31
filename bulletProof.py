# bulletProof.py

# Write a (bullet proof) function called averageTo(aList, toIndex)
# The function should take in a list and an index. 
# The function will return the average of the numbers upto and including the toIndex in the aList.
# When I say "bullet proof", I would like the function to always return an integer, even if a error occurs (say return -1), 
# but it will use logging to make a meaningful log warning, for any error that occurs (eg the aList contains an entry that is not a number/ toIndex is not valid, 
# there are many things that could go wrong)
# Write the code to test all the things that could go wrong with this function, and a test to check the function does work.
# The test code can be in the same file or different file.
#
# author: Tomasz

import logging
logging.basicConfig(level=logging.DEBUG)

def averageTo(aList, toIndex):
    total = 0
    average = -1 # to compensate the index range
    
    # Check if toIndex is longer then the length of aList plus higher than 0
    try:
        if (toIndex <= count) and (toIndex >= 0):
            try:
                for i in range(toIndex):
                    total = total + aList[i]
                average = total / toIndex

            # Error for TypeError
            except TypeError:
                logging.debug("At least one of the entries in the list was not a number.")
            # Error for toIndex = 0
            except ZeroDivisionError:
                logging.debug("Index appears to be 0, please ensure the index is no equal zero")
        # negative index
        elif toIndex <=0:
            logging.debug("The index is below Zero")
        # index longer than list
        else:
            logging.debug("The index was out of range")
    # Exception for index out of range
    except TypeError:
        logging.debug("The index is higher than number of items in the list")
    # successfully ran function
    return average

if __name__ == '__main__':
    assert averageTo([1, 2, 3, 4], 3)
    assert averageTo([1, 2, 3, 4], 0)
    assert averageTo([1, 2, 3, 4], 5)
    assert averageTo([1, 2, 3, 4],-4)
    assert averageTo([1, 2, 3, 4], 'x')
    assert averageTo([1, 2, 3, 'test'], 4)
