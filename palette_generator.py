import argparse

import numpy as np
from sklearn.cluster import KMeans


def hex_to_rgb(value: str) -> list[int]:
    value = value.strip().lstrip("#")
    if len(value) != 6:
        raise ValueError("Colors must be six-digit hex values")
    try:
        return [int(value[index:index + 2], 16) for index in (0, 2, 4)]
    except ValueError as exc:
        raise ValueError("Invalid hex color") from exc


def rgb_to_hex(rgb: np.ndarray) -> str:
    channels = [max(0, min(255, int(round(channel)))) for channel in rgb]
    return "#" + "".join(f"{channel:02x}" for channel in channels)


def generate_palette(colors: list[str], count: int = 3) -> list[str]:
    if not colors:
        raise ValueError("At least one color is required")
    if count <= 0 or count > len(colors):
        raise ValueError("Count must be positive and no larger than the number of colors")
    rgb_values = np.array([hex_to_rgb(color) for color in colors], dtype=float)
    model = KMeans(n_clusters=count, random_state=42, n_init=10)
    model.fit(rgb_values)
    return [rgb_to_hex(center) for center in model.cluster_centers_]


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a compact color palette.")
    parser.add_argument("colors", help="Comma-separated hex colors")
    parser.add_argument("--colors", type=int, default=3, dest="count")
    args = parser.parse_args()
    for color in generate_palette(args.colors.split(","), args.count):
        print(color)


if __name__ == "__main__":
    main()
