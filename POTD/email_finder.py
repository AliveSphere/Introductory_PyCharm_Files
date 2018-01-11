# Charles Buyas cjb8qf


import re
import urllib.request


# [\w\-\.]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,} == expression I'll need to use to search for
# addresses like bar.ba@test.co.uk


def find_emails_in_website(url):
    stream = urllib.request.urlopen(url)
    empty_list = []
    g = []
    for line in stream:
        decoded = line.decode("UTF-8").strip()
        decoded = decoded.replace(' at ', '@')
        decoded = decoded.replace(' dot ', '.')
        decoded = decoded.replace('(at)', '@')
        decoded = decoded.replace(' (dot)', '.')
        decoded = decoded.replace('NOSPAM', '')
        email_finder_regex = re.compile(r'[\w\-\.]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}')
        match_object_1 = email_finder_regex.findall(decoded)
        for i in range(len(match_object_1)):
            g.append(match_object_1[i])
    for x in range(len(g)):
        if g[x] not in empty_list:
            empty_list.append(g[x])
    return empty_list
