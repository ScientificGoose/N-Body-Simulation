from vector.Vector2D import Vector2D
from vector.Vector3D import Vector3D


def main():

    vec1 = Vector2D(1.0, 5.5)
    vec2 = Vector2D(6.6, 12.0)

    print(f'x = {vec1.get_x}\ny = {vec1.get_y}')

    vec1.add(vec2)

    print(f'\nx = {vec1.get_x}\ny = {vec1.get_y}')

    print(f"\nDistance between: {vec1.get_distance_between(vec2)}")

    vec3 = Vector3D(1.0, 5.5, 5.6)
    vec4 = Vector3D(6.6, 12.0, 6.8)

    print(f'x = {vec3.get_x}\ny = {vec3.get_y}\nz = {vec3.get_z}')

    vec3.add(vec4)

    print(f'\nx = {vec3.get_x}\ny = {vec3.get_y}\nz = {vec3.get_z}')

    print(f"\nDistance between: {vec3.get_distance_between(vec4)}")


if __name__ == "__main__":
    main()