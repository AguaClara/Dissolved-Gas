#ProCoDa Method File

##States
- *OFF*: The peristaltic pump is off.
- *Running*: The peristaltic pump is running.


##Set Points
- *OFF*:This setpoint is used to turns all outputs off.
- *ON*: This setpoint turns on the peristaltic pump on.
- *PumpOutput*: This setpoint is used to turn on the peristaltic pump at the correct number of RPMs to achieve the desired flow rate, given the Tubing ID.


##Variables
- *FlowRate*: This variable is the desired flow rate. In the subteam's reactor, this represents the fluidization velocity.
- *TubingID*: This variable represents the ID associated with tubing being used, based on the diameter of the tubing.
