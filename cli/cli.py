import click
import os

command_files_location = os.path.join(os.path.dirname(__file__), "commands")


class CLI(click.MultiCommand):
    def list_commands(self, ctx):
        """
        Obtain a list of all the available commands
        :param ctx: Click context
        :return:List of commands
        """

        available_commands = []

        for command_filename in os.listdir(command_files_location):
            if not command_filename.startswith("__init__") and command_filename.endswith(".py"):
                available_commands.append(command_filename.split(".")[0])

        available_commands.sort()
        return available_commands

    def get_command(self, ctx, name):
        """
        Get information for a specified command
        :param ctx: Click Context
        :param name: Command name
        :return: Information about the command
        """
        ns = {}
        command_file_location = os.path.join(command_files_location, name + ".py")

        # creates a code object evaluates it and add it to dictionary.
        with open(command_file_location) as f:
            code = compile(f.read(), command_file_location, "exec")
            eval(code, ns, ns)

        return ns["cli"]  # executes cli function of the module command_file_location


# entry point of the cli application. runs when you run without arguments
@click.command(cls=CLI)
def cli():
    """Commands to help manage the project"""
    pass
