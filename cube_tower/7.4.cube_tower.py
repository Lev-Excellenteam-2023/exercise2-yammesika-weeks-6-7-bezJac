from cube_tower import CubeTower

"""
    This main function creates 1000 CubeTower objects and uses the CubeTower class to generate a random number of cubes
    to be attempted to add to each tower.(only cube meeting the criteria defined in CubeTower class will be added)
    For each tower, the function appends the height (i.e., the number of cubes in the tower) to a list called height. 
    the function prints the maximum height of all the towers created. 
"""


def main():
    height = []
    for i in range(1000):
        cube_tower = CubeTower()
        cube_generator = CubeTower.randomize_tower()
        for cube in cube_generator:
            cube_tower.add_cube(cube)
        height.append(len(cube_tower.tower))
    print(f"Tallest Tower created: {max(height)}")


if __name__ == "__main__":
    main()
