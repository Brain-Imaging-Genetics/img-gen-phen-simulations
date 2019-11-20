# img-gen-phen-simulations

(JBP) I have found that availability of imaging genetic datasets is very poor, and we often need to validate methods that analyze these kind of data. While there are already existing possible starting points, I would like to take the opportunity of the hackathon to start a clean python package dedicated to the simulation of (genetic, imaging, phenotypes). The package would help authors testing analysis methods under different assumptions, it should therefore be well documented, well tested, easy to install, easy to develop in, and extensible.

The main steps would be
1. generate genomes (or a portion of those)
2. generate “corresponding” brain images
3. generate associated phenotypes  

One key aspect would be to try to develop the code such that it is clean and easily extensible, and useful for a large community. These types of tools are well adapted to common development. Very simple linear generative models should be first developed leaving the possibility of including more complex models later. This could be used to integrate some of Yue’s proposal.

More detailed steps
    - generate N simulated genomes, one per subject. There are different ways of doing this but you can start with very simple assumption about linkage disequilibrium. Look at the tools or packages already available for this. This can build on Yue’s simulations.
    - Generate basic demographic data for these simulated participants
    - generate a functional (fMRI) brain image per participant: start with an existing brain image (eg, find one on Openneuro or Neurovault) and create new subjects by adding gaussian smoothed noise. In a future step, signals specific to demographic data could be added.
    - add signal (a list of x,y,z coordinate) as a function of a list of alleles. Start with a simple linear function, but organize the code such that non linear functions could be developed easily in the future
    - create P phenotypes (for example P=10-20) from brain regions signals. To start, a simple linear generative model, where clinical or behavioural phenotypes are constructed as a linear function of the values in the brain images could be used with random weights.

Note:
Several teams could work in parallel on this: the genome generation, the brain images generation and the phenotype generation could be started in parallel with  well defined inputs and outputs.



