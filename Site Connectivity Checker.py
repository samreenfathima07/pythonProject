# import urllib
# use urllib.request to get the data from the url
# write a func that takes a url
# returns a response

import urllib.request as urllib


def main(url):
    url = url
    print("checking connectivity ")

    response = urllib.urlopen(url)
    print("connected to", url, "successfully")
    print("The response code was: ", response.getcode())


print("This is a site connectivity checker program")
input_url = input("input the url of the site : ")


main(input_url)





