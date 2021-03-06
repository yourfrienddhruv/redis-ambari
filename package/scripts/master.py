import sys, os, pwd, signal, time
from resource_management import *
from subprocess import call

class Master(Script):
  def install(self, env):

    # Install packages listed in metainfo.xml
    self.install_packages(env)

    #if any other install steps were needed they can be added here

  #To stop the service, use the linux service stop command and pipe output to log file
  def stop(self, env):
    import params
    Execute('service redis stop >>' + params.stack_log)

  #To start the service, use the linux service start command and pipe output to log file
  def start(self, env):
    import params
    Execute('service redis start >>' + params.stack_log)

  #To get status of the, use the linux service status command
  def status(self, env):
    import params
    Execute('service redis status')

if __name__ == "__main__":
  Master().execute()
