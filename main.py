import argparse

from pictonara.generate import get_card_masks
from pictonara.plot import make_mask_images


def generate_and_plot():
    parser = argparse.ArgumentParser(description="Create Pictonara Masks")
    parser.add_argument("-p", "--num_players", type=int, default=4)
    args = parser.parse_args()

    c = get_card_masks(num_players=args.num_players)
    make_mask_images(c)
    print("Complete!")


if __name__ == "__main__":
    generate_and_plot()
