# Dissolved Gas, Fall 2018 Subteam

### Thomas Bradford, Karalyn Buhl, Isaac Singer

### 26 October, 2018

## Abstract
Excess dissolved air in a water treatment plant’s influent water decreases the functionality of the treatment plant's filters and sedimentation tanks. The Dissolved Gas subteam begins its first semester with the goal to design a gravity-powered apparatus that extracts this gas from influent water prior to entry into the treatment plant through the use of a fluidized bed. The subteam will gather literature, develop designs, fabricate a small-scale prototype, and iterate improvements based on experimental data to work towards a model that may be scaled up for application in an AguaClara plant. In the Fall 2018 semester, the subteam aims to fabricate an apparatus that quantitatively reduces the amount of dissolved gas in influent water. In future semesters, the subteam will aim to maximize the quantity of dissolved gas that is removed, as well to minimize the complexity and cost of fabricating the apparatus.

## Introduction
Excess dissolved gas in influent water in AguaClara plants at Tamara, Honduras and EL PODA, Nicaragua has significantly reduced the plants' efficiencies. Excess gas causes bubbles to form in the sedimentation tank, causing flocs that should settle to rise and to continue into the remainder of the plant. [**CEO: explain why this happens, ie  the bubble catch on flocs and float them out the top.**] In the plant's sand filter, gas bubbles form between sand particles and effectively clog the filter [(Scardina, 2004)](https://vtechworks.lib.vt.edu/bitstream/handle/10919/26497/PaoloScardinaDissertation2004.pdf?sequence=1). To remedy this, the Dissolved Gas subteam intends to design a reactor that removes such dissolved gas from influent water prior to entering the plant, in order to preserve the efficiency of the water treatment process.

To clarify, “excess dissolved gas” does not entail *bubbles* being present in influent water. The influent water is *supersaturated* with gas: gas molecules are dispersed throughout the water, not congregated in bubbles. Due to the presence of this excess gas, bubbles form in the plant's sedimentation tank and in its sand filter. For this reason, the subteam plans to remove the excess gas through the use of a reactor stationed prior to the plant.

For the sake of efficiency, the term “supersaturated water” will be used in this report to reference water containing excess dissolved gas, whether air or otherwise.

The basic conception of the system design is as follows: influent water will flow from its source at a high elevation. Once the influent water is near to the AguaClara plant, piping will direct it upwards into a reactor. Atmospheric pressure decreases as elevation increases [(Hodanbosi)](https://www.grc.nasa.gov/www/k-12/WindTunnel/Activities/fluid_pressure.html). According to Henry’s Law, gas becomes less soluble at lower pressures, making bubble formation more likely [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html). Aspects of the reactor will further encourage bubble formation (a.k.a nucleation) in the reactor. The water, then containing gas bubbles, will flow upward and out of the reactor. Piping will direct the water downward into a basin containing a vent through which gas may exit the water. The water, no longer supersaturated, will then flow into the treatment plant. Figure 1 illustrates this general design.
<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Figure%201_%20GeneralUpdated.png?raw=true" height=450>
</p>


**Figure 1**: The above diagram depicts (not to scale) the general design of the system to remove excess dissolved gas from influent water, as the above paragraph describes.

At the start of the semester, the subteam considered two options for the design of the reactor itself [omit "itself"]: a fluidized bed reactor, and a vertical plate reactor. As of yet [So far], the subteam has focused its research on the fluidized bed reactor. While technical details are more thoroughly discussed in the Literature Review section, the main attributes of the two options are as follows.

A fluidized bed reactor consists of an enclosed reactor containing a suspension of particles, such as sand grains, in a fluid; they are kept in suspension by a particular flow rate directed upwards [(Department of Chemical Engineering, 2017)](http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf). This flow is that of the influent water, entering the reactor from the bottom and flowing upwards toward an exit pipe. The suspended particles provide surfaces on which bubbles can form. The bubbles then rise from the reactor, leaving the sand particles behind. Figure 2 illustrates this design.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Fluidized_Bed_Reactor.jpg?raw=true" height=450>
</p>

**Figure 2**: The above diagram depicts (not to scale) the general concept of a fluidized bed reactor using sand particles, as the above paragraph describes.

A vertical plate reactor consists of an enclosed reactor containing a series of parallel, vertically aligned, textured plates. Supersaturated water enters the bottom of the reactor and flows upward along the plates to reach the exit pipe. The texturization of the plates provides sites for bubbles to form while the water flows. In theory, after reaching a specific critical diameter, these bubbles detach from the plates and flow upwards as effluent. Figure 3 illustrates this design. [**CEO:have you looked specifically into the detachment process at all? or is it trivial compared with formation?**]

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Figure3_VerticalPlateReactor.png?raw=true" height=450>

</p>

**Figure 3**: The above diagram depicts (not to scale) the general concept of a vertical plate reactor, as the above paragraph describes. The plates, depicted by brown lines, extend outward from the plane of the page.

The subteam considered that the vertical plate reactor design has the potential benefit of keeping bubbles stationary while they grow and accumulate. In the case of a fluidized bed reactor [In a fluidized bed reactor], bubbles may immediately travel upward once they form, since their formation site (sand grains) is mobile. Bubbles may depart the fluid at a smaller size, carrying a high internal pressure, and being likely to rupture and disperse into solution.

Despite these benefits, the subteam believes the fluidized bed reactor may still be more effective, because a large number of sand grains may provide a greater surface area for bubbles to form than individual, vertical plates. The subteam intends to first design and fabricate a prototype fluidized bed reactor and to evaluate its feasibility as a solution. The subteam will consider the vertical plate reactor at a later time in the semester and will weigh the merits of both designs [merit of each design].

The remainder of this report will include further explanation of concepts such as fluidized beds and considerations of pressure that will inform parameters of the reactor's design. The general design of the first prototype reactor that the subteam plans to fabricate will be discussed in the Future Work section.

## Literature Review

The subteam concentrated its research on optimizing the fluidized bed reactor and manipulating pressure to ensure maximum dissolved gas removal. The subteam’s research can be summarized as follows: gas solubility decreases with decreasing ambient pressure. Therefore, to catalyze bubble growth in a reactor for ease of gas removal, the subteam aims to design a reactor exerting minimal pressure on gas molecules. Such pressure can be controlled by altering the reactor’s height, by influencing bubble size, and by modifying dimensions of the tubing in the system. Pressure control, combined with providing nucleation sites in a fluidized bed reactor, will help the dissolved gas form stable bubbles that will escape from the water. The subteam hypothesizes that this will solve the problems that the plants at El PODA, Nicaragua and Tamara, Honduras are facing. [**CEO:This is a big claim**]

### Fluidized Beds & Bubble Nucleation

When a liquid or a gas is pumped through a granular solid at a certain velocity, the granular solid behaves like a fluid. The minimum velocity required to cause this behavior is known as the minimum fluidization velocity. This value depends on numerous characteristics of the fluidized bed, including particle density, shape, size, and porosity [(Department of Chemical Engineering, 2017)](http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf). The relationship is quantified by the equation below [(Weber-Shirk)](https://courses.cit.cornell.edu/cee4540/pdf/Filtration.pdf).

$$ V_{minfl}= \frac{\phi g D^2}{36kv(1-\phi)}(\frac{\rho_s}{\rho_w}-1) $$

<p style="text-align: center;">
Equation 1
</p>

**Variables**
$V_{minfl}$ = Minimum approach velocity required to fluidize the sand bed
$\phi$ = Porosity (Approximately 0.4 for uniform size media) (Note: porosity and voidage are equal quantities)
$g$ = Acceleration due to gravity
$D$ = Diameter of a sand grain
$k$ = Kozeny constant (approximately equal to 5 for most filtration conditions)
$v$ = Kinematic viscosity of water
$\rho_s$ = Density of sand particles
$\rho_w$ = Density of water

In the reactor the subteam plans to use, sand will serve as the granular solid and water as the fluid. Water has a known density and kinematic viscosity, but the material properties of sand may vary. The subteam will determine these quantities in the near future.

Because of the reactor’s dependence on bubble formation, much of the subteam’s research was also directed toward bubble nucleation sites. The subteam found through research that the solid particles in the fluidized beds will provide nucleation sites for bubble formation.

Typically, small, solid particles can provide a place for bubbles to grow large enough so they rise to the top of the reactor and escape [(Boudreau et al., 2005)](https://pubs.geoscienceworld.org/gsa/geology/article/33/6/517/103815/bubble-growth-and-rise-in-soft-sediments). Boudreau found that bubbles that form in sand-like sediments are spherical, in contrast to the oblate spheroid-shaped bubbles that form in muddy sediments. His research suggests that the difference in shape is caused by the differences in responses to the stress of the materials; while mud fractures under stress, sand “acts fluidly or plastically in response to growth stresses.” This gives the subteam an idea of what type of materials to use in the reactor because the subteam needs the particles to have a fluid-like behavior.

Bubble formation and size in gas-solid fluidized beds is fairly predictable at low gas velocities [(Harrison and Leung, 1961)](https://www.nature.com/articles/190433a0). However, Schulz states that this is not the case for liquid-solid fluidized beds: “In most liquid-fluidized beds, … although instability is present and can be seen in the form of wavy structures this does not lead rapidly to bubble formation.” [(Schulz, 2004)](https://www.opuscula.agh.edu.pl/vol24/1/art/opuscula_math_2412.pdf). This [instability] could cause problems for the subteam, but luckily there are solutions to commonly reported issues.

If bubble formation is slow or inconsistent, it may be due to the ratio between the density of the particles and the density of water. Schulz found that bubble formation was present in fluidized beds with high ratios, so the subteam may want to consider using denser particles if problems arise. [**CEO:This would require a higher fluidization velocity as well, but in the lab that is easy to do!**]

The subteam aims to remove the most gas from the influent water as possible by creating bubbles. As previously stated, bubbles can be created by providing nucleation sites on sand grains, and it can also be done by decreasing gas solubility.

### Controlling Pressure
The solubility of a gas in a solution is directly proportional to its partial pressure above said solution [**CEO:It does also depend on the gas and the solution, the k value for a particular system is very specific to the system. This could be good to mention**][(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html).

A formula that illustrates this relationship is Henry's Law, given below.

$$ C=k P $$
<p style="text-align: center;">
Equation 2
</p>

**Variables**
$C$ = Dissolved gas’s concentration at equilibrium
$k$ = Henry’s Law constant, which is determined experimentally for each combination of gas, solvent, and temperature. In this case, the interface may be considered as the border between the bubble and the surrounding water.
$P$ = Dissolved gas’s partial pressure at the interface of liquid and gas

Therefore, in order to decrease gas's solubility inside of the reactor, the subteam must find a way to decrease the pressure. This  pressure can be minimized through control of two components.

The first of these components is the water pressure at the site of bubble formation. As the height difference between the fluidized bed and the vent changes, the water pressure changes, given by the following relation [(Hodanbosi)](https://www.grc.nasa.gov/www/k-12/WindTunnel/Activities/fluid_pressure.html).

$$\Delta P = \rho g \Delta h$$
<p style="text-align: center;">
Equation 3
</p>

**Variables**
$\Delta P$ = Change in pressure
$\rho$ = Density of the material
$g$ = Acceleration due to gravity
$\Delta h$ = Change in depth

Because water pressure decreases in shallower depths, building a reactor at a certain height will minimize pressure, and as a result, minimize gas solubility.

Another factor that influences the pressure difference between the reactor and the vent is that of *head loss*; head loss corresponds to energy lost due to friction, which in turn depends on material properties of the piping [(CodeCogs, 2012)](http://www.codecogs.com/library/engineering/fluid_mechanics/pipes/head_loss/pipe-head-loss.php). In this case, the relevant piping is the effluent pipe through which water exits the reactor and passes into the vent. Head loss is dependent on tubing parameters according to the following equation [(Weber-Shirk)](https://courses.cit.cornell.edu/cee4540/pdf/Flow%20Control%20and%20Measurement.pdf).

 $$ h_f = \frac{32\mu L V}{\rho g D^2} $$
<p style="text-align: center;">
Equation 4
</p>

**Variables**
$h_f$ = Head loss
$\mu$ = Kinematic viscosity of water
$L$ = Length of the pipe in question
$g$ = Acceleration due to gravity
$\rho$ = Density of water
$D$ =Diameter of the pipe in question
$V$ = Velocity of water in the pipe

Building off Equation 4, the pressure difference between two ends of a pipe due to head loss is given by the following equation [(Brown, 2000)](https://bae.okstate.edu/faculty-sites/Darcy/DarcyWeisbach/Darcy-WeisbachEq.htm).

$$\Delta P =  \rho  g h_f$$
<p style="text-align: center;">
Equation 5
</p>

**Variables**
$h_f$ = Head loss in a pipe, as given in Equation 4
$\rho$ = Density of water
$\Delta P$ = Change in pressure across the pipe
$g$ = Acceleration due to gravity

Second, a bubble’s pressure can be expressed as a function of its diameter [(Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html). As pressure increases, bubble size decreases. However, once the pressure exceeds 3.5 atmospheres, the bubbles will stop decreasing in size [(Han, M., 2002)](https://doi.org/10.2166/ws.2002.0148). The relationship between pressure, surface tension, and bubble radius is given below:

$$P_i = P_o + 4 \frac{T}{R}$$
<p style="text-align: center;">
Equation 6
</p>

**Variables**
$P_i$ = Pressure inside the bubble
$P_o$ = Pressure outside the bubble
$T$ = Surface tension
$R$ = Bubble radius

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Bubble_Surface_Tension.jpg?raw=true" height=350>

</p>

**Figure 4**: The above diagram shows the descriptions of surface tension, pressure inside the bubble, and pressure outside the bubble for the given equation [(Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html).

The dissolved gas subteam plans on using the principles of this formula to even further decrease the pressure inside the bubble. Because it is known that an increase in radius will result in a decrease in pressure, the subteam must find a way to increase bubble radius.

One way to increase radius may be to prevent the bubbles in the reactor from quickly escaping; if bubbles stay inside the reactor for a longer period of time, it will have a longer time to expand.

In the Analysis section, Equations 2-6 are evaluated and related to one another to form one basis for parameters of the system design. In the following weeks, the subteam plans to fabricate and test the effectiveness of a fluidized bed reactor whose parameters are informed by this basis.

## Analysis
Through conceptual analysis and algebraic manipulation, Equations 2-6 combine to form an estimation of a gas’ solubility in water in an apparatus as illustrated in Figure 1. The following paragraphs walk through this process; all variables have been defined in the Literature Review section.

The pressure relevant to Henry's Law (i.e. the pressure of a gas above a liquid, in Equation 2) is the pressure *within* a bubble [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html).
$$ C = k P $$
<p style="text-align: center;">
Equation 2
</p>

$P$ equates to the gas pressure within a bubble. Therefore, $P$ is relabeled as $P_b$ (i.e. pressure in a bubble).

As shown in Equation 6, the pressure within a bubble is directly related to the bubble's radius, the liquid's surface tension, and the pressure outside the bubble [(Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html).

$$P_i = P_o + 4 \frac{T}{R}$$
<p style="text-align: center;">
Equation 6
</p>

$P_i$ denotes the pressure within a bubble, and therefore is relabeled as $P_b$. $P_o$ denotes the pressure outside of the bubble, and is relabeled $P_r$.

The pressure outside of the bubble (i.e. the pressure within the liquid) can be equated to atmospheric pressure plus a change in pressure due to the height difference between the reactor and the vent (Equation 3), plus a change in pressure due to head loss in the tubing connecting the reactor and the vent (Equation 5).

$$\Delta P = \rho g \Delta h$$
<p style="text-align: center;">
Equation 3
</p>

In Equation 3, the difference in pressure is that between atmospheric pressure (i.e. the pressure at the vent) and the pressure within the reactor itself. Therefore, if $\Delta P$ is expanded to $P_r - P_{atm}$ (i.e. pressure in the reactor minus atmospheric pressure), this equation may be rearranged into $P_r = P_{atm} - \rho g \Delta h $. The final term of this equation was negated to indicate that, while $\Delta h$ increases in magnitude, the pressure in the reactor decreases. [**CEO: check equations formatting here**]

Pressure difference due to head loss must also be taken into account, since it contributes to the pressure difference between the vent and the reactor.

$$\Delta P =  \rho  g h_f$$
<p style="text-align: center;">
Equation 5
</p>

Similarly to Equation 3, the difference in pressure can be expanded to $P_r - P_{atm}$.

These [**four**] equations may be combined and rearranged given their relabeled variables. The following relationship emerges to relate the solubility of the gas in the reactor to a bubble's radius, the height of the reactor, the water's surface tension, the dimensions of the effluent tubing, and the constant relevant to Henry's Law:

$$C = k(\frac{4T}{R} + P_{atm} - \rho g \Delta h + \rho g h_f)$$
<p style="text-align: center;">
Equation 7
</p>

**Variables**
$C$ = Solubility of a gas in the water
$k$ = A constant for a given substance at a given temperature; related to Henry’s Law
$T$ = Surface tension of the water at a given temperature
$R$ = Radius of a bubble in the reactor
$P_{atm}$= Atmospheric air pressure at the level of the vent
$⍴$ = Density of water
$g$ = Acceleration due to gravity
$\Delta h$ = Height difference between the vent and the reactor (this is a negative quantity)
$h_f$ = Head loss in the outlet tubing, as given in Equation 4

Equation 7 mathematically summarizes the concepts addressed in the Literature Review section. In order to minimize gas solubility (and therefore, to maximize the amount of gas that is removed from influent water): the radii of bubbles that form must be maximized, the head loss in the exit tubing must be minimized, and the height difference between the reactor and vent must be maximized, within reason. Further considerations may arise when Equation 4 is substituted for the $h_f$ value.

While Equation is powerful in its efficiency, it may only act as an approximation of the solubility of a gas in the fluidized bed reactor. Equations 2-6 assume equilibrium: that the rates of air shifting from liquid to gas phase and vice versa are equal. The system may not be in equilibrium while the reactor is in use. Therefore, Equation 7 remains only a qualitative description of the relationships between different system parameters. [**CEO: nice job including a shortcoming of these assumptions. This is always good to consider**]

In the near future, the subteam will perform exact calculations and optimizations with these parameters in mind. Equation 7, supplemented by Equation 1 concerning fluidization velocity, will be instrumental in informing the subteam's fabrication of the prototype apparatus.

## Future Work

Now that the subteam has a solid understanding of the grounding principles of fluidization and pressure, as well as Equation 7 as a guideline to optimize the system, the subteam will move on to focus on fabrication of a prototype system, followed by experimentation, evaluation, and iteration. [**CEO: good summary of the rest of your process**]

The prototype design will align with that illustrated below in Figure 5. Exact parameters (such as the length of the reactor) will be calculated and measured in the coming days during the fabrication process.

[**CEO: How will you be supersaturating the influent? Include that here until your methods section is developed.**]

The prototype system’s design is as follows: a peristaltic pump will pump supersaturated water into a tube system and through the fluidized bed reactor. The reactor, likely built using a plastic, transparent pipe, will contain a sand bed. This will be fluidized by the influent water, which will be traveling at no slower than the sand’s fluidization velocity. Ideally, as the supersaturated water travels through the reactor, excess gas particles in the water will accumulate on the sand grains and form bubbles. Such bubbles will then depart from their sand grains and flow upward, out of the reactor, through the effluent tubing and into a bucket. This bucket will act as the open-faced vent (as in Figure 1) for the air bubbles to escape into the atmosphere.

One should note that a mesh will be installed at the bottom of the reactor to prevent any sand from falling down/out of the reactor.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype_Diagram.jpg?raw=true" height=450>

</p>

**Figure 5**: The above diagram depicts (not to scale) the prototype the subteam plans to built to test the hypothesis regarding the use of a fluidized bed reactor to encourage bubble formation.

If the design functions ideally, the effluent water will no longer contain excess dissolved gas. [**CEO: have you defined a way to characterize excess? Are there any measurements from plants about the gas concentrations in the afffected plants? This could give you a good place to define a more specific goal**] The subteam will test the functionality of the prototype in two ways. First, the subteam will determine qualitatively, likely with the assistance of a camera, whether bubbles form inside the reactor. If this is true, the premise of using a fluidized bed to encourage bubble formation and to remove dissolved gas from water is valid. After modifying the system as necessary to achieve qualitative success, the subteam will move on to a quantitative analysis of the prototype. The subteam will use dissolved oxygen probes to determine the difference in concentration of dissolved oxygen between the influent and effluent water. With such data, the subteam will then modify the system as necessary to optimize the amount of dissolved gas that is removed.

[**CEO: when looking at bubble formation and gas concentrations are you considering that there will be relatively large concentrations of other gasses present or are you only supersaturating the water with oxygen?**]

When building the prototype, the subteam will look to minimize head loss, maximize bubble radius, and maximize the difference in depth between the reactor and the bucket. These parameters are illustrated in Equation 7, with the purpose of minimizing gas' solubility and therefore maximizing bubble formation within the reactor.

The subteam looks forward to fabrication and experimentation, and hopefully to restoring the efficiency of AguaClara’s water treatment plants.  

## Bibliography
Averill, B., & Eldredge, P. (n.d.). *Principles of General Chemistry* (Vol. 1). Creative Commons. Retrieved from https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html

Boudreau, B. P., Algar, C., Johnson, B. D., Croudace, I., Reed, A., Furukawa, Y., … Gardiner, Bruce S. (2005, June 5). *Bubble growth and rise in soft sediments.* Retrieved September 17, 2018, from https://pubs.geoscienceworld.org/gsa/geology/article/33/6/517/103815/bubble-growth-and-rise-in-soft-sediments

Brown, G. (2000, June 22). *The Darcy-Weisbach Equation*. Retrieved from https://bae.okstate.edu/faculty-sites/Darcy/DarcyWeisbach/Darcy-WeisbachEq.htm

CodeCogs.(2012, February 24). Pipe Head Loss. Retrieved from http://www.codecogs.com/library/engineering/fluid_mechanics/pipes/head_loss/pipe-head-loss.php

Department of Chemical Engineering. (2017, February). *Fluidization: A Unit Operation in Chemical Engineering.* Gainesville, FL: University of Florida. Retrieved from http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf.

Han, M., Park, Y., Lee, J., & Shim, J. (2002). *Effect of pressure on bubble size in dissolved air flotation.* Water Science and Technology: Water Supply, 2(5–6), 41–46. https://doi.org/10.2166/ws.2002.0148

Harrison, D., & Leung, L. S. (1961, April 29). *Bubble Formation at an Orifice in a Fluidized Bed | Nature*. Retrieved September 20, 2018, from https://www.nature.com/articles/190433a0

Hodanbosi, C. (n.d.). *Fluids Pressure and Depth*. Retrieved from https://www.grc.nasa.gov/www/k-12/WindTunnel/Activities/fluid_pressure.html

Hyperphysics. (n.d.). *Surface Tension and Bubbles.* Retrieved from http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html

Mori, S., & Wen, C. Y. (1975). *Estimation of bubble diameter in gaseous fluidized beds.* AIChE Journal, 21(1), 109–115. https://doi.org/10.1002/aic.690210114

Scardina, P... (2004). *Effects of Dissolved Gas Supersaturation and Bubble Formation on Water Treatment Plant Performance* (Unpublished doctoral dissertation). Virginia Polytechnic Institute and State University. Blacksburg, Virginia. https://vtechworks.lib.vt.edu/bitstream/handle/10919/26497/PaoloScardinaDissertation2004.pdf?sequence=1

Schulz, P. (2004). *Instability and the formation of bubbles and the plugs in fluidized beds*, 24(1), 27. Retrieved from https://www.opuscula.agh.edu.pl/vol24/1/art/opuscula_math_2412.pdf

Weber-Shirk, M. *Filtration Theory: On removing little particles with big particles* [PowerPoint Slides]. Retrieved from https://courses.cit.cornell.edu/cee4540/pdf/Filtration.pdf.

Weber-Shirk, M. *Flow Control and Measurement* [PowerPoint Slides]. Retrieved from https://courses.cit.cornell.edu/cee4540/pdf/Flow%20Control%20and%20Measurement.pdf.
