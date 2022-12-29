#1...Straight Waveguide
#2...Wedge
#3...Dreieck
#4...Fibre

import meep as mp
import numpy as np

geometries = [
    
    #1
    [mp.Block(
        mp.Vector3(mp.inf,1,mp.inf),
        center = mp.Vector3(),
        material = mp.Medium(epsilon=12)
    )],
    
    #2
    [mp.Wedge(
        radius = 5,
        wedge_angle = 0.1*np.pi,
        center = mp.Vector3(),
        material = mp.Medium(epsilon=1.45)
    )],
    
    #3
    [mp.Prism(
        [
            mp.Vector3(0,0,0),
            mp.Vector3(1,0,0),
            mp.Vector3(0.5,np.sqrt(0.75),0)
        ],
        height=1,
        center = mp.Vector3(),
        material = mp.Medium(epsilon=1.45)
    )],
    
    #4
    """
    [mp.Prism(
        [
            m*mp.Vector3(0,0,0),
            m*mp.Vector3(1,0,0),
            m*mp.Vector3(1+l,l,0),
            m*mp.Vector3(l,l,0)
        ],
        height=1,
        center = mp.Vector3(),
        material = mp.Medium(epsilon=1.45)
    ),mp.Prism(
        [
            m*mp.Vector3(0,0,0),
            m*mp.Vector3(0.16,0,0),
            m*mp.Vector3(0.16*(1+k*l),0.16*k*l,0),
            m*mp.Vector3(0.16*k*l,0.16*k*l,0)
        ],
        height=1,
        center = m*mp.Vector3(-0.55,0,0),
        material = mp.Medium(epsilon=1.7)
    ),mp.Prism(
        [
            m*mp.Vector3(0,0,0),
            m*mp.Vector3(0.16,0,0),
            m*mp.Vector3(0.16*(1+k*l),0.16*k*l,0),
            m*mp.Vector3(0.16*k*l,0.16*k*l,0)
        ],
        height=1,
        center = m*mp.Vector3(0.55,0,0),
        material = mp.Medium(epsilon=1.7)
    )]
    """
]