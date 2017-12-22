import py

import pytest
from pytest_cookies import Cookies


@pytest.fixture(scope="session")
def cookies(request, _cookiecutter_config_file):
    template_dir = request.config.option.template
    p = py.path.local('tests/baked')
    if p.exists():
        p.remove()
    output_factory = py.path.local('tests').mkdir('baked').mkdir
    return Cookies(template_dir, output_factory, _cookiecutter_config_file)


@pytest.fixture
def context():
    return {
        'project_name': 'Project',
        'project_slug': 'project',
    }