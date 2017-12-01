# portal_interview
I chose to use a dictionary in Python, which allows to match key to value pairs. This way the name of the event can be seperated from the time and the name refers to the time. The date/time (which are the values) is represented by an array which holds month, day, year, start_time_in_minutes, end_time_in_minutes, in that order. I chose to use arrays for the date so I can compare the values individually and I chose to represent time in minutes because, based on the format provided by the instructions, minutes were the smallest quantity, which would give me the most accurate comparisons.

My algorithm for overlap() is as follows:
I compare every event with every other event,
if the dates match, and they aren't the same event, I then check to see if both the start time and the end time of one event are between the start and end time of the other event (this only really works if the second event has a longer end time, but since I compare all of them, I don't need to find the max -- which wastes time, but I ran out of time to optimize it).
If the start and end time of one event are between the start and end time of the other events, then I add it to a set, to get rid of duplicates, and then convert it to list, as per the intructions, and return it.

The only edge case I can think of in the now 2 minutes I have is if the data structure holds a lot of data, since I compare each item to every other item and I didn't get a chance to optimize it, it would make the program run for a long time.
