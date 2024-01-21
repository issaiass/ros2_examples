from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    cpp_parameter = Node(
        package="cpp_parameters",
        executable="param_node_cpp",
        name="param_node_cpp",
        output="screen",
        emulate_tty=True,
        parameters=[{"my_parameter": "Panama"}]
    )

    ld.add_action(cpp_parameter)
    
    return ld
