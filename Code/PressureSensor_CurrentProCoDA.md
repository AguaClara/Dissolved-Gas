### Current Prototype: ProCoDA

The following template was copied from the Report Template Spring 2019 file in the Research Reports folder.

---
## ProCoDA Method File
Use this section to explain your method file. This could be broken up into several components as shown below:

### States
Here, you should describe the function of each state in your method file, both in terms of its overall purpose and also in terms of the details that make it distinct from other states. For example:
\begin{itemize}
\item \underline{OFF} - Resting state of ProCoDA. All sensors, relays, and pumps are turned off.
\end{itemize}

### Set Points

Here, you should list the set points used in your method file and explain their use as well as how each was calculated.
---
The following was recorded on February 21, 2019.

## ProCoDA Method file
### States
We are not using states for our experiments since they will also be short term and handle manually.

### Set Points
1) ON Setpoint; this is when the system is being used
2) OFF Setpoint; this is when the system is not being used
3) Tubing ID Setpoint; this is a constant variable which is the code of the pump tubing we used
4) Flow Rate Setpoint; this is a constant which is the flow-rate going through the reactor
5) Tubing Output Setpoint; This is a variable setpoint which incorporates Tubing ID and Flow Rate in order to give fluidization velocity
