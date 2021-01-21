# Priority Queues
# TC: O(NlongN)
# SC: O(N)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # if there is no meeting to be scheduled, then no room is being allocated
        if not intervals:
            return 0
          
        # create a heap
        free_rooms = []
        
        # sort the meetings in increasing order of their start time
        intervals.sort(key = lambda x: x[0])
        
        # Add the first meeting. We have to give a new room to the first meeting
        heapq.heappush(free_rooms, intervals[0][1])
        
        # For all the remaining meeting rooms
        for i in intervals[1:]:
            
            # if the room due to free up, the earliest is free. Assign that room to this meeting
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
                
            # if a new room is to be assigned, then also we add to the heap
            # if an old room is allocated, then also we have to add to the heap with updated end time
            
            heapq.heappush(free_rooms, i[1])
            
        return len(free_rooms)
        
# Chronological Ordering
# TC: O(NlogN)
# SC: O(N)

# priority queue
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # if there are no meetings, return 0, no need for any rooms
        if not intervals:
            return 0
            
        used_room = 0
        
        # separate the start and end timings and sort them individually
        
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)
        
        # The two pointers in the algo: s_ptr and e_ptr
        s_pointer = 0
        e_pointer = 0
        
        # Until all the meetings have been processed
        while s_pointer < L:
            # if there is a meeting that has ended by the time the meeting at start_pointer
            if start_timings[s_pointer] >= end_timings[e_pointer]:
                # free up a room and increment an end pointer
                used_rooms -= 1
                e_pointer += 1
                
            # we do this irespective of whether a room frees up or not
            # If a room got free, then this used_rooms += 1 would not have any effect
            # used_rooms would remain the same in that case. If no room was free, then this would increase used_rooms
            
            used_rooms += 1
            s_pointer += 1
        
        return used_rooms
                
# Link: https://leetcode.com/problems/meeting-rooms-ii/   
    
    
