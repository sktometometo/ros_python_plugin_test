cmake_minimum_required(VERSION 3.0.2)
project(base)

find_package(catkin REQUIRED)

catkin_python_setup()

catkin_package(
)

#catkin_install_python(PROGRAMS
#  scripts/my_python_script
#  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
#)
