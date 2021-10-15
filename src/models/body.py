from math import pow
from vectors import Vector, Vector2D, Vector3D


class Body:
	"""
	This class represents a body in space.

	Parameters
	----------
	name (str):
		The name of the body.
	mass (float):
		The mass of the body.
	position (Vector):
		The position of the body in space.
	velocity (Vector):
		The velocity of the body.
	acceleration (Vector):
		The acceleration of the body.

	Methods
	-------
	get_distance_between(body) -> float:
		Get distance from this object to the input Body.
	calculate_velocity(body_list, body_idx, step=1) -> Vector:
		This method will calculate the velocity for the step.
	calculate_acceleration(body_list, body_idx) -> Vector:
		This method will calculate the net acceleration on the body.
	"""
	def __init__(self, name="", mass=0.0, position_vector=None, velocity_vector=None, acceleration_vector=None):
		self._name = name
		self._mass = mass
		self._position = position_vector
		self._velocity = velocity_vector
		self._acceleration = acceleration_vector

	@property
	def name(self) -> str:
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def mass(self):
		return self._mass
	
	@mass.setter
	def mass(self, mass=0):
		self._mass = mass

	@property
	def position(self) -> Vector:
		return self._position

	@position.setter
	def position(self, position_vector=None):
		self._position = position_vector

	@property
	def velocity(self) -> Vector:
		return self._velocity

	@velocity.setter
	def velocity(self, velocity_vector=None):
		self._velocity = velocity_vector

	@property
	def acceleration(self):
		return self._acceleration

	@acceleration.setter
	def acceleration(self, acceleration_vector=None):
		self._acceleration = acceleration_vector

	def get_distance_between(self, vector) -> float:
		"""
		This method will calculate the distance between this object and the input object.

		Parameters
		----------
		body (vector):
			A Body object to calculate the distance to.

		returns (float): The distance between the objects centers.
		"""
		if type(self._position) == type(vector):
			return self._position.get_distance_to(vector)
		else:
			raise ValueError("Vectors are not the same dimension!")

	def calculate_acceleration(self, body_list, body_idx) -> Vector:
		"""
		This method will calculate the net acceleration on the object.

		Parameters
		----------
		body_list (Body):
			The list of bodies to calculate the gravitational force.
		body_idx (int):
			The index in the list for this object.

		returns (Vector): The net Vector for the acceleration. 
		"""

		G = 6.67408e-11  # Gravitational constant.
		target = body_list[body_idx]

		if isinstance(self._acceleration, Vector2D):
			temp_acceleration = Vector2D()
		elif isinstance(self._acceleration, Vector3D):
			temp_acceleration = Vector3D()
		else:
			raise ValueError("Incompatible Vectors!")

		for body in body_list:
			if body != target:
				distance = target.get_distance_between(body.position)
				force = (G * target.mass * body.mass) / pow(distance, 2)
				temp_vector = target.position.get_difference_vector(body.position)
				temp_vector.apply_scalar(force/target.mass)
				temp_acceleration.add(temp_vector)

		return temp_acceleration

	def calculate_velocity(self, bodies, index, time_step=1):
		"""
		This method will calculate the total velocity applied to the body for each iteration.

		Parameters
		----------
		bodies (Body): The list of bodies in the system.
		time_step (float): How much time is passed between iterations.

		returns None
		"""
		acceleration = self.calculate_acceleration(bodies, index)
		acceleration.apply_scalar(time_step)
		self._velocity.add(acceleration)

	def update_position(self):
		"""
		This method will update the position of the body.

		Parameters
		----------
		bodies (Body): A list of bodies in the system.
		time_step (int): The default time to pass in the simulation.

		returns: None
		"""
		self._position.add(self._velocity)
