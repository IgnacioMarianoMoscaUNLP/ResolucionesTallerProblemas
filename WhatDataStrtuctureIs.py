import heapq
from collections import deque

def main():
    while True:
        try:
            n = int(input())
        except EOFError:
            break
        
        stack_possible = True
        queue_possible = True
        pq_possible = True
        
        stack = []
        queue = deque()
        pq = []
        
        for _ in range(n):
            command = input().split()
            if command[0] == '1':
                value = int(command[1])
                stack.append(value)
                queue.append(value)
                heapq.heappush(pq, -value)
            else:
                value = int(command[1])
                if not stack_possible and not queue_possible and not pq_possible:
                    continue
                
                if stack_possible and (not stack or stack.pop() != value):
                    stack_possible = False
                if queue_possible and (not queue or queue.popleft() != value):
                    queue_possible = False
                if pq_possible and (not pq or -heapq.heappop(pq) != value):
                    pq_possible = False
        
        if stack_possible + queue_possible + pq_possible == 0:
            print("impossible")
        elif stack_possible + queue_possible + pq_possible > 1:
            print("not sure")
        elif stack_possible:
            print("stack")
        elif queue_possible:
            print("queue")
        else:
            print("priority queue")

if __name__ == "__main__":
    main()
