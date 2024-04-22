from collections import deque


input_packets = [
    "S Mary", "P Dee", "P Dee", "E Eileen", "E Mike", "E Joe", "P Dee",
    "E Vicky", "E George", "P Dee", "P Joe", "E Sally", "P Joe", "S Pete",
    "P Dee", "S Bill", "S Chase", "E Price", "P Dee", "E Sue"
]

priority_queue = deque()
standard_queue = deque()
economy_queue = deque()

for packet in input_packets:
    priority_level, name = packet.split(' ')
    if priority_level == 'P':
        priority_queue.append(name)
    elif priority_level == 'S':
        standard_queue.append(name)
    elif priority_level == 'E':
        economy_queue.append(name)

while priority_queue or standard_queue or economy_queue:
    for _ in range(3):
        if priority_queue:
            print("Priority:", priority_queue.popleft())

    for _ in range(2):
        if standard_queue:
            print("Standard:", standard_queue.popleft())

    if economy_queue:
        print("Economy:", economy_queue.popleft())