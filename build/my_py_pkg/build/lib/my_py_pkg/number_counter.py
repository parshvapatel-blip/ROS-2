#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool 


class NumberCounterNode(Node): 
    def __init__(self):
        super().__init__("number_counter") 
        self.subscriber_ = self.create_subscription(Int64 , "number" ,self.callback, 10 )
        self.publisher_ = self.create_publisher(Int64 , "number_count" , 10)
        self.create_timer(1 , self.publish)
        self.get_logger().info("Counting numbers...")
        self.counter_ = 0
        self.server_ = self.create_service(SetBool , "reset_counter" , self.callback_reset_counter)

    def callback(self , msg):
        self.counter_ += 1

    def publish(self):
        msg = Int64()
        msg.data = self.counter_
        self.publisher_.publish(msg)

    def callback_reset_counter(self , request: SetBool.Request, response: SetBool.Response):
        data = request.data
        if data == True:
            self.counter_  = 0

        if self.counter_ == 0:
            response.success = True
            response.message = "No error"
        else:
            response.success = False
            response.message = "Could not reset to 0"

        return response

        
 
 
def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()