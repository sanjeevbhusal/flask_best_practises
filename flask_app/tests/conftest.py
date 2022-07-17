import pytest
from main import create_app


@pytest.fixture(scope="session")
def app():
    params = {'TESTING': True, 'DEBUG': True}

    _app = create_app(settings_override=params)

    # Establish a context before running the test
    ctx = _app.app_context()
    ctx.push()
    yield _app
    ctx.pop()


@pytest.fixture(scope="function")
def client(app):
    yield app.test_client()
