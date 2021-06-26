import rospy


class BaseClass(object):

    def __init__(self, name):

        self.name = name

    def run(self):

        rospy.logerr('name: {}, Please implement this method'.format(self.name))
