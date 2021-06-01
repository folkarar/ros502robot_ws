import roslib
import getch
import rospy

from geometry_msgs.msg import Twist



def main():
    rospy.init_node('keyboard_input')
    publisher = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
    speed = 0.0
    ang_z = 1
    print("q: +speed")
    print("z: -speed")
    print("w: +move")
    print("s: -move")
    print("a: +angz")
    print("d: -angz")
    
    twist = Twist()
    while(1):
        key = getch.getch()
        print(key)
        if key == "q" and speed < 3:
            speed += 0.15
            print("speed :",speed)
        elif key == "z" and speed > 0.2:
            speed -= 0.15
            print("speed :",speed)
        elif key == "w":
            twist.linear.x = speed
            
        elif key == "s":
            twist.linear.x = -speed
        elif key == "a":
            twist.angular.z = ang_z
        elif key == "d":
            twist.angular.z = -ang_z
        elif key == "b":
            twist.angular.z = 0
            twist.linear.x =0
        elif key == "f":
            break
        publisher.publish(twist)

        
        
        


main()


