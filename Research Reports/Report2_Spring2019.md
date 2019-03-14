# Dissolved Gas, Spring 2019 Subteam
#### Saul Bernaber, Thomas Bradford, Emily Wood
#### 15 March 2019

## Abstract
Excess dissolved air in a treatment plant’s influent water decreases the functionality of the plant's components. The Dissolved Gas subteam aims to design a gravity-powered apparatus to extract excess gas from influent water prior to entry into a plant. The Fall 2018 subteam fabricated a small-scale prototype incorporating a fluidized bed reactor. The Spring 2019 subteam will experimentally evaluate the prototype: given qualitative success, the subteam will test the prototype's effectiveness by measuring change in dissolved oxygen concentration across the apparatus. The Spring 2019 subteam will iterate improvements to work toward a prototype for application in an AguaClara plant.

## Table of Contents

- [Introduction](#Introduction) [Update Figure 3; update the introduction to talk about initial evaluation of the experimental apparatus]
- [Literature Review](#Literature-Review) [Consider adding a reference about oxygen solubility vs. temperature]
  - [Fluidized Beds and Bubble Formation](#Fluidized-Beds-and-Bubble-Nucleation)
  - [Controlling Pressure](#Controlling-Pressure)
  - [Gas Solubility versus Temperature](#Gas-Solubility-versus-Temperature)
  - [Analysis of Literature](#Analysis-of-Literature)
- [Previous Work](#Previous-Work)
- [Methods](#Methods) [Emily] (including new figures)
- [Results and Analysis](#Results-and-Analysis) [Tommy]
- [Conclusions](#Conclusions) [Tommy]
- [Future Work](#Future-Work) [Tommy]
- [Bibliography](#Bibliography) [Update to make sure all sources are cited]
- [Manual](#Manual) [Saul]
  - [Experimental Methods](#Experimental-Methods)
  - [Fabrication Manual](#Fabrication-Manual)
  - [Python Code](#Python-Code)
  - [ProCoDa Code](#ProCoDa-Method-File)


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
**The subteam built...and tested...and will...**

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

### Gas Solubility versus Temperature

**Summarize the information & why it relates to our experimental apparatus**

<p style="text-align: center;">
<img src="https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/section_17/67558bdc4beb64e06b29db7b4c8d74bb.jpg" height=350>

</p>

**Figure X**: The above graph displays the solubility (mg / 100 g water) of five gases as a function of temperature (degrees Celisus) at a partial pressure of 1 atm [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html).

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
Explain the techniques you have used to acquire additional data and insights. Reserve fine detail for the Manual at the end of the report, but use this section to give an overview with enough detail for the reader to understand your Results and Analysis. Describe your apparatus, and have a justification for every decision you made and every parameter you chose in the design of the apparatus. Be especially careful to detail the conditions your experiments were conducted under, as this information is especially important for interpreting your results

Below, some example sections are given. Sectioning the report is meant to keep similar information together.  Continue making sections as necessary, or delete sections if you do not need them. Feel free to add subsubsections to further delineate the information. For example, under the Experimental Apparatus section below, the EStaRS team might consider having sections such as "Filter Design" and "Filter Fabrication".

### Experimental Apparatus

**NOTE**: Mention RPM as it relates to fluidization velocity?

Explain your apparatus setup using enough detail such that future teams can recreate your apparatus. Make sure to explain why you built it this way.

**Schematic**:
<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype2/Schematic%20of%20apparatus.jpg?raw=true" height = 350>

</p>

**Figure X**


* Design (calculations, constraints)

  $\frac{-b\pm\sqrt{b^2-4ac}}{2a}$
* Schematic (label parts)

  <img src="https://github.com/jillianwhiting/Jillian-Whiting/blob/master/Images/IMG_0009.jpg?raw=true" height=250 width=200>

* Image (from lab; label parts)
* Materials (dimensions, materials)
* Complications in construction
* If already constructed: write a brief summary of important constraints, include any revisions to apparatus, also reference the prior report where construction is described

**Installing a Pressure Sensor**

**Rewrite this in paragraph form ew465**
1. **Edit** To install the pressure sensor, use a 1/4" 18NPT Pipe Tap to tap the pipe 70 cm from its bottom (influent) end. Tap the aperture. Thread a push-to-connect component into the tapped aperture, with the connection made watertight with Teflon tape.
2. **Edit** Insert **_____** hard tubing into the connector. Insert the negative end of the pressure sensor into the exposed tubing, sealing with medium clear PVC cement.

**Installing a Pressure Regulator**

A pressure regulator was installed between the sink and the peristaltic pump to maintain consistent flow of influent water.

The pressure regulator [**Insert Figure Number**] was oriented such that the direction of water flow matched the arrow on the apparatus. The left side was connected to the sink using a piece of 26" long and 3/8" diameter hard plastic tubing, and the right side was connected to the peristaltic pump using the original piece of clear flex tubing that was attached to the pump. The flow of water was reduced by tightening the screw and nut on the top of the pressure regulator, until no leakage occurred when peristaltic pump was turned off.  

![Picture of Reducing Valve](https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Pressure_Regulator.JPG?raw=true)
**Need to make this smaller ew465**

**Note: the above format used to insert a photo doesn't allow for dimension alteration, far as I know. To do that, try the following:**
<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/PressureRegulator_SideBySide.jpg?raw=true" height = 300>

</p>

**Figure X**:

**Creating a Forked Flow System**

The subteam needed a way to measure the temperature (and eventually the dissolved oxygen content) of the influent water before it entered the reactor. The subteam’s solution was to create a forked flow system in which some of the influent water is diverted to a separate container before reaching the peristaltic pump. The temperature of the diverted water could then be measured in this container. This model was chosen to avoid inadvertently changing any properties of the influent water during measurement. To clarify, a dissolved oxygen probe consumes oxygen in the process of measuring its concentration, and would therefore lead to an overestimate of the actual dissolved oxygen content flowing into the reactor.

To fabricate the forked flow system, a 0.75’’ hole was drilled near the bottom of a 500 mL Nalgene bottle. A slightly larger 1.6” hole was drilled near the top of the Nalgene. This hole was used to insert a tapered push-to-connect into the bottle, since the push-to-connect was too large to fit through the neck of the bottle. The larger 1.6” hole was then plugged to prevent leakage. The push-to-connect was oriented such that its tapered end protruded from the hole near the bottom of the Nalgene, and secured with a washer.

Next, two pieces of clear flex tubing were connected to either side of a T push-to-connect such that they were oriented in a straight line. The pump influent tube was then connected to the T push-to-connect such that it was perpendicular to the two shorter pieces of clear flex tubing. One end of the short clear flex tubing was connected to the peristaltic pump and the other end was attached to the push-to-connect of the Nalgene bottle.  

**Insert more pictures ew465**

The Nalgene apparatus:
<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype2/FlowAccumulator1_SideBySide.jpg?raw=true" height=300>

**Figure X**:

### Procedure
Discuss your experimental procedure. How did you run your experiment? What were you testing? What were the values of relevant parameters?

**Qualitative Temp Experiment**

## Results and Analysis
Numerical and video data from the experiments described in the Methods section was analyzed.

**Table 1**: Displays the data collected during Trials 1 through 6 of the experiments performed on March 10. This includes: experiment duration (s), average pressure difference between the interior and exterior of the reactor (Pa), the average temperature of influent water (C), and corresponding standard deviations. Full data records can be found on [this site](https://docs.google.com/spreadsheets/d/1TsF6WTH7_1kZF3rtxQfxWHmNm25GDSTorC64Gjq5S7U/edit?usp=sharing).  

|              Trial               |    1    |    2    |    3    |    4    |    5    |    6    |
|:--------------------------------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|     Approximate duration (s)     |   25    |   25    |   25    |   25    |   15    |   15    |
| Average pressure difference (Pa) | 5971.72 | 5065.84 | 3758.40 | 4134.08 | 3601.98 | 3452.05 |
|        Standard deviation (Pa)        |  98.46  | 423.64  | 189.06  | 299.66  |  10.31  |  11.74  |
| Percent standard deviation| 1.65        | 8.36        |5.03         |7.25  | 0.29   | 0.34        |
| Average temperature (C)      |  22.05  |  19.91  |  18.63  |  33.03  |  35.79  |  36.85  |
|        Standard deviation (C)        |  0.42   |  0.33   |  0.19   |  1.65   |  0.36   |  0.50   |
|    Percent standard deviation    |  1.89   |  1.65   |  1.03   |  4.98   |  1.01   |  1.35   |

Video recordings were also taken of each Trial. Bubbles were seen to form in the fluidized bed reactor, as shown in Figure X. This demonstrates the basic feasibility of encouraging bubble growth with a fluidized bed. However, between Trials 1-3 and Trials 4-6, there were no consistent, visually assessable differences in bubble formation. Figures ____ and _____ exemplify this, and all full-length videos can be found on [this site](https://drive.google.com/drive/folders/1bybRun4xh5kzI4QvrN0ZPXhFWCMlhZhN?usp=sharing). While the effect of temperature on gas solubility was not the focus of the subteam's work, it was an aspect the subteam considered for designing the experimental apparatus, to simulate input of supersaturated water.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Gifs/march10_trial1.gif?raw=true" height = 400>
</p>

**Figure X**: The GIF above displays a clip from the recording of Trial 1.


<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Gifs/march10_trial4.gif?raw=true" height = 400>
</p>

**Figure X**: The GIF above displays a clip from the recording of Trial 4.

**Edit this**
Despite the approximate ten degree difference in temperatures between Trials 1-3 and Trials 4-6, there was not a significant difference observed in the quantity or size of bubbles generated in the fluidized bed.

This can potentially be explained after a quick analysis of Figure _____.

While Figure ___ assumes a partial pressure of 1 atm of the gas of interest, this analysis considers the qualitative principles that the Figure illustrates. In Figure ____, in the range of 20 to 30 degrees C (the approximate range of experimental temperatures), the percent difference in solubility of oxygen and nitrogen (the primary components of air) is relatively small. As temperature increases from 20 to 30 degrees C, a 50% increase in temperature, oxygen's solubility drops from approximately 4.3 to 3.5 mg / 100 $H_2O$, only an approximately 18% decrease in solubility. Such a difference in solubility may not have visually assessable consequences for bubble formation.

To observe an appreciable difference in bubble formation in the fluidized bed, a greater temperature difference between Trials may be required. For instance, over the range 10 to 40 degrees C, oxygen's solubility shifts from approximately 5 to 3 mg / 100 $H_2O$, a percent change of 40%. This percent change is twice that which characterized Trials 1 - 6 on March 10, and such a difference may provide more distinguishable results.

The subteam also observed that, with the exception of Trial 6, percent standard deviation in temperature decreased as the influent water's temperature reached extremes relative to the trials' conditions. This suggested that the temperature of each trial's influent water had begun to plateau, but had not yet reached the extreme values of the influent water's potential temperatures.

## Conclusions
While some bubbles formed in the fluidized bed reactor, experimental data revealed shortcomings in the experimental setup. There was no visually discernable difference in bubble formation between fluidized beds whose influent water streams had a temperature difference of approximately ten degrees Celsius.

The subteam considered measuring the temperature of the reactor's effluent, to determine whether the water's temperature remains relatively constant as it passes through the reactor. The subteam also considered conducting experiments at more extreme temperatures, to take advantage of the greater difference in solubility, as discussed in the Results and Analysis section.

## Future Work
The subteam will progress with experimentation, evaluation, and iteration of the apparatus.

The subteam has qualitatively determined that bubbles do form within the fluidized bed reactor. This suggests that the premise of using a fluidized bed to encourage bubble formation and to remove excess dissolved air from water is plausible. The subteam will modify the experimental method, considering more extreme temperatures so as to prove the difference in oxygen's solubility and improve the opportunity for observational evaluation. The subteam also will consider using a camera set-up to have consistent video recordings of experiments, to avoid errors or uncertainty due to avoidable error such as hand movement. The subteam will also consider making a larger flow accumulator, or otherwise changing the experimental apparatus such that the duration of experiments increases.

After system improvements, the subteam will also progress to more thorough, quantitative analysis of the prototype. The subteam will use dissolved oxygen probes to determine the difference in concentration of dissolved oxygen between the influent and effluent water. (**The subteam expects that the water's dissolved oxygen content is proportional to the water's dissolved air content since the major source of the dissolved oxygen is air. Therefore, the system's effectiveness in removing dissolved oxygen should be proportional to the system's effectiveness in removing dissolved air.**) After analysis of concentration data, the subteam will modify the system to optimize the removal of dissolved gas.

In future semesters, the subteam must also consider the end goal of scaling up the prototype. The prototype's method to remove excess dissolved gas from influent water must feasibly apply on a practical scale. As part of this end goal, as pertaining to a fluidized bed reactor, the subteam must evaluate the validity of the calculated fluidization flow of the sand bed, and the validity of the calculated entrainment velocity. In order to reliably scale up a fluidized bed reactor, the fluidization flow must be reliably calculable.

The subteam looks forward to future semesters' experimentation and iteration to analyze and improve the system, and to eventually develop a practical reactor.

# Manual
The goal of this section is to provide all of the guidance that would be necessary for a future team to pick up your work where you left off. Please try to be thorough and put yourselves in the shoes of a newcomer to the project. Below are some recommended sections, but the manual will likely take a slightly different form for each team.

## Special Components
If your subteam uses a particular part that is unique and you could foresee a future subteam needing to order it or learn more about it, please include basic information like the vendor where it was purchased, catalog/item number, and a link to any documentation.

A Pressure regulator is a device that manages the pressure. For the purposes of the subteam we use it in order to decrease the pressure coming from the water supply (Sink).
This allows for the flow rate of the influent water to be stopped when the peristaltic pump is stopped.

The specifications of the Pressure Regulator are as follows:
**You know what to do here**

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

#### Determining the Average Diameter of Silica Sand Grains

The average diameter of the silica sand grains was needed to calculate the sand bed’s fluidization velocity ([Equation 1](#Equation-1)). The subteam used the following procedure to approximate the average diameter of the sand grains.

1. Acquire a sample of silica sand and a digital caliper.
2. Randomly select a number of sand grains, preferably greater than or equal to ten, from the sample.
3. Using the caliper, measure each sand grain’s diameter three times to account for the grains’ asymmetrical natures. Record these measurements.
4. Compute the average diameter for all sand grains in the sample.

#### Measuring Pipe Dimensions

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

### Fabrication Manual

**Necessary edits**:
- New tubing size.
- Installation of the Forked System

**Materials required**
1. PVC pipe of approximately 0.5 m length and 1 in. diameter, whose ends are labeled with opposing colors of tape, as shown in Figure 8. This is described further in the Measuring Pipe Dimensions section of the Manual.
2. A fine wire mesh
3. Approximately 70 mL of silica sand, measured with a graduated cylinder.
4. Circular hose clamps
5. 3/16-inch diameter clear flex tubing
6. 3/8-inch diameter clear flex tubing
7. Size 18 Masterflex tubing
8. 600 RPM Peristaltic pump
9. Barbed fittings & push-to-connect components
10. Access to a sink containing a push-to-connect nozzle
11. A plastic bucket
12. 200 kPa pressure sensor
13. ProCoDA Box
14. **1/4" hard tubing (for the pressure sensor)**
15. Teflon tape
16. 1/4 " Threaded push-to-connect component
17. 1/4 " 18NPT Pipe Tap
18. Medium clear PVC cement
19. 12. Two copies of the following pipe-tubing connector component:


<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype_1/PipeConnector1.jpg?raw=true" height=250
</p>

Recall **Figure 7** from the Methods section. The above flow connector enables the reactor (pipe) to be connected to clear flex tubing.

**Fabrication**
1. To install the pressure sensor, use a 1/4" 18NPT Pipe Tap to tap the pipe 70 cm from its bottom (influent) end. Tap the aperture. Thread a push-to-connect component into the tapped aperture, with the connection made watertight with Teflon tape.
2. **Edit** Insert 1/4" hard tubing into the connector. Insert the negative end of the pressure sensor into the exposed tubing, sealing with medium clear PVC cement.
3. Cut the wire mesh to obtain a circular mesh whose radius is approximately that of the pipe.
4. Place the mesh at the bottom of the pipe reactor, at the side designated for influent to enter the pipe. Place this mesh into the flow component that from (12.).
5. Pour the 70 mL of sand into the pipe, such that it settles on the mesh.
6. Fasten the second copy of the flow component from (12.) to the effluent (top) end of the reactor.
7. Mount the pipe on the 80/20 arm using circular clamps, screwed tight around the reactor.
8. Connect Size 18 Masterflex tubing to the Peristaltic Pump.
9. Connect 3/8-inch diameter clear flex tubing from the sink to the influent end of the Peristaltic Pump.
10. Connect 3/16-inch diameter clear flex tubing from the effluent end of the peristaltic pump to the influent end of the reactor.
11. Cut approximately 2.7 m of 3/16-inch diameter clear flex tubing. Connect this to the effluent (upper) end of the reactor, and lead it down into the bucket.
12. Connect the 200 kPa pressure sensor to the ProCoDA box.


### Cleaning Procedure
The experiments are really low maintenance and easy to wrap up.

1. Turn off the Peristaltic Pump
2. Close off water supply
3. Disconnect the flex tubing used for influent water from the water supply

## ProCoDA Method File

###States
- *OFF*: The peristaltic pump is off.
- *Running*: The peristaltic pump is running.


###Set Points
- *OFF*:This setpoint is used to turns all outputs off.
- *ON*: This setpoint turns on the peristaltic pump on.
- *PumpOutput*: This setpoint is used to turn on the peristaltic pump at the correct number of RPMs to achieve the desired flow rate, given the Tubing ID.


###Variables
- *FlowRate*: This variable is the desired flow rate. In the subteam's reactor, this represents the fluidization velocity.
- *TubingID*: This variable represents the ID associated with tubing being used, based on the diameter of the tubing.

## Python Code

### Determining the Sand Bed's Fluidization Flow

The subteam used the following code, copied from the file FluidizationVelocity.py found on the subteam's GitHub page, to estimate the fluidization velocity and fluidization flow of the sand bed in the prototype reactor. The code is based on [Equation 1](#Equation-1). The code requests as input: the reactor's cross-sectional area; the kinematic viscosity of water at a particular temperature (e.g. room temperature); the sand's porosity, which the subteam experimentally determined; silica sand's density; the average diameter of the sand grains, which the subteam measured. The code outputs the velocity and flow of water required to fluidize the sand bed.

The following values were used for the subteam to calculate the fluidization flow of 2.54 mL/s:

Cross-sectional area of the reactor: 481.1 mm$^2$
Porosity of the silica sand: 0.35
Density of silica sand: 2650 kg/m$^3$ [(Weber-Shirk)](https://courses.cit.cornell.edu/cee4540/pdf/Filtration.pdf)
Average diameter of the silica sand grains: 0.91 mm
Kinematic viscosity of water: 0.9344 mm$^2$/s [(Anton Paar)](https://wiki.anton-paar.com/en/water/)

```python
# This code assumes the user knows the porosity of the sand used in the fluidized bed. This code makes use of aide_design, a package provided by AguaClara Cornell

# Assumptions: All input values are real numbers.

from aguaclara.play import*
import math
import numpy as nm

def FluidizationVelocity(area_reactor, porosity, density_sand, diameter, viscosity):
    """This function also takes in values of the area of the reactor, porosity of sand,
  density of the sand, diameter of sand grains, and kinematic viscosity of water.

  >>> from aguaclara.play import*
  >>> FluidizationVelocity(5, 5, 5, 5, 5):
The reactor's fluidization velocity is 8464 millimeter / second.
The reactor's fluidization flow is 42.32 milliliter / second.
  """
    area_reactor = float(input("\nWhat is the cross sectional area of the" + " fluidized bed reactor, in units of millimeters squared?\n"))*u.mm**2
    porosity = float(input("What is the porosity of the sand bed?\n"))
    density_sand = float(input("What is the density of the sand, in units of" + "kilograms per cubic meter?\n"))*u.kg/(u.m**3)
    density_water = 997*u.kg/(u.m**3)
    diameter = float(input("What is the average diameter of the sand grains," + "in units of millimeters?\n")) * u.mm
    g = 9.8 * u.m/(u.s**2)
    kozeny = 5  # This is an approx. value, suggested by Fluidization Source 4
    viscosity = float(input("What is the kinematic viscosity of water, in" + "units of millimeters squared per second?\n"))*u.mm**2/u.s
    # The following variable definitions are based off those in the equation in
    # Fluidization Source 4.
    fluidization_velocity_FirstTerm = (porosity**3 * g * (diameter)**2)/(36*kozeny*(viscosity)*(1-porosity))
    fluidization_velocity_SecondTerm = (density_sand/density_water - 1)
    fluidization_velocity = fluidization_velocity_FirstTerm *fluidization_velocity_SecondTerm * (1000*u.mm)/(1*u.m)
    fluidization_flow = fluidization_velocity * area_reactor * (0.001*u.mL)/(1*u.mm**3)
    print("\nThe reactor's fluidization velocity is " + str(fluidization_velocity)+".")
    print("The reactor's fluidization flow is " + str(fluidization_flow) + ".")

```

### Calculating Averages and Standard Deviations

The following code, copied from the file StandardDeviation.py found on the subteam's GitHub page, outputs the average value and the standard deviation of a group of input values.

```python
import math
import numpy as nm
import aide_design as ad
from aide_design import utility as ut
from aide_design.play import*

print("\n"+"Please input only real numbers; make sure the list is at least two items long! If you're done inputting your list, just type 'done'."+"\n")
values = []
item = "blank"
for n in range(100):
    item = input("What number would you like to add to the list?" +"\n")
    if item == "done":
        break
    else:
        try:
            values.append(float(item))
        except:
            print("It seems like you didn't input a number. Please try again!")

total=0
for n in range(len(values)):
    total += values[n]

average= total / len(values)

numerator = 0
for n in range(len(values)):
    numerator += (values[n]-average)**2

standard_deviation = math.sqrt(numerator / (len(values)-1))

print("The list you've entered has an average value of " + str(ut.sig(average, 4)) +", with a standard deviation of "+ str(ut.sig(standard_deviation, 4))+'.')
```

### Determining Head Loss in the Effluent Tubing

This code follows [Equation 4](#Equation-4), and may be found on the subteam's GitHub page. It outputs the head loss in tubing containing a laminar flow, and requests as input: the absolute viscosity of water; the tubing length, the water's velocity, the and the pipe's diameter.

```python

import math
import numpy as nm
import aide_design as ad
from aide_design import utility as ut
from aide_design.play import*

viscosity = float(input("What is the dynamic (i.e. absolute) viscosity of water, in units of millipascal seconds?\n"))*(1/1000) * u.kg/u.m/u.s
effluent_tubing_length = float(input("What is the length of the effluent tubing, in units of meters?\n"))*u.m
velocity = float(input("What is the velocity of water in the effluent piping, in units of meters per second?\n"))*u.m/u.s

density_water = 997*u.kg/(u.m**3)
g = 9.8 *u.m/(u.s**2)
pipe_diameter = float(input("What is the diameter of the effluent piping, in units of meters?\n"))*u.m

Head_Loss = (32 * viscosity * effluent_tubing_length * velocity)/(density_water * g * pipe_diameter**2)

print("The Head Loss due to the effluent tubing is "+ str(ut.sig(Head_Loss,3))+".")
```

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
