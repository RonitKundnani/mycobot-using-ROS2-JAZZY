# myCobot 280 — ROS 2 (Jazzy) Arm Simulation & Motion Planning

Simulation of a 6-DOF myCobot 280 manipulator in Gazebo with collision-aware
motion planning via MoveIt.


## Stack
ROS 2 Jazzy · MoveIt · Gazebo · RViz · URDF

## Run
```bash
colcon build
source install/setup.bash
ros2 launch mycobot_moveit demo.launch.py
