from multiprocessing import cpu_count
import os

bind = "0.0.0.0:5000"

if os.environ.get("PATCHSERVER_PORT"):
   print "Change port for patchserver"
   bind = "0.0.0.0:"+os.environ.get("PATCHSERVER_PORT")

workers = 2
threads = 2 * cpu_count()
