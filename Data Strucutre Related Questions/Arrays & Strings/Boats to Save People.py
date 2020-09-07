"""
Boats to Save People - Medium #881

You are trying to add people in safety boats

Given an array called 'people' and integer 'limit',
people is an array of people's weights, i-th person has a weight people[i]
and each boat can carry at most limit

Each boat carries at most 2 people at the same time
Given that their weight sum is at most limit

Return the minimum number of boats to carry every given person
"""

class Solution:
    def numSecueBoats(self, people: List[int], limit: int) -> int:
        # Sort the weights of people in ascedning order
        people.sort()

        # Initialize left, right pointers and counter for boats
        left = 0
        right = len(people) - 1
        boats = 0

        # Until there is no one left,
        while(left <= right):
            # If the last person, add himself on the boat
            if (left == right):
                boats += 1
                break

            # If sum of weight of the lightest (people[left]) and the heaviest (people[right]) people
            # is smaller than the limit the boat can carry, add them to the boat
            if (people[left] + people[right] <= limit):
                left += 1

            # If not, add the heaviest person on the boat by himself
            right -= 1
            boats += 1


        return boats


"""
Time Complexity : O(n log(n))
Space Complexity: O(1)
"""