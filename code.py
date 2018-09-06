def page():
    f = open('index.html')
    html = f.read()
    f.close()
    return html
