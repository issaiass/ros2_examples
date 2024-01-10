from setuptools import find_packages, setup

package_name = 'py_pubsub'

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
          'publisher = py_pubsub.publisher_member_function:main',
          'subscriber = py_pubsub.subscriber_member_function:main',
          'custom_publisher = py_pubsub.custom_publisher:main',
          'custom_subscriber = py_pubsub.custom_subscriber:main',
        ],
    },
)
