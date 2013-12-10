# Author: silvio.traversaro@iit.it    
#

import sys
import time
import os
from optparse import OptionParser

import naoqi
from naoqi import ALProxy

#This is the list of the names of the device to log
sensor_to_log_list = [ 'DCM/Time',
                       'DCM/CycleTime',
                       'Device/SubDeviceList/Head/Touch/Middle/Sensor/Value',
                       "Device/SubDeviceList/HeadPitch/Position/Sensor/Value",
                       "Device/SubDeviceList/HeadYaw/Position/Sensor/Value",
                       "Device/SubDeviceList/LAnklePitch/Position/Sensor/Value",
                       "Device/SubDeviceList/LAnkleRoll/Position/Sensor/Value",
                       "Device/SubDeviceList/LElbowRoll/Position/Sensor/Value",
                       "Device/SubDeviceList/LElbowYaw/Position/Sensor/Value",
                       "Device/SubDeviceList/LHand/Position/Sensor/Value",
                       "Device/SubDeviceList/LHipPitch/Position/Sensor/Value",
                       "Device/SubDeviceList/LHipRoll/Position/Sensor/Value",
                       "Device/SubDeviceList/LHipYawPitch/Position/Sensor/Value",
                       "Device/SubDeviceList/LKneePitch/Position/Sensor/Value",
                       "Device/SubDeviceList/LShoulderPitch/Position/Sensor/Value",
                       "Device/SubDeviceList/LShoulderRoll/Position/Sensor/Value",
                       "Device/SubDeviceList/LWristYaw/Position/Sensor/Value",
                       "Device/SubDeviceList/RAnklePitch/Position/Sensor/Value",
                       "Device/SubDeviceList/RAnkleRoll/Position/Sensor/Value",
                       "Device/SubDeviceList/RElbowRoll/Position/Sensor/Value",
                       "Device/SubDeviceList/RElbowYaw/Position/Sensor/Value",
                       "Device/SubDeviceList/RHand/Position/Sensor/Value",
                       "Device/SubDeviceList/RHipPitch/Position/Sensor/Value",
                       "Device/SubDeviceList/RHipRoll/Position/Sensor/Value",
                       "Device/SubDeviceList/RKneePitch/Position/Sensor/Value",
                       "Device/SubDeviceList/RShoulderPitch/Position/Sensor/Value",
                       "Device/SubDeviceList/RShoulderRoll/Position/Sensor/Value",
                       "Device/SubDeviceList/RWristYaw/Position/Sensor/Value",
                       "Device/SubDeviceList/InertialSensor/AccelerometerX/Sensor/Value",
                       "Device/SubDeviceList/InertialSensor/AccelerometerY/Sensor/Value",
                       "Device/SubDeviceList/InertialSensor/AccelerometerZ/Sensor/Value",
                       "Device/SubDeviceList/InertialSensor/GyroscopeX/Sensor/Value",
                       "Device/SubDeviceList/InertialSensor/GyroscopeY/Sensor/Value",
                       "Device/SubDeviceList/InertialSensor/AngleX/Sensor/Value",
                       "Device/SubDeviceList/InertialSensor/AngleY/Sensor/Value",
		       "Device/SubDeviceList/LFoot/FSR/FrontLeft/Sensor/Value",
                       "Device/SubDeviceList/LFoot/FSR/FrontRight/Sensor/Value",
                       "Device/SubDeviceList/LFoot/FSR/RearLeft/Sensor/Value",
                       "Device/SubDeviceList/LFoot/FSR/RearRight/Sensor/Value",
                       "Device/SubDeviceList/RFoot/FSR/FrontLeft/Sensor/Value",
                       "Device/SubDeviceList/RFoot/FSR/FrontRight/Sensor/Value",
                       "Device/SubDeviceList/RFoot/FSR/RearLeft/Sensor/Value",
                       "Device/SubDeviceList/RFoot/FSR/RearRight/Sensor/Value"]
                        
def getdata(NAOIP='nao.local',NAOPORT=9559,PERIOD_IN_SECONDS=0.05):                                        #set name
    log=ALProxy('ALLogger',NAOIP,NAOPORT)                                #call ALLogger
    frame = ALProxy('ALFileManager',NAOIP,NAOPORT)                        #call ALFileManager
    
    filepath = "/home/nao/datalog.tsv"                                #try to open file
    
    try:
        output=open(filepath,'w')                                    #use os.open ,1 for buffer
        log.info('log','file opened success!!')
    except Exception,e:
        log.info('log','file opened failed!!')
        exit('stop')                                                        #stop when failed    returns "1"
 
    mem = ALProxy('ALMemory',NAOIP,NAOPORT)                            #call ALMemory
    output.write('SampleNumber\t'+('\t'.join(sensor_to_log_list)))
    output.flush()
    x=0
    log.info('log','loop start')
    while 1:
        start_time = time.time()
        data = mem.getListData(sensor_to_log_list)
        data.insert(0,x)
        str_data = map(str,data)
        temp_data = '\t'.join(str_data)
        output.write(temp_data+'\n')
        x += 1
        end_time = time.time()
        #print('Seconds for getting data and putting in file: '+str(end_time-start_time))
        #quick hack to avoid busy waiting 
        remaining_time = PERIOD_IN_SECONDS-end_time+start_time;
	if( remaining_time > 0 ):
	    time.sleep(remaining_time)
        
def main():
    """ Script to dump values of the sensors related to identifiation on 
        NAO. 
        

    """
    parser = OptionParser()
    parser.add_option("--pip",
                      help="Parent broker port. The IP address or your robot",
                    dest="pip")
    parser.add_option("--pport",
        help="Parent broker port. The port NAOqi is listening to",
        dest="pport",
        type="int")
    parser.set_defaults(
        pip='nao.local',
        pport=9559)

    (opts, args_) = parser.parse_args()
    pip   = opts.pip
    pport = opts.pport
    
    #todo: use pip and pport configure by NAO
    getdata()
    

main()    
