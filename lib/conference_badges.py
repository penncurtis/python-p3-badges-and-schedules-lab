def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    rooms = range(1,9)
    assign = []
    for room in rooms:
        assign.append(f"Hello, {names[room - 1]}! You\'ll be assigned to room {room}!")
    return assign

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)

    for assign in assign_rooms(names):
        print(assign)
