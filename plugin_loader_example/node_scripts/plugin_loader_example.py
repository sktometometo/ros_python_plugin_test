#!/usr/bin/env python

import rospy

def main():

    rospy.init_node('plugin_loader_example')

    package_name = rospy.get_param('~package')
    module_name = rospy.get_param('~module_name')
    class_name = rospy.get_param('~class_name')

    try:
        pluginclass = getattr(getattr(__import__(package_name),module_name),class_name)
    except Exception as e:
        rospy.logerr('Plugin load failed: {}'.format(e))
        return

    # need validation that pluginclass is a child class of baseclass

    rate = rospy.Rate(1)
    instance = pluginclass('test')
    while not rospy.is_shutdown():
        rate.sleep()
        instance.run()


if __name__ == '__main__':
    main()
