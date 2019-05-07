# Dissolved Gas, Spring 2019 Subteam
#### Saul Bernaber, Thomas Bradford, Emily Wood
#### 10 May 2019

**[Sidney: Hello friends! i will be commenting throughout your report in these bolded brackets.]**

**[I see that you guys have created a new file. PLEASE DO NOT DELETE GRADER COMMENTS IN YOUR SUBMISSIONS. We need to be able to refer back to them to see that you have properly addressed them. After we see that you have addressed them, we will delete the comments ourselves. In the future, we would greatly appreciate it if you didn't start a new file but continuously worked on one file.]**

**[Overall: Good job! Your writing is always superb. I would say that you need to improve on using your figures effectively throughout your report. It's hard to follow your report through when I have to jump around to find the correct figure you are referring to. Be consistent in linking (or not linking) sections of your report. Try to go back and add comments to your Python code.]**

## Abstract
Excess dissolved air in a treatment plant’s influent water decreases the functionality of the plant's components. The Dissolved Gas subteam continued research to design a gravity-powered apparatus to extract excess gas from influent water prior to entry into a plant. The Fall 2018 subteam fabricated a small-scale prototype incorporating a fluidized bed reactor. The Spring 2019 subteam began to experimentally evaluate the prototype: given qualitative success, the subteam tested the prototype's effectiveness by measuring change in dissolved oxygen concentration across the apparatus. In future semesters, the subteam will continue to troubleshoot currently malfunctional aspects of the prototype, and to iterate improvements to work toward a prototype for application in an AguaClara plant.

**[Please use past tense to refer to current semester and prior semester work.]**

## Table of Contents

- [Introduction](#Introduction)
- [Literature Review](#Literature-Review)
  - [Fluidized Beds and Bubble Formation](#Fluidized-Beds-and-Bubble-Nucleation)
  - [Controlling Pressure](#Controlling-Pressure)
  - [Gas Solubility versus Temperature](#Gas-Solubility-versus-Temperature)
  - [Analysis of Literature](#Analysis-of-Literature)
- [Previous Work](#Previous-Work)
- [Methods](#Methods)
  - [Experimental apparatus](#Eperimental-Apparatus)
    - [Pressure Regulator Installation](#Pressure-Regulator-Installation)
    - [Forked Flow System Installation](#Forked-Flow-System-Installation)
    - [Flow Accumulator Modifications](#Flow-Accumulator-Modifications)
    - [Temperature Probe Installation](#Temperature-Probe-Installation)
    - [Pressure Sensor Installation](#Pressure-Sensor-Installation)
    - [Dissolved Oxygen Probe Installation](#Dissolved-Oxygen-Probe-Installation)
  - [Experimental Procedure](#Experimental-Procedure)
    - [Testing Bubble Formation Qualitatively](#Testing-Bubble-Formation-Qualitatively)
      - [Testing Wider Temperature Ranges](#Testing-Wider-Temperature-Ranges)
    - [Testing Dissolved Oxygen Removal Quantitatively](#Testing-Dissolved-Oxygen-Removal-Quantitatively)
    - [Testing Dissolved Oxygen Probe Functionality](#Testing-Dissolved-Oxygen-Probe-Functionality)
    - [Testing Pressure Difference versus Flow Rate](#Testing-Pressure-Difference-versus-Flow-Rate)
- [Results and Analysis](#Results-and-Analysis)
- [Conclusions](#Conclusions)
- [Future Work](#Future-Work)
- [Bibliography](#Bibliography)
- [Manual](#Manual)
  - [Experimental Methods](#Experimental-Methods)
    - [Determining the Porosity of Silica Sand](#Determining-the-Porosity-of-Silica-Sand)
    - [Determining the Average Diameter of Silica Sand Grains](#Determining-the-Average-Diameter-of-Silica-Sand-Grains])
    - [Measuring Pipe Dimensions](#Measuring-Pipe-Dimensions)
    - [Evaluating Bubble Formation](#Evaluating-Bubble-Formation)
  - [Fabrication Manual](#Fabrication-Manual)
  - [Python Code](#Python-Code)
  - [ProCoDa Method File](#ProCoDa-Method-File)

## Introduction

Excess dissolved gas in influent water of AguaClara plants at Tamara, Honduras and El Poda, Nicaragua has reduced the plants' efficiencies. To clarify: “excess dissolved gas” does not entail bubbles being present in influent water. The influent water is supersaturated with gas: gas molecules are dispersed throughout the water, not congregated in bubbles. This report uses the term “supersaturated water” to denote water containing excess dissolved gas, whether air or otherwise.

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

In a fluidized bed reactor, bubbles may immediately travel upward once they form, since their nucleation sites (sand grains) are relatively mobile. Bubbles may depart the fluid at a relatively small diameter, carrying a high internal pressure, being likely to rupture and disperse into solution. Despite these potential issues, the subteam believes the fluidized bed reactor may still be effective, because a large number of sand grains may provide a large surface area for bubbles to nucleate. In future semesters, the subteam may consider an alternative reactor type and consider any contrasting merits.

After gathering and analyzing literature, the Fall 2018 subteam fabricated a prototype fluidized bed reactor using a transparent PVC pipe, silica sand, and flow components. The subteam assembled a basic apparatus to resemble the design proposed in Figure 1. Figure 3 presents a photograph of this apparatus. Influent water passes in through a peristaltic pump and through tubing into a vertically oriented fluidized bed reactor, and out into a small bucket. Further details on this apparatus are given in the Methods and Manual sections, and earlier stages are described in the [Fall 2018 Final Report](https://github.com/AguaClara/Dissolved-Gas/blob/master/Research%20Reports/Final_Report.md).

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Apparatus_20190427.jpg?raw=true" height = 430>

</p>

**Figure 3**: The left-hand photograph is of the current prototype apparatus. The right-hand photograph contains graphical enhancement to clarify the system's progression. Influent water (purple arrow) enters the system and is diverted to two paths. One path leads to a flow accumulator (blue rectangle) and then down into a large bucket. The second path leads through the peristaltic pump (orange rectangle), flows up into the fluidized bed reactor (green rectangle), exits the reactor as effluent water (dotted purple), pours into a small flow accumulator (yellow rectangle) that serves as an open-faced vent, and then down into a second bucket.

To simulate input of supersaturated water, the subteam has decided to use heated water that already contains dissolved air. Since the solubility of gases decreases as temperature increases, such water should behave as supersaturated [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html). The Spring 2019 experimentally evaluated this approach, as described in the Methods section. The subteam intends to progress to quantitative evaluation of the apparatus, and to iterate improvements.

The subteam began to use dissolved oxygen probes to measure the difference in concentration of dissolved oxygen between the influent and effluent water. The subteam expected that the water's dissolved oxygen content is proportional to the water's dissolved air content, since the major source of the dissolved oxygen is air. Therefore, the system's effectiveness in removing dissolved oxygen should be proportional to the system's effectiveness in removing dissolved air. After fixing the current issues with the dissolved oxygen probes, and subsequent analysis of concentration data, the subteam will modify the system to optimize the removal of excess dissolved gas.

The remainder of this report includes further explanation of concepts such as fluidized beds and considerations of pressure, details of the experimental apparatus, and discussions of the experiments that the Spring 2019 subteam performed .

## Literature Review
The subteam concentrated its research on optimizing the system's fluidized bed reactor and manipulating pressure to ensure maximum dissolved gas removal. The subteam’s research can be summarized as follows: gas solubility decreases with decreasing ambient pressure. Therefore, to catalyze bubble growth in a reactor for ease of gas removal, the subteam aimed to design a reactor exerting minimal pressure on gas molecules. Such pressure can be controlled by altering the reactor’s height, by influencing bubble size, and by modifying dimensions of the tubing in the system. Pressure control, combined with providing nucleation sites in a fluidized bed reactor, helps the dissolved gas form stable bubbles that escape from the surrounding water. The subteam hypothesizes that such a reactor design can be developed to alleviate the problems that the plants at El Poda, Nicaragua and Tamara, Honduras are facing.

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
The subteam plans to evaluate the apparatus's effectiveness by measuring the difference in dissolved oxygen content between the influent and effluent water. As stated in the Introduction, the subteam expects that the water's dissolved oxygen content is proportional to the water's dissolved air content, since the major source of the dissolved oxygen in influent water is air.  To encourage bubbles to form in the reactor and to simulate the behavior of supersaturated influent water, the subteam plans to utilize the relationship between gas solubility and temperature.

The subteam considered using, as influent, heated water that already contains dissolved air. Since the solubility of gases decreases as temperature increases, such water should behave as supersaturated [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html).

<p style="text-align: center;">
<img src="https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/section_17/67558bdc4beb64e06b29db7b4c8d74bb.jpg" height=350>

</p>

**Figure 5**: The above graph displays the solubility (mg / 100 g water) of five gases as a function of temperature (C) at a partial pressure of 1 atm [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html).

As illustrated by Figure 5, oxygen and nitrogen are less soluble in water as temperature increases. As described in the Methods section, the subteam began to evaluate the change in gas solubility at different temperatures, by evaluating differences in bubble formation.

### Analysis of Literature
Through conceptual analysis and algebraic manipulation, Equations 3-7 combine to form an estimation of a gas’ solubility in water in the subteam's prototype apparatus. The following paragraphs describe this process. All relevant variables have been defined in the Literature Review section.

The pressure relevant to Henry's Law (i.e. the pressure of a gas above a liquid, in [Equation 3](#Equation-3)) is the pressure *within* a bubble [(Averill & Eldredge)](https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/s17-04-effects-of-temperature-and-pre.html).
$$ C = k P $$

Since $P$ equates to the gas's pressure within a bubble, $P$ is relabeled as $P_b$.

As [Equation 7](#Equation-7) shows, the pressure within a bubble is directly related to the bubble's radius, the liquid's surface tension, and the pressure outside the bubble [(Hyperphysics)](http://hyperphysics.phy-astr.gsu.edu/hbase/surten2.html).

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

[Equation 9](#Equation-9), supplemented by [Equation 1](#Equation-1) concerning fluidization velocity, informed the subteam's fabrication of the prototype apparatus. In the subteam's work, the equation may be used to perform optimizations once the subteam has gathered sufficient experimental data.

## Previous Work

The Fall 2018 subteam's work comprised research, design, fabrication, and basic experimentation to begin development of a reactor to remove excess dissolved gas from influent water in AguaClara plants.

The subteam's research focused on developing a fluidized bed reactor that would encourage bubble formation by providing bubble nucleation sites. The subteam gathered literature on the relevant concepts such as fluidization, bubble nucleation, and gas solubility. As detailed in the Analysis of Literature section, the subteam combined key variables to derive [Equation 9](#Equation-9) for the approximate solubility of a gas in water.

The subteam then experimentally determined relevant system parameters (eg. sand bed porosity and sand grain diameter), and designed and fabricated a small-scale fluidized bed reactor. Python code was developed to facilitate easy calculation of the fluidization velocity and fluidization flow of the sand bed. Python code was also written to calculate the head loss through the reactor's effluent tubing. This code is provided in the Manual section.

After fabricating the prototype system, the subteam ran basic tests to determine its functionality. The reactor's sand bed failed to consistently fluidize while using a 100 RPM peristaltic pump. However, the Spring 2019 subteam recently acquired a 600 RPM peristaltic pump to incorporate into the system.

Further specifics concerning the subteam's work during the Fall 2018 semester are described in the [Fall 2018 Final Report](https://github.com/AguaClara/Dissolved-Gas/blob/master/Research%20Reports/Final_Report.md).

The subteam looks forward to testing the prototype to confirm its functionality, optimize its performance, and to eventually develop a practical reactor.

## Methods

### Experimental Apparatus

The Fall 2018 subteam fabricated a prototype fluidized bed reactor and assembled an accompanying system. The Spring 2019 subteam modified this system to its current form, as Figure 3 shows. The Methods section of the [Fall 2018 Final Report](https://github.com/AguaClara/Dissolved-Gas/blob/master/Research%20Reports/Final_Report.md) details the fabrication of the reactor itself, and describes procedures to determine the reactor's parameters. This included calculation of the fluidized bed's fluidization velocity, and the corresponding flow rate of influent water. The Methods and Manual sections of this report detail the accompanying system and changes made in the Spring 2019 semester.

In summary: the reactor is a 0.5 m transparent PVC pipe, capped with components that allow influent and effluent connections with clear flex tubing. The reactor contains a 70 mL bed of Silica sand. Figure 6 depicts the reactor separately from the system, prior to installation of a pressure sensor.

Readers should note that a mesh screen is installed at the bottom of the reactor to prevent any sand from falling down/out of the reactor. Figure 8 in the [Fall 2018 Final Report](https://github.com/AguaClara/Dissolved-Gas/blob/master/Research%20Reports/Final_Report.md) further depicts the mesh.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype_1/Prototype1_Sand.jpg?raw=true" height=450>

</p>

**Figure 6**: The above photograph shows the Prototype 1 reactor labeled with the Fall 2018 subteam members' names and with the appropriate influent (white) and effluent (red) tape labels. The reactor contained a silica sand bed (green circle).

The system design surrounding the reactor aligned with that illustrated below in Figure 7. The design was as follows: from the water source (a sink), water flowed into a pressure regulator, which decreased water pressure in order to prevent leakage in the tubing system.

As stated in the Literature Review section, the subteam considered using heated water to act as supersaturated influent water, since water that is saturated with air, once heated, becomes supersaturated [(Florida State University)](https://www.chem.fsu.edu/chemlab/chm1046course/solubility.html).

Water then flowed out of the pressure regulator, through clear flex tubing, and forked into two streams: one flowed into a flow accumulator containing a temperature probe, and the other flowed into a peristaltic pump. Water flowing through the peristaltic pump continued through a tube system and into the fluidized bed reactor. The reactor's sand bed is fluidized by the influent water, which travels at no slower than the sand’s fluidization velocity. This corresponded to a flow rate of 2.54 mL/s, as calculated using the [Python code](###Determining-the-Sand-Bed's-Fluidization-Flow) given in the Manual **[Where did this come from? Could you link or reference? Also, it shows up as a link in the markdown file.]**. The influent water's flow rate was controlled manually via the peristaltic pump. As supersaturated water flowed through the reactor, excess air particles in the water would ideally accumulate on the sand grains and form bubbles. Such bubbles then departed from their nucleation sites, flowed upward out of the reactor (through the effluent tubing), and flowed into a bucket. While effluent water flowed out of the reactor, a pressure sensor connected to ProCoDA recorded the pressure difference between the reactor's interior and the outside atmosphere. The bucket into which effluent water empties acts as the open-faced vent for air bubbles to escape into the atmosphere.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Schematic_20190427.jpg?raw=true" height = 450>

</p>

**Figure 7**: The above is diagram is a schematic of the current apparatus, as described in the above paragraphs. Black arrows represent the flow of water.

#### Pressure Regulator Installation

A pressure regulator was installed between the sink and the peristaltic pump to maintain consistent flow pressure of influent water.

The pressure regulator (Figure 8) was oriented such that the direction of water flow matched the arrow on the apparatus. The influent side was connected to the sink using a piece of 3/8" diameter hard plastic tubing. The effluent side was connected to the peristaltic pump using the piece of clear flex tubing that was attached to the pump. The flow pressure of water was reduced by tightening the screw and nut on the top of the pressure regulator, until no leakage occurred when peristaltic pump was turned off.  

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype2/PressureRegulator_20190404.jpg?raw=true" height = 300>

</p>

**Figure 8**: The above photograph depicts the pressure regulator installed prior to the peristaltic pump. Water (purple arrow)**[Is the influent not entering from left to right?]** enters the regulator from the sink, and passes through to continue to the peristaltic pump and flow accumulator.

#### Forked Flow System Installation

The subteam needed a way to measure the temperature (and eventually the dissolved oxygen content) of the influent water before it entered the reactor. The subteam installed a forked flow system in which some influent water, incoming from the pressure regulator, was diverted into a separate container before reaching the peristaltic pump. The temperature of the diverted water could be measured in this container. This model was chosen to avoid inadvertently changing any properties of the influent water during measurement. Specifically: a dissolved oxygen probe consumes oxygen in the process of measuring its concentration. If a dissolved oxygen probe were used to measure dissolved oxygen content of influent water that then flowed into the reactor, the dissolved oxygen content actually present in the reactor would be lesser.

To fabricate the forked flow system, a 0.75" hole was drilled near the bottom of a 500 mL Nalgene bottle. A 1.6” hole was drilled near the top of the bottle. This hole was used to insert a tapered push-to-connect into the bottle, since the push-to-connect was too large to fit through the neck of the bottle. The larger 1.6” hole was then plugged to prevent leakage. The push-to-connect was oriented such that its tapered end protruded from the hole near the bottom of the Nalgene. It was secured with a washer. The resulting apparatus, a flow accumulator, is Figure 9 shows.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype2/FlowAccumulator1_SideBySide.jpg?raw=true" height=300>

**Figure 9**: The above are two photographs of the flow accumulator, as discussed in the above paragraphs.

Two pieces of clear flex tubing were then connected to either side of a T push-to-connect, labeled A and B in Figure 10 below. The peristaltic pump influent tube (labeled C) was then connected to the T push-to-connect such that it was perpendicular to the two shorter pieces of clear flex tubing. One end of the short clear flex tubing (labeled A) was connected to the peristaltic pump and the other end (labeled B) was attached to the push-to-connect of the Nalgene bottle.

<p style="text-align: center;">
<img src="https://raw.githubusercontent.com/AguaClara/Dissolved-Gas/master/Images/Prototype2/FlowFork_Aerial_20190313edited.jpg" height=300>

**Figure 10**: The above is a bird's-eye view of the portion of the apparatus in which flow diverts between the flow accumulator and the peristaltic pump.

**[Instead of explaining everything first and then plopping some images below the explanation for the reader to figure out, could you weave the image into your explanation to make it more seamless? Use your figures effectively.]**

#### Flow Accumulator Modifications

The subteam modified the influent flow accumulator so that it could be drained easily and longer tests could be run. A 1/2" hole was drilled on the side of the flow accumulator opposite the influent push-to-connect, about half-way up the bottle. A piece of clear flex tubing was inserted into this hole and guided into a large bucket on the floor.

The subteam added a second flow accumulator in order to measure the temperature and dissolved oxygen concentration of the effluent water. To construct the effluent flow accumulator, a second 500 mL Nalgene bottle was obtained and a 5/16” hole was drilled approximately 5 cm from the bottom of the container.  A piece of clear flex tubing was inserted into this hole and guided to another large bucket on the floor.

The subteam realized that there was a difference in depth between the water in both flow accumulators at equilibrium, an experimental oversight that decreased the precision of the dissolved oxygen probes measurements. The subteam decided to modify the effluent flow accumulator to eliminate this variable.

The depth of water at equilibrium in the influent flow accumulator was approximately 15.75 cm, measured from the bottom of the 500 mL Nalgene bottle to the surface of the water when the pump was running. The subteam acquired a new 500 mL Nalgene for the effluent flow accumulator and drilled a hole the same height (15.75 cm) from the bottom of the Nalgene. The original effluent flow accumulator was discarded and the new one was connected in its place, obtaining the setup seen in Figure 3.

Additionally, the subteam realized that it would need a way to visually verify that the membrane of the dissolved oxygen probes were free of bubbles before beginning experiments. The subteam used a bandsaw to remove the top of  each flow accumulator, such that the dissolved oxygen probe membrane could be viewed clearly, as Figure 11 shows below.

<p style="text-align: center;">
<img src="https://raw.githubusercontent.com/AguaClara/Dissolved-Gas/master/Images/Accumulator_20190425.jpg" height=300>

**Figure 11**: This figure shows the modified flow accumulator after removing the top of the Nalgene bottle

#### Temperature Probe Installation

The subteam needed to monitor the temperature of the influent and effluent flow for two main reasons. First, the subteam’s hypothesis relied on the idea that supersaturated water could be obtained by increasing its temperature. Therefore, measuring the temperature of the influent flow was integral to determining if supersaturation had been achieved. Secondly, the subteam needed to confirm that the temperature remained the same on average throughout the experiment. In other words, a change in temperature between when the water entered the system and when the water exited the system would create uncertainty in the results. This is because any observed change in dissolved oxygen content could then be attributed to either a change in temperature or to bubble formation by the fluidized bed.  

Two temperature probes were obtained and connected to the ProCoDa box. One temperature probe was labeled ‘influent’ and the other ‘effluent’ before being placed in their respective flow accumulators.

#### Pressure Sensor Installation

The subteam hypothesized that a decrease in pressure inside the reactor would decrease the solubility of the gas and therefore encourage bubble formation. The subteam installed a pressure sensor near the top of the reactor to monitor this pressure difference between the inside of the reactor and atmospheric pressure. Figure 12 displays this.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype2/PressureSensor_Diagram.jpg?raw=true" height = 350>

</p>

**Figure 12**: The above diagram depicts the reactor (green rectangle) and the inserted pressure sensor (orange line).

To install the pressure sensor, the reactor was first emptied of sand and water. The PVC pipe comprising the reactor was tapped with a 1/4" 18NPT pipe tap about 70 cm from the influent end of the reactor. A 1/4" push-to-connect was wrapped with Teflon tape and threaded into the tapped aperture to form a water-tight seal.

The negative end of the pressure sensor was inserted into a piece of 1/4" hard tubing. The connection between the hard tubing and the pressure sensor was sealed with medium clear PVC cement. The other end of the hard tubing was inserted into the 1/4" push-to-connect. The pressure sensor was then plugged into the ProCoDA box at the subteam's work station, such that pressure data could be collected via ProCoDA.

**[It's really weird because it seems like you refer to your figures prematurely and then they pop up later in the report and don't refer to them in the text that the figure is actually buried in. If you need those figures earlier, put them earlier. If you want to keep them where they are, could you make them useful where they are put?]**

#### Dissolved Oxygen Probe Installation

Two dissolved oxygen probes were acquired to measure the dissolved oxygen concentration of both the influent and effluent water. A membrane cap was installed on each probe and each probe was calibrated according to standard procedures described by the [Environmental Engineering Laboratory Research Textbook](https://monroews.github.io/EnvEngLabTextbook/Gas_Transfer/Gas_Transfer.html), under 'Install the Membrane Cap on the Dissolved Oxygen Probe' and 'Calibrate the Dissolved Oxygen Probe,' respectively. Care was taken such that no bubbles were trapped inside of the membrane, as this would prohibit the probes from giving accurate readings. The probes were numbered 1 and 2 and connected to the ProCoDa box. Probe 1 was assigned to the influent flow accumulator and Probe 2 was assigned to the effluent flow accumulator.

### Experimental Procedure

#### Testing Bubble Formation Qualitatively

Using the [ProCoDA method file](#ProCoDa-Method-File) given in the Manual, the subteam determined that an RPM of 41.1 was necessary to fluidize the reactor. To ensure fluidization, the subteam decided to conduct experiments at 60 RPM, a relatively arbitrary flow rate that will be subject to further consideration in the future.

On March 10, the subteam conducted brief, qualitative experiments to determine if the fluidized bed successfully promoted bubble formation. The subteam also structured the tests to qualitatively show differences between bubble formation at different temperatures of influent water.

Six experimental trials were conducted. Each trial began with the flow accumulator being empty. Influent water was introduced to the system and pumped through the reactor at 60 RPM. The influent water's temperature was monitored during each trial using a temperature probe inserted in the flow accumulator. The pressure difference between the interior and exterior of the reactor was measured with the pressure sensor installed in the reactor. Temperature and pressure data was recorded with ProCoDA and the average, standard deviation, and percent standard deviation for each trial was calculated.

The subteam intended to test bubble formation at two relatively extreme temperatures: the warmest and the coolest temperatures provided by the laboratory sink serving as the water source. To this end, the subteam ran three trials while the sink supplied warm water, and three trials while the sink supplied cool water.  

During each trial, video recordings of the fluidized bed were taken using Smartphone cameras. Bubble formation was visually analyzed from these videos, which are provided in the Results and Analysis section. Once the flow accumulator filled with water, the experimental trial ended, and data collection halted.

##### Testing Wider Temperature Ranges

The subteam repeated the experiment from March 10 using a wider temperature range, in order to see a more discernible difference between bubble formation in cold and supersaturated water.
The subteam achieved a wider temperature range by running the sink with either hot or cold water for several minutes before beginning data collection. Additionally, this allowed water already present in the reactor to equilibrate to the new temperature.

For reference, the subteam determined the hottest and coldest temperatures that the laboratory sink could produce. This was done by recording the temperature of the influent water for several minutes until it approached a constant value. This test was repeated 3 times for both hot and cold water, and the equilibrium temperatures were averaged.

### Testing Dissolved Oxygen Removal Quantitatively

Having observed the formation of bubbles in the reactor using supersaturated water, the subteam began experiments to quantitatively determine if the fluidized bed successfully removed dissolved oxygen from the influent flow.  

Both temperature probes were connected to the ProCoDa box and placed in the influent and effluent flow accumulators respectively. Cold water was run through the apparatus for several minutes at a rate of 70.0 RPM until the temperature of the influent and effluent water equilibrated. The flow rate of the peristaltic pump was increased from the 60.0 RPM used in the qualitative bubble formation tests to increase the fluidization of the sand bed. The approximate pressure difference between the inside of the reactor and atmospheric pressure was recorded.

Only four probes could be connected to the ProCoDa box simultaneously. The subteam chose to disconnect the pressure sensor and instead connect both dissolved oxygen probes under the assumption that the pressure difference between the interior of the reactor and atmospheric pressure would remain relatively constant for a given RPM.

The subteam recorded the temperature and dissolved oxygen concentration of the influent and effluent water in the flow accumulators for approximately five minutes. This entire process was repeated for hot (supersaturated) water.

### Testing Dissolved Oxygen Probe Functionality

Initial quantitative experiments testing the removal of dissolved oxygen by the fluidized bed reactor showed that the dissolved oxygen concentration of the effluent water was higher than the dissolved oxygen concentration of the influent water. The subteam suspected that a faulty dissolved oxygen probe or incorrect probe calibration was the source of these results.

The subteam tested the functionality of the dissolved oxygen probes by taking a reading while holding them in air. A correctly functioning probe would record a voltage of -0.17 V (the voltage is negative due to backwards wiring in the probe itself). As an additional test, the subteam used the same probe to measure the dissolved oxygen concentration in both the influent and effluent flow accumulators while the peristaltic pump was running at 70.0 RPM. The subteam compared these dissolved oxygen concentration readings to see if the effluent concentration was still higher than the influent concentration, as observed previously.

### Testing Pressure Difference versus Flow Rate

The subteam observed that the pressure difference between the interior of the reactor and atmospheric pressure fluctuated when the flow rate was changed. The subteam ran a brief experiment to explore this relationship. Starting at 30.0 RPM, the subteam recorded the pressure difference between the interior of the reactor and atmospheric pressure as flow rate was increased. The RPM of the peristaltic pump was increased by 5.0 RPM approximately every 30 seconds, to a maximum of 100.0 RPM. This gradual increase in RPM gave the pressure sensor reading enough time to settle.

The following section of the report presents a discussion of the experimental data.

## Results and Analysis

### Testing Bubble Formation Qualitatively
 **[You don't need to say this. We know you analyzed stuff. This is the analysis section.]**

**Table 1**: Displays data collected during Trials 1 through 6 of the experiments performed on March 10. This includes: experiment duration (s), average pressure difference between the exterior and interior of the reactor (Pa), the average temperature of influent water (C), and corresponding standard deviations. Full data records can be found on [this site](https://docs.google.com/spreadsheets/d/1TsF6WTH7_1kZF3rtxQfxWHmNm25GDSTorC64Gjq5S7U/edit?usp=sharing). After the March 10 experiments, all further analysis was performed using Python code.

|              Trial               |    1    |    2    |    3    |    4    |    5    |    6    |
|:--------------------------------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|     Approximate duration (s)     |   25    |   25    |   25    |   25    |   15    |   15    |
| Average pressure difference (Pa) | 5971.72 | 5065.84 | 3758.40 | 4134.08 | 3601.98 | 3452.05 |
|        Standard deviation (Pa)        |  98.46  | 423.64  | 189.06  | 299.66  |  10.31  |  11.74  |
| Percent standard deviation in pressure| 1.65        | 8.36        |5.03         |7.25  | 0.29   | 0.34        |
| Average temperature (C)      |  22.05  |  19.91  |  18.63  |  33.03  |  35.79  |  36.85  |
|        Standard deviation (C)        |  0.42   |  0.33   |  0.19   |  1.65   |  0.36   |  0.50   |
|    Percent standard deviation in temperature    |  1.89   |  1.65   |  1.03   |  4.98   |  1.01   |  1.35   |

As Figure 13 shows, bubbles formed in the fluidized bed. This demonstrated the basic feasibility of encouraging bubble growth with a fluidized bed. However, between Trials 1-3 and Trials 4-6, there were no consistent, visible differences in bubble formation. Figures 12 and 13 exemplify this, and all full-length videos can be found on [this site](https://drive.google.com/drive/folders/1bybRun4xh5kzI4QvrN0ZPXhFWCMlhZhN?usp=sharing). While the effect of temperature on gas solubility was not the focus of the subteam's work, it was a concept the subteam considered leveraging to design the experimental apparatus, to simulate input of supersaturated water.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Gifs/march10_trial1.gif?raw=true" height = 300>
</p>

**Figure 13**: The image above displays a clip from the recording of Trial 1.


<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Gifs/march10_trial4.gif?raw=true" height = 300>
</p>

**Figure 14**: The image above displays a clip from the recording of Trial 4.

Despite the approximate ten degree temperature difference between Trials 1-3 and Trials 4-6, there was no significant difference observed in the quantity or the size of bubbles generated in the fluidized bed.

This can potentially be explained after a quick analysis of Figure 5.

<p style="text-align: center;">
<img src="https://2012books.lardbucket.org/books/principles-of-general-chemistry-v1.0/section_17/67558bdc4beb64e06b29db7b4c8d74bb.jpg" height=350>

</p>

Recall **Figure 5** from the Literature Review section. While Figure 5 assumes a partial pressure of 1 atm of the gas of interest, this analysis considers the qualitative principles that the figure illustrates.

In Figure 5, in the range of 20 to 30 C (the approximate range of experimental temperatures for Trials 1-6), the percent difference in solubility of oxygen and nitrogen (the primary components of air) is relatively small. As temperature increases from 20 to 30 C, a 50% increase in temperature, oxygen's solubility drops from approximately 4.3 to 3.5 mg / 100 g $H_2O$, an approximately 18% decrease in solubility. Such a difference in solubility may not have visible consequences for bubble formation.

To observe an appreciable difference in bubble formation in the fluidized bed, a greater temperature difference between trials may have been required. For instance, over the range 10 to 40 C, oxygen's solubility shifts from approximately 5 to 3 mg / 100 g $H_2O$, a percent change of 40%. This percent change is twice that which characterized Trials 1-6, and such a difference may have provided more distinguishable results.

An alternative explanation was the following experimental oversight. At the time of these experiments, only the temperature of influent water was recorded. The temperature of influent water measured at the first flow accumulator was irrelevant if this temperature was not approximately that of the water which passed through the reactor.

The subteam also observed that, with the exception of Trial 6, percent standard deviation in temperature decreased as the influent water's temperature reached extremes relative to the trials' conditions. This suggested that the temperature of each trial's influent water had begun to plateau, but had not yet reached extreme values of the laboratory sink's potential temperatures.

#### Testing Wider Temperature Ranges

When two temperature probes were installed in the system, the temperature of the influent versus effluent water was measured to be relatively consistent across the system. As Figure 15 shows, after an initial ladjustment period, influent and effluent temperatures reached relatively stable levels of 43 and 41 C, respectively.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/temperaturevtime_20190319trial3.png?raw=true" height=350>

</p>

**Figure 15**: Displays temperature (C) versus time (Mins) of the influent and effluent samples of water in the system. The graph was generated using [this Python code](https://github.com/AguaClara/Dissolved-Gas/blob/master/Code/Temperature_Difference_Graph.py).

Such results showed that the water's temperature passing through the fluidized bed was changing appreciably and predictably between trials.

In the video recordings of new trials at more extreme temperatures, there was a marked difference in bubble formation between flow of warm and cool water. Figure 16 shows bubble formation while cool water, at approximately 15 C, was pumped through the reactor. Figure 17 shows bubble formation while warm water, at approximately 35 C, was pumped through the reactor.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Gifs/Cold_Water_20190326.gif?raw=true" height=300>

</p>

**Figure 16**: The image above displays a clip from a recording of cool water (at approximately 15 C) flowing through the reactor on March 26.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Gifs/Hot_Water_20190326.gif?raw=true" height=300>

</p>

**Figure 17**: The image above displays a clip from a recording of warm water (at approximately 35 C) flowing through the reactor on March 26.


There was markedly more bubble formation while warm water flowed through the reactor. These results justified the subteam’s experimental procedure, as introduced in the Introduction: pumping heated water through the reactor would help encourage bubble formation, mimicking the behavior of supersaturated influent water.

### Testing Dissolved Oxygen Removal Quantitatively

When the subteam tested influent versus effluent concentration of dissolved oxygen (i.e. DO), the dissolved oxygen probes measured seemingly impossible results. The effluent DO content was measured to be higher than the influent DO content. Figure 18 displays the results of one experimental trial from April 12.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/DOconcentrationvtime_20190412.png?raw=true" height = 350>

</p>

**Figure 18**: The graph above displays dissolved oxygen concentration (mg / L) versus time (Mins) of the influent and effluent samples of water in the system. The graph was generated using [this Python code](https://github.com/AguaClara/Dissolved-Gas/blob/master/Code/Dissolved_Oxygen_Difference_Graphreal.py).

Barring the possibility of a leak, this result should have been impossible, since no oxygen should have entered the system between the inlet and outlet. However, the subteam considered that oxygen bubbles may have formed on the membranes of the DO probes and skewed the probes' measurements. As Figure 19 shows, bubbles were found on the membranes.


<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/MembraneBubbles_20190427.jpg?raw=true" height = 350>

</p>

**Figure 19**: The above photograph shows bubbles (circled in red) that had formed on the membranes of a DO probe.

Bubbles present on the probe membranes likely influenced experimental results. The probes probably interpreted the bubbles as areas of high concentration of oxygen. To avoid problems due to bubble accumulation on the probe membranes, the subteam to opened the tops of the flow accumulators, such that the membranes would be visible and the subteam could manually keep them clear of air bubbles.

### Testing Dissolved Oxygen Probe Functionality
To continue troubleshooting due to the apparently impossible experimental results concerning the change of DO content across the system, the subteam checked the voltage output of each DO probe while exposed only to air. One probe output -0.17 V, while the other output -0.05 V. According to specifications provided by Dr. Weber-Shirk, this indicated that the second probe was malfunctioning, as it should have output -0.17 V while exposed only to air. This result suggested another contributing factor to the strange experimental measurements.

### Testing Dissolved Oxygen Content with Only One Probe
When the subteam used the remaining functional probe to test influent versus effluent DO content, the impossible results persisted, though to a smaller degree. Figure 20 shows these results.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/DOconcentrationvtime_20190423.png?raw=true" height = 350>

</p>

**Figure 20**: The above graph displays dissolved oxygen concentration (mg/L) versus time (Mins) in the samples of water from the system. Influent was measured from 0 to 1.5 minutes; effluent was measured from 1.5 minutes onward. The graph was generated using [this Python code](https://github.com/AguaClara/Dissolved-Gas/blob/master/Code/Dissolved_Oxygen_Difference(1_probe)\_Graphreal.py).

The subteam hypothesized that the persisting issues may have arisen from issues concerning the pressure within the reactor, which the next section of the report discusses.

### Testing Pressure Sensor Consistency

The pressure difference between the interior and exterior of the reactor was not measured to be a consistent value. The subteam had expected that the pressure difference between the interior and exterior of the reactor would be positive. As in, the interior of the reactor would be at a lower pressure than the atmospheric pressure, so as to encourage bubble growth (as discussed in the Analysis of Literature section). However, the subteam found that with increasing flow rates, the pressure difference decreased and became negative. Figure 21 displays this trend.

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/pressurevtime_20190423.png?raw=true" height = 350>

</p>

**Figure 21**: The above graph displays the pressure difference (cm) across the reactor's surface versus time (Mins) while flow rate increased. The graph was generated using [this Python code](https://github.com/AguaClara/Dissolved-Gas/blob/master/Code/Pressure_vs_time(varying_flow_rate).py).

While the pressure difference was relatively consistent at any given flow rate (as visible in the graph's step-like shape), the pressure difference was clearly dependent on flow rate.

The subteam hypothesized that this dependence was due to increasing head loss in the effluent tubing as flow rate increased. As [Equation 5](#Equation-5) shows, head loss increases with flow rate. Recalling that the pressure sensor measures $P_{atm} - P_r$ (i.e. the reactor's internal pressure subtracted from atmospheric pressure),  [Equation 8](#Equation-8) may be rearranged to show:

####Equation 10

$$P_{atm} - P_r = \rho g \Delta h - \rho g h_f$$


As [Equation 10](#Equation-9) shows, increasing head loss (i.e. $h_f$) leads a decreased measured pressure difference. This relationship explained the data shown in Figure 21. The subteam had not considered the effect of the flow rate on the head loss, or its effect on the pressure within the reactor. This was an experimental oversight. The Conclusions section addresses the subteam's solution to this mistake.

## Conclusions
The experimental procedure of using heated water was demonstrated to be valid. Hotter water seemed to encourage more bubble growth than cold water, and thus seemed an adequate experimental substitute for room-temperature supersaturated water. Videos demonstrated that the reactor encouraged bubble growth, and that temperature remained relatively consistent across the apparatus. Together, these aspects built a strong case for continuing experiments with this reactor prototype.

The subteam measured higher effluent dissolved oxygen content than influent dissolved content. While troubleshooting, the subteam found that the pressure difference across the reactor surface was heavily dependent on influent flow rate. The subteam decided that a new effluent tube would be necessary:  in order to minimize effluent head loss (c.f. [Equation 4](#Equation-4)) using a wider effluent tube from the reactor would result in a lower effluent water velocity, and help to minimize head loss, and hopefully reduce the dependency of the pressure difference on the flow rate through the reactor.

The subteam also concluded that one of the dissolved oxygen probes used in the experimental apparatus was malfunctioning.

However, given further results, there was another, yet unknown factor that is skewing the results; it may be a system failure, such as an unseen leak.

## Future Work
The subteam will need to obtain a new, working dissolved oxygen probe, and to replace the effluent tubing of the reactor so as to minimize the dependency of the pressure gradient on head loss. The subteam will also continue to troubleshoot to determine the issue with the DO probe measurements.

In upcoming semesters, the subteam will continue to run tests to pinpoint areas in which the reactor can improve.

First, the subteam will consider running a pure control test: measuring the dissolved oxygen in influent versus effluent water when the reactor contains no sand. Hypothetically, the difference would be negligible, and this could serve as a satisfying benchmark for demonstrating the fluidized bed’s effectiveness in removing dissolved oxygen.

The subteam has qualitatively demonstrated that bubbles do form within the fluidized bed reactor. This suggests that the premise of using a fluidized bed to encourage bubble formation and to remove excess dissolved air from water is plausible.

The subteam also will consider using a camera set-up to obtain consistent video recordings of experiments, to avoid error and uncertainty due to variables such as hand movement. Also, switching out the temperature probe for a new one, considering that the one the subteam has used is not the latest model.

The subteam should also consider in the future to add a flow accumulator directly after the peristaltic pump in order to dampen oscillations from the peristaltic pump. Such an addition would result in consistent water flow going into the reactor.

As mentioned in the Methods section, the experimental setting of 60 RPM for the peristaltic pump was relatively arbitrary, albeit being sufficiently above the fluidized bed's fluidization velocity. The subteam will consider optimizing flow rate, and will consider the entrainment velocity of the fluidized bed, so as to clearly delineate the minimum and maximum flow rates acceptable for experimental trials.

After system improvements, the subteam will progress to more thorough, quantitative analysis of the prototype. The subteam will continue to use dissolved oxygen probes to determine the difference in concentration of dissolved oxygen between the influent and effluent water. After analysis of concentration data, the subteam will modify the system to optimize the removal of dissolved gas. The subteam will experimentally determine what ways the reactor can be modified to increase removal of DO, whether it is exploring different substances, or trying an alternative reactor structure to encourage bubble formation. Research the effect of varying velocities on effectiveness of the apparatus; research ways to encourage larger bubble size; research ideal dimensions of the reactor; research the effect on the apparatus of non-gaseous contaminant on the effectiveness of the reactor.

The subteam must also consider the end goal of scaling up the prototype. The prototype's method to remove excess dissolved gas from influent water must feasibly apply on a practical scale. As part of this end goal, as pertaining to a fluidized bed reactor, the subteam must evaluate the validity of the calculated fluidization flow of the sand bed, and the validity of the calculated entrainment velocity. In order to reliably scale up a fluidized bed reactor, these values must be reliably calculable.

The subteam looks forward to further experimentation and iteration to analyze and improve the system, and to eventually develop a practical reactor.

**[Sometimes when you mention other sections in your report, you link them and other times you don't. Either way, could you keep it consistent?]**

# Manual

### Special Components

#### Pressure Regulator

A pressure regulator is a device that manages the flow pressure of a fluid. The subteam utilized this device to decrease the flow pressure of the water supply (sink). This allowed for the flow rate of the influent water to be stopped when the peristaltic pump is stopped.

The specifications of the Pressure Regulator are as follows:

Company: B&G
Part Number: 110192
Model Number: FB-38
Max Press: 125 PSI
Max Temp: 225°F
Set At: 12 lbs

A 26" piece of hard plastic tubing with 3/8" diameter was used to connect the reducing valve to the sink. The other side of the pressure regulator was connected directly to the influent tubing.

### Experimental Methods

#### Determining the Porosity of Silica Sand

The porosity of silica sand was needed to calculate the sand bed's fluidization velocity ([Equation 1](#Equation-1)). The procedure used to determine the porosity of the silica sand used in the reactor is based on the procedure outlined by [Worth, 2018](https://socratic.org/questions/how-do-scientists-measure-the-porosity-of-soil). The equation for determining porosity may be verified by dimensional analysis in comparison with the equation found in the source: [Department of Chemical Engineering, 2017](http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf).

To see this procedure in more depth visit [Fall 2018 Final Report](https://github.com/AguaClara/Dissolved-Gas/blob/master/Research%20Reports/Final_Report.md).

#### Determining the Average Diameter of Silica Sand Grains

The average diameter of the silica sand grains was needed to calculate the sand bed’s fluidization velocity ([Equation 1](#Equation-1)). The subteam used the following procedure to approximate the average diameter of the sand grains.

1. Acquire a sample of silica sand and a digital caliper.
2. Randomly select a number of sand grains, preferably greater than or equal to ten, from the sample.
3. Using the caliper, measure each sand grain’s diameter three times to account for the grains’ asymmetrical natures. Record these measurements.
4. Compute the average diameter for all sand grains in the sample.

#### Measuring Pipe Dimensions

The prototype fluidized bed reactor was comprised of a transparent PVC pipe containing a silica sand bed, modified with components specified in the Fabrication Manual.

In order to find more information regarding the set-up and measurements of the pipe dimensions please visit [Fall 2018 Final Report](https://github.com/AguaClara/Dissolved-Gas/blob/master/Research%20Reports/Final_Report.md).

#### Evaluating Bubble Formation

This experiment was described in the [Methods section](#Experimental-Procedure).

**Setting up the Temperature Probe and Pressure Sensor**
1. Configure the temperature probe and pressure sensor as directed by the procedure laid out in the [AguaClara Tutorial Wiki](https://aguaclara.github.io/aguaclara_tutorial/research/procoda.html), beginning with the line "Connect a sensor".

**Setting up the Dissolved Oxygen Probes**
1. Configure the dissolved oxygen probe as directed by the procedure laid out in the [Environmental Engineering Lab Textbook](https://monroews.github.io/EnvEngLabTextbook/ProCoDA/ProCoDA.html#heading-procoda-dissolved-oxygen), under ProCoDA, Dissolved Oxygen, beginning with the line "Dissolved oxygen diffuses".

Note: Make sure that there are no bubbles present in the membrane of the DO Probe, as this will negatively impact the DO readings.

**Optional Precaution**
1. Obtain a hammer. If the fluidized bed does not fluidize, but instead begins to travel up the reactor as a single unit, use the hammer to tap against the PVC pipe and disperse the sand bed as necessary.

**Conducting the Experiment**
1. Assemble the flow system, as shown in Figure 7 and described in the [Experimental Apparatus](#Experimental-Apparatus) section.
2. Ensure that the flow accumulator is empty.
3. Ensure that the fluidized bed reactor is filled with water.
4. Set the peristaltic pump to the desired RPM, but ensure that it has not started pumping.   
5. Turn on the sink to start supplying water to the system.
6. Making sure that the data is being saved where appropriate. Do this under Data Directory Path.
7. Press data-log button on ProCoDA to begin recording pressure, temperature data, and Dissolved Oxygen. If done correctly, a green light will appear.
8. Turn on the peristaltic pump, such that water begins to be pumped through the reactor.
9. Press comment button on ProCoDA, and write "start Trial X" to denote that experimental trial X has begun. In this case, "X" is some arbitrary label for the trial.
10. Begin to record a video of the fluidized bed, using a Smartphone.
11. When the flow accumulator is full of water, press data-log button on ProCoDA to stop recording data.
12. Write "stop Trial X" to denote that experimental trial X has ended.
13. Stop taking the video of the fluidized bed.
14. Turn off the peristaltic pump.
15. Empty the flow accumulator.
16. If no more experimental trials are to be conducted, turn off the sink.

**Cleaning Procedure**
The experiments are really low maintenance and easy to wrap up.

1. Turn off the peristaltic pump.
2. Close off water supply.
3. Disconnect the flex tubing used for influent water from the water supply.

### Fabrication Manual

#### Materials required
1. PVC pipe of approximately 0.5 m length and 1 in. diameter, whose ends are labeled with opposing colors of tape, as Figure 6 shows. This is described further in the Measuring Pipe Dimensions section of the Manual.
2. A fine wire mesh
3. Approximately 70 mL of silica sand, measured with a graduated cylinder.
4. Circular hose clamps
5. 3/16-inch diameter clear flex tubing
6. 3/8-inch diameter clear flex tubing
7. Size 18 Masterflex tubing
8. 600 RPM peristaltic pump
9. Barbed fittings & push-to-connect components
10. Access to a sink containing a push-to-connect nozzle
11. A plastic bucket
12. 200 kPa pressure sensor
13. ProCoDA Box
14. 1/4" hard tubing (for the pressure sensor)
15. Teflon tape
16. 1/4 " Threaded push-to-connect component
17. 1/4 " 18NPT Pipe Tap
18. Medium clear PVC cement
19. 500 mL Nalgene container
20. 1 'T' push-to-connect 3/8" SK266-001 with O-ring and Washer
21. 1 Tapered Threaded push-to-connects 3/8" NSF-51 45 SK266-001
22. 2 pieces clear flex tubing (0.76 outer diameter, 0.70 inner diameter) approximately 7 inches long
23. Two copies of the following pipe-tubing connector component:
24. Two Large containers
25. Two Long clear flex tubing

<p style="text-align: center;">
<img src="https://github.com/AguaClara/Dissolved-Gas/blob/master/Images/Prototype_1/PipeConnector1.jpg?raw=true" height=250
</p>

**Figure 22**: The above flow connector enables the reactor (pipe) to be connected to clear flex tubing.

#### Fabrication

Fabrication instructions for the fluidized bed reactor are provided in the [Fall 2018 Final Report](https://github.com/AguaClara/Dissolved-Gas/blob/master/Research%20Reports/Final_Report.md).


##### Installing the pressure sensor
1. Empty the reactor of sand. Ensure that the wire mesh remains at the bottom of the reactor.
2. Use a 1/4" 18NPT Pipe Tap to tap the pipe 70 cm from its bottom (influent) end. Tap the aperture. Thread a push-to-connect component into the tapped aperture, with the connection made watertight with Teflon tape.
3. Insert 1/4" hard tubing into the connector. Insert the negative end of the pressure sensor into the exposed tubing, sealing with medium clear PVC cement.
4. Pour the 70 mL of sand into the pipe, such that it settles on the mesh.
5. Fasten the second copy of the flow component (Figure 15) to the effluent (top) end of the reactor.
6. Mount the pipe on the 80/20 arm using circular clamps, screwed tight around the reactor.
7. Connect the 200 kPa pressure sensor to the ProCoDA box.

##### Fabricating the Flow Accumulator
1. Using a 3/4" hole saw, drill a hole near the bottom of the 500 mL Nalgene container.
2. Use a 1.6" hole saw to drill a hole near the top of the same 500 mL Nalgene.
3. Insert threaded push-to-connect into the upper hole of Nalgene container.
4. Orient the push-to-connect until it is protruding from the 3/4" (lower) hole, with the narrower side facing outwards.
5. Secure the push-to-connect to the Nalgene container with the washer.
6. Put the  plug in the upper hole of the Nalgene container.
7. Use a Bandsaw to cut off the top of the Nalgene container

Note: The second hole was made in order to insert the push-to-connect inside the Nalgene container (i.e. flow accumulator). The Bandsaw was used in order to have more space to place the different probes (Temperature and Do probes).

##### Assembling the flow system
1. Connect Size 18 Masterflex tubing to the Peristaltic Pump.
2. Connect 3/8-inch diameter clear flex tubing from the sink to the influent end of the Peristaltic Pump.
3. Connect 3/16-inch diameter clear flex tubing from the effluent end of the peristaltic pump to the influent end of the reactor.
4. Cut approximately 2.7 m of 3/16-inch diameter clear flex tubing. Connect this to the effluent (upper) end of the reactor, and lead it down into the bucket.
5. Connect the 2 pieces of clear flex tubing to either side of the T push-to-connect such that they are oriented 180 degrees of each other.
6. Connect the influent tube to the third side of the T push-to-connect, such that it is perpendicular to the 2 7" clear flex tubing.
7. Attach one end of the short clear flex tubing to the peristaltic pump. Attach the other end of the short clear flex tubing to the push-to-connect of the Nalgene container.




## ProCoDA Method File **[Not Done]**

This was used to correlate the RPM of the peristaltic pump to the flow rate in mL/s. **[Could you upload the method file and actually link it here?]**

###States
- *OFF*: The peristaltic pump is off.
- *Running*: The peristaltic pump is running.

###Set Points
- *OFF*: This setpoint is used to turns all outputs off.
- *ON*: This setpoint turns on the peristaltic pump on.
- *PumpOutput*: This setpoint is used to turn on the peristaltic pump at the correct number of RPMs to achieve the desired flow rate, given the Tubing ID.

###Variables
- *FlowRate*: This variable is the desired flow rate. In the subteam's reactor, this represents the fluidization velocity.
- *TubingID*: This variable represents the ID associated with tubing being used, based on the diameter of the tubing.

For the experiment described in the Methods section, the following values were used:
- PumpOutput: 41.1 RPM
- FlowRate: 2.54 mL/s
- Tubing ID: 18

## Python Code

### Determining the Sand Bed's Fluidization Flow

The subteam used the following code, copied from the file FluidizationVelocity.py found on the subteam's [GitHub page](https://github.com/AguaClara/Dissolved-Gas/tree/master/Code)  **[link it]**, to estimate the fluidization velocity and fluidization flow of the sand bed in the prototype reactor. The code is based on [Equation 1](#Equation-1). The code requests as input: the reactor's cross-sectional area; the kinematic viscosity of water at a particular temperature (e.g. room temperature); the sand's porosity, which the subteam experimentally determined; silica sand's density; the average diameter of the sand grains, which the subteam measured. The code outputs the velocity and flow of water required to fluidize the sand bed.

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
