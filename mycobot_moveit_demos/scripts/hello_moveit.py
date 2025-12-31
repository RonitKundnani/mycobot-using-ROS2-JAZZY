#!/usr/bin/env python3
"""
@file hello_moveit.py
@brief ROS 2 + MoveIt 2 Python example (OOP style)

This node demonstrates how to use MoveIt 2 from Python
using a class-based (OOP) design.
"""

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseStamped
from moveit.planning import MoveGroupInterface


class HelloMoveIt(Node):
    """
    A class-based ROS 2 node for controlling a robot arm using MoveIt 2.
    """

    def __init__(self):
        super().__init__(
            "hello_moveit",
            automatically_declare_parameters_from_overrides=True
        )

        self.get_logger().info("Initializing HelloMoveIt node...")

        # Create MoveGroupInterface for the arm
        self.arm_group = MoveGroupInterface(
            node=self,
            name="arm"
        )

        self._configure_moveit()
        self._move_to_target_pose()

    def _configure_moveit(self):
        """Configure planner, pipeline, and limits."""

        self.arm_group.set_planning_pipeline_id("ompl")
        self.arm_group.set_planner_id("RRTConnectkConfigDefault")
        self.arm_group.set_planning_time(1.0)

        self.arm_group.set_max_velocity_scaling_factor(1.0)
        self.arm_group.set_max_acceleration_scaling_factor(1.0)

        self.get_logger().info(
            f"Pipeline: {self.arm_group.get_planning_pipeline_id()}"
        )
        self.get_logger().info(
            f"Planner: {self.arm_group.get_planner_id()}"
        )
        self.get_logger().info(
            f"Planning time: {self.arm_group.get_planning_time():.2f}s"
        )

    def _move_to_target_pose(self):
        """Plan and execute motion to a target pose."""

        target_pose = PoseStamped()
        target_pose.header.frame_id = "base_link"
        target_pose.header.stamp = self.get_clock().now().to_msg()

        target_pose.pose.position.x = 0.061
        target_pose.pose.position.y = -0.176
        target_pose.pose.position.z = 0.168

        target_pose.pose.orientation.x = 1.0
        target_pose.pose.orientation.y = 0.0
        target_pose.pose.orientation.z = 0.0
        target_pose.pose.orientation.w = 0.0

        self.arm_group.set_pose_target(target_pose)

        self.get_logger().info("Planning to target pose...")

        success, plan = self.arm_group.plan()

        if success:
            self.get_logger().info("Planning successful. Executing...")
            self.arm_group.execute(plan)
        else:
            self.get_logger().error("Planning failed!")


def main():
    rclpy.init()
    node = HelloMoveIt()
    rclpy.shutdown()


if __name__ == "__main__":
    main()


"""#!/usr/bin/env python3
# 
# @file hello_moveit.py
# @brief ROS 2 + MoveIt 2 Python example (OOP style)

# This node demonstrates how to use MoveIt 2 from Python
# using a class-based (OOP) design.
# 

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseStamped
from moveit.planning import MoveGroupInterface


class HelloMoveIt(Node):
    
    #A class-based ROS 2 node for controlling a robot arm using MoveIt 2.
    

    def __init__(self):
        super().__init__(
            "hello_moveit",
            automatically_declare_parameters_from_overrides=True
        )

        self.get_logger().info("Initializing HelloMoveIt node...")

        # Create MoveGroupInterface for the arm
        self.arm_group = MoveGroupInterface(
            node=self,
            name="arm"
        )

        self._configure_moveit()
        self._move_to_target_pose()

    def _configure_moveit(self):
        #Configure planner, pipeline, and limits.

        self.arm_group.set_planning_pipeline_id("ompl")
        self.arm_group.set_planner_id("RRTConnectkConfigDefault")
        self.arm_group.set_planning_time(1.0)

        self.arm_group.set_max_velocity_scaling_factor(1.0)
        self.arm_group.set_max_acceleration_scaling_factor(1.0)

        self.get_logger().info(
            f"Pipeline: {self.arm_group.get_planning_pipeline_id()}"
        )
        self.get_logger().info(
            f"Planner: {self.arm_group.get_planner_id()}"
        )
        self.get_logger().info(
            f"Planning time: {self.arm_group.get_planning_time():.2f}s"
        )

    def _move_to_target_pose(self):
        # Plan and execute motion to a target pose.

        target_pose = PoseStamped()
        target_pose.header.frame_id = "base_link"
        target_pose.header.stamp = self.get_clock().now().to_msg()

        target_pose.pose.position.x = 0.061
        target_pose.pose.position.y = -0.176
        target_pose.pose.position.z = 0.168

        target_pose.pose.orientation.x = 1.0
        target_pose.pose.orientation.y = 0.0
        target_pose.pose.orientation.z = 0.0
        target_pose.pose.orientation.w = 0.0

        self.arm_group.set_pose_target(target_pose)

        self.get_logger().info("Planning to target pose...")

        success, plan = self.arm_group.plan()

        if success:
            self.get_logger().info("Planning successful. Executing...")
            self.arm_group.execute(plan)
        else:
            self.get_logger().error("Planning failed!")


def main():
    rclpy.init()
    node = HelloMoveIt()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
"""