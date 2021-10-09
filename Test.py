from vector.Vector2D import Vector2D
from vector.Vector3D import Vector3D
from body.Body import Body


def main():

    #vector_test()
    body_test()
    

def vector_test():
    # vec1 = Vector2D(1.0, 5.5)
    # vec2 = Vector2D(6.6, 12.0)
    # #print(f'x = {vec1.x}\ny = {vec1.y}')
    # vec1.add(vec2)
    # #print(f'\nx = {vec1.x}\ny = {vec1.y}')
    # #print(f"\nDistance between: {vec1.get_distance_between(vec2)}")
    # vec3 = Vector3D(1.0, 5.5, 5.6)
    # vec4 = Vector3D(6.6, 12.0, 6.8)
    # vec5 = vec3.get_difference_vector(vec4)
    # print(f'x = {vec5.x}\ny = {vec5.y}\nz = {vec5.z}')
    # vec3.add(vec4)
    # #print(f'\nx = {vec3.x}\ny = {vec3.y}\nz = {vec3.z}')
    # #print(f"\nDistance between: {vec3.get_distance_between(vec4)}")
    pass

def body_test():

    bodies = []
    bodies.append(Body("Sun", mass=1.989e30, position_vector=Vector2D(0.0, 0.0), velocity_vector=Vector2D(10800.0, 10800.0),
        acceleration_vector=Vector2D()))
    bodies.append(Body("Earth", mass=5.972e24, position_vector=Vector2D(1.49e8, 1.49e8), velocity_vector=Vector2D(),
        acceleration_vector=Vector2D()))

    # print(f"\nThe distance between {bodies[0].name} and {bodies[1].name} is {bodies[0].get_distance_between(bodies[1].position)}.")

    # temp_acceleration = bodies[0].calculate_acceleration(bodies, 0)
    # print("The acceleration vector will add the following to the x and y coordinates.")
    # print(f"\nx += {temp_acceleration.x:.1E}")
    # print(f"\ny += {temp_acceleration.y:.1E}\n")

    # print(f"\n{bodies[1].name} x = {bodies[1].velocity.x}") 
    # print(f"\n{bodies[1].name} y = {bodies[1].velocity.y}") 
    bodies[0].calculate_velocity(bodies, 1.0)
    # print(f"\n{bodies[1].name} x = {bodies[1].velocity.x}") 
    # print(f"\n{bodies[1].name} y = {bodies[1].velocity.y}")


if __name__ == "__main__":
    main()