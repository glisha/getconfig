#!/usr/bin/python

import ConfigParser
import subprocess
import datetime
import os
import tools
import threading


Config = ConfigParser.ConfigParser()
Config.read("getconfig.ini")
timeout = int(Config.get('GENERAL','timeout'))
mail_from = Config.get('GENERAL','mail_from').split()
mail_to = Config.get('GENERAL','alert_mails').split()

Config = ConfigParser.ConfigParser()
Config.read("device_list.ini")

mail_body = ""
for device in Config.sections():
        type = Config.get(device,'type')
        ip = Config.get(device,'ip')
        user = Config.get(device,'user')
        password = Config.get(device,'password')
        enable = Config.get(device,'enable')

        datum = datetime.datetime.now().strftime("%Y-%m-%d")

        output_dir = "configs/%s/" % (datum)
        if not os.path.exists(output_dir):
                os.makedirs(output_dir) 
        output_path = "%s/%s.config_run%s" % (output_dir,device,os.getpid())
        output_file = open(output_path,"w")

        expect_path = "expect/%s" % type

        proc = subprocess.Popen(['/usr/bin/expect',expect_path,ip,device,user,password,enable],stdout = output_file, stderr = subprocess.PIPE)

        #set timer to kill hanged connections   
        kill_proc = lambda p: p.kill()
        timer = threading.Timer(timeout, kill_proc, [proc])

        try:
                timer.start()
                stdout,stderr = proc.communicate()
                if not proc.returncode == 0:
                        mail_body += "Backup of %s - %s (%s)  FAILED.<br>" % (type,device,ip)
                        mail_subject = "Switch backup script FAILED."
                        print "Processing %s - %s (%s)  FAILED." % (type,device,ip)
                else:
                        print "Processing %s - %s (%s) success" % (type,device,ip)
        finally:
                timer.cancel()

if not mail_body == "":
        tools.mail_send(mail_from, mail_to, mail_subject, mail_body)

