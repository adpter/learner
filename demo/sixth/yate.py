from string import Template


def start_response(resp="text/html"):
    return 'Content_type: ' + resp + '\n\n'


def include_header(the_title):
    with open('templates/header.html') as headf:
        head_text = headf.read()
    head = Template(head_text)
    return head.substitute(title=the_title)


print(start_response())
print(include_header("Welcome"))
