class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        

        # conf rooms requried 

        # [start, end times]

        # 0.                30 
        #    5.     10
        #               15.     20


        #      7.       10
        # 2.   4 

        #end < st

        #2,4.  7,10

        # sort based on start times 
        # push first value to heap , end time 
        #2,4.   7,10 --> 4 to heap , no , next iteration 

        #. 0,30.  5,10.  15,20 
        #  30 to heap .. 5 < 30, so push 10, is 15 < 10, no keep as it is 

        # return size of heap

        heap1=[]
        intervals.sort() # based on sort times ,if based on diff param , guess need to specify lambda 

        heapq.heappush(heap1,intervals[0][1])

        for i in range(1,len(intervals)):
            if heap1[0] <= intervals[i][0]: # need to have lastest meeting end time, and check if its free or not 
                heapq.heappop(heap1)
                # means before the prev interval 
            heapq.heappush(heap1,intervals[i][1])

        print(len(heap1))
        return len(heap1)