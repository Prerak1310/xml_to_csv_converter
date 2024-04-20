for record in myroot.findall("row"):
            for col_value in record:
                if col_value.text is None:
                    continue
                else:
                    data_list.append(col_value.text)
            csvwriter.writerow(data_list)
            data_list.clear()