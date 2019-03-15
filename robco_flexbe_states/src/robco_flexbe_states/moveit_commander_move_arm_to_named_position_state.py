#!/usr/bin/env python
import sys
# import copy
# import rospy
import moveit_commander
from flexbe_core import EventState, Logger
# from moveit_commander import MoveGroupCommander

"""
#     #################################
#     # SRG Stefan: 
#     # Created by Stefan SRG 13.3.2019, based on:	
#     # https://github.com/team-vigir/vigir_behaviors/blob/master/vigir_flexbe_states/src/vigir_flexbe_states/moveit_commander_move_group_state.py
#     #################################
"""

class MoveitCommanderMoveGroupNamedPositiomState(EventState):
  """
  Uses Moveit Commander to plan & execute trajectory to a named position.

	-- planning_group 	string 	Name of the MoveGroupCommander planning group.
  -- named_position 	string 	Name of the MoveGroupCommander named position to move the arm to.

  <= reached                  Navigation to named position succeeded.
  <= failed                   Navigation to named position failed.
  """
  
  def __init__(self, planning_group, named_position):
    """Constructor"""
    super(MoveitCommanderMoveGroupNamedPositiomState, self).__init__(outcomes=['reached', 'failed'])

    self._planning_group = planning_group
    self._named_position = named_position
    # Logger.loginfo("Predi inicializirane na robot comander")
    # moveit_commander.roscpp_initialize(sys.argv)
    Logger.loginfo("About to robot RobotCommander()")
    self.robot = moveit_commander.RobotCommander()
    Logger.loginfo("About to make PlanningSceneInterface()")
    self.scene = moveit_commander.PlanningSceneInterface()
   
    Logger.loginfo("About to make mgc in init with group %s" % self._planning_group)
    # self.group_to_move = moveit_commander.MoveGroupCommander(self._planning_group)
    self.group_to_move = moveit_commander.MoveGroupCommander('robot')

    Logger.loginfo("finished making mgc in init.")

    self._done = False


  def execute(self, userdata):
    """Execute this state"""
    if self._done is not False:
      return self._done
  
  def on_enter(self, userdata):
    # create the motion goal
    Logger.loginfo("Entering MoveIt Commander code!")

    # if len(self._joint_names) != len(userdata.target_joint_config):
    #   Logger.logwarn("Number of joint names (%d) does not match number of joint values (%d)"
    #                   % (len(self._joint_names), len(userdata.target_joint_config)))

    # self.group_to_move.set_joint_value_target(dict(zip(self._joint_names, userdata.target_joint_config)))
    self.group_to_move.set_start_state_to_current_state()
    self.group_to_move.clear_pose_targets()
    self.group_to_move.get_current_pose()
    self.group_to_move.set_named_target("reach_up")


    # execute the motion
    try: 
      Logger.loginfo("Moving %s to: %s" % (self._planning_group, self._named_position))
      result = self.group_to_move.go(wait=True)
    except Exception as e:
      Logger.logwarn('Was unable to execute move group request:\n%s' % str(e))
      self._done = "failed"

    if result:
      self._done = "reached"
    else:
      self._done = "failed"
