# Each row should be in a <row></row> tag
# first row should not have any mistakes

import xml.etree.ElementTree as ET
import os
import csv

for filename in os.listdir("./input_files"):
    if filename.endswith(".xml"):
        output_file_name = os.path.splitext(filename)[0]
        with open(
            f"./output_files/{output_file_name}.csv", "w", newline="", encoding="utf-8"
        ) as csvfile:
            csvwriter = csv.writer(csvfile)
            headers = []
            data_list = []
            # creating element tree
            mytree = ET.parse(f"./input_files/{filename}")
            # root tag
            myroot = mytree.getroot()
            # getting all headers for csv file
            for header in myroot[0]:
                headers.append(header.tag)
            csvwriter.writerow(headers)
            # getting all records for csv file
            for record in myroot.findall("row"):
                for col_value in record:
                    if col_value.text is None:
                        continue
                    else:
                        data_list.append(col_value.text)
                csvwriter.writerow(data_list)
                data_list.clear()
    else:
        continue
