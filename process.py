

with open("noticias/noticias.txt","r") as _file:
    _NEWS = []
    _body = ""
    _head = ""
    for _line in _file:
        print _line
