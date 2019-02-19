# Dissolved Gas, Fall 2018 Subteam

### Thomas Bradford, Karalyn Buhl, Isaac Singer

### 28 September, 2018
[Shuo: Hello Dissolved gas! I'll add my comments in the brackets like this. Feel free to delete these comments later. ]
[Overall, it's a pretty good start for the report. Only major revision you guys need to do is to check the format of equations. Follow the grading rubric for report and see where you can improve next time. Looking forward to your next report! ]

## Abstract
Excess dissolved air in a water treatment plant’s influent water decreases functionality of the treatment plant's filters and sedimentation tanks. The Dissolved Gas subteam begins its first semester with the goal to design a gravity-powered apparatus that extracts this gas from influent water prior to entry into the treatment plant. The subteam will gather literature, develop designs, fabricate a small-scale prototype, and iterate improvements based on experimental data to work towards a model that may be scaled up for application in an AguaClara plant. [Very clear and concise. Since it's the first semester of your team, you can also state the goal in this semester and the goal in the long run.]

## Introduction
Excess dissolved gas in influent water in AguaClara plants at Tamara, Honduras and EL PODA, Nicaragua has inhibited the plants' efficiencies. Excess gas causes bubbles to form in the sedimentation tank, causing flocs that should settle to rise and continue into the remainder of the plant. In the sand filter, gas bubbles form between sand particles and effectively clog the filter [(Scardina, 2004)](https://vtechworks.lib.vt.edu/bitstream/handle/10919/26497/PaoloScardinaDissertation2004.pdf?sequence=1). To remedy this, the Dissolved Gas subteam intends to design a reactor that removes such dissolved gas from influent water prior to entering the plant, in order to preserve the efficiency of the water treatment process.

To clarify, “excess dissolved gas” does not entail bubbles being present in influent water. Gas is supersaturated in the influent water: the molecules are dispersed throughout the water, not congregated in bubbles. Bubbles form in the sedimentation tank and in the sand filter, within the plant itself, due to the presence of this excess gas. For this reason, the subteam plans to remove the excess gas through the use of a reactor stationed prior to the plant.

For the sake of efficiency, the term “supersaturated water” will be used in this report to reference water containing excess dissolved gas, whether air or otherwise.

The current conception of the overall system design is as follows: influent water will flow from its source at a high elevation. Once the influent water has descended from its source and is near to the AguaClara plant, piping will direct this influent water upwards into a reactor. Atmospheric pressure decreases with height; according to Henry’s Law, gas becomes less soluble at lower pressures, making bubble formation more likely. Aspects of the reactor will further encourage bubble formation (a.k.a nucleation) in the reactor. The water, now containing gas bubbles, will flow upward out of the reactor. Piping will direct the water downward into a basin containing a vent where gaseous bubbles may exit the water. The water, no longer supersaturated, then flows into the treatment plant. Figure 1 illustrates this design.
<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Figure%201_%20GeneralUpdated.png?raw=true" height=450>
</p>


**Figure 1**: The above diagram depicts (not to scale) the general design of the system to remove excess dissolved gas from influent water, as the above paragraph describes.

The subteam currently considers two main options for the design of the reactor itself: a fluidized bed reactor, and a vertical plate reactor. As of yet, the subteam has focused its research on the fluidized bed reactor. While technical details are more thoroughly discussed in the Literature Review section, the main attributes of the two options are as follows.

A fluidized bed reactor consists of an enclosed reactor containing a suspension of particles, such as sand, in a liquid; they are kept in suspension by a particular flow rate directed upwards. This flow is that of the influent supersaturated water, entering the reactor from the bottom and flowing upwards toward an exit pipe. The suspended particles provide surfaces on which bubbles can form. The bubbles then rise from the reactor, leaving the sand particles behind. Figure 2 illustrates this design.
<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Figure%202_%20Fluidized%20Bed.png?raw=true" height=450>
</p>

**Figure 2**: The above diagram depicts (not to scale) the general concept of a fluidized bed reactor using sand particles, as the above paragraph describes.

A vertical plate reactor consists of an enclosed reactor containing a series of parallel, vertically aligned, textured plates. Supersaturated water enters the bottom of the reactor and flows upward along the plates to reach the exit pipe. The texturization of the plates provides sites for bubbles to form while the water flows. In theory, after reaching a specific critical diameter, these bubbles detach from the plates and flow upwards as effluent. Figure 3 illustrates this design.
<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Figure3_VerticalPlateReactor.png?raw=true" height=450>

</p>

**Figure 3**: The above diagram depicts (not to scale) the general concept of a vertical plate reactor as the above paragraph describes. The plates, depicted by brown lines, extend outward in the plane of the page.

The subteam considers that the vertical plate reactor design has the potential benefit of keeping bubbles stationary while they grow and accumulate. In the case of a fluidized bed reactor, bubbles may immediately travel upward once they form, since their formation site is mobile. They may depart the fluid at a smaller size, carrying a high internal pressure, and being likely to rupture and disperse into solution.

The subteam intends to first design and fabricate a prototype fluidized bed reactor, and to evaluate its feasibility as a solution. The subteam will consider the vertical plate reactor at a later time in the semester and will weigh the merits of both designs. [Enough background information which is related to the problem. Diagrams are precise and understandable. You can breifly explain the outline of the rest of the report next time.(Since the first report is only four parts, it's good enough.)]

## Literature Review
The subteam concentrated its research on two subjects in particular: the effect of ambient pressure on gas solubility, and bubble nucleation sites. Understanding these topics is necessary to understanding the subteam’s potential fluidized bed reactor.

The subteam’s research is summarized as follows: gas solubility decreases with decreasing ambient pressure. Therefore, to catalyze bubble growth for ease of gas removal, the subteam aims to design a reactor exerting minimal pressure on gas molecules. Such pressures can be controlled by altering the reactor’s height. Pressure control, combined with providing nucleation sites in a fluidized bed reactor, will help the dissolved gas form stable bubbles that will escape from the water. The subteam hypothesizes that this will solve the problems that the plants at El PODA, Nicaragua and Tamara, Honduras are facing.

The solubility of a gas in a solution changes proportionally to the partial pressure above said solution [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html).

A formula that illustrates this relationship is Henry's Law, given below. [The formula below isn't shown as Latex format. Is it possible to make it look like LaTex equations? You can check here for the formatting:https://confluence.cornell.edu/display/AGUACLARA/Style+Guide+for+Figures%2C+Tables%2C+and+Equations]

$C=k\Delta P$

C is the dissolved gas’s concentration at equilibrium, P is the dissolved gas’s partial pressure at the interface of liquid and gas, and k is the Henry’s Law constant, which is determined experimentally for each combination of gas, solvent, and temperature. In this case, the interface may be considered as the border between the bubble and the surrounding water.

This partial pressure can be minimized through control of two components.

The first of these components is the water pressure at the site of bubble formation. As the height difference between the fluidized bed and the vent changes, the water pressure changes, given by the following relation. 

$\Delta P = \rho*g*\Delta h$

Second, a bubble’s pressure can be expressed as a function of its diameter. As pressure increases, bubble size decreases. However, once the pressure exceeds 3.5 atmospheres, the bubbles will stop decreasing in size. In order to further minimize the pressure within bubbles, the subteam may explore methods to encourage the growth of large bubbles.

Because of the reactor’s dependence on gas solubility and bubble formation, much of the subteam’s research was also directed toward bubble nucleation sites. To catalyze bubble formation, the fluidized sand bed must provide the dissolved gas particles with nucleation sites in the reactor.

Typically, small, solid particles can provide a place for bubbles to grow large enough so they rise to the top of the reactor and escape. [(Boudreau et al. (2005))](https://pubs.geoscienceworld.org/gsa/geology/article/33/6/517/103815/bubble-growth-and-rise-in-soft-sediments) found that bubbles that form in sand-like sediments are spherical, in contrast to the oblate spheroid-shaped bubbles that form in muddy sediments. His research suggests that the difference in shape is caused by the differences in responses to the stress of the materials; while mud fractures under stress, sand “acts fluidly or plastically in response to growth stresses.” This gives the subteam an idea of what type of materials to use in the reactor because the subteam needs the particles to have a fluid-like behavior.

Bubble formation and size in gas-solid fluidized beds is fairly predictable at low gas velocities, as proven by [Harrison and Leung (1961)](https://www.nature.com/articles/190433a0). However, Schultz (2004) states that this is not the case for liquid-solid fluidized beds: “In most liquid-fluidized beds, … although instability is present and can be seen in the form of wavy structures this does not lead rapidly to bubble formation.” (Schultz 2004). This could cause problems for the subteam, but luckily there are solutions to commonly reported issues.

If bubble formation is slow or inconsistent, it may be due to the ratio between the density of the particles and the density of water. Schultz found that bubble formation was present in fluidized beds with high ratios, so the subteam may want to consider using more dense particles if problems arise.

In the following weeks, the subteam plans to test the effectiveness of a fluidized bed reactor in removing excess dissolved gas. [All sources are well cited in the correct format. Research mentioned above are relevant. ]


## Bibliography
Averill, B., & Eldredge, P. (n.d.). Principles of General Chemistry (Vol. 1). Creative Commons. Retrieved from https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html

Boudreau, B. P., Algar, C., Johnson, B. D., Croudace, I., Reed, A., Furukawa, Y., … Gardiner, Bruce S. (2005, June 5). Bubble growth and rise in soft sediments. Retrieved September 17, 2018, from https://pubs.geoscienceworld.org/gsa/geology/article/33/6/517/103815/bubble-growth-and-rise-in-soft-sediments

Harrison, D., & Leung, L. S. (1961, April 29). Bubble Formation at an Orifice in a Fluidized Bed | Nature. Retrieved September 20, 2018, from https://www.nature.com/articles/190433a0

Mori, S., & Wen, C. Y. (1975). Estimation of bubble diameter in gaseous fluidized beds. AIChE Journal, 21(1), 109–115. https://doi.org/10.1002/aic.690210114

Scardina, P... (2004). Effects of Dissolved Gas Supersaturation and Bubble Formation on Water Treatment Plant Performance (Unpublished doctoral dissertation). Virginia Polytechnic Institute and State University. Blacksburg, Virginia. https://vtechworks.lib.vt.edu/bitstream/handle/10919/26497/PaoloScardinaDissertation2004.pdf?sequence=1

Schulz, P. (2004). Instability and the formation of bubbles and the plugs in fluidized beds, 24(1), 27.
