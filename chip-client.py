import click

@click.group()
def chip_client():
    pass

@chip_client.command()
def cmd1():
    '''Command on chip_client'''
    click.echo('chip_client cmd1')

@chip_client.command()
def cmd2():
    '''Command on chip_client'''
    click.echo('chip_client cmd2')

if __name__ == '__main__':
    chip_client()
