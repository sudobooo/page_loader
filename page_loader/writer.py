def write_html(path, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def write_content(path, content):
    with open(path, "wb") as file:
        file.write(content)
