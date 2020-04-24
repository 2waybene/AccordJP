import click
#from analysisPipes import model_step_1

@click.group()
def main(args=None):
    pass



@main.command()
@click.argument('workingPath', type=click.Path(exists=True))

def launch_model_step_1 (workingPath):
    click.echo ('Launch Model Step 1')
#    model_step_1 (workingPath)

@main.command()
def initdb():
    click.echo('Initialized the database')

@main.command()
def dropdb():
    click.echo('Dropped the database')

if __name__ == "__main__":
    main()
