import pytest
from app import PyTezApp


@pytest.fixture
def app():
    return PyTezApp()


@pytest.fixture
def test_client(app):
    return app.test_session()
