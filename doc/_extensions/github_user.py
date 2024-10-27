from docutils import nodes
from sphinx.util.docutils import SphinxRole

class GitHubUserRole(SphinxRole):
    def run(self):
        username = self.text.strip()
        url = f"https://github.com/{username}"
        node = nodes.reference(rawtext=self.rawtext, text=f"@{username}", refuri=url, **self.options)
        return [node], []

def setup(app):
    """Register extension with Sphinx."""
    app.add_role('github_user', GitHubUserRole())
    return {
        'version': '1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
