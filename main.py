import holoocean 
import numpy as np 
import controlAUV as Control 
 
scenario = "diy-ExampleLevel" 
simulationConfiguration = holoocean.packagemanager.get_scenario(scenario) 
 
command = np.array([0, 0, 0, 0, 0, 0, 0, 0])  # AUV stopped 
 
# with tf.device('/GPU:0'): 
with holoocean.make(scenario) as env: 
 
    while True: 
 
        env.act("auv0", command)  # send the command to the AUV 
        state = env.tick()  # refresh simulation 
 
        if 'q' in Control.pressed_keys:  # quit 
            break 
 
        command = Control.parse_keys(Control.pressed_keys, Control.force)  # get button pressed 
