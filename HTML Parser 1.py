from html.parser import HTMLParser

# Create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        # Loop through attributes and print them
        for name, value in attrs:
            print(f"-> {name} > {value}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        # Loop through attributes and print them
        for name, value in attrs:
            print(f"-> {name} > {value}")

if __name__ == '__main__':
    # Read the number of lines
    n = int(input())
    
    # Read the HTML code block
    html_code = ""
    for _ in range(n):
        html_code += input() + "\n"
        
    # Instantiate the parser and feed it the HTML
    parser = MyHTMLParser()
    parser.feed(html_code)
