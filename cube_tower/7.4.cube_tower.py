from typing import List
from cube_tower import CubeTower

"""
    the main calls create_towers_with_cubs to create 1000 CubeTower objects and uses the CubeTower class to generate a
    random number of cubes to be attempted to add to each tower.(only cube meeting the criteria defined in 
    CubeTower class will be added)
    the height of each tower is calculated and the max height is printed
"""


def create_towers_with_cubs(number_of_towers: int) -> List[CubeTower]:
    """
    create cube tower objects with random amount of cubes added to the tower
    :param number_of_towers: number of objects to create
    :return: list containing the objects
    """
    towers = []
    for _ in range(number_of_towers):
        cube_tower = CubeTower()
        cube_generator = CubeTower.randomize_tower()
        for cube in cube_generator:
            cube_tower.add_cube(cube)
        towers.append(cube_tower)
    return towers


def main():
    towers = create_towers_with_cubs(1000)
    heights = [len(single_cube_tower.tower) for single_cube_tower in towers]
    print(f"Tallest Tower created: {max(heights)}")


if __name__ == "__main__":
    main()
