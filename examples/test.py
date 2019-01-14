import sys,os
sys.path.insert(1,os.path.join(sys.path[0],'..'))

from QuantumPhysics import stephans_law
print(stephans_law.compute_energy(3500))
