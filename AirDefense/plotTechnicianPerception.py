import matplotlib.pyplot as plt

# PLOTTING 
plot = plt.gcf()
ax = plt.gca()

time = 0
timeLimit = 500

def plotTechnicianPerception(threatPerception, civilPerception, blueAssets, technicianFieldOfView):
    # PLOT THREATS THAT TECHNICIAN IS AWARE OF
    for track in threatPerception:
        print("Perceived Threat: ", track._name)
        plt.scatter(track._position_x, track._position_y, color="Red")
        plt.text(track._position_x, track._position_y, track._name, color="Red")

    # PLOT FRIENDLY TRACKS THAT TECHNICIAN IS AWARE OF
    for track in civilPerception:
        print("Perceived Friend: ", track._name)
        plt.scatter(track._position_x, track._position_y, color="Green")
        plt.text(track._position_x, track._position_y, track._name, color="Green")

    # PLOT BLUE ASSETS IN THEIR POSITIONS
    for asset in blueAssets:
        plt.scatter(asset._position_x, asset._position_y, color="Blue")
        plt.text(asset._position_x, asset._position_y, asset._name, color="Blue")
        
    # ADD TECHNICIAN FIELD OF VIEW
    ax.add_patch(technicianFieldOfView)

    # ADJUST PLOT FEATURES
    plt.grid()
    plt.ylim([-10, 250])

    # SHOW PLOT
    plt.savefig('technicianPerception.png')