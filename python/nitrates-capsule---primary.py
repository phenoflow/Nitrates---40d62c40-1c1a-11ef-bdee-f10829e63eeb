# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2024.

import sys, csv, re

codes = [{"code":"18964","system":"gprdproduct"},{"code":"24671","system":"gprdproduct"},{"code":"13534","system":"gprdproduct"},{"code":"8428","system":"gprdproduct"},{"code":"12804","system":"gprdproduct"},{"code":"8324","system":"gprdproduct"},{"code":"4609","system":"gprdproduct"},{"code":"776","system":"gprdproduct"},{"code":"44179","system":"gprdproduct"},{"code":"47950","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('nitrates-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["nitrates-capsule---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["nitrates-capsule---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["nitrates-capsule---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)