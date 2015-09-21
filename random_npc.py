"""
Example output


"""

import click
import random
import constants
import names

def generate_stats(race, gender, level):
    """ Get stats for character
    """
    pass

@click.command()
@click.argument('race')
@click.argument('gender')
@click.option('--show_stats', default=False, help="Generate stats?")
@click.option('--level', default=constants.NORMAL, help="How hard should this character be? Easy, Normal or Hard")
def run(race, gender, show_stats, level):
    # Check race
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

    if show_stats:
        # Build stats
        stats = generate_stats(race, gender, level)

    should_we_save = click.prompt("Save this NPC?", type=bool)
    if should_we_save:
        # Write to file
        with open('characters.txt', 'a') as f:
            content = "{first} {last}, {race}, {gender}\n".format(
                first=first,
                last=last,
                race=race,
                gender=gender
            )
            f.write(content)


if __name__ == '__main__':
    run()
