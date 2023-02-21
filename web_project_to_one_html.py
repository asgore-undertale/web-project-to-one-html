import re, os

def replace_js(match):
    f = open(dir + match.group(1), "r", encoding="utf8")
    return "<script>" + f.read() + "</script>"
def replace_css(match):
    f = open(dir + match.group(1), "r", encoding="utf8")
    return "<style>" + f.read() + "</style>"

path = input("File path: ")
dir = os.path.dirname(path) + "/"
f = open(path, "r", encoding="utf8")
text = f.read()
text = re.sub("<script src=\"(.*?)\"></script>", replace_js, text)
text = re.sub("<link rel=\"stylesheet\" href=\"(.*?)\"/>", replace_css, text)
print(text)
