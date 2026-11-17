import unittest

from palette_generator import generate_palette


class PaletteGeneratorTests(unittest.TestCase):
    def test_palette_has_requested_size(self):
        palette = generate_palette(["#ff0000", "#f01010", "#0000ff", "#1010ee"], 2)
        self.assertEqual(len(palette), 2)
        self.assertTrue(all(color.startswith("#") and len(color) == 7 for color in palette))

    def test_invalid_count_is_rejected(self):
        with self.assertRaises(ValueError):
            generate_palette(["#ff0000"], 2)


if __name__ == "__main__":
    unittest.main()
