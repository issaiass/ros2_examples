cmake_minimum_required(VERSION 3.8)
project(cpp_pubsub)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(custom_msg_srv REQUIRED)


if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

add_executable(publisher src/publisher_member_function.cpp)
ament_target_dependencies(publisher rclcpp std_msgs)

add_executable(subscriber src/subscriber_member_function.cpp)
ament_target_dependencies(subscriber rclcpp std_msgs)

# custom messages uses this
add_executable(custom_publisher src/custom_msg_publisher.cpp)
ament_target_dependencies(custom_publisher rclcpp geometry_msgs custom_msg_srv)

add_executable(custom_subscriber src/custom_msg_subscriber.cpp)
ament_target_dependencies(custom_subscriber rclcpp geometry_msgs custom_msg_srv)

install(TARGETS
  publisher
  subscriber
  custom_publisher
  custom_subscriber
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
