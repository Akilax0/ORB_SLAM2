import yaml

import time 
import math
from decimal import Decimal
import re
from datetime import datetime
import sys
import getopt
import os


'''
%YAML:1.0

#--------------------------------------------------------------------------------------------
# Camera Parameters. Adjust them!
#--------------------------------------------------------------------------------------------

# Camera calibration and distortion parameters (OpenCV) 
Camera.fx: 718.856
Camera.fy: 718.856
Camera.cx: 607.1928
Camera.cy: 185.2157

Camera.k1: 0.0
Camera.k2: 0.0
Camera.p1: 0.0
Camera.p2: 0.0

############## ADD ###########################
Camera.k3: 0.0 

Camera.width: 640
Camera.height: 192

# b = bKITTI/ dKITTI * dmax
Camera.bKITTI : 0.54
Camera.dKITTI : 80
# dmax = max CNN predicted depth of input sequence (keep track of depth)


Camera.dmax: 80

# bf = b * fx 


# IR projector baseline times fx (aprox.)
#Camera.bf: 40.0

# IR projector baseline times fx (aprox.) / depth 
# find depth relatively and multiply
Camera.bf: 80


# Close/Far threshold. Baseline times.
ThDepth: 35.0

# Deptmap values factor 
DepthMapFactor: 5000.0

###############################################

# Camera frames per second 
Camera.fps: 10.0

# Color order of the images (0: BGR, 1: RGB. It is ignored if images are grayscale)
Camera.RGB: 1

#--------------------------------------------------------------------------------------------
# ORB Parameters
#--------------------------------------------------------------------------------------------

# ORB Extractor: Number of features per image
ORBextractor.nFeatures: 2000

# ORB Extractor: Scale factor between levels in the scale pyramid 	
ORBextractor.scaleFactor: 1.2

# ORB Extractor: Number of levels in the scale pyramid	
ORBextractor.nLevels: 8

# ORB Extractor: Fast threshold
# Image is divided in a grid. At each cell FAST are extracted imposing a minimum response.
# Firstly we impose iniThFAST. If no corners are detected we impose a lower value minThFAST
# You can lower these values if your images have low contrast			
ORBextractor.iniThFAST: 20
ORBextractor.minThFAST: 7

#--------------------------------------------------------------------------------------------
# Viewer Parameters
#--------------------------------------------------------------------------------------------
Viewer.KeyFrameSize: 0.1
Viewer.KeyFrameLineWidth: 1
Viewer.GraphLineWidth: 1
Viewer.PointSize: 2
Viewer.CameraSize: 0.15
Viewer.CameraLineWidth: 2
Viewer.ViewpointX: 0
Viewer.ViewpointY: -10
Viewer.ViewpointZ: -0.1
Viewer.ViewpointF: 2000
'''

def prepend_line(file_name, line):
    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)

def read_and_modify_one_block_of_yaml_data(filename, key, value):    
    skip_lines = 1
    with open(f'{filename}.yaml', 'r') as f:
        for i in range(skip_lines):
            _ = f.readline()

        data = yaml.load(f, Loader=yaml.FullLoader)
        data[f'{key}'] = float(f'{value}')
        loaded_data = list(data)
        print(data) 
        print(loaded_data)
    print('done!')

    with open(f'{filename}.yaml', 'w') as file:
        yaml.dump(data,file, sort_keys=False)
    print(loaded_data) 

    prepend_line(f'{filename}.yaml',"%YAML:1.0")

if __name__ == "__main__":
    argv = sys.argv

    arg_input = ""
    arg_help = "{0} -i <input>".format(argv[0])
    
    try:
        opts, args = getopt.getopt(argv[1:], "hi:", ["help", "input="])
    except:
        print(arg_help)
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help)  # print the help message
            sys.exit(2)
        elif opt in ("-i", "--input"):
            arg_input = arg
    
    arg_arr = arg_input.split('/')
    arg_arr.append("max_depth.txt")
    depth_file = '/'.join(arg_arr)
    print(depth_file)



    #output_file = arg_input + "/epoch_out.txt"
    f1 = open(depth_file, "w")
    #f.write("Now the file has more content!")
    
    with open(arg_input) as f:
        lines = f.readlines()
        
        for i in lines:
            i = i.strip('\n')
            print("line:",i)
    f.close()




    read_and_modify_one_block_of_yaml_data('KITTI00-02', key='Camera.dmax', value=40)

