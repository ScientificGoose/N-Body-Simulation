import pytest
from src.models import Body, Vector2D


def body_test():
    bodies = []
    bodies.append(Body("Sun", mass=1.989e30, position_vector=Vector2D(0.0, 0.0), velocity_vector=Vector2D(),
                       acceleration_vector=Vector2D()))
    bodies.append(Body("Earth", mass=5.972e24, position_vector=Vector2D(1.49e8, 1.49e8), velocity_vector=Vector2D(108000.0, 0.0),
                       acceleration_vector=Vector2D()))
    bodies.append(Body("Jupiter", mass=1.898e27, position_vector=Vector2D(8.166e8, 8.166e8), velocity_vector=Vector2D(105249.6, 0.0),
                       acceleration_vector=Vector2D()))

    # print(f"\nThe distance between {bodies[0].name} and {bodies[1].name} is {bodies[0].get_distance_between(bodies[1].position)}.")

    # temp_acceleration = bodies[0].calculate_acceleration(bodies, 0)
    # print("The acceleration vector will add the following to the x and y coordinates.")
    # print(f"\nx += {temp_acceleration.x:.1E}")
    # print(f"\ny += {temp_acceleration.y:.1E}\n")

    print("Start")
    print(f"\nname    : {bodies[0].name}")
    print(f"Position: x={bodies[0].position.x:.3E} y={bodies[0].position.y:.3E}")

    print(f"\nname    : {bodies[1].name}")
    print(f"Position: x={bodies[1].position.x:.3E} y={bodies[1].position.y:.3E}")

    print(f"\nname    : {bodies[2].name}")
    print(f"Position: x={bodies[2].position.x:.3E} y={bodies[2].position.y:.3E}")
    for index, body in enumerate(bodies):
        body.calculate_velocity(bodies, index=index, time_step=1.0)

    for body in bodies:
        body.update_position()

    print("First Iter")
    print(f"\nname    : {bodies[0].name}")
    print(f"Position: x={bodies[0].position.x:.3E} y={bodies[0].position.y:.3E}")

    print(f"\nname    : {bodies[1].name}\n")
    print(f"Position: x={bodies[1].position.x:.3E} y={bodies[1].position.y:.3E}")

    print(f"\nname    : {bodies[2].name}")
    print(f"Position: x={bodies[2].position.x:.3E} y={bodies[2].position.y:.3E}")

    for index, body in enumerate(bodies):
        body.calculate_velocity(bodies, index=index, time_step=1.0)

    for body in bodies:
        body.update_position()

    print("Second Iter")
    print(f"\nname    : {bodies[0].name}")
    print(f"Position: x={bodies[0].position.x:.3E} y={bodies[0].position.y:.3E}")

    print(f"\nname    : {bodies[1].name}")
    print(f"Position: x={bodies[1].position.x:.3E} y={bodies[1].position.y:.3E}")

    print(f"\nname    : {bodies[2].name}")
    print(f"Position: x={bodies[2].position.x:.3E} y={bodies[2].position.y:.3E}")
