# Pressure within a bubble

The hypothesis in this file is an in-progress attempt to connect information drawn from the various sources in the Literature folder. Hopefully, the various relationships and equations concerning pressure, surface tension, reactor height, and gas solubility will unify into one cohesive relationship of properties.

For the sake of brevity, all mentioned sources are found in the Literature folder. Sources are cited in the following format: <Page> <Source>, e.g. "Surface Tension Source 2".

According to Surface Tension Source 1, the pressure within a bubble is directly related to the pressure outside the bubble, plus a quotient determined by the liquid's surface tension and the bubble's radius.

The subteam considers that the pressure outside of the bubble, the pressure within the liquid, may be determined by the atmospheric pressure plus a change in pressure due to the height of the reactor due to a reference point (in this case, the reference point is the vent for the bubbles, downstream from the reactor). Pressure changes due to height are addressed in Ambient Pressure and Gas Solubility Source 4.

The subteam considers that the pressure relevant to Henry's Law is the pressure within the bubble; the lower the pressure within the bubble, the lower the solubility of the gas in the surrounding solution. This is addressed in Ambient Pressure and Gas Solubility Source 1.

The subteam believes that the equations relating these quantities may be combined to form one cohesive equation. This equation gives the solubility of the gas in solution as a function of a bubble's radius, the height of the reactor, surface tension, and the constant relevant to Henry's Law.

This theory may act as an approximation of the pressure within the bubbles. These equations assume equilibrium: that the rates of air shifting from liquid to gas phase and vice versa are equal. This may not be the case in the entirety of the reactor.

Head loss in the effluent tubing must also be taken into account.

The following group of equations may be combined, given the above reasoning:

From Ambient Pressure Source 1:
$$C = k P $$

In this equation, P approximates the gas pressure within a bubble; the subteam considers the bubble-water border as an interface between a liquid and a gas, as considered by Henry's Law. Therefore, P will be denoted as $P_b$ (pressure in a bubble).

From Ambient Pressure Source 4:
$$ P = \rho g h $$

From this equation one can extrapolate that $ \Delta P = \rho g \Delta h $. In this equation, the difference in pressure is that between atmospheric pressure (the pressure at the open-faced vent, downstream from the reactor) and the pressure within the reactor itself. Therefore, if $\Delta P$ is expanded to $P_r - P_{atm}$ (pressure in the reactor minus atmospheric pressure), this equation may be modified to read as $P_r = P_{atm} + \rho g \Delta h $.


From Ambient Pressure Source 5:
$$ h_f = \frac{32\mu L V}{\rho g D^2} $$

Pressure difference due to head loss must also be taken into account, in terms of the pressure difference between the open-faced vent and the reactor itself. Combined with the previous equation, the relationship becomes: $P_r = P_{atm} - \rho g \Delta h +  \rho g h_f $. The reasoning for the negative sign prior to the second term is as follows: the reactor is higher than the vent; therefore, $\Delta h$ is a positive term. However, pressure decreases as depth decreases. The negative sign's purpose is to indicate this relationship and illustrate it mathematically.  

From Surface Tension Source 1:
$$P_i = P_o + 4 \frac{T}{R}$$

In this equation, $P_i$ denotes the pressure within a bubble, and may be relabeled as $P_b$. $P_o$ denotes the pressure outside of the bubble, which may be denoted $P_r$ given the above reasoning.

When all of these equations are combined, the following relationship appears:

$$C = k(\frac{4T}{R} + P_{atm} - \rho g \Delta h +  \rho g h_f)$$

Due to the above reasoning concerning assumption of equilibrium, the above equation is a qualitative description of the relationships between different parameters, rather than a quantitative relationship. All variables that are left undefined on this page are defined in their respective pages in the Literature folder. 
