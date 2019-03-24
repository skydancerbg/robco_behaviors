#!/usr/bin/env python
import rospy
import math

from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxyPublisher, ProxySubscriberCached
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from tf import transformations

class TurnInPlaceMyVer(EventState):
    '''
	Turns the robot in place to a set angle in degrees

	-- angle 	float 	Angle to turn to in degrees
    -- speed    float   Turn speed

	<= failed 			    If behavior is unable to ready on time
	<= done 				Example for a failure outcome.

	'''
    def __init__(self, angle, speed):
        #add input and output keys
        super(TurnInPlaceMyVer, self).__init__(outcomes=['failed', 'done'])
        self.odom_data = None
        self.initial_orientation = None
        self.cur_orientation = None
        self._angle = angle
        self._speed = speed
        self._turn = False
        self._turn_angle = None
        self.cmd_pub = Twist()
        # self.sub = rospy.Subscriber("/odom", Odometry, self.odom_callback)
        # self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10 )

        self._vel_topic = '/cmd_vel'
        self._odom_topic = '/odom'

        #create publisher passing it the vel_topic_name and msg_type
        self.pub = ProxyPublisher({self._vel_topic: Twist})
        #create subscriber
        self.odom_sub = ProxySubscriberCached({self._odom_topic: Odometry})

    def execute(self, userdata):
        Logger.loginfo('Entering execute')

        if self.odom_sub.has_msg(self._odom_topic):
            self.data = self.odom_sub.get_last_msg(self._odom_topic)
            self.odom_sub.remove_last_msg(self._odom_topic)
            # Logger.loginfo('Odom data.pose.pose.orientation: %s' % self.data.pose.pose.orientation)
            self.cur_orientation = self.data.pose.pose.orientation
            
            cur_angle = transformations.euler_from_quaternion((self.cur_orientation.x, self.cur_orientation.y, 
            self.cur_orientation.z, self.cur_orientation.w))
    
            start_angle = transformations.euler_from_quaternion((self.initial_orientation.x, self.initial_orientation.y, 
            self.initial_orientation.z, self.initial_orientation.w))

            Logger.loginfo('initial orientation: %f' % start_angle[2])
            Logger.loginfo('current orientation: %f' % cur_angle[2])
            
            turn_so_far = math.fabs(cur_angle[2] - start_angle[2])
            #  Logger.loginfo      ("Current Robot turn at: %f" % turn_so_far)
            #send feedback (current Robot Heading)
            # self._feedback.heading = turn_so_far
            Logger.loginfo      ("The Robot turned so far: %s" % turn_so_far)
            
            if (turn_so_far >= self._turn_angle):
                #reset some variables if done turning
                self._turn = False
                # self.initial_orientation = None
                # self._result.done = "done"
                # self._as.set_succeeded(self._result)
                Logger.loginfo      ("Turn successfully completed!")
                return 'done'
                    
       
            # Turn the robot
            Logger.loginfo('# Turn the robot')

            if self._turn:
                self.cmd_pub.linear.x = 0.0
                if self._angle   > 0:
                    self.cmd_pub.angular.z = self._speed
                else:
                    self.cmd_pub.angular.z = -self._speed
                self.pub.publish(self._vel_topic, self.cmd_pub)
            
            else: #stop the robot before breaking out
                Logger.loginfo('#stop the robot before breaking out')
                self.cmd_pub.angular.z = 0.0
                self.pub.publish(self._vel_topic, self.cmd_pub)
                # return 'done'


                       

        
    def on_exit(self, userdata):
        self.cmd_pub.angular.z = 0.0
        self.pub.publish(self._vel_topic, self.cmd_pub)
        #self.scan_sub.unsubscribe_topic(self.scan_topic)
        Logger.loginfo("Turn in place ENDED!")
        
    def on_start(self):
        Logger.loginfo("Turn in place READY!")
        # self._start_time = rospy.Time.now() #bug detected! (move to on_enter)
        if not self.pub:
            Logger.loginfo('Failed in - if not self.pub: ')
            return 'failed'
        #read odom data
        if self.odom_sub.has_msg(self._odom_topic):
            self.data = self.odom_sub.get_last_msg(self._odom_topic)
            # self.odom_sub.remove_last_msg(self._odom_topic)
            Logger.loginfo('Initial Robot orientation: %s' % self.data.pose.pose.orientation)
            self.cur_orientation = self.data.pose.pose.orientation
        # r = rospy.Rate(30)
        self._turn_angle = math.fabs((self._angle   * math.pi)/ 180)
        Logger.loginfo ("TAngle to turnt to in Rad: %s" % self._turn_angle)
        
        #set initial orientation
        if not self.initial_orientation:
            Logger.loginfo('if not self.initial_orientation ')
            self.initial_orientation = self.cur_orientation
            self._turn = True
   
        
    def on_stop(self):
		Logger.loginfo("Turn in place STOPPED!")
		self.cmd_pub.linear.x = 0.0
		self.pub.publish(self._vel_topic, self.cmd_pub)

    def scan_callback(self, data):
        self.data = data