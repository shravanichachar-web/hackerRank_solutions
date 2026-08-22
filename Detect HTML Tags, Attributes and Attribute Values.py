from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            # attr[0] is the attribute name, attr[1] is the attribute value
            print(f"-> {attr[0]} > {attr[1]}")
            
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

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
