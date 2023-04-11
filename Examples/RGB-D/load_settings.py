import yaml


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

def read_and_modify_one_block_of_yaml_data(filename, key, value):
    with open(f'{filename}.yaml', 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        data[f'{key}'] = float(f'{value}')
        loaded_data = list(data)
        print(data) 
        print(loaded_data)
    print('done!')

    with open(f'{filename}.yaml', 'w') as file:
        yaml.dump(data,file, sort_keys=False)
    print(loaded_data) 



read_and_modify_one_block_of_yaml_data('KITTI00-02', key='Camera.dmax', value=30)

