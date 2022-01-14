"""
Inside conditions.json, you will see a subset of UNSW courses mapped to their 
corresponding text conditions. We have slightly modified the text conditions
to make them simpler compared to their original versions.

Your task is to complete the is_unlocked function which helps students determine 
if their course can be taken or not. 

We will run our hidden tests on your submission and look at your success rate.
We will only test for courses inside conditions.json. We will also look over the 
code by eye.

NOTE: This challenge is EXTREMELY hard and we are not expecting anyone to pass all
our tests. In fact, we are not expecting many people to even attempt this.
For complete transparency, this is worth more than the easy challenge. 
A good solution is favourable but does not guarantee a spot in Projects because
we will also consider many other criteria.
"""
import json

import re

# NOTE: DO NOT EDIT conditions.json
with open("./conditions.json") as f:
    CONDITIONS = json.load(f)
    f.close()

def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.
    
    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """
    
    # TODO: COMPLETE THIS FUNCTION!!!

    # print(CONDITIONS)

    for condition in CONDITIONS:
        if condition == target_course:
            # required_list = CONDITIONS[target_course].split('AND', flags=re.IGNORECASE)
            required_list = re.split("AND", CONDITIONS[target_course], flags=re.IGNORECASE)
            print(required_list)

            ################################################################
            # Basic checks
            if len(CONDITIONS[target_course]) == 0:
                return True
            elif len(CONDITIONS[target_course]) == 8:
                for course in courses_list:
                    if course in CONDITIONS[target_course]:
                        return True
            ################################################################
            
            elif "and" not in CONDITIONS[target_course] and "or" in CONDITIONS[target_course]:
                for course in courses_list:
                    if course in CONDITIONS[target_course]:
                        return True

            # print(CONDITIONS[target_course])
    
    return False

def handle_basic():
    pass


if __name__ == "__main__":
    print(is_unlocked([], "COMP1511")) # true 
    print(is_unlocked([], "COMP9301")) # false 
    print(is_unlocked(["MATH1081"], "COMP3153")) # true 
    print(is_unlocked([], "COMP1521")) 
    print(is_unlocked([], "COMP2511")) 
    print(is_unlocked([], "COMP3151")) 
    print(is_unlocked([], "COMP3900")) 



    