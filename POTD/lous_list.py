# Charles Buyas cjb8qf


import urllib.request


def instructors(department):
    site = "http://stardock.cs.virginia.edu/louslist/Courses/view/"
    stream = urllib.request.urlopen(site + department)
    class_info = []
    for line in stream:
        inner_value_list = line.decode("UTF-8").strip().split(";")
        if inner_value_list[4] not in class_info:
            class_info.append(inner_value_list[4])
    class_info.sort()
    return class_info


def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    site = "http://stardock.cs.virginia.edu/louslist/Courses/view/"
    stream = urllib.request.urlopen(site + dept_name)
    class_info = []
    big_list = []
    for line in stream:
        inner_value_list = line.decode("UTF-8").strip().split(";")
        class_info.append(inner_value_list)
    list_of_true = [True]*len(class_info)
    if has_seats_available:
        for i in range(len(class_info)):
            if class_info[i][15] >= class_info[i][16]:
                list_of_true[i] = False
    if level is not None:
        for i in range(len(class_info)):
            level_string = str(level)[0]
            if str(class_info[i][1])[0] != level_string:
                list_of_true[i] = False
    if not_before is not None:
        for i in range(len(class_info)):
            if int(class_info[i][12]) < not_before:
                list_of_true[i] = False
    if not_after is not None:
        for i in range(len(class_info)):
            if int(class_info[i][12]) > not_after:
                list_of_true[i] = False
    for i in range(len(class_info)):
        if list_of_true[i]:
            big_list.append(class_info[i])
    return big_list
