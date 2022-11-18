## Chapter 10: files and exceptions

#with open('filepath') as aliasNameForTheFile:
    #line1 = aliasNameForTheFile.readline()
    #line2 = aliasNameForTheFile.readline()
    #line3 = aliasNameForTheFile.readline()

    #all_lines = aliasNameForTheFile.readline()

    #file_content = aliasNameForTheFile.read()

    ## aliasNameForTheFile.close(), no need to close when you read a file
    #starting with "with"

filepath1 = '../data/products.txt'
filepath2 = '../data/sample.txt'


with open(filepath1) as prod_list:
    contents = prod_list.read()
    print("Contents of the file: \n", contents)

with open(filepath1) as prod_list:
    print("now we are trying to loop throught the contents")
    all_lines = prod_list.readlines()
    print(all_lines)

#print('printing the line 5', all_lines[4])

for line in all_lines:
        print(line)

print("****************WRITE file appending new content ******************")
with open(filepath1, 'a') as prod_list:
    prod_list.write('playstation 5\n')
    prod_list.write('learning python book\n')
    prod_list.write('First head to Selenium book\n')
    #check the file contents now

print("****************WRITE file replacing old content with new ******************")
#with open(filepath1, 'w') as prod_list:
    #prod_list.write('spiderman jacket\n')
    #prod_list.write('batman mask\n')
    #prod_list.write('smart tv samsung 70\n')
    #check the file contents now


#H/W: 10-3, 10-4, 10-5

