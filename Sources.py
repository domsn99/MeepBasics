import meep as mp
import numpy as np

def moving_electron_2D(x0, y0, vx0, vy0, f):
    global initx
    initx = x0
    global inity
    inity = y0
    global vx
    vx = vx0
    global vy
    vy = vy0
    global freq
    freq = f
    
    return [mp.Source(
        src = mp.ContinuousSource(frequency = freq),
        center = mp.Vector3(initx,inity),
        component = mp.Ez
    )]

def move_source(sim):
    sim.change_sources([mp.Source(mp.ContinuousSource(frequency = freq), 
                                  component=mp.Ez,
                                  center=mp.Vector3(initx + vx*sim.meep_time(), 
                                                    inity + vy*sim.meep_time())
                                 )
                       ])

sources = [
    [mp.Source(
     mp.ContinuousSource(frequency=0.15),
     component = mp.Ez,
     center = mp.Vector3(-7,0)
    )]
]