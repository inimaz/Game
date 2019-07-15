#import seaborn as sns
import matplotlib.pyplot as plt
import time

def paint_world(world):
#    sns.heatmap(world)
    plt.subplot()
    plt.imshow(world)
    plt.colorbar()
    plt.show()
    
    input('')