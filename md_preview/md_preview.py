import markdown as md
import os
import sys
import tempfile
import time


def render(markdown):
    template_path = os.path.join(
        os.path.dirname(__file__), 'templates', 'markdown_rendered.html')

    template = ''
    with open(template_path, 'r') as fd:
        template = fd.read()

    html_content = md.markdown(markdown)
    html = template.replace('__CONTENT__', html_content)

    return html


def get_temp_dir():
    if os.name == 'nt':
        return tempfile.gettempdir()
    else:
        return '/tmp'


def open_file(filepath):
    if os.name == 'nt':
        os.system("start " + filepath)
    elif sys.platform.startswith('darwin'):
        os.system("open " + filepath)
    else:
        os.system("xdg-open " + filepath)


def view_in_browser(text):
    tmpdir = get_temp_dir()
    with tempfile.NamedTemporaryFile(
            mode='w', suffix='.html', dir=tmpdir, delete=False) as temp_fd:
        temp_fd.write(text.encode("utf-8"))
        temp_fd.close()
        open_file(temp_fd.name)
        time.sleep(2)
        os.unlink(temp_fd.name)
