#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from my_robot_interfaces.msg import HardwareStatus

class HardwareSatusPublisherNode(Node): # Modify Name
    def __init__(self):
        super().__init__("hardware_status_publisher") # Modify Name
        self.hw_status_pub_ = self.create_publisher(HardwareStatus, "hardware_statuss", 10)
        self.timer_ = self.create_timer(1.0, )
        self.get_logger().info("Hw status publisher has started.")
    
    def publish_hw_status(self):
        msg = HardwareStatus()
        msg.temprature = 43.7
        msg.are_motors_ready = True
        msg.debig_message = "Mothing Special"
        self.hw_status_pub_.publish(msg)

def main(args = None):
    rclpy.init(args = args)
    node = HardwareSatusPublisherNode() # Modify Name
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()