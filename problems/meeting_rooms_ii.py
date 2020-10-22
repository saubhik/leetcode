from heapq import heapreplace, heappush
from typing import List


class Solution:
    """
    == Intuition ==
    This problem is very similar to something that employees of a company can face
    potentially on daily basis.
    Suppose you work at a company and you belong to the IT department and one of your
    job responsibilities is securing rooms for meetings that are to happen throughout
    the day in the office.
    You have multiple meeting rooms in the office and you want to make judicious use
    of them. You don't really want to keep people waiting and want to give a group of
    employees a room to hold the meeting right on time.
    At the same time, you don't really want to use too many rooms unless absolutely
    necessary. It would make sense to hold meetings in different rooms provided that
    the meetings are colliding with each other, otherwise you want to make use of as
    less rooms as possible to hold all of the meetings. How do you go about it?
    I just represented a common scenario at an office where given the start and end
    times for meetings to happen throughout the day, you, as an IT guy need to setup
    and allocate the room numbers to different teams.
    Let's approach this problem from the perspective of a group of people who want to
    hold a meeting and have not been allocated a room yet. What would they do?
    This group would essentially go from one room to another and check if any meeting
    room is free. If they find a room that is indeed free, they would start their
    meeting in that room. Otherwise, they would wait for a room to be free. As soon as
    the room frees up, they would occupy it.
    This is the basic approach that we will follow in this question. So, it is a kind
    of simulation but not exactly. In the worst case we can assign a new room to all of
    the meetings but that is not really optimal. Unless of course they all collide with
    each other.
    We need to be able to find out efficiently if a room is available or not for the
    current meeting and assign a new room only if none of the assigned rooms is
    currently free.
    Let's look at the first approach based on the idea we just discussed.

    == Approach 1: Priority Queues ==
    We can't really process the given meetings in any random order. The most basic way
    of processing the meetings is in increasing order of their start times and this is
    the order we will follow.

    Let's do a dry run of an example problem with sample meeting times and see what our
    algorithm should be able to do efficiently.

    We will consider the following meeting times for our example: (1,10), (2,7), (3,19),
    (8,12), (10,20), (11,30). The first part of the tuple is the start time for the
    meeting and the second value represents the ending time. We are considering the
    meetings in a sorted order of their start times.
    We assign (1,10) to a new room.
    We assign (2,7) to a new room since the first one is busy.
    We assign (3,19) to new room, Room 3, since the first 2 are busy.
    (8,12) is assigned to Room 2.
    (10,20) is assigned to Room 1.
    (11,30) is assigned to a new room, Room 4, since the others are busy.
    Overall, we have to use 4 different rooms to accommodate all the meetings.

    Sorting part is easy, but for every meeting how do we find out efficiently if a
    room is available or not? At any point of time, we have multiple rooms that can be
    occupied and we don't really care which room is free as long as we find one when
    required for a new meeting.

    A naive way to check if a room is available or not is to iterate on all the rooms
    and see if one is available when we have a new meeting at hand.

    However, we can do better than this by making use of priority queues or the min-heap
    data structure.

    Instead of manually iterating on every room that's been allocated and checking if
    the room is available or not, we can keep all the rooms in a min heap where the key
    for the min heap would be the ending time of the meeting.

    So, every time we want to check if any room is free or not, simply check the topmost
    element of the min heap as that would be the room that would get free the earliest
    out of all the other rooms currently occupied.

    If the room we extracted from the top of the min heap isn't free, then no other room
    is. So, we can save time here and simply allocate a new room.

    == Complexity Analysis ==
    Time Complexity: O(nlogn).
        - There are 2 major portions that take up time here. One is sorting of the array
        that takes O(nlogn) considering that the array consists of n elements.
        - Then we have the min-heap. In the worst case, all n meetings will collide with
        each other. In any case, we have n add operations on the heap. In the worst case
        we will have n extract-min operations as well. Overall complexity is O(nlogn)
        since extract-min operation on a heap takes O(lgn).
    Space Complexity: O(n).
        Because we construct the min-heap and that can contain n elements in the worst
        case as described above in the time complexity section. Hence, the space
        complexity is O(n).
    """

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        rooms_heap = []

        for (start, end) in intervals:
            if rooms_heap and rooms_heap[0] <= start:
                # Room available
                heapreplace(rooms_heap, end)
            else:
                heappush(rooms_heap, end)

        return len(rooms_heap)
