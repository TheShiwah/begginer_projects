# import urllib
# use urllib.request  to get the data from the url
# write a function that takes a url
# return a response

import urllib.request as urllib


def main(url):
    print("checking connectivity")

    response = urllib.urlopen(url)
    print("Connected to ", url, "succesfully")
    print("The response code was ", response.getcode())


print("This is a site connectivity checker program")
input_url = input("Input url of the site you want to check: ")

main(input_url)
