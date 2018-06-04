# 1KP

Simple notebook to map taxonomy information onto sequences we retrieve after querying the 1KP database.

You need to supply your email, the output file from 1KP, the xml file from 1KP, a file location for where you want to output 
the cleaned sequences, and whether you want to trim the species (explained below) and add Taxonomy information 
(At the moment we just add the Family, but can add other details if it's needed)



## Trimming the species:

The output headers will look like this -
`>scaffold_SSDU_2044987_Papaver_bracteatum_3_samples_combined_Ranunculales`

The species names sometimes have additional information placed after them (such as the 3_samples_combined in the previous example).
You can specify to include this or not via the trim variable. If you don't want it just set

`trim = True`

Without it the header now looks like -

`>scaffold_SSDU_2044987_Papaver_bracteatum_Ranunculales`

Some of the files don't map to a Family and these will be printed out when the script runs. 
You may wish to manually add these into the sequences. 
Some of them simply had misspelt species names from the 1KP database. 
They are still added to the output file, just without the Family name

So they look like this -

`>scaffold_SSDU_2044987_Papaver_bracteatum`
