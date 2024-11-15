import click

import just_count.square


@click.command()
@click.argument("number", type=int)
def main(number):
    print(f"The square of {number} is {just_count.square.square(number)}")


if __name__ == "__main__":
    main()
