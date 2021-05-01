import numpy as np
import unittest
from pictonara.generate import get_card_masks


class MaskTest(unittest.TestCase):
    def test_card_masks_are_random(self):
        np.random.seed(42)
        for num_players in [4]:
            masks1 = get_card_masks(num_players=num_players)
            masks2 = get_card_masks(num_players=num_players)
            self.assertFalse((masks1 == masks2).all())

    def test_each_player_has_five_cards_marked(self):
        for num_players in [4]:
            masks = get_card_masks(num_players=num_players)
            num_players_with_five_marked = len(np.where(np.sum(masks, axis=1) == 5)[0])
            self.assertEqual(num_players_with_five_marked, num_players)

    def test_card_masks_all_overlap_in_exactly_one_spot(self):
        for num_players in [4]:
            masks = get_card_masks(num_players=num_players)
            num_complete_overlaps = len(np.where(np.sum(masks, axis=0) == num_players)[0])
            self.assertEqual(num_complete_overlaps, 1)

    def test_two_individual_card_masks_overlap_in_more_than_one_spot(self):
        for num_players in [4]:
            masks = get_card_masks(num_players=num_players)
            for i, m1 in enumerate(masks):
                for j, m2 in enumerate(masks):
                    if i != j:
                        has_complete_information = 1 == len(np.where(np.sum(masks, axis=0) == 2)[0])
                        self.assertFalse(has_complete_information)


if __name__ == '__main__':
    unittest.main()
