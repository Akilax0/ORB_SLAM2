import json
import os
import numpy as np
import quaternion

class KITTIParameterLoader:
    def __init__(self):
        print('initialize camera parameter loader')

    def get_intrinsic(self, path):
        fx = 718.856
        fy = 718.8566
        cx = 607.1928
        cy = 185.2157
        s = 0.00

        mat_intrinsic = np.array([[fx, s, cx],
                                  [0, fy, cy],
                                  [0, 0, 1]])
        return mat_intrinsic

    def get_extrinsic(self, path):
        with open(path, 'r') as f:
            param_cam = json.load(f)['camera_data']
            param_translation = param_cam['location_worldframe']
            param_rotation = param_cam['quaternion_xyzw_worldframe']

            mat_rotation = quaternion.as_rotation_matrix(
                np.quaternion(param_rotation[3], param_rotation[0], param_rotation[1], param_rotation[2]))
            mat_translation = np.array([[param_translation[0]], [param_translation[1]], [param_translation[2]]])
            mat_extrinsic = np.concatenate(
                [np.concatenate([mat_rotation, mat_translation], axis=1), np.array([[0, 0, 0, 1]])], axis=0)
            return mat_extrinsic
