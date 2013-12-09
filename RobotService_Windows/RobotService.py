#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Python -*-

"""
 @file RobotService.py
 @brief ModuleDescription
 @date $Date$


"""
import sys
import time
sys.path.append(".")

# Import RTM module
import RTC
import OpenRTM_aist

import sqlite3


# Import Service implementation class
# <rtc-template block="service_impl">

# </rtc-template>

# Import Service stub modules
# <rtc-template block="consumer_import">
# </rtc-template>


# This module's spesification
# <rtc-template block="module_spec">
robotservice_spec = ["implementation_id", "RobotService", 
		 "type_name",         "RobotService", 
		 "description",       "ModuleDescription", 
		 "version",           "1.0.0", 
		 "vendor",            "Hiroaki Matsuda", 
		 "category",          "SERVER", 
		 "activity_type",     "STATIC", 
		 "max_instance",      "1", 
		 "language",          "Python", 
		 "lang_type",         "SCRIPT",
		 ""]
# </rtc-template>

##
# @class RobotService
# @brief ModuleDescription
# 
# 
class RobotService(OpenRTM_aist.DataFlowComponentBase):
	
	##
	# @brief constructor
	# @param manager Maneger Object
	# 
	def __init__(self, manager):
		OpenRTM_aist.DataFlowComponentBase.__init__(self, manager)

		self._d_str = RTC.TimedString(RTC.Time(0,0),"")
		"""
		"""
		self._stringOut = OpenRTM_aist.OutPort("string", self._d_str)

	def onInitialize(self):
		# Bind variables and configuration variable
		
		# Set InPort buffers
		self.addOutPort("string",self._stringOut)
		
		# Set OutPort buffers
		
		# Set service provider to Ports
		
		# Set service consumers to Ports
		
		# Set CORBA Service Ports

		self.first = 0
		self.last_index = 0
		
		return RTC.RTC_OK
	
	def onActivated(self, ec_id):
	
		return RTC.RTC_OK
	

	def onDeactivated(self, ec_id):
	
		return RTC.RTC_OK
	

	def onExecute(self, ec_id):

                if self.first == 0:

                        self.con = sqlite3.connect('./WebServer/data.db', isolation_level=None)
                        self.cur = self.con.cursor()
                        self.cur.execute("SELECT * from val")
                        for row in self.cur.fetchall():
                            self.last_index = row[0]

                        self.first = 1

                else:

                        self.cur.execute("SELECT * from val")
                        for row in self.cur.fetchall():
                                    if self.last_index < row[0]:
                                            self.last_index = row[0]
                                            print row[1]
                                            self._d_str.data = str(row[1])
                                            self._stringOut.write()
                    
	
		return RTC.RTC_OK
	

def RobotServiceInit(manager):
    profile = OpenRTM_aist.Properties(defaults_str=robotservice_spec)
    manager.registerFactory(profile,
                            RobotService,
                            OpenRTM_aist.Delete)

def MyModuleInit(manager):
    RobotServiceInit(manager)

    # Create a component
    comp = manager.createComponent("RobotService")

def main():
	mgr = OpenRTM_aist.Manager.init(sys.argv)
	mgr.setModuleInitProc(MyModuleInit)
	mgr.activateManager()
	mgr.runManager()

if __name__ == "__main__":
	main()

