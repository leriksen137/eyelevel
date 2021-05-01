import numpy as np


def get_card_masks(num_players: int) -> np.ndarray:
    if num_players == 3:
        masks = np.random.random([num_players, 16])  # TODO
    elif num_players == 4:
        masks = np.asarray([[1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, ],
                            [1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, ],
                            [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, ],
                            [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, ]])
    elif num_players == 5:
        masks = np.random.random([num_players, 16])  # TODO
    else:
        raise ValueError("Game currently only supported for 3, 4, or 5 players.")

    # permute columns
    rng = np.random.default_rng()
    rng.shuffle(masks, axis=1)

    return masks
