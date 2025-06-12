try:
    import matplotlib.pyplot as plt
    import numpy as np
    import random
    
    r = random.randint(1, 40)
    
    
    xpoints = np.array([3, 2, 5, 8, 4, 10])
    ypoints = np.array([38, 27, 82, 40, 10, 10])
    
    plt.plot(xpoints, ypoints)
    plt.show()
except:
    print("\33[91mCan't find Display :1\33[0m")