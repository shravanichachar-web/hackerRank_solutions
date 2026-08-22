import sys
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        # Check if the comment spans multiple lines
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)
        
    def handle_data(self, data):
        # Ignore if the data is just a newline character
        if data != '\n':
            print(">>> Data")
            print(data)

if __name__ == '__main__':
    # Read the number of lines
    n = int(input())
    
    # Read the HTML code block
    html_code = ""
    for _ in range(n):
        html_code += input().rstrip() + '\n'
        
    # Instantiate the parser and feed it the HTML code
    parser = MyHTMLParser()
    parser.feed(html_code)
    parser.close()
