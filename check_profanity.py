from urllib.request import urlopen
from urllib.parse import quote


def read_text():
    quotes = open(r"C:\Users\Chetanya\PycharmProjects\FullStackWebDevelopment\prank\check.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    final = quote(text_to_check)
    query = "http://www.wdylike.appspot.com/?q=" + final
    print(query)
    connection = urlopen(query)
    print("\n")
    output = str(connection.read())
    false = 'false'
    if false in output:
        print("False")
    else:
        print("true")


read_text()
