from vector.Vector2D import Vector2D


def main():

    vec1 = Vector2D(1.0, 5.5)
    vec2 = Vector2D(6.6, 12.0)

    print(f'x = {vec1.get_x}\ny = {vec1.get_y}')

    vec1.add_vector(vec2)

    print(f'\nx = {vec1.get_x}\ny = {vec1.get_y}')


if __name__ == "__main__":
    main()