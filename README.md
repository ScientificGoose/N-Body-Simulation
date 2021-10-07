# N-Body-Simulation
 A simulation for gravitational attraction for N bodies in up to R3 space.
 
 ### Details
 An N-Body simulation is used to simulate an dynamic system of N number of bodies that have a physical interaction with each other, in this case gravity. The complexity of the current algorithm is <img src="http://www.sciweavers.org/tex2img.php?eq=O%28n%5E2%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="O(n^2)" width="50" height="21" />.
 
 The program will generate N number of bodies and loop for a set number of steps. Each step the list of bodies will be iterated through, and the net force applied to the acceleration of the body, using the following equation:
 
![Formula](Force_Formula.jpg)

![Parameters](Parameters.jpg)

This acceleration will be applied to the existing velocity of the body. Once the list of bodies has been processed, another iteration will be done. This second iteration will use the new velocity to update the position in space.

### Tasks


### Reference
http://www.scholarpedia.org/article/N-body_simulations_(gravitational)
