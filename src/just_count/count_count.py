import click

import just_count.square
import just_count.square_root


@click.command()
@click.argument("number", type=int)
@click.argument("sqrt_or_sqr")
def main(number, sqrt_or_sqr):
    if sqrt_or_sqr == "square":
        print(f"The square of {number} is {just_count.square.square(number)}")
    elif sqrt_or_sqr == "square_root":
        print(
            f"The square root of {number} is {just_count.square_root.square_root(number)}"
        )


if __name__ == "__main__":
    main()
