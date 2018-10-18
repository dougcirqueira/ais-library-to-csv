# -*- coding: iso-8859-15 -*-


import sys
import pandas as pd
from collections import OrderedDict

reload(sys)  
sys.setdefaultencoding('utf8')

# Filename
filename = "example_exported_data.txt"

# Data to CSV
title_vec = []
author_vec = []
publication_vec = []
year_vec = []
abstract_vec = []

# Read Lines
lines = [line.strip() for line in open(filename, "r").readlines()]

# Variable to control the skip to a next record
count_next_record_lines = 0

# Data
title = ""
author = ""
publication = ""
year = ""
abstract = ""

# Scan lines
for line in lines:
	if line.startswith("%T "):
		title = line[3:]

	elif line.startswith("%A "):
		author += line[3:] + ";"

	elif line.startswith("%B "):
		publication = line[3:]

	elif line.startswith("%D "):
		year = line[3:]

	elif line.startswith("%X "):
		abstract = line[3:]

	elif line == "":
		count_next_record_lines += 1

		if count_next_record_lines > 1:
			count_next_record_lines = 0

			title_vec.append(title)
			author_vec.append(author)
			publication_vec.append(publication)
			year_vec.append(year)
			abstract_vec.append(abstract)

			title = ""
			author = ""
			publication = ""
			year = ""
			abstract = ""


# Save data to a OrderedDict
dataFrameDict = OrderedDict([('publication',publication_vec), ('year',year_vec), ('author',author_vec),
							('title',title_vec), ('abstract',abstract_vec)])

# Export data using pandas
dataFrame = pd.DataFrame(data=dataFrameDict)
dataFrame.to_csv("ais.csv", index=False)
