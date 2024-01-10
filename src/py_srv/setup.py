from setuptools import find_packages, setup

package_name = 'py_srv'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='issaiass',
    maintainer_email='issaiass@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'server_member_function = py_srv.server_member_function:main',
            'client_member_function = py_srv.client_member_function:main',
            'custom_server = py_srv.add_three_ints_server:main',
            'custom_client = py_srv.add_three_ints_client:main',
        ],
    },
)
