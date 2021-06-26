import rospy
from base.libbase import BaseClass


class PrintPlugin(BaseClass):

    def __init__(self, name):

        super(PrintPlugin, self).__init__(name)

    def run(self):

        rospy.loginfo('name: {}, this class is PrintPlugin'.format(self.name))
