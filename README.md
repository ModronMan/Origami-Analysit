# Origami-Analyst
Origami analyst is a Framework tool, based off the work of Beveridge and Barran [1] which provides predictive structural data on a protein based off Mass Spectrometry and Ion mobility data provided by the user.
It is still a work in progress and my first project to upload to github, it was set as project by my supervisor for my PhD.
I am a first year PhD student and I am very new to programming.


So far I have completed a GUI for the Collision Cross Section Boundary calculation. How this GUI works is very simple:

1. first you simply import a <filename>.txt of your amino acid sequence, it must be single letter code in upper case.

2. Second click calculate and the program will carry out the calculation to give you your CCSB and output the answers below.

The Kappa parameter [2] which describes an amino acid sequences shape i.e. being compact or extended has been added. This parameter 
is implemented my localCIDER a program developed by localCIDER [3] was developed in the Pappu lab by Alex Holehouse, with additional code by James Ahad and Mary Richardson. Many of the early ideas were pioneered by Dr. Rahul Das.
Kappa ranges: 0 < K < 1, with lower values indicating an extended structure and higher values a more compact one.


References:
[1] R. Beveridge, S. Covill, K. J. Pacholarz, J. M. D. Kalapothakis, C. E. Macphee and P. E. Barran, Anal. Chem., 2014, 86, 10979–     10991.
[2] A. S. Holehouse, R. K. Das, J. N. Ahad, M. O. G. Richardson and R. V Pappu, Biophys. J., 2017, 112, 16–21.
[3] R. K. Das and R. V Pappu, Proc. Natl. Acad. Sci., 2013, 110, 13392–13397

