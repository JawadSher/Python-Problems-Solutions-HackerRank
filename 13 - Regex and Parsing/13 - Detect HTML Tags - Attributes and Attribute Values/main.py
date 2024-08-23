from html.parser import HTMLParser

class My_HTML_Parser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        self.handle_attrs(attrs = attrs)
    
    def handle_attrs(self, attrs):
        [print(f"-> {x[0]} > {x[1]}") for x in attrs]
    
n = int(input())
parser = My_HTML_Parser()

for _ in range(n):
    code = input()
    parser.feed(code)
