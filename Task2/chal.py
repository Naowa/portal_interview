MINUTES = 60
calendar = {
    "Interview at The Portal" : [2, 23, 2017, (14*MINUTES), (15*MINUTES + 30)],
    "Lunch with Cindy" : [2, 25, 2017, (11*MINUTES), (12*MINUTES)],
    "Dinner with John" : [2, 24, 2017, (16*MINUTES), (16*MINUTES + 30)],
    "Conference" : [2, 24, 2017, (10*MINUTES), (16*MINUTES + 30)],
    "Meeting with Jeff" : [3, 29, 2017, (11*MINUTES), (11*MINUTES + 30)],
    "Meeting with Anne" : [3, 29, 2017, (11*MINUTES), (11*MINUTES + 30)],
    "Meeting with Steve" : [2, 5, 2017, (10*MINUTES), (16*MINUTES + 30)],
    "Meeting with Jill" : [2, 6, 2017, (14*MINUTES), (15*MINUTES + 30)],
}

def overlap():
    overlapped_events = set()
    for x in calendar.items():
        for y in calendar.items():
            if (x[1][0], x[1][1], x[1][2]) == (y[1][0], y[1][1], y[1][2]) and x[0] != y[0]:
                if y[1][3] <= x[1][3] <= y[1][4] and y[1][3] <= x[1][4] <= y[1][4]:
                    overlapped_events.add(x[0])
                    overlapped_events.add(y[0])
    return list(overlapped_events)

for x in overlap():
    print(x)
