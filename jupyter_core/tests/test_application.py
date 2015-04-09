from tempfile import mkdtemp
from jupyter_core import application

def test_basic():
    app = application.JupyterApp()

def test_dirs():
    td = mkdtemp()
    