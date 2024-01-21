from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()
    
    param_node = Node(
        package='py_parameters',
        executable='py_param_node',
        name='py_parameters_node',
        output='screen',
        emulate_tty=True,
        parameters=[{'my_parameter': 'Panama'}]
    )
    
    ld.add_action(param_node)

    return ld
