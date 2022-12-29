import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.animation as animation
from tqdm.notebook import tqdm, trange

def geometry_check(eps):
    plt.figure(figsize=(eps[0].shape[1] / 72.,
                        eps[0].shape[0] / 72.), dpi=288)
    plt.imshow(eps[0], interpolation='spline36', cmap='binary')
    plt.show()
    

def sim_to_plot(frames, eps, cmap, timestamp):
    assert len(frames) > 0
    plt.figure(figsize=(frames[0].shape[1] / 72.,
                        frames[0].shape[0] / 72.), dpi=288)
    if eps is not None:
        plt.imshow(eps[0], interpolation='spline36', cmap='binary')
    plt.imshow(frames[timestamp], interpolation='spline36', cmap=cmap, alpha=0.9)
    plt.axis('off')
    plt.savefig("Files/sim.png",dpi=150)
    plt.show()
    
def sim_to_gif(frames, eps, prefix, save_dir, cmap, fps, interval=50):
    p = 0
    assert len(frames) > 0
    plt.figure(figsize=(frames[0].shape[1] / 72.,
                        frames[0].shape[0] / 72.), dpi=288)
    waves = plt.imshow(frames[0], interpolation='spline36', cmap=cmap, 
                       norm=colors.SymLogNorm(linthresh=0.02, vmin=np.min(frames), vmax=np.max(frames), base=10))
    bar = tqdm(range(len(frames)), desc='Animation save progress: ')
                   
    if eps is not None:
        dielectric = plt.imshow(eps[0], interpolation='spline36', cmap='binary', alpha=0.2)
    plt.axis('off')

    def animate(i):
        if eps is not None:
            dielectric.set_data(eps[0])
        waves.set_data(frames[i])
        bar.update()

    anim = animation.FuncAnimation(
        plt.gcf(), animate, frames=len(frames), interval=interval)
    output_path = "{}/{}.gif".format(save_dir, prefix)
    anim.save(output_path, writer='pillow', fps=fps)
    print("finished")
    plt.close()