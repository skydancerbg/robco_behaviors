#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from flexbe_core import EventState, Logger
# from moveit_commander import MoveGroupCommander


    #################################
    # SRG Stefan: Created by SRG 13.3.2019
    # Based on: https://github.com/team-vigir/vigir_behaviors/blob/master/vigir_flexbe_states/src/vigir_flexbe_states/moveit_commander_move_group_state.py
    #################################

class MoveitCommanderMoveToNamedPositionState(EventState):
  """
  Uses moveit commander to move the arm to named position.

  <= reached 			  Named position reached.
  <= failed 				Example for a failure outcome.
  """
  
  def __init__(self):
    """Constructor"""
    super(MoveitCommanderMoveToNamedPositionState, self).__init__(outcomes=['reached', 'failed'])

    # self._planning_group = planning_group_name
    self._planning_group = "robot"
    # self._named_position = named_position_name
    # self._joint_names = joint_names
    # Logger.loginfo("About to make mgc in init with group %s" % self._planning_group)
    Logger.loginfo("mina init")

    self._done = False


  def execute(self, userdata):
    """Execute this state"""
    if self._done is not False:
      return self._done
  
  def on_enter(self, userdata):
    # create the motion goal
    # Logger.loginfo("Entering MoveIt Commander code!")

    # if len(self._joint_names) != len(userdata.target_joint_config):
    #   Logger.logwarn("Number of joint names (%d) does not match number of joint values (%d)"
    #                   % (len(self._joint_names), len(userdata.target_joint_config)))

    # self.group_to_move.set_joint_value_target(dict(zip(self._joint_names, userdata.target_joint_config)))               


    # execute the motion
    try: 
      # KCLogger.loginfo("Moving %s to: %s" % (self._planning_group, ", ".join(map(str, userdata.target_joint_config))))
      # result = self.group_to_move.go()
      Logger.loginfo("predi 0 red")
      moveit_commander.roscpp_initialize(sys.argv)
      Logger.loginfo("predi 1 red")
      robot = moveit_commander.RobotCommander()
      Logger.loginfo("predi 2 red")
      scene = moveit_commander.PlanningSceneInterface()
      Logger.loginfo("predi 3 red")
      group = moveit_commander.MoveGroupCommander("robot")

      Logger.loginfo("finished making mgc in init.")
      group.set_start_state_to_current_state()
      group.clear_pose_targets()
      group.get_current_pose()
      group.set_named_target("reach_up")
      result = group.go(wait=True)
    except Exception as e:
      Logger.logwarn('Was unable to execute move group request:\n%s' % str(e))
      self._done = "failed"

    if result:
      self._done = "reached"
    else:
      self._done = "failed"

  def on_exit(self, userdata):
		# This method is called when an outcome is returned and another state gets active.
		# It can be used to stop possibly running processes started by on_enter.

		# pass # Nothing to do in this example.
    moveit_commander.roscpp_shutdown()


















############################################################################################################
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from flexbe_core import EventState, Logger
# from moveit_commander import MoveGroupCommander


    #################################
    # SRG Stefan: Created by SRG 13.3.2019
    # Based on: https://github.com/team-vigir/vigir_behaviors/blob/master/vigir_flexbe_states/src/vigir_flexbe_states/moveit_commander_move_group_state.py
    #################################

class MoveitCommanderMoveToNamedPositionState(EventState):
  """
  Uses moveit commander to move the arm to named position.

  <= reached 			  Named position reached.
  <= failed 				Example for a failure outcome.
  """
  
  def __init__(self):
    """Constructor"""
    super(MoveitCommanderMoveToNamedPositionState, self).__init__(outcomes=['reached', 'failed'])

    # self._planning_group = planning_group_name
    self._planning_group = "robot"
    # self._named_position = named_position_name
    # self._joint_names = joint_names
    # Logger.loginfo("About to make mgc in init with group %s" % self._planning_group)
    Logger.loginfo("predi 0 red")
    moveit_commander.roscpp_initialize(sys.argv)
    Logger.loginfo("predi 1 red")
    self._robot = moveit_commander.RobotCommander()
    Logger.loginfo("predi 2 red")
    self._scene = moveit_commander.PlanningSceneInterface()
    Logger.loginfo("predi 3 red")
    self._group = moveit_commander.MoveGroupCommander("robot")

    Logger.loginfo("finished making mgc in init.")

    self._done = False


  def execute(self, userdata):
    """Execute this state"""
    if self._done is not False:
      return self._done
  
  def on_enter(self, userdata):
    # create the motion goal
    # Logger.loginfo("Entering MoveIt Commander code!")

    # if len(self._joint_names) != len(userdata.target_joint_config):
    #   Logger.logwarn("Number of joint names (%d) does not match number of joint values (%d)"
    #                   % (len(self._joint_names), len(userdata.target_joint_config)))

    # self.group_to_move.set_joint_value_target(dict(zip(self._joint_names, userdata.target_joint_config)))               


    # execute the motion
    try: 
      # KCLogger.loginfo("Moving %s to: %s" % (self._planning_group, ", ".join(map(str, userdata.target_joint_config))))
      # result = self.group_to_move.go()
      self._group.set_start_state_to_current_state()
      self._group.clear_pose_targets()
      self._group.get_current_pose()
      self._group.set_named_target("reach_up")
      result = self._group.go(wait=True)
    except Exception as e:
      Logger.logwarn('Was unable to execute move group request:\n%s' % str(e))
      self._done = "failed"

    if result:
      self._done = "reached"
    else:
      self._done = "failed"

  def on_exit(self, userdata):
		# This method is called when an outcome is returned and another state gets active.
		# It can be used to stop possibly running processes started by on_enter.

		# pass # Nothing to do in this example.
    moveit_commander.roscpp_shutdown()