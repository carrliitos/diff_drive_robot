"""drive_my_robot controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

def main():

    # create the Robot instance.
    robot = Robot()
    
    # get the time step of the current world.
    timestep = 64
    
    # max speed
    max_speed = 6.28 # angular velocity
    
    # create motor instance
    left_motor = robot.getDevice("motor_1")
    right_motor = robot.getDevice("motor_2")
    
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    num_side = 4
    length_side = 0.25
    
    wheel_radius = 0.025
    linear_velocity = wheel_radius * max_speed
    
    duration_side = length_side/linear_velocity
    start_time = robot.getTime()
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
        current_time = robot.getTime()
    
        # (1) Read sensors
        left_motor_speed = max_speed
        right_motor_speed = max_speed
        
        if current_time > start_time + duration_side:
            left_speed = 0
            right_speed = 0
        
        left_motor.setVelocity(left_motor_speed)
        right_motor.setVelocity(right_motor_speed)
        
        # (2) Process data
        
        # (3) Make decisions
        
        # (4) Send motor commands
    
    # Enter here exit cleanup code.


if __name__ == "__main__":
    main()
