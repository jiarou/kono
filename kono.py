

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

print "Start test sample"

# Connects to the current device, and return a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
print "ok"



# Kono app's package name
package = 'com.kono.reader'
# Kono app's name of the start Activity
main_activity = 'com.kono.reader.MainActivity'

run_component = package + '/' + main_activity 

print "Launching Kono"
device.startActivity(component=run_component)

# sending an event which simulate a click on the menu button

device.touch(340, 1144, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
print "touch world"

device.drag((441,723),(441,339),0.1,10)

device.drag((441,723),(441,339),0.1,10)

device.drag((441,723),(441,339),0.1,10)
MonkeyRunner.sleep(2)
device.touch(340, 1144, "DOWN_AND_UP")
MonkeyRunner.sleep(5)
device.touch(450, 235, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
device.touch(32, 95, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
device.touch(626, 228, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
device.touch(588, 380, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
device.touch(626, 228, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
device.touch(400, 378, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
device.touch(60, 98, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
device.touch(626, 228, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
device.touch(216, 351, "DOWN_AND_UP")
MonkeyRunner.sleep(2)
device.touch(32, 95, "DOWN_AND_UP")
MonkeyRunner.sleep(2)



print "End of script"