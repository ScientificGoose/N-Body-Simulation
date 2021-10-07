# N-Body-Simulation
 A simulation for gravitational attraction for N bodies in up to R3 space.
 
 ### Details
 An N-Body simulation is used to simulate an dynamic system of N number of bodies that have a physical interaction with each other, in this case gravity. The complexity of the current algorithm is <img src="http://www.sciweavers.org/tex2img.php?eq=O%28n%5E2%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="O(n^2)" width="50" height="21" />.
 
 The program will generate N number of bodies and loop for a set number of steps. Each step the list of bodies will be iterated through, and the net force applied to the acceleration of the body, using the following equation:
 
<img src="http://www.sciweavers.org/tex2img.php?eq=%5Cvec%7BF%7D_i%20%3D%20-%20%5Csum_%7Bj%20%5Cneq%20i%7D%20%5Cfrac%7BG%20m_i%20m_j%0A%20%20%20%20%28%5Cvec%7Br%7D_i%20-%20%5Cvec%7Br%7D_j%29%7D%7B%28%7C%5Cvec%7Br%7D_i%20-%20%5Cvec%7Br%7D_j%7C%5E2%20%2B%20%5Cepsilon%5E2%29%5E%7B3%2F2%7D%7D%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\vec{F}_i = - \sum_{j \neq i} \frac{G m_i m_j    (\vec{r}_i - \vec{r}_j)}{(|\vec{r}_i - \vec{r}_j|^2 + \epsilon^2)^{3/2}}" width="219" height="53" />
<img src="http://www.sciweavers.org/tex2img.php?eq=%5Cvec%7BF_%7Bi%7D%7D%20%3D%20%5Ctext%7BNet%20force%20applied%20to%20i.%7D%20%5C%5C%0AG%20%3D%206.67408%20%5Ctimes%2010%5E%7B-11%7Dm%5E%7B3%7Dkg%5E%7B-1%7Ds%5E%7B-2%7D.%20%5C%5C%0Am_%7Bi%7D%20%3D%20%5Ctext%7BMass%20of%20body%20i%7D%20%5C%5C%0Am_%7Bj%7D%20%3D%20%5Ctext%7BMass%20of%20body%20j%7D%20%5C%5C%0A%28%5Cvec%7Br_%7Bj%7D%7D%20-%20%5Cvec%7Br_%7Bi%7D%7D%29%20%3D%20%5Ctext%7BThe%20distance%20between%20the%20bodies%20centers%7D%20%5C%5C%0A%5Cepsilon%5E%7B2%7D%20%3D%20%5Ctext%7BSoftener%20used%20to%20prevent%20infinite%20numbers%7D%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="\vec{F_{i}} = \text{Net force applied to i.} \\G = 6.67408 \times 10^{-11}m^{3}kg^{-1}s^{-2}. \\m_{i} = \text{Mass of body i} \\m_{j} = \text{Mass of body j} \\(\vec{r_{j}} - \vec{r_{i}}) = \text{The distance between the bodies centers} \\\epsilon^{2} = \text{Softener used to prevent infinite numbers}" width="426" height="146" />
This acceleration will be applied to the existing velocity of the body. Once the list of bodies has been processed, another iteration will be done. This second iteration will use the new velocity to update the position in space.

### Tasks


### Reference
http://www.scholarpedia.org/article/N-body_simulations_(gravitational)
