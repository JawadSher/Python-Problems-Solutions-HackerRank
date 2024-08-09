from collections import Counter

K = int(input())
rooms = map(int, input().split())
rooms_counting = Counter(rooms)
captain_room = -1

for i in rooms_counting:
    if rooms_counting[i] == 1:
        captain_room  = i

print(captain_room)
