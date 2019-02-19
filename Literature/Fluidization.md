# Sources on Fluidization Parameters

## Source 1: Fluidization: A Unit Operation in Chemical Engineering
#### Citation
Department of Chemical Engineering. (2017, February). *Fluidization: A Unit Operation in Chemical Engineering.* Gainesville, FL: University of Florida. Retrieved from http://ww2.che.ufl.edu/unit-ops-lab/experiments/FB/FB-manual.pdf.

#### Useful Formulas
$$ \epsilon=\frac{V_t-V_p}{V_t} $$
$$ \epsilon=1-\frac{m}{\rho_p A H} $$
$\rho_p =$ density of particles

- The subteam will likely be using Silica sand, which has a density of approximately 2650 kg/m^3.  


$m =$ the total mass of the particles in the bed
$A =$ the cross sectional area of the tube
$H =$ the height of the bed
$\epsilon =$ the porosity of the bed (aka. the bed voidage)
$V_t =$ total volume of the bed $= AH$
$V_p =$ total volume of particles within the fluidized bed $= AH(1-\epsilon)$

This source contains information relating to the minimum fluidization velocity required to fluidized a bed of particles. We will use this information to determine the minimum velocity of influent water in order to fluidize the sand bed in our fluidized bed reactor.

## Source 2: Fluid Mechanics for Fluidized Beds
#### Citation
Thornill, D. (1990). *Fluid Mechanics for Fluidized Beds.* Retrieved from http://faculty.washington.edu/finlayso/Fluidized_Bed/FBR_Fluid_Mech/fluid_bed_scroll.htm.

#### Useful Formulas

$$ g(\rho_s-\rho)=\frac{1.75 \rho u^2}{d \epsilon^3}+ \frac{150 \mu (1-\epsilon)u}{d^2 \epsilon^2} $$

$\rho_s =$ catalyst density
$\rho =$ fluid density
$u =$ fluid velocity
$d =$ particle diameter
$\epsilon =$ void space of the bed (Warning: this is *not* equal to the bed voidage, despite the sources using equivalent symbols)
$\mu =$ fluid viscosity
$g =$ acceleration due to gravity

## Source 3: Bed height and material density effects on fluidized bed hydrodynamics
#### Citation
Guevara, D. E. (2010). *Bed height and material density effects on fluidized bed hydrodynamics* (master’s thesis). Iowa State University, Ames, Iowa. Retrieved from https://lib.dr.iastate.edu/cgi/viewcontent.cgi?article=2653&context=etd

#### Summary of Information

Determined that $U_{mf}$ (minimum fluidization velocty) is increased when the sand density of size is increased.

## Source 4: Filtration Theory
#### Citation
Weber-Shirk, M. *Filtration Theory: On removing little particles with big particles* [PowerPoint Slides]. Retrieved from https://courses.cit.cornell.edu/cee4540/pdf/Filtration.pdf.

#### Useful Formulas
$$ V_{minfl}= \frac{\phi^3 g D^2}{36kv(1-\phi)}(\frac{\rho_s}{\rho_w}-1) $$

$V_{minfl} =$ minimum approach velocity required to fluidize the sand bed
$\phi =$ porosity, $\frac{Volume Of Voids}{Total Volume} = 0.4$ for uniform size media (Note: porosity and voidage are, in this case, equal quantities)
$g =$ acceleration due to gravity
$D^2 =$ diameter of the sand grain, squared
$k =$ Kozeny constant, approximately equal to 5 for most filtration conditions
$\rho_w =$ density of water
$\rho_s =$ density of sand particles
$v =$ kinematic viscosity

$\rho_{SilicaSand} = 2650 kg/m^3$

## Source 5: Densities of Materials
#### Citation
Engineering Toolbox. (2010). *Dirt and Mud - Densities.* Retrieved October 5, 2018, from https://www.engineeringtoolbox.com/dirt-mud-densities-d_1727.html

#### Useful information

$\rho_{sand} =$ 1905 kg/m^3 (wet)

## Source 6: Diameter of a Grain of sand
#### Citation
Price, I. (2000). *Diameter of a Grain of Sand.* Retrieved October 5, 2018, from https://hypertextbook.com/facts/2000/IlanaPrice.shtml

#### Useful information

The diameter of a grain of sand can vary from 0.05mm up to 2 mm, with the average size of .2mm. Sand particles between 0.05mm and 0.2mm in diameter are considered fine sand, and grains of sand with a diameter from .2mm to 2mm are considered coarse.

## Source 7: Viscosity of Water
#### Citation
*Viscosity of Water – Viscosity table and viscosity chart* : Anton Paar Wiki. (2018). Retrieved October 29, 2018, from https://wiki.anton-paar.com/en/water/

#### Useful information
This website tabulates the kinematic viscosity of water at various temperatures.

## Source 8: Process Fluid Mechanics | *Entrainment Velocity*
#### Citation
Denn, M. (1980). Process Fluid Mechanics (pp. 72-73). Upper Saddle River, NJ: Prentice Hall PTR.

#### Useful information
There is a threshold velocity above which a fluidized bed's constituent particles will begin to flow upwards with the fluidizing agent, rather than remaining in suspended fluidization. The following equation (equation 55 in the textbook) solves for this velocity.

$$ v_{max} = \frac{(\rho_{p}-\rho)g D^2_p}{18\eta}$$

$v_{max}$ = entrainment velocity of the fluidized bed
$\rho_{p}$ = density of the fluidized bed's particles
$\rho$ = density of the fluidizing agent
$\eta $ = dynamic viscosity of the fluidizing agent
$D_p $ = average diameter of the fluidized bed's particles
$g $ = acceleration due to gravity
