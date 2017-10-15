from lxml import etree as ET
from Bio import Entrez
import re

Entrez.email = "ENTER YOUR EMAIL HERE"
fasta = "files/output_small.fasta"
xml = "files/output_small.xml"
output = "files/cleaned.fasta"
trim = False
add_taxonomy = True

class Rename_1KP():

    def __init__(self, fasta, xml, output, trim=True, add_taxonomy=True):
        self.fasta = fasta
        self.xml = xml
        self.output = output
        self.trim = trim
        self.add_taxonomy = add_taxonomy
        self.full_names = {}
        self.taxonomy_dict = {}
        self.tax_id_string = ""

    # Map a species name to a taxonomic ID
    def get_tax_id(self, species):
        species = species.replace(" ", "+").strip()
        search = Entrez.esearch(term = species, db = "taxonomy", retmode = "xml")
        record = Entrez.read(search)
        if len(record['IdList']) == 0:
            print ("Couldn't find taxonomic information for %s \n " % (species))
            return ""
        else:
            return record['IdList'][0]

    # Map a taxonomic ID to the taxonomic information
    def get_tax_data(self, taxid):
        search = Entrez.efetch(id = taxid, db = "taxonomy", retmode = "xml")
        return Entrez.read(search)



    # Create a mapping from short headers to longer headers
    def map_headers(self):
        xml_parsed = ET.parse(self.xml).getroot()
        for itm in xml_parsed.xpath("/BlastOutput/BlastOutput_iterations/Iteration/Iteration_hits/Hit/Hit_def/text()"):
            short_header = itm.split("-")[1] + "-" + itm.split("-")[2]

            # Do we need to trim the trailing information?
            if self.trim:

                self.full_names[short_header] = "-".join(itm.split("-")[0:4])
                species = "-".join(itm.split("-")[3:4])
            else:
                self.full_names[short_header] = itm
                species = "-".join(itm.split("-")[3:])


            # Do we need to create a mapping from species name to taxonomy?
            if self.add_taxonomy:
                trimmed_species = "-".join(itm.split("-")[3:4])

                if (species not in self.taxonomy_dict):
                    tax_id = self.get_tax_id(trimmed_species)
                    self.tax_id_string += "," + tax_id
                    self.taxonomy_dict[trimmed_species] = ""


    def get_taxonomy(self):
        # Remove blank hits and the leading comma
        tax_id_string = re.sub(',,+', ',', self.tax_id_string)[1:]
        data = self.get_tax_data(tax_id_string)

        for x in range(len(data)):
            species = "_".join(data[x]['ScientificName'].split(" "))
            lineage = {species: d['ScientificName'] for d in data[x]['LineageEx'] if d['Rank'] in ['family']}

            self.taxonomy_dict[species] = "_" + lineage[species]


    def write_file(self):

        # Open the output file and replace the shorter header with the longer header
        with open(fasta) as infile, open(output, 'w') as outfile:
            for line in infile:
                if line.startswith(">"):
                    id = line[1:].strip()

                    line = line.replace(id, self.full_names[id]).strip()
                    if self.add_taxonomy:
                        species = "_".join(line.split("-")[3:4]).strip()
                        line += self.taxonomy_dict[species] + "\n"


                outfile.write(line.replace("-", "_"))

rename_1KP = Rename_1KP(fasta, xml, output, trim, add_taxonomy)
rename_1KP.map_headers()
rename_1KP.get_taxonomy()
rename_1KP.write_file()
