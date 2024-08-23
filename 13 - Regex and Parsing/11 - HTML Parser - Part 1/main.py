from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        self.handle_attrs(attrs = attrs)
        
    def handle_endtag(self, tag):
        print("End   :", tag)
        
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        self.handle_attrs(attrs = attrs)
        
    def handle_attrs(self, attrs):
        [print(f"-> {i[0]} > {i[1]}") for i in attrs]


parser = MyHTMLParser()

n = int(input())
for _ in range(n):
    code = input()
    parser.feed(code)
