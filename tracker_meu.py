# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 22:01:02 2021

@author: Henrique Buzzi
"""

import math

class EuclideanDist_Tracker:
    def __init__(self):
        self.center_points = {}
        self.id_counter = 0
        
    def update(self, bb, user_limiarDist):
        def new_obj_detected():
            object_not_detected = True
            for id, c_point in self.center_points.items():
                dist = math.hypot(bb_cx - c_point[0], bb_cy - c_point[1])
                if dist < user_limiarDist:
                    self.center_points[id] = (bb_cx, bb_cy)
                    bb_with_id.append([x, y, w, h, id])
                    object_not_detected = False
                    break
            return object_not_detected
        
        bb_with_id = []
        
        for object_bb in bb:
            x, y, w, h = object_bb
            bb_cx = x + (w// 2)
            bb_cy = y + (h// 2)
            
            if new_obj_detected():
                self.center_points[self.id_counter] = (bb_cx, bb_cy)
                bb_with_id.append([x, y, w, h, self.id_counter])
                self.id_counter += 1
        
        # Clean the dictionary by center points to remove IDS not used anymore
        new_center_points = {}
        for obj_bb_id in bb_with_id:
            #_, _, _, _, object_id = obj_bb_id
            center = self.center_points[obj_bb_id[4]]
            new_center_points[obj_bb_id[4]] = center
        
        self.center_points = new_center_points
        return bb_with_id