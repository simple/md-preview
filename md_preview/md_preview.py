import os
import time
from tempfile import NamedTemporaryFile
from github3 import GitHub

gh = GitHub()


def github_login_with_token(username, token):
    gh.login(username=username, token=token)


def render_markdown(markdown):
    template_path = os.path.join(
        os.path.dirname(__file__), 'templates', 'markdown_rendered.html')

    template = ''
    with open(template_path, 'r') as fd:
        template = fd.read()

    html_content = gh.markdown(markdown, mode='markdown')
    html = template.replace('__CONTENT__', html_content)

    return html


def open_in_browser(text):
    with NamedTemporaryFile(
            mode='w', suffix='.html', dir='/tmp', delete=False) as temp_fd:
        temp_fd.write(text)
        temp_fd.close()
        os.system("open " + temp_fd.name)
        time.sleep(5)
        os.unlink(temp_fd.name)
