#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    else:
        items = list(a_dictionary.items())
        values = list(a_dictionary.values())
        status = 0
        for item in items:
            for i in range(0, len(values)):
                if item[1] < values[i]:
                    status += 1
            if status == 0:
                return (item[0])
            else:
                status = 0
