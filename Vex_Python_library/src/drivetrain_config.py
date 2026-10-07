# Directions: Input the proper drivetrain type into the first dictionary entry labeled driveType
# Then describe the ports and locations of each motor, inertial sensors, and other physical characteristics.

driveTrain = {
    "driveType" : "4-motor", # (options are 2-motor, 4-motor, 6-motor, h-drive, x-drive, mechanum)
    "motor1" : (1, "fl"),    # (format is a tuple with (PORT NUMBER, MOTOR LOCATION). r = right, fl = front-left.)
    "motor2" : (2, "fr"),    # use r and l for 2 and 6 motor drivetrains. s = strafe motor for h-drive
    "motor3" : (3, "bl"),
    "motor4" : (4, "br"),
    # "motor5" : (5, "r"),
    # "motor6" : (6, "l"),
    "inertial" : 10,        # Port number for inertial sensor
    "wheelSize" : 4         # Wheelsize in millimeters
}