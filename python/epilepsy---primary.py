# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"F25y000","system":"readv2"},{"code":"F25B.00","system":"readv2"},{"code":"F25C.00","system":"readv2"},{"code":"F255100","system":"readv2"},{"code":"667N.00","system":"readv2"},{"code":"F257.00","system":"readv2"},{"code":"F132111","system":"readv2"},{"code":"F25E.00","system":"readv2"},{"code":"F254000","system":"readv2"},{"code":"8BIF.00","system":"readv2"},{"code":"F25y100","system":"readv2"},{"code":"F25y400","system":"readv2"},{"code":"F25F.00","system":"readv2"},{"code":"F25D.00","system":"readv2"},{"code":"667E.00","system":"readv2"},{"code":"F255500","system":"readv2"},{"code":"F25z.00","system":"readv2"},{"code":"F25z.11","system":"readv2"},{"code":"F256100","system":"readv2"},{"code":"Eu80300","system":"readv2"},{"code":"6674.00","system":"readv2"},{"code":"1O30.00","system":"readv2"},{"code":"F255200","system":"readv2"},{"code":"1473.00","system":"readv2"},{"code":"F258.00","system":"readv2"},{"code":"667B.00","system":"readv2"},{"code":"667M.00","system":"readv2"},{"code":"F25..00","system":"readv2"},{"code":"F254200","system":"readv2"},{"code":"37592.0","system":"readv2"},{"code":"44252.0","system":"readv2"},{"code":"55665.0","system":"readv2"},{"code":"2907.0","system":"readv2"},{"code":"96641.0","system":"readv2"},{"code":"51998.0","system":"readv2"},{"code":"32288.0","system":"readv2"},{"code":"65673.0","system":"readv2"},{"code":"11186.0","system":"readv2"},{"code":"40806.0","system":"readv2"},{"code":"43679.0","system":"readv2"},{"code":"34079.0","system":"readv2"},{"code":"48134.0","system":"readv2"},{"code":"9979.0","system":"readv2"},{"code":"988.0","system":"readv2"},{"code":"36203.0","system":"readv2"},{"code":"26733.0","system":"readv2"},{"code":"49737.0","system":"readv2"},{"code":"24309.0","system":"readv2"},{"code":"49322.0","system":"readv2"},{"code":"71801.0","system":"readv2"},{"code":"39023.0","system":"readv2"},{"code":"59185.0","system":"readv2"},{"code":"55260.0","system":"readv2"},{"code":"68486.0","system":"readv2"},{"code":"105679.0","system":"readv2"},{"code":"4093.0","system":"readv2"},{"code":"34792.0","system":"readv2"},{"code":"37906.0","system":"readv2"},{"code":"27526.0","system":"readv2"},{"code":"56359.0","system":"readv2"},{"code":"4801.0","system":"readv2"},{"code":"26015.0","system":"readv2"},{"code":"3607.0","system":"readv2"},{"code":"45927.0","system":"readv2"},{"code":"22804.0","system":"readv2"},{"code":"37782.0","system":"readv2"},{"code":"18471.0","system":"readv2"},{"code":"30816.0","system":"readv2"},{"code":"45602.0","system":"readv2"},{"code":"23415.0","system":"readv2"},{"code":"22341.0","system":"readv2"},{"code":"49340.0","system":"readv2"},{"code":"38307.0","system":"readv2"},{"code":"55739.0","system":"readv2"},{"code":"4602.0","system":"readv2"},{"code":"108409.0","system":"readv2"},{"code":"9887.0","system":"readv2"},{"code":"7945.0","system":"readv2"},{"code":"37644.0","system":"readv2"},{"code":"73542.0","system":"readv2"},{"code":"23634.0","system":"readv2"},{"code":"31920.0","system":"readv2"},{"code":"68946.0","system":"readv2"},{"code":"26144.0","system":"readv2"},{"code":"65699.0","system":"readv2"},{"code":"30604.0","system":"readv2"},{"code":"98870.0","system":"readv2"},{"code":"69831.0","system":"readv2"},{"code":"9886.0","system":"readv2"},{"code":"71719.0","system":"readv2"},{"code":"4478.0","system":"readv2"},{"code":"3175.0","system":"readv2"},{"code":"31830.0","system":"readv2"},{"code":"99548.0","system":"readv2"},{"code":"59120.0","system":"readv2"},{"code":"99731.0","system":"readv2"},{"code":"9747.0","system":"readv2"},{"code":"9569.0","system":"readv2"},{"code":"8187.0","system":"readv2"},{"code":"573.0","system":"readv2"},{"code":"6271.0","system":"readv2"},{"code":"17399.0","system":"readv2"},{"code":"63826.0","system":"readv2"},{"code":"25330.0","system":"readv2"},{"code":"19170.0","system":"readv2"},{"code":"11394.0","system":"readv2"},{"code":"1715.0","system":"readv2"},{"code":"19363.0","system":"readv2"},{"code":"40105.0","system":"readv2"},{"code":"5525.0","system":"readv2"},{"code":"5152.0","system":"readv2"},{"code":"30635.0","system":"readv2"},{"code":"53483.0","system":"readv2"},{"code":"21885.0","system":"readv2"},{"code":"5117.0","system":"readv2"},{"code":"G40","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('epilepsy-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["epilepsy---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["epilepsy---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["epilepsy---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
