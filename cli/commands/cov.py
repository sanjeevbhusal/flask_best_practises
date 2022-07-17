import subprocess
import click


@click.command()  # tells click that the function will be a click command
@click.argument('path', default='flask_app')  # arguments to be supplied
def cli(path):
    """
    Generates a test coverage report.

    :param path: Path for a module/package for test-coverage
    :return: Subprocess call result
    """

    command = f"pytest --cov-report term-missing --cov={path}"

    # subprocess.call runs the command line equivalent code from file
    result = subprocess.call(command, shell=True)
    return result
