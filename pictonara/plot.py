import matplotlib.pyplot as plt
import numpy as np


def make_mask_images(masks: np.ndarray) -> None:

    colors = ['c', 'm', 'y', 'k', 'g']
    for player_idx, mask in enumerate(masks):
        fig, ax = plt.subplots(4, 4)
        for card_idx, m in enumerate(mask):
            if m == 1:
                ax[card_idx % 4, card_idx // 4].hist(m, bins=1, color=colors[player_idx])
            ax[card_idx % 4, card_idx // 4].set_xticks([])
            ax[card_idx % 4, card_idx // 4].set_yticks([])

        plt.savefig(f"../player_{player_idx+1}_of_{masks.shape[0]}")
        plt.close()
