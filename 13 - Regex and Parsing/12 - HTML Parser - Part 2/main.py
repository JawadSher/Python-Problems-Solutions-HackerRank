from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, comment):
        if "\n" in comment: 
            print(f">>> Multi-line Comment\n{comment}")
            
        if "\n" not in comment:
            print(f">>> Single-line Comment\n{comment}")

    def handle_data(self, data):
        if data.strip():  
            print(f">>> Data")
            print(data)

html = ""
for _ in range(int(input())):
    html += input().rstrip() + '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
