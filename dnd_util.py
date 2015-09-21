"""
Example output


"""

import click
import random
import constants
import names
import os
import csv

active_location = None

def generate_stats(race, gender, level):
    """ Get stats for character
    """
    pass

def generate_npc(race, gender, level, show_stats):
    global active_location

    if race.lower() not in constants.ALLOWED_RACES:
        click.echo("'%s' is not an allowed race" % race)
        return

    # Check gender
    if gender.lower() not in constants.ALLOWED_GENDERS:
        click.echo("'%s' is not an allowed gender" % gender)
        return

    # Build name
    first, last = names.generate_name(race, gender)

    click.echo("\n\n\n-------------------------------------------")
    click.echo(click.style("{f} {l}\n".format(f=first, l=last), fg="magenta"))
    click.echo(click.style("PERSONALITY : ", fg="yellow", bold=True) + "nothing")
    click.echo(click.style("IDEAL       : ", fg="yellow", bold=True) + "nothing")
    click.echo(click.style("BOND        : ", fg="yellow", bold=True) + "nothing")
    click.echo(click.style("FLAW        : ", fg="yellow", bold=True) + "nothing")
    click.echo("-------------------------------------------\n\n\n")

    should_we_save = click.confirm("Save NPC?", default=False)

    # Check location
    if not active_location:
        active_location = click.prompt("No location set. Where are you?", type=str)

    if should_we_save:
        fieldnames = ['first_name', 'last_name', 'race', 'gender', 'location']
        file_name = 'characters.csv'

        # Check that file exist and has headers
        if not os.path.isfile(file_name):
            with open(file_name, 'wb') as check:
                writer = csv.DictWriter(check, fieldnames=fieldnames)
                writer.writeheader()

        # Write to file
        with open(file_name, 'a') as csvfile:

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({
                'first_name': first,
                'last_name': last,
                'race': race.lower(),
                'gender': gender.lower(),
                'location': active_location
            })

def process_command(command):
    global active_location
    normalized_command = command.lower()
    if normalized_command == 'help':
        click.echo('')
        click.echo("location                    -- get location")
        click.echo("set location                -- change location")
        click.echo("npc                         -- generate NPC")
        click.echo('')
    elif normalized_command == 'location':
        if active_location:
            click.echo("You are currently in %s" % active_location)
        else:
            click.echo("No active location set. To set, enter `set location`")
    elif normalized_command == 'set location':
        active_location = click.prompt("What is the name of the location?", type=str)
        process_command("location")
    elif normalized_command == 'npc':
        race = click.prompt("Race", type=str, default=constants.HUMAN)
        gender = click.prompt("Gender", type=str)
        level = click.prompt("Level (optional)", type=str, default=constants.NORMAL)
        show_stats = click.confirm("Show Stats? (optional)", default=False)

        generate_npc(race, gender, level, show_stats)




@click.command()
def run():

    click.echo("=======================================================")
    click.echo("\n\nWelcome to DND 5e Util\n\n")
    click.echo("Enter `help` to get a list of commands")
    click.echo("=======================================================")

    while True:
        command = click.prompt(">>", type=str, prompt_suffix=' ')
        if command == 'quit':
            return
        else:
            process_command(command)


if __name__ == '__main__':
    run()
