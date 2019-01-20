# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
#
# domain_name("http://github.com/carbonfive/raygun") == "github"
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"

import re


def domain_name(url):
    if re.match(r'.*www\..*', url):
        return url.split('www.')[1].split('.')[0]
    return url.split('//')[1].split('.')[0]


assert domain_name("http://github.com/carbonfive/raygun") == "github"
assert domain_name("http://www.zombie-bites.com") == "zombie-bites"
assert domain_name("https://www.cnet.com") == "cnet"