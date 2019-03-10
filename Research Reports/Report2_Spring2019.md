# Dissolved Gas, Spring 2019 Subteam
#### Saul Bernaber, Thomas Bradford, Emily Wood
#### 15 March 2019

## Abstract
Excess dissolved air in a treatment plant’s influent water decreases the functionality of the plant's components. The Dissolved Gas subteam aims to design a gravity-powered apparatus to extract excess gas from influent water prior to entry into a plant. The Fall 2018 subteam fabricated a small-scale prototype incorporating a fluidized bed reactor. The Spring 2019 subteam will experimentally evaluate the prototype: given qualitative success, the subteam will test the prototype's effectiveness by measuring change in dissolved oxygen concentration across the apparatus. The Spring 2019 subteam will iterate improvements to work toward a prototype for application in an AguaClara plant.

## Table of Contents

- [Introduction](#Introduction) [Update the figure]
- [Literature Review](#Literature-Review)
  - [Fluidized Beds and Bubble Formation](#Fluidized-Beds-and-Bubble-Nucleation)
  - [Controlling Pressure](#Controlling-Pressure)
  - [Analysis of Literature](#Analysis-of-Literature)
- [Previous Work](#Previous-Work)
- [Methods](#Methods) [Emily]
- [Results and Analysis](#Results-and-Analysis) [Tommy]
- [Conclusions](#Conclusions) [Tommy]
- [Future Work](#Future-Work) [Tommy]
- [Bibliography](#Bibliography)
- [Manual](#Manual) [Saul]
  - [Experimental Methods](#Experimental-Methods)
  - [Fabrication Manual](#Fabrication-Manual)
  - [Python Code](#Python-Code)
  - [ProCoDa Code](#ProCoDa-Code)


## Introduction

Excess dissolved gas in influent water of AguaClara plants at Tamara, Honduras and El Poda, Nicaragua has significantly reduced the plants' efficiencies. To clarify: “excess dissolved gas” does not entail *bubbles* being present in influent water. The influent water is *supersaturated* with gas: gas molecules are dispersed throughout the water, not congregated in bubbles. This report uses the term “supersaturated water” to denote water containing excess dissolved gas, whether air or otherwise.

Due to the presence of this excess gas, bubbles form in the plants' sedimentation tanks. Flocs adhere to these bubbles and rise, causing materials that should settle to float and to continue into the remainder of the plants. Bubbles also form in the plants' sand filters between sand particles, effectively clogging the filters [(Scardina, 2004)](https://vtechworks.lib.vt.edu/bitstream/handle/10919/26497/PaoloScardinaDissertation2004.pdf?sequence=1). To remedy these issues, the Dissolved Gas subteam intends to develop a reactor that removes such dissolved gas from influent water prior to entering the plant.

The basic concept of the system's design was as follows. Influent water will flow from its source at a high elevation. Once the influent water has descended and nears an AguaClara plant, piping will direct it upwards into a reactor. Atmospheric pressure decreases as elevation increases [(Hodanbosi)](https://www.grc.nasa.gov/www/k-12/WindTunnel/Activities/fluid_pressure.html), and in accordance with Henry’s Law, the gas becomes less soluble at lower pressures, making bubble formation more likely [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html). The subteam will research and implement different reactor components to further encourage bubble formation (i.e. nucleation). The water and the gas bubbles that form will then flow upward and out of the reactor. Piping will direct this effluent downward into a liquid-gas separator (e.g. a basin containing a vent) such that the gas bubbles may escape the water. The water, no longer supersaturated, will then flow into the treatment plant. Figure 1 illustrates this general design.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Figure%201_%20GeneralUpdated.png?raw=true" height=450>
</p>

**Figure 1**: This diagram depicts (not to scale) the general design of the system to remove excess dissolved gas from influent water, as the above paragraph describes.

The subteam has focused its research on the use of a fluidized bed reactor. While technical details are more thoroughly discussed in the Literature Review section, the main attributes of such a reactor are as follows.

A fluidized bed reactor consists of an enclosed bed of particles, such as sand grains, suspended in a fluid. They are kept in suspension by a particular flow rate directed upwards (i.e. the "fluidization flow" of the sand bed) [(Department of Chemical Engineering, 2017)](http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf). This flow is that of the influent water, entering the reactor from the bottom and flowing upwards toward an exit pipe. The suspended particles provide surfaces on which bubbles can form. The bubbles then rise from the reactor, leaving the sand behind. Figure 2 illustrates this design.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Fluidized_Bed_Reactor.jpg?raw=true" height=400>
</p>

**Figure 2**: This diagram depicts (not to scale) the general concept of a fluidized bed reactor using sand particles, as the above paragraph describes.

In a fluidized bed reactor, bubbles may immediately travel upward once they form, since their nucleation sites (sand grains) are relatively mobile. Bubbles may depart the fluid at a small diameter, carrying a high internal pressure, being likely to rupture and disperse into solution. Despite these potential issues, the subteam believes the fluidized bed reactor may still be effective, because a large number of sand grains may provide a large surface area for bubbles to nucleate. In future semesters, the subteam may consider an alternative reactor type and weigh the merit of alternative designs.

After gathering and analyzing literature, the Fall 2018 subteam fabricated a prototype fluidized bed reactor using a transparent PVC pipe, silica sand, and flow components. The subteam assembled a basic apparatus to resemble the design proposed in Figure 1. Figure 3 presents a photograph of this apparatus. Influent water passes in through a peristaltic pump and through tubing into a vertically oriented fluidized bed reactor, and out into a small bucket. Further details on this apparatus are given in the Methods and Manual sections of the [Fall 2018 Final Report](https://github.com/AguaClara/Dissolved-Gas/blob/master/Research%20Reports/Final_Report.md).

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype2/Prototype2_photodiagram.jpg?raw=true" height = 430 width = 2000>


</p>

**Figure 3**: The left-hand photograph is of the current prototype apparatus. The right-hand photograph contains graphical enhancement to clarify the system's progression. Influent water (purple arrow) enters the system through the peristaltic pump (orange rectangle), flows up into the fluidized bed reactor (green rectangle), exits the reactor as effluent water (dotted purple), and pours into a small bucket (yellow rectangle) that serves as an open-faced vent.

The Spring 2019 subteam plans to determine qualitatively, likely with the assistance of a camera, if air bubbles form inside the reactor. If this is true, the premise of using a fluidized bed to encourage bubble formation and to remove excess dissolved air from water is valid. After modifying the system as necessary to achieve qualitative success, the subteam will move on to a quantitative analysis of the prototype. The subteam will use dissolved oxygen probes to determine the difference in concentration of dissolved oxygen between the influent and effluent water. The subteam expects that the water's dissolved oxygen content is proportional to the water's dissolved air content, since the major source of the dissolved oxygen is air. Therefore, the system's effectiveness in removing dissolved oxygen should be proportional to the system's effectiveness in removing dissolved air. After analysis of concentration data, the subteam will modify the system to optimize the removal of excess dissolved gas.

The remainder of this report includes further explanation of concepts such as fluidized beds and considerations of pressure. The Spring 2019 subteam looks forward to pursuing experiments to evaluate the reactor's feasibility as a solution.

## Literature Review
The subteam concentrated its research on optimizing the system's fluidized bed reactor and manipulating pressure to ensure maximum dissolved gas removal. The subteam’s research can be summarized as follows: gas solubility decreases with decreasing ambient pressure. Therefore, to catalyze bubble growth in a reactor for ease of gas removal, the subteam aimed to design a reactor exerting minimal pressure on gas molecules. Such pressure can be controlled by altering the reactor’s height, by influencing bubble size, and by modifying dimensions of the tubing in the system. Pressure control, combined with providing nucleation sites in a fluidized bed reactor, helps the dissolved gas form stable bubbles that escape from the surrounding water. The subteam hypothesizes that such a reactor design can be developed to alleviate the problems that the plants at El PODA, Nicaragua and Tamara, Honduras are facing.

### Fluidized Beds and Bubble Nucleation

When a liquid or a gas is pumped through a granular solid at a certain velocity, the material behaves like a fluid. The velocity required to cause this behavior is known as the minimum fluidization velocity. The corresponding flow rate may be denoted as the minimum fluidization flow. The minimum fluidization velocity depends on characteristics of the fluidized bed, including particle density, shape, size, and porosity [(Department of Chemical Engineering, 2017)](http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf). The equation below quantifies this relationship [(Weber-Shirk)](https://courses.cit.cornell.edu/cee4540/pdf/Filtration.pdf).

#### Equation 1

$$ V_{minfl}= \frac{\phi^3 g D^2}{36kv(1-\phi)}(\frac{\rho_s}{\rho_w}-1) $$

**Variables**
$D$ = Diameter of a sand grain
$g$ = Acceleration due to gravity
$k$ = Kozeny constant (approximately equal to 5 for most filtration conditions)
$\phi$ = Porosity (Approximately 0.4 for uniform size media) (Note: porosity and voidage are equal quantities)
$\rho_s$ = Density of sand particles
$\rho_w$ = Density of water
$v$ = Kinematic viscosity of water
$V_{minfl}$ = Minimum approach velocity required to fluidize the sand bed

In the prototype reactor the subteam fabricated, sand serves as the granular solid and water serves as the fluid. Water has a known density and kinematic viscosity, but the material properties of sand vary. The subteam used silica sand to construct the prototype reactor. The subteam experimentally determined the silica sand's porosity and average grain diameter, as discussed in the Methods section of the [Fall 2018 Final Report](https://github.com/AguaClara/Dissolved-Gas/blob/master/Research%20Reports/Final_Report.md). The subteam found silica sand's density in a presentation by [Weber-Shirk](https://courses.cit.cornell.edu/cee4540/pdf/Filtration.pdf).

Conversely to fluidization velocity: when a liquid or gas flows through a granular solid at a certain threshold velocity known as the fluidized bed's "entrainment velocity", the grains no longer fluidize. They flow upward along with the gas or liquid (Denn, 1980). In the case that a fluidized bed reactor is implemented in an AguaClara plant, the reactor must be designed such that the entrainment velocity is never reached by the influent water. Equation 2 quantifies entrainment velocity.

#### Equation 2
$$ v_{max} = \frac{(\rho_{p}-\rho)g D^2_p}{18\eta}$$

**Variables**
$D_p $ = Diameter of a sand grain
$\eta $ = Dynamic viscosity of water
$g $ = Acceleration due to gravity
$\rho_{p}$ = Density of sand particles
$\rho$ = Density of the fluidizing agent
$v_{max}$ = Entrainment velocity of the fluidized bed

The subteam will consider the entrainment velocity of the fluidized bed in the event of designing a scaled up reactor.

Because of the reactor’s dependence on bubble formation, the subteam also directed research toward bubble nucleation sites. The subteam found that the solid particles in the fluidized beds would provide nucleation sites for bubble formation.

Typically, small, solid particles can provide a place for bubbles to grow large enough so they rise to the top of a reactor and escape [(Boudreau et al., 2005)](https://pubs.geoscienceworld.org/gsa/geology/article/33/6/517/103815/bubble-growth-and-rise-in-soft-sediments). Boudreau found that bubbles that form in sand-like sediments are spherical, in contrast to the oblate spheroid-shaped bubbles that form in muddy sediments. His research suggests that the difference in shape is caused by the differences in responses to the stress of the materials. While mud fractures under stress, sand “acts fluidly or plastically in response to growth stresses.” This informed the subteam as to what type of materials to use in the reactor because the subteam needed the particles to have fluid-like behavior.

Bubble formation and size in gas-solid fluidized beds is fairly predictable at low gas velocities [(Harrison and Leung, 1961)](https://www.nature.com/articles/190433a0). However, Schulz states that this is not the case for liquid-solid fluidized beds: “In most liquid-fluidized beds, … although instability is present and can be seen in the form of wavy structures this does not lead rapidly to bubble formation” [(Schulz, 2004)](https://www.opuscula.agh.edu.pl/vol24/1/art/opuscula_math_2412.pdf). This instability could cause problems for the subteam, but there are solutions to commonly reported issues.

If bubble formation is slow or inconsistent, it may be due to the ratio between the density of the particles and the density of water. Schulz found that bubble formation was present in fluidized beds with high ratios, so the subteam may want to consider using denser particles if problems arise.

The subteam aims to remove the most gas from the influent water as possible by generating bubbles. As previously stated, bubble formation can be encouraged by providing nucleation sites on sand grains. It can also be encouraged by decreasing gas solubility through manipulation of pressure.

### Controlling Pressure

The solubility of a gas in a solution is directly proportional to its partial pressure above said solution. It is also dependent on a particular constant, determined by the composition of the gas and the solution, and the temperature of both [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html).

Henry's Law quantifies this relationship, represented by the following equation.

#### Equation 3

$$ C=k P $$

**Variables**
$C$ = Dissolved gas’s concentration in a solvent at equilibrium
$k$ = Henry’s Law constant, which is determined experimentally for each combination of gas, solvent, and temperature. In this case, the interface may be considered as the border between the bubble and the surrounding water.
$P$ = Dissolved gas’s partial pressure at the interface of liquid and gas

Therefore, in order to decrease gas's solubility inside of the reactor, the subteam must find a way to decrease the pressure. This pressure can be minimized through control of two components.

The first component is the water pressure at the site of bubble formation. As the height difference between the fluidized bed and the vent changes, the water pressure changes, given by the following equation [(Hodanbosi)](https://www.grc.nasa.gov/www/k-12/WindTunnel/Activities/fluid_pressure.html).

#### Equation 4

$$\Delta P = \rho g \Delta h$$

**Variables**
$g$ = Acceleration due to gravity
$\Delta h$ = Change in depth
$\Delta P$ = Change in pressure
$\rho$ = Density of the material

Because water pressure decreases at lesser depths, building a reactor at a greater height in the water column will minimize pressure inside the reactor, and as a result, minimize gas solubility.

Another factor that influences the pressure difference between the reactor and the vent is that of *head loss*. Head loss corresponds to energy lost due to friction, which in turn depends on material properties of the piping [(CodeCogs, 2012)](http://www.codecogs.com/library/engineering/fluid_mechanics/pipes/head_loss/pipe-head-loss.php). In this case, the relevant piping is the effluent pipe through which water exits the reactor and passes into the vent. Head loss is dependent on tubing parameters according to the following equation [(Brown, 2000)](https://bae.okstate.edu/faculty-sites/Darcy/DarcyWeisbach/Darcy-WeisbachEq.htm).

#### Equation 5

 $$ h_f = \frac{32\mu L V}{\rho g D^2} $$

**Variables**
$D$ = Diameter of the pipe in question
$g$ = Acceleration due to gravity
$h_f$ = Head loss
$L$ = Length of the pipe in question
$\mu$ = Absolute viscosity of water
$\rho$ = Density of water
$V$ = Velocity of water in the pipe

Building off of [Equation 5](#Equation-5), the pressure difference between two ends of a pipe due to head loss is given by the following equation [(Brown, 2000)](https://bae.okstate.edu/faculty-sites/Darcy/DarcyWeisbach/Darcy-WeisbachEq.htm).

#### Equation 6

$$\Delta P = \rho g h_f$$

**Variables**
$g$ = Acceleration due to gravity
$h_f$ = Head loss in a pipe, as given in [Equation 5](#Equation-5)
$\Delta P$ = Change in pressure across the pipe
$\rho$ = Density of water

Second, a bubble’s internal pressure can be expressed as a function of its radius [(Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html). As internal pressure increases, bubble size decreases. However, once the pressure exceeds 3.5 atmospheres, the bubbles will stop decreasing in size [(Han, M., 2002)](https://doi.org/10.2166/ws.2002.0148). The relationship between pressure, surface tension, and bubble radius is shown by the following equation.

#### Equation 7

$$P_i = P_o + 4 \frac{T}{R}$$

**Variables**
$P_i$ = Pressure inside the bubble
$P_o$ = Pressure outside the bubble
$R$ = Bubble radius
$T$ = Surface tension

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Bubble_Surface_Tension.jpg?raw=true" height=350>

</p>

**Figure 4**: This diagram illustrates the above descriptions of surface tension, pressure inside the bubble, and pressure outside the bubble as given in [Equation 7](#Equation-7) [(Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html).

The subteam plans on using the principles of this equation to further decrease the pressure inside the bubble. Because it is known that an increase in radius will result in a decrease in pressure, the subteam must find a way to increase bubble radius. One way to increase radius may be to prevent the bubbles in the reactor from quickly escaping. If a bubble stays inside the reactor for a relatively longer period of time, it will have a longer time to expand.

In the Analysis of Literature section, Equations 3-7 are evaluated and related to one another to form one basis for parameters of the system's design.

### Analysis of Literature
Through conceptual analysis and algebraic manipulation, Equations 3-7 combine to form an estimation of a gas’ solubility in water in an apparatus as illustrated in Figure 1. The following paragraphs describe this process. All relevant variables have been defined in the Literature Review section.

The pressure relevant to Henry's Law (i.e. the pressure of a gas above a liquid, in [Equation 3](#Equation-3)) is the pressure *within* a bubble [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html).
$$ C = k P $$

Since $P$ equates to the gas's pressure within a bubble, $P$ is relabeled as $P_b$.

As shown in [Equation 7](#Equation-7), the pressure within a bubble is directly related to the bubble's radius, the liquid's surface tension, and the pressure outside the bubble [(Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html).

$$P_i = P_o + 4 \frac{T}{R}$$

$P_i$ denotes the pressure within a bubble and therefore is relabeled as $P_b$. $P_o$ denotes the pressure outside of the bubble and is relabeled $P_r$ (i.e. pressure in the liquid within the reactor).

The pressure outside of the bubble can be equated to atmospheric pressure, plus a change in pressure due to the height difference between the reactor and the vent ($\Delta P_{height}$) [(Equation 4)](#Equation-4), plus a change in pressure due to head loss in the tubing connecting the reactor and the vent ($\Delta P_{head loss}$) [(Equation 6)](#Equation-6).

$$\Delta P_{height} = \rho g \Delta h$$

$$\Delta P_{head loss} = \rho g h_f$$

The greater the difference in height, the lower the pressure within the reactor. The greater the head loss, the greater the pressure within the reactor. Thus, the pressure within the reactor may be written as follows:

####Equation 8

$$P_r = P_{atm} + \Delta P_{height} + \Delta P_{head loss} = P_{atm} - \rho g \Delta h + \rho g h_f$$

The second term of this equation was negated to indicate that, while $\Delta h$ increases in magnitude, the pressure in the reactor decreases.

These equations may be combined and rearranged given their relabeled variables. The following relationship emerges to relate the solubility of the gas in the reactor to a bubble's radius, the height of the reactor, the water's surface tension, the dimensions of the effluent tubing, and the constant relevant to Henry's Law:

#### Equation 9

$$C = k(\frac{4T}{R} + P_{atm} - \rho g \Delta h + \rho g h_f)$$

**Variables**
$C$ = Solubility of a gas in the water
$g$ = Acceleration due to gravity
$\Delta h$ = Height difference between the vent and the reactor (this is a negative quantity)
$h_f$ = Head loss in the outlet tubing, as given in [Equation 5](#Equation-5)
$k$ = A constant for a given substance at a given temperature, related to Henry’s Law
$P_{atm}$= Atmospheric air pressure at the level of the vent
$R$ = Radius of a bubble in the reactor
$⍴$ = Density of water
$T$ = Surface tension of the water at a given temperature

[Equation 9](#Equation-9) mathematically summarizes the concepts addressed in the Literature Review section. In order to minimize gas solubility (and therefore, to maximize the amount of gas that is removed from influent water): the radii of bubbles that form must be maximized, the head loss in the exit tubing must be minimized, and the height difference between the reactor and vent must be maximized within reason. Further considerations may arise when [Equation 5](#Equation-5) is substituted for the $h_f$ value.

While [Equation 9](#Equation-9) is powerful in its efficiency, it may only act as an approximation of the solubility of a gas in the fluidized bed reactor. Equations 3-7 assume equilibrium: that the rates of air shifting from liquid to gas phase and vice versa are equal. The system may not be in equilibrium while the reactor is in use. Therefore, [Equation 9](#Equation-9) remains only a qualitative description of the relationships between different system parameters.

[Equation 9](#Equation-9), supplemented by [Equation 1](#Equation-1) concerning fluidization velocity, informed the subteam's fabrication of the prototype apparatus. In future semesters, the equation may be used to perform optimizations once the subteam has gathered sufficient experimental data.

## Previous Work

The Fall 2018 subteam's work comprised research, design, fabrication, and basic experimentation to begin development of a reactor to remove excess dissolved gas from influent water in AguaClara plants.

The subteam's research focused on developing a fluidized bed reactor that would encourage bubble formation by providing bubble nucleation sites. The subteam gathered literature on the relevant concepts such as fluidization, bubble nucleation, and gas solubility. As detailed in the Analysis of Literature section, the subteam combined key variables to derive [Equation 9](#Equation-9) for the approximate solubility of a gas in water.

The subteam then experimentally determined relevant system parameters (eg. sand bed porosity and sand grain diameter), and designed and fabricated a small-scale fluidized bed reactor. [Python code](https://github.com/AguaClara/Dissolved-Gas/blob/master/Code/FluidizationVelocity.py) was developed to facilitate easy calculation of the fluidization velocity and fluidization flow of the sand bed. [Python code](https://github.com/AguaClara/Dissolved-Gas/blob/master/Code/HeadLoss.py) was also written to calculate the head loss through the reactor's effluent tubing.

After fabricating the prototype system, the subteam ran basic tests to determine its functionality. The reactor's sand bed failed to consistently fluidize while using a 100 RPM peristaltic pump. However, the Spring 2019 subteam recently acquired a 600 RPM peristaltic pump, pictured in Figure 3, to incorporate into the system.

Further specifics concerning the subteam's work during the Fall 2018 semester are described in the [Fall 2018 Final Report](https://github.com/AguaClara/Dissolved-Gas/blob/master/Research%20Reports/Final_Report.md).

The subteam looks forward to testing the prototype to confirm its functionality, optimize its performance, and to eventually develop a practical reactor.

## Methods
**Installing a Pressure Sensor**
**Creating Forked Flow System**
**Installing a Pressure Regulator**
(need to put all of this in paragraph form **ew465**)
A pressure regulator was installed between the sink and the influent end of the tubing. This was done to maintain consistent water flow into the peristaltic pump.

A piece 26" 3/8 diameter hard plastic tubing was used to connect the reducing valve to the sink. The other side of the reducing valve was connected directly to the influent tubing.

**Reducing Valve**
B&G V56001 Strainer E79
Part Number: 110192
Model Number: FB-38
Max Press: 125 PSI
Max Temp: 225°F
Set At: 12 lbs

![Picture of Reducing Valve](https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Pressure_Regulator.JPG?raw=true)

**Qualitative Temp Experiment**


Explain the techniques you have used to acquire additional data and insights. Reserve fine detail for the Manual at the end of the report, but use this section to give an overview with enough detail for the reader to understand your Results and Analysis. Describe your apparatus, and have a justification for every decision you made and every parameter you chose in the design of the apparatus. Be especially careful to detail the conditions your experiments were conducted under, as this information is especially important for interpreting your results

Below, some example sections are given. Sectioning the report is meant to keep similar information together.  Continue making sections as necessary, or delete sections if you do not need them. Feel free to add subsubsections to further delineate the information. For example, under the Experimental Apparatus section below, the EStaRS team might consider having sections such as "Filter Design" and "Filter Fabrication".

### Experimental Apparatus
Explain your apparatus setup using enough detail such that future teams can recreate your apparatus. Make sure to explain why you built it this way.
* Design (calculations, constraints)

  $\frac{-b\pm\sqrt{b^2-4ac}}{2a}$
* Schematic (label parts)

  <img src="https://github.com/jillianwhiting/Jillian-Whiting/blob/master/Images/IMG_0009.jpg?raw=true" height=250 width=200>

* Image (from lab; label parts)
* Materials (dimensions, materials)
* Complications in construction
* If already constructed: write a brief summary of important constraints, include any revisions to apparatus, also reference the prior report where construction is described

### Procedure
Discuss your experimental procedure. How did you run your experiment? What were you testing? What were the values of relevant parameters?

## Results and Analysis
Present an observation (results), then explain what happened (analysis).  Each paragraph should focus on one aspect of your results. In that same paragraph, you should interpret that result.  
In other words, there should not be two distinct paragraphs, but instead one paragraph containing one result and the interpretation and analysis of this result. Here are some guiding questions for results and analysis:

When describing your results, present your data, using the guidelines below:
* What happened? What did you find?
* Show your experimental data in a professional way.
```python
from aide_design.play import*
x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])
plt.figure('ax',(10,8))
plt.plot(x,y,'*')
plt.savefig('/Users/jillianwhiting/github/Jillian-Whiting/Images/linear')
plt.show()
```
![linear](https://github.com/jillianwhiting/Jillian-Whiting/blob/master/Images/linear.png?raw=true)
Figure 1: Captions are very important for figures. Captions go below figures.

After describing a particular result, within a paragraph, go on to connect your work to fundamental physics/chemistry/statics/fluid mechanics, or whatever field is appropriate. Analyze your results and compare with theoretical expectations; or, if you have not yet done the experiments, describe your expectations based on established knowledge. Include implications of your results. How will your results influence the design of AguaClara plants? If possible provide clear recommendations for design changes that should be adopted. Show your experimental data in a professional way using the following guidelines:
* Why did you get those results/data?
* Did these results line up with expectations?
* What went wrong?
* If the data do not support your hypothesis, is there another hypothesis that describes your new data?

## Conclusions
Explain what you have learned and how that influences your next steps. Why does what you discovered matter to AguaClara?

Make sure that you defend your conclusions with facts and results.

## Future Work
Describe your plan of action for the next several weeks of research. Detail the next steps for this team. How can AguaClara use what you discovered for future projects? Your suggestions for challenges for future teams are most welcome. Should research in this area continue?

## Bibliography
Logan, B. E., Hermanowicz, S. W., & Parker,A. S. (1987). A Fundamental Model for Trickling Filter Process Design. Journal (Water Pollution Control Federation), 59(12), 1029–1042.

# Manual
The goal of this section is to provide all of the guidance that would be necessary for a future team to pick up your work where you left off. Please try to be thorough and put yourselves in the shoes of a newcomer to the project. Below are some recommended sections, but the manual will likely take a slightly different form for each team.

## Fabrication Details
Include any information related to the fabrication of equipment, experimental apparatuses, or technologies. Include the purpose of each step and the fabrication methods used. Reference appropriate safety precautions.

The prototype was made with simple parts that are easily found around the lab. There is a PVC pipe where our reactor is present

## Special Components
If your subteam uses a particular part that is unique and you could foresee a future subteam needing to order it or learn more about it, please include basic information like the vendor where it was purchased, catalog/item number, and a link to any documentation.

### Experimental Methods

#### Determining the Porosity of Silica Sand

The porosity of silica sand was needed to calculate the sand bed's fluidization velocity ([Equation 1](#Equation-1)). The following procedure was used to determine the porosity of the silica sand used in the reactor, based on the procedure outlined by [Worth, 2018](https://socratic.org/questions/how-do-scientists-measure-the-porosity-of-soil). The equation for determining porosity may be verified by dimensional analysis in comparison with the equation found in the source: [Department of Chemical Engineering, 2017](http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf).

**Set-Up**
1. Acquire silica sand, water, and two graduated cylinders.
2. Transfer a portion of the sand to a graduated cylinder and record the sand bed’s volume. This is the “sample volume”, $V_{sample}$.
3. Pour an excess volume of water into a second graduated cylinder. Record this volume.

**Experiment**
1. Pour water from its graduated cylinder into the graduated cylinder containing sand until the meniscus’ peak is level with that of the sand bed. This equates to saturating the sand with water.
2. Record the volume of water remaining in its respective graduated cylinder. Subtract this volume from the initial volume of water present in the graduated cylinder; the difference is the volume of water used to saturate the sand. This quantity is the "pore volume", $V_{pore}$.
3. Repeat the Set-Up and Experimental Steps 1-2  until three trials’ worth of data has been recorded.
4. Use [Equation 8](#Equation-8) to calculate the sand’s average porosity ($\phi$).

$$\phi = \frac{V_{pore}}{V_{sample}}$$

#### Determining the Average Diameter of Silica Sand Grains [Complete, no edit necessary]

The average diameter of the silica sand grains was needed to calculate the sand bed’s fluidization velocity ([Equation 1](#Equation-1)). The subteam used the following procedure to approximate the average diameter of the sand grains.

1. Acquire a sample of silica sand and a digital caliper.
2. Randomly select a number of sand grains, preferably greater than or equal to ten, from the sample.
3. Using the caliper, measure each sand grain’s diameter three times to account for the grains’ asymmetrical natures. Record these measurements.
4. Compute the average diameter for all sand grains in the sample.

#### Measuring Pipe Dimensions [Complete, no edit necessary]

The prototype fluidized bed reactor was comprised of a transparent PVC pipe containing a silica sand bed, modified with components specified in the Fabrication Manual.

**Set-Up**
The subteam cut the pipe to be a particular length prior to taking measurements.
1. Acquire a transparent PVC pipe of approximately 1” diameter, a Sawzall reciprocating saw, colored tape in two shades, permanent markers, measuring tape, and a caliper.
2. Use a measuring tape and marker to indicate a length of 0.5 m on the PVC pipe. Cut the PVC pipe using the Sawzall such that it matches this length.
3. Wrap tape of opposing colors on opposing ends of the pipe, but *leave several inches between the edge of the pipe and the tape itself*. The tape should be several inches from the edge of the pipe. Use this tape to maintain awareness of the pipe's orientation.

**Measurement**
1. Use a caliper to take the following measurements on both opposite ends of the pipe:
- Measure the thickness of the pipe’s wall in three locations. Compute the average thickness of the pipe’s wall.
- Measure the diameter of the pipe (including the wall) in three locations. These measurements are of the pipe’s “outer diameter”. Compute the average outer diameter of the pipe.
- Subtract twice the wall’s thickness from the outer diameter; the difference is the “inner diameter”. Use this quantity to calculate the cross-sectional area of the pipe.
2. Compute the average cross-sectional area of the pipe, using the measurements taken at both ends.

### Cleaning Procedure
Step 1.

## Experimental Checklist
Another potential section could include a list of things that you need to check before running an experiment.

## ProCoDA Method File
Use this section to explain your method file. This could be broken up into several components as shown below:

### States
Here, you should describe the function of each state in your method file, both in terms of its overall purpose and also in terms of the details that make it distinct from other states. For example:
\begin{itemize}
\item \underline{OFF} - Resting state of ProCoDA. All sensors, relays, and pumps are turned off.
\end{itemize}

### Set Points
Here, you should list the set points used in your method file and explain their use as well as how each was calculated.

## Python Code

### Variables
$g$: gravity
$\sigma$: dispersion
$a$: amplitude
$h$: water depth
$H$: distance from wave crest to trough (2$a$)
$T$: wave period
$\lambda$: wavelength
$k$: wavenumber
$c_p$: celerity (wave phase speed)
$P$: pressure
$F$: force
$u$, $w$: x-velocity, z-velocity components

```python
# Comment
```

# Add/Delete/Change this Template as you see Fit
When using this template keep in mind that this serves three purposes. The first is to provide your team feedback on your progress, assumptions, and conclusions. The second is to keep your team focused on what you are learning and doing for AguaClara. Another is to educate future teams on what you've learned and done. This document should be comprehensive, consistent, and well-written. With that in mind, add, subtract, or move sections. Reach out to the RAs and graders for help with figuring out what should or shouldn't include. Focus on how wonderful a reference you are making through this and work hard on communicating amongst yourselves and with future teammates. (Delete this section before submitting)

```python
# To convert the document from markdown to pdf
pandoc Name_of_this_file.md -o TeamName_Research_Report.pdf
```

## Bibliography

Averill, B., & Eldredge, P. (n.d.). *Principles of General Chemistry* (Vol. 1). Creative Commons. Retrieved from https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html

Boudreau, B. P., Algar, C., Johnson, B. D., Croudace, I., Reed, A., Furukawa, Y., … Gardiner, Bruce S. (2005, June 5). *Bubble growth and rise in soft sediments.* Retrieved September 17, 2018, from https://pubs.geoscienceworld.org/gsa/geology/article/33/6/517/103815/bubble-growth-and-rise-in-soft-sediments

Brown, G. (2000, June 22). *The Darcy-Weisbach Equation*. Retrieved from https://bae.okstate.edu/faculty-sites/Darcy/DarcyWeisbach/Darcy-WeisbachEq.htm

CodeCogs.(2012, February 24). Pipe Head Loss. Retrieved from http://www.codecogs.com/library/engineering/fluid_mechanics/pipes/head_loss/pipe-head-loss.php

Denn, M. (1980). Process Fluid Mechanics (pp. 72-73). Upper Saddle River, NJ: Prentice Hall PTR.

Department of Chemical Engineering. (2017, February). *Fluidization: A Unit Operation in Chemical Engineering.* Gainesville, FL: University of Florida. Retrieved from http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf.

Han, M., Park, Y., Lee, J., & Shim, J. (2002). *Effect of pressure on bubble size in dissolved air flotation.* Water Science and Technology: Water Supply, 2(5–6), 41–46. https://doi.org/10.2166/ws.2002.0148

Harrison, D., & Leung, L. S. (1961, April 29). *Bubble Formation at an Orifice in a Fluidized Bed | Nature*. Retrieved September 20, 2018, from https://www.nature.com/articles/190433a0

Hodanbosi, C. (n.d.). *Fluids Pressure and Depth*. Retrieved from https://www.grc.nasa.gov/www/k-12/WindTunnel/Activities/fluid_pressure.html

Hyperphysics. (n.d.). *Surface Tension and Bubbles.* Retrieved from http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html

Scardina, P... (2004). *Effects of Dissolved Gas Supersaturation and Bubble Formation on Water Treatment Plant Performance* (Unpublished doctoral dissertation). Virginia Polytechnic Institute and State University. Blacksburg, Virginia. https://vtechworks.lib.vt.edu/bitstream/handle/10919/26497/PaoloScardinaDissertation2004.pdf?sequence=1

Schulz, P. (2004). *Instability and the formation of bubbles and the plugs in fluidized beds*, 24(1), 27. Retrieved from https://www.opuscula.agh.edu.pl/vol24/1/art/opuscula_math_2412.pdf

Weber-Shirk, M. *Filtration Theory: On removing little particles with big particles* [PowerPoint Slides]. Retrieved from https://courses.cit.cornell.edu/cee4540/pdf/Filtration.pdf.

Weber-Shirk, M. *Flow Control and Measurement* [PowerPoint Slides]. Retrieved from https://courses.cit.cornell.edu/cee4540/pdf/Flow%20Control%20and%20Measurement.pdf.
