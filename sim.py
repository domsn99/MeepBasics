from Libraries import *
from Visualisation import *
from Geometries import *
from Sources import *

sx = 16
sy = 16
sz = 0
posx = 4
posy = 4
m=2
l=4
k=6.3
cell = mp.Vector3(sx, sy, sz)

dpml = 1
pml_layers = [mp.PML(thickness=dpml)]
resolution = 10

geometry = [mp.Prism(
        [
            m*mp.Vector3(0,0,0),
            m*mp.Vector3(1,0,0),
            m*mp.Vector3(1+l,l,0),
            m*mp.Vector3(l,l,0)
        ],
        height=1,
        center = mp.Vector3(posx,posy),
        material = mp.Medium(epsilon=1.45)
    ),mp.Prism(
        [
            m*mp.Vector3(0,0,0),
            m*mp.Vector3(0.16,0,0),
            m*mp.Vector3(0.16*(1+k*l),0.16*k*l,0),
            m*mp.Vector3(0.16*k*l,0.16*k*l,0)
        ],
        height=1,
        center = m*mp.Vector3(-0.55+posx/m,posy/m,0),
        material = mp.Medium(epsilon=1.47)
    ),mp.Prism(
        [
            m*mp.Vector3(0,0,0),
            m*mp.Vector3(0.16,0,0),
            m*mp.Vector3(0.16*(1+k*l),0.16*k*l,0),
            m*mp.Vector3(0.16*k*l,0.16*k*l,0)
        ],
        height=1,
        center = m*mp.Vector3(0.55+posx/m,posy/m,0),
        material = mp.Medium(epsilon=1.47)
    )]

#geometry = geometries[0]
source = moving_electron_2D(0,-8,0,0.7,1e-10)

sim = mp.Simulation(cell_size = cell,
                    boundary_layers = pml_layers,
                    geometry = geometry,
                    sources = source,
                    resolution = resolution)

sim.run(until=0.1)
eps_data = sim.get_array(center=mp.Vector3(), size=cell, component=mp.Dielectric)
plt.figure()
plt.imshow(eps_data.transpose(), interpolation='spline36', cmap='binary')
plt.savefig("Files/test.png",dpi=150)
plt.show()

sim.use_output_directory("Files")

sim.run(move_source, mp.at_beginning(mp.to_appended("eps",mp.output_epsilon)),
        mp.to_appended("ez", mp.at_every(0.6, mp.output_efield_z)),
        until=10)


f = h5py.File('Files/sim-ez.h5', 'r')
efield_z = np.array(f.get('ez'))
print("efield loaded")
f = h5py.File('Files/sim-eps.h5', 'r')
eps = np.array(f.get('eps'))
print("eps loaded")
f.close()

savedir = '/mnt/c/users/domin/OneDrive - TU Wien/Coding/GitHub/Meep_basics/Files'
prefix = 'sim'

#sim_to_plot(efield_z.transpose(),eps.transpose(),'RdBu',len(efield_z.transpose())-1)
sim_to_gif(efield_z.transpose(),eps.transpose(),prefix,savedir,'RdBu',30)