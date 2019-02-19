### Analysis of Literature

*The following is equivalent to the Analysis of Literature section found in the Final Report from Fall 2018. However, certain sections have been edited for clarity. The content of this document will likely be used to edit future reports.*

Through conceptual analysis and algebraic manipulation, Equations 2-6 combine to form an estimation of a gas’ solubility in water in an apparatus as illustrated in Figure 1. The following paragraphs describe this process; all variables have been defined in the Literature Review section.

The pressure relevant to Henry's Law (i.e. the pressure of a gas above a liquid, in [Equation 2](#Equation-2)) is the pressure *within* a bubble [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html).
$$ C = k P $$

$P$ equates to the gas's pressure within a bubble. Therefore, $P$ is relabeled as $P_b$ (i.e. pressure in a bubble).

As shown in [Equation 6](#Equation-6), the pressure within a bubble is directly related to the bubble's radius, the liquid's surface tension, and the pressure outside the bubble [(Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html).

$$P_i = P_o + 4 \frac{T}{R}$$

$P_i$ denotes the pressure within a bubble and therefore is relabeled as $P_b$. $P_o$ denotes the pressure outside of the bubble and is relabeled $P_r$ (i.e. pressure in the liquid within the reactor).

The pressure outside of the bubble can be equated to atmospheric pressure, plus a change in pressure due to the height difference between the reactor and the vent ($\Delta P_{height}$) [(Equation 3)](#Equation-3), plus a change in pressure due to head loss in the tubing connecting the reactor and the vent ($\Delta P_{head loss}$) [(Equation 5)](#Equation-5).

$$\Delta P_{height} = \rho g \Delta h$$

$$\Delta P_{head loss} = \rho g h_f$$

The greater the difference in height, the lower the pressure within the reactor. The greater the head loss, the greater the pressure within the reactor. Thus, the pressure within the reactor may be written as follows:

####Equation 3.1

$$P_r = P_{atm} + \Delta P_{height} + \Delta P_{head loss} = P_{atm} - \rho g \Delta h + \rho g h_f$$

The second term of this equation was negated to indicate that, while $\Delta h$ increases in magnitude, the pressure in the reactor decreases.

These equations may be combined and rearranged given their relabeled variables. The following relationship emerges to relate the solubility of the gas in the reactor to a bubble's radius, the height of the reactor, the water's surface tension, the dimensions of the effluent tubing, and the constant relevant to Henry's Law:

#### Equation 7

$$C = k(\frac{4T}{R} + P_{atm} - \rho g \Delta h + \rho g h_f)$$

**Variables**
$C$ = Solubility of a gas in the water
$k$ = A constant for a given substance at a given temperature; related to Henry’s Law
$T$ = Surface tension of the water at a given temperature
$R$ = Radius of a bubble in the reactor
$P_{atm}$= Atmospheric air pressure at the level of the vent
$⍴$ = Density of water
$g$ = Acceleration due to gravity
$\Delta h$ = Height difference between the vent and the reactor (this is a negative quantity)
$h_f$ = Head loss in the outlet tubing, as given in [Equation 4](#Equation-4)

[Equation 7](#Equation-7) mathematically summarizes the concepts addressed in the Literature Review section. In order to minimize gas solubility (and therefore, to maximize the amount of gas that is removed from influent water): the radii of bubbles that form must be maximized, the head loss in the exit tubing must be minimized, and the height difference between the reactor and vent must be maximized, within reason. Further considerations may arise when [Equation 4](#Equation-4) is substituted for the $h_f$ value.

While [Equation 7](#Equation-7) is powerful in its efficiency, it may only act as an approximation of the solubility of a gas in the fluidized bed reactor. Equations 2-6 assume equilibrium: that the rates of air shifting from liquid to gas phase and vice versa are equal. The system may not be in equilibrium while the reactor is in use. Therefore, [Equation 7](#Equation-7) remains only a qualitative description of the relationships between different system parameters.

[Equation 7](#Equation-7), supplemented by [Equation 1](#Equation-1) concerning fluidization velocity, informed the subteam's fabrication of the prototype apparatus. In future semesters, the equation may be used to perform optimizations once the subteam has gathered sufficient experimental data.
