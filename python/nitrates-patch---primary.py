# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2024.

import sys, csv, re

codes = [{"code":"3091","system":"gprdproduct"},{"code":"4772","system":"gprdproduct"},{"code":"15582","system":"gprdproduct"},{"code":"2632","system":"gprdproduct"},{"code":"15581","system":"gprdproduct"},{"code":"6336","system":"gprdproduct"},{"code":"9523","system":"gprdproduct"},{"code":"8601","system":"gprdproduct"},{"code":"8289","system":"gprdproduct"},{"code":"9323","system":"gprdproduct"},{"code":"2695","system":"gprdproduct"},{"code":"11585","system":"gprdproduct"},{"code":"3646","system":"gprdproduct"},{"code":"2631","system":"gprdproduct"},{"code":"11189","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('nitrates-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["nitrates-patch---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["nitrates-patch---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["nitrates-patch---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
