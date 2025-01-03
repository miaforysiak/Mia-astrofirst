This repository has some material for initial exercises for students
starting to perform astrophysics research, and some example material.

The goal of the initial exercises is to introduce you to the data and
to make sure you develop some of the same tools necessary for the
further tasks you will do later.

1. Create your own GitHub repository that mirrors the structure of
this one. You will have to:

 * Create an account on GitHub
 * Create a repository with an informative name related to your project.
 * Clone the repository to your local machine (use 'git clone')
 * Create a directory structure in your working copy mirroring this product's
 * Copy the README files from the directories.
 * Commit the changes (use 'git commit')
 * Push the changes back to GitHub (use 'git push')

2. Make sure you can use your product. If the directory of the root
directory of your product is called , then your shell will have to have:

 * /bin added to its /opt/anaconda3/bin:/opt/anaconda3/condabin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin environmental variable, and
 * /python added to its  environmental variable.

This should happen in your .bashrc file (assuming you are using the
bash shell. If this is done correctly, you should be able to run
2. Make sure you can use your product. If the directory of 
the root
directory of your product is called $PRODUCT_DIR, then your 
shell will have to have:

 * $PRODUCT_DIR/bin added to its $PATH environmental 
variable, and
 * $PRODUCT_DIR/python added to its $PYTHONPATH 
environmental variable.example_script from the command line without 
error.

3. Find, read in, and plot information in an astronomical data file,
within the Jupyter environment. You will use data from the MaNGA
survey.  Figuring out how to do the tasks below will require reading
fairly extensively in the documentation.

 * Read the basic description of MaNGA (note the availability of the technical papers there): https://www.sdss4.org/surveys/manga/
 * Read the description of the catalogs for the survey: https://www.sdss4.org/dr17/manga/manga-data/catalogs/
 * Retrieve the DRPAll file for DR17, and plot the log of the stellar mass versus the redshift. Please:
   - Put the MaNGA data file in a standard directory tree that follows the same form as on the SDSS servers, using the same environmental variables. That means it should live somewhere like /[version]/drpall-[version].fits
   - Use the ELPETRO version of the mass
   - Color the points depending on whether they are Primary, Primary+, Secondary, or Ancillary. You will need to read the documentation to figure out how to do this!
   - Label the figure properly with units!
   - Write out the figure as a PNG file.
   - Send me the PNG.

4. Now you should have a Jupyter notebook which solves the above problem. Convert this into a Python script that you can run independently of a Jupyter notebook. Commit and push the script to GitHub.

5. Perform some calculations on a data file and then write it out as an output FITS file, then plot the results. You can do this the same way as above (Jupyter notebook, then convert to a script) or write it directly as a script.

 * Retrieve the DAPAll file, which you can find on the same page as the DRPAll file above. Again, put it in a similar directory structure as exists on the SDSS servers. 
 * Using the entries that are in both, calculate the log of the H-alpha line
   luminosity. Please:
    - Use the EMLINE_GFLUX_TOT measurement of the H-alpha flux (which has the label 'Ha-6564' in the documentation)
    - If the H-alpha line flux value is zero or negative, or the redshift is zero or negative, exclude it from the calculations
    - Output as a FITS file a table with one row per row of the DAPAll file, in the same order, with enough information to identify each row uniquely and to plot the log of the H-alpha luminosity and the log of the stellar mass.
 * Write a script to read in the output file and make a plot of the log H-alpha luminosity vs the log of the mass.
 * Commit and push the script to GitHub.

6. From your file, select some galaxies with large ratios of H-alpha
to stellar mass, and some with relatively low ratios. Go to the Marvin
web interface for MaNGA and take a look at these galaxies. Think about
the following:

 * Are there trends you can notice between the mass, H-alpha, luminosity,
   and the way the galaxy looks?
 * Look at a few high H-alpha cases. Using the spectrum viewer find
   the H-alpha line at 6563 Angstroms in the rest frame. How does it
   compare to the other lines? How does it vary across the galaxy?
 * Now look at the maps available in the Marvin viewer. There is a
   way to show the H-alpha maps. Again, look at a few cases, and thing
   about the different patterns you see

7. If you are going to be actually working with MaNGA data, you should
now do the following:

 * Retrieve this file: https://data.sdss5.org/sas/sdsswork/sandbox/mnsa/0.3.1/
 * Create a directory on your local machine for MNSA data, set the environmental variable MNSA_DATA, and put the file in the directory /0.3.1
 * Examine the HDUs in this file. You should see that it already has the DRP information stored in its SUMMARY HDU, and the matched Pipe3D outputs in the PIPE3D HDU, and some other information
 * Make sure you can run the script example_plot_absmag. Compare it to the script you wrote. Notice how the script is very simple, and just calls functions to do anything complex. This is good practice for modular code.

These exercises should have built out some of the basic skills
necessary to start asking some *real* questions of the data. There is
still a lot more to learn. Further examples will appear as necessary
in astrofirst.
