def can_attend_all_appointments(intervals):
    intervals.sort(key = lambda x: x[0])
    start, end = 0, 1
    for x in range(1, len(intervals)):
        if intervals[x][start] < intervals[x-1][end]:
            return False
    return True


def main():
  print("Can attend all appointments: " + 
            str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
  print("Can attend all appointments: " + 
            str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
  print("Can attend all appointments: " + 
            str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))

if __name__ == "__main__":
    main()