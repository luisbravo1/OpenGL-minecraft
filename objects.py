# Attributes for Wolf Model
wolfAtt = {
  "head" : {
    "position": (0,0,0),
    "size": (1,1,1),
    "rotation": (0,0,0,0),
    "color": (0.87, 0.87, 0.87),
    "texture": "./textures/fur_texture.png"
  },
  "nose": {
    "position": (0,-0.5,1.3),
    "size": (0.5,0.5,0.5),
    "rotation": (0,0,0,0),
    "color": (0.87, 0.87, 0.87)
  },
  "body": {
    "position": (0,0.1,-2),
    "size": (1.2,1,2),
    "rotation": (0,0,0,0),
    "color": (0.87, 0.87, 0.87)
  },
  "tail": {
    "position": (0,-0.2,-4),
    "size": (0.2,0.2,1),
    "rotation": (-45,1,0,0),
    "color": (0.87, 0.87, 0.87)
  },
  "leg_fr": {
    "position": (0.5,-1.5,-0.8),
    "size": (0.2,1,0.2),
    "rotation": (45,0,0,0),
    "color": (0.87, 0.87, 0.87)
  },
  "leg_fl": {
    "position": (-0.5,-1.5,-0.4),
    "size": (0.2,1,0.2),
    "rotation": (-45,0,0,0),
    "color": (0.87, 0.87, 0.87)
  },
  "leg_br": {
    "position": (0.5,-1.5,-2),
    "size": (0.2,1,0.2),
    "rotation": (-45,0,0,0),
    "color": (0.87, 0.87, 0.87)
  },
  "leg_bl": {
    "position": (-0.5,-1.5,-3),
    "size": (0.2,1,0.2),
    "rotation": (45,0,0,0),
    "color": (0.87, 0.87, 0.87)
  },
}

# Attributes for Steve Model
steveAtt = {
  "head" : {
    "position": (0,1.6,0),
    "size": (0.6,0.6,0.6),
    "rotation": (0,0,0,0),
    "color": (0.98,0.92,0.81),
    # "texture": "./textures/steve_face.png",
  },
  "body": {
    "position": (0,0,0),
    "size": (0.75,1,0.3),
    "rotation": (0,0,0,0),
    "color": (0.25,0.79,0.96),
    # "texture": "./textures/blue_pants.jpeg"
  },
  "left_arm_skin": {
    "position": (-1,0,-0.5),
    "size": (0.35,1,0.3),
    "rotation": (45,1,0,0),
    "color": (0.25,0.79,0.96)
  },
  "right_arm_skin": {
    "position": (1,0,0.5),
    "size": (0.35,1,0.3),
    "rotation": (-45,1,0,0),
    "color": (0.25,0.79,0.96)
  },
  "right_leg": {
    "position": (0.25,-2,-0.5),
    "size": (0.375,1.2,0.3),
    "rotation": (45,0,0,0),
    "color": (0.11, 0.40, 1)
  },
  "left_leg": {
    "position": (-0.25,-2,0.5),
    "size": (0.375,1.2,0.3),
    "rotation": (-45,0,0,0),
    "color": (0.11, 0.40, 1)
  },
  "pickaxe_stick": {
    "position": (1, 0.2, 1.4),
    "size": (0.1, 1, 0.1),
    "rotation": (45, 0, 0, 0),
    "color": (0.5, 0.32, 0)
  },
  "pickaxe_stone_o": {
    "position": (1, 0.9, 1.6),
    "size": (0.1, 0.6, 0.1),
    "rotation": (90, 0, 0, 0),
    "color": (0.45, 0.45, 0.45)
  },
  "pickaxe_stone_s": {
    "position": (1, 0.3, 2.2),
    "size": (0.1, 0.6, 0.1),
    "rotation": (0, 0, 0, 0),
    "color": (0.45, 0.45, 0.45)
  }
}

# Attributes for Tree Model
treeAtt = {
  "trunk": {
    "position": (0,0,0),
    "size": (1,3,1),
    "rotation": (0,0,0,0),
    "color": (0.41,0.25,0.2)
  },
   "leaves_lower": {
    "position": (0,3,0),
    "size": (4,2,4),
    "rotation": (0,0,0,0),
    "color": (0.075,0.50,0.059)
  },
   "leaves_middle": {
    "position": (0,5,0),
    "size": (3,1,3),
    "rotation": (0,0,0,0),
    "color": (0.075,0.50,0.059)
  },
   "leaves_upper1": {
    "position": (0,6,0),
    "size": (2,1,1),
    "rotation": (0,0,0,0),
    "color": (0.075,0.50,0.059)
  },
   "leaves_upper2": {
    "position": (0,6,0),
    "size": (1,1,2),
    "rotation": (0,0,0,0),
    "color": (0.075,0.50,0.059)
  }
}

# Attributes for Mountain Model
mountainAtt = {
  "floor_lower1": {
    "position": (0,-2,-35),
    "size": (20,1,20),
    "rotation": (0,0,0,0),
    "color": (0.54,0.37,0.27)
  },
  "floor_lower2": {
    "position": (-20,-2,-25),
    "size": (7,1,30),
    "rotation": (0,0,0,0),
    "color": (0.54,0.37,0.27)
  },
  "floor_middle1": {
    "position": (0,-1,-37),
    "size": (18,1,18),
    "rotation": (0,0,0,0),
    "color": (0.54,0.37,0.27)
  },
  "floor_middle2": {
    "position": (-21,-1,-27),
    "size": (5,1,28),
    "rotation": (0,0,0,0),
    "color": (0.54,0.37,0.27)
  },
  "floor_middle3": {
    "position": (0,0,-39),
    "size": (16,1,16),
    "rotation": (0,0,0,0),
    "color": (0.54,0.37,0.27)
  },
  "floor_middle4": {
    "position": (-21,0,-30),
    "size": (5,1,25),
    "rotation": (0,0,0,0),
    "color": (0.54,0.37,0.27)
  },
  "floor_upper1": {
    "position": (7,1,-39),
    "size": (8,2,10),
    "rotation": (0,0,0,0),
    "color": (0.54,0.37,0.27)
  },
  "floor_upper2": {
    "position": (-21,1,-35),
    "size": (5,1,20),
    "rotation": (0,0,0,0),
    "color": (0.54,0.37,0.27)
  },
  "floor_upper3": {
    "position": (-21,2,-43),
    "size": (4,2,10),
    "rotation": (0,0,0,0),
    "color": (0.54,0.37,0.27)
  },
  "floor_upper4": {
    "position": (-21,4,-43),
    "size": (3,2,7),
    "rotation": (0,0,0,0),
    "color": (0.54,0.37,0.27)
  }
}

# Attributes for Pig Model
pigAtt = {
  "head" : {
    "position": (0,0,0),
    "size": (0.6,0.6,0.6),
    "rotation": (0,0,0,0),
    "color": (0.98,0.63, 0.58),
    # "texture": "./textures/pink_text.jpeg"
  },
  "nose" : {
    "position": (0,-0.2,0.7),
    "size": (0.3,0.2,0.1),
    "rotation": (0,0,0,0),
    "color": (0.98,0.75,0.72)
  },
  "body": {
    "position": (0,-0.1,-1),
    "size": (0.8,0.5,1),
    "rotation": (0,0,0,0),
    "color": (0.98,0.63, 0.58)
  },
  "leg_fl": {
    "position": (-0.4,-0.8,-0.3),
    "size": (0.3,0.5,0.3),
    "rotation": (45,0,0,0),
    "color": (0.98,0.63, 0.58)
  },
  "leg_fr": {
    "position": (0.4,-0.8,-0.1),
    "size": (0.3,0.5,0.3),
    "rotation": (-45,0,0,0),
    "color": (0.98,0.75,0.72)
  },
  "leg_bl": {
    "position": (-0.4,-0.8,-1.3),
    "size": (0.3,0.5,0.3),
    "rotation": (-45,0,0,0),
    "color": (0.98,0.75,0.72)
  },
  "leg_br": {
    "position": (0.4,-0.8,-1.5),
    "size": (0.3,0.5,0.3),
    "rotation": (45,0,0,0),
    "color": (0.98,0.63, 0.58)
  }
}

# Attributes for Skeleton Model
skeletonAtt = {
  "head" : {
    "position": (0,1.4,0),
    "size": (0.6,0.6,0.6),
    "rotation": (0,0,0,0),
    "color": (0.85, 0.85, 0.85)
  },
  "body": {
    "position": (0,0.5,0),
    "size": (0.75,0.5,0.2),
    "rotation": (0,0,0,0),
    "color": (0.87, 0.87, 0.87)
  },
  "column": {
    "position": (0,-0.5,-0.1),
    "size": (0.2,0.5,0.05),
    "rotation": (0,0,0,0),
    "color": (0.87, 0.87, 0.87)
  },
  "rib": {
    "position": (0,-0.3,0),
    "size": (0.5,0.1,0.05),
    "rotation": (0,0,0,0),
    "color": (0.82, 0.82, 0.82)
  },
  "ribl": {
    "position": (-0.4,-0.2,0),
    "size": (0.1,0.2,0.1),
    "rotation": (0,0,0,0),
    "color": (0.82, 0.82, 0.82)
  },
  "ribr": {
    "position": (0.4,-0.2,0),
    "size": (0.1,0.2,0.1),
    "rotation": (0,0,0,0),
    "color": (0.82, 0.82, 0.82)
  },
  "hip": {
    "position": (0,-1,0.1),
    "size": (0.6,0.1,0.3),
    "rotation": (0,0,0,0),
    "color": (0.90, 0.90, 0.90)
  },
  "left_arm_skin": {
    "position": (-0.8,0,0),
    "size": (0.2,1,0.2),
    "rotation": (0,0,0,0),
    "color": (0.85, 0.85, 0.85)
  },
  "right_arm_skin": {
    "position": (0.8,0,0),
    "size": (0.2,1,0.2),
    "rotation": (0,0,0,0),
    "color": (0.85, 0.85, 0.85)
  },
  "right_leg": {
    "position": (0.35,-2,0),
    "size": (0.2,1,0.2),
    "rotation": (0,0,0,0),
    "color": (0.87, 0.87, 0.87)
  },
  "left_leg": {
    "position": (-0.35,-2,0),
    "size": (0.2,1,0.2),
    "rotation": (0,0,0,0),
    "color": (0.87, 0.87, 0.87)
  },
}
