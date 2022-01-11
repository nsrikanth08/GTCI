from __future__ import print_function


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

def merge(intervals):
    if len(intervals) < 2:
        return intervals
    result = []
    intervals.sort(key = lambda x: x.start)
    start = intervals[0].start
    end = intervals[0].end
    for x in range(1, len(intervals)):
        if intervals[x].start <= end:
            end =  max(end, intervals[x].end)
        else:
            result.append(Interval(start, end))
            start = intervals[x].start
            end = intervals[x].end
    result.append(Interval(start, end))
    return result
    

def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()

if __name__ == "__main__":
    main()
