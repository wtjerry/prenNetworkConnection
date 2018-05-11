class Config:
    BINDING_USE_REAL_MOVEMENT = True
    BINDING_USE_REAL_GOAL_DETECTION = True 
    BINDING_USE_REAL_MAGNET = True 
    BINDING_USE_REAL_TELESCOPE = True 
    BINDING_USE_REAL_POSITION = True
    BINDING_USE_REAL_BALANCER = False
    BINDING_USE_REAL_LOAD_POSITION_COMPARER = True
    BINDING_USE_REAL_TILT_ENGINE = False

    CONTROLLER_MOVE_TO_LOAD_SPEED = 3
    CONTROLLER_MOVE_TO_GOAL_SPEED = 4
    CONTROLLER_SEARCH_GOAL_SPEED = 2
    CONTROLLER_FINISH_SPEED = 4
    CONTROLLER_REVERT_MOVEMENT = 0
    CONTROLLER_START_DROP_ZONE = 900
    CONTROLLER_END_DROP_ZONE = 3300
    CONTROLLER_DISTANCE_TO_GOAL_SLOWER = 100
    CONTROLLER_INITIAL_LOAD_HEIGHT = 185 
    CONTROLLER_END_TELESCOPE_HEIGHT = 200
    CONTROLLER_END_SPEED = 2
    CONTROLLER_END_PARCOURS_POSITION = 4200
    CONTROLLER_END_SLOW_DOWN_POSITION = 3400
    CONTROLLER_DISTANCE_CAMERA_TELESCOPE = 300
    CONTROLLER_GOAL_DETECTION_THRESHOLD = 25

    COMPARER_LOAD_POSITION = 650

    POSITION_LOAD_HEIGHT = 50
    POSITION_START_X_POS = 265
    POSITION_GROUND_TO_CABLE_ANGLE = 0.141897
