nao_scripts
===========

nao_identification_datalogger.py
--------------------------------

###Upload on the Nao
To upload the script on the Nao, you can use scp:
```
scp nao_identification_datalogger.py nao@192.168.1.1:/home/nao/nao_identification_datalogger.py
```
where you have to substitute 192.168.1.1 with Nao IP address.

Or simply use the [upload utility of Choreographe]
(http://www.aldebaran-robotics.com/documentation/software/choregraphe/file_upload_download.html)

###Execute
You can execute the script directly from the nao terminal:
```
ssh  nao@192.168.1.1
./nao_identification_datalogger.py
```
this will save the data in the /home/nao/datalog.tsv file.

Alternativly you can modify the /home/nao/naoqi/preferences/autoload.ini file to automatically
execute the script at the boot of the Nao, as described in [Nao documentation](http://www.aldebaran-robotics.com/documentation/dev/python/running_python_code_on_the_robot.html)
Warning: this could saturate Nao on-board disk if you leave it open for a long time.
