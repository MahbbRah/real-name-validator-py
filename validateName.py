from names_dataset import NameDataset
import csv

# m = NameDataset()
# firstNameRes = m.search_first_name('kuddus')
# lastName = m.search_last_name('lever')

# print(firstNameRes, lastName)


with open('data/scraped_results_1615315764360.csv', 'r') as csv_file_input:
    with open('data/scraped_results_1615315764360-out.csv', 'w') as csv_file_output:
        csv_reader = csv.reader(csv_file_input, delimiter=',')
        writer = csv.writer(csv_file_output, lineterminator='\n')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                writer.writerow(row)
                line_count += 1
            else:
                # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                firstAndLastName =  row[0].split()
                m = NameDataset()
                firstNameRes = m.search_first_name(firstAndLastName[0])
                lastName = m.search_last_name(firstAndLastName[1])

                if firstNameRes == True:
                    print("First Name is Valid", firstNameRes)
                    row[1] = firstAndLastName[0]

                if lastName == True:
                    print("last name is valid", lastName)
                    row[2] =  firstAndLastName[1]

                writer.writerow(row)

                # print(firstNameRes, lastName)

                # print(firstAndLastName[0])
                line_count += 1
        print(f'Processed {line_count} lines.')