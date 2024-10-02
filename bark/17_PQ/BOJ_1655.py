import sys
import heapq

v = int(sys.stdin.readline())
minHeap, maxHeap = [], []
answer = []
for i in range(v):
    t = int(sys.stdin.readline())
    if len(maxHeap) == 0:
        heapq.heappush(maxHeap, -t)
    else:
        if len(minHeap) == 0:
            if t > -maxHeap[0]:
                heapq.heappush(minHeap, t)
            else:
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))
                heapq.heappush(maxHeap, -t)
        else:
            if t < minHeap[0]:
                heapq.heappush(maxHeap, -t)
            else:
                heapq.heappush(minHeap, t)
        
        if len(minHeap) - len(maxHeap) > 1:
            heapq.heappush(maxHeap, -heapq.heappop(minHeap))
        elif len(minHeap) - len(maxHeap) < -1:
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))
        
        if len(minHeap) - len(maxHeap) == 1:
            heapq.heappush(maxHeap, -heapq.heappop(minHeap))
        
    answer.append(-maxHeap[0])
for i in answer:
    print(i)