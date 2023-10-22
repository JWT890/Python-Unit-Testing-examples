input_file = open("C:/Users/JW/Desktop/annual rainfall.txt")
out_file = open("toprainfall_places.txt", "w")
count = 0
places = {}
regions = {}
place_regions = {}

header = next(input_file)
print(header, "\n")

for aline in input_file:
    items = aline.split('\t')
    places[items[1].strip()] = int(items[3])
    place_regions[items[1].strip()] = items[4].strip()

sorted_places = sorted(places.items(), key=lambda x: x[1], reverse=True)
columns = header.split('\t')
print('{}\t{}\n'.format(columns[1].strip(), columns[3].strip()))
out_file.write('{}\t{}\n'.format(columns[1].strip(), columns[3].strip()))
for key, value in sorted_places:
    #print(key, ' ', value, end='\n')
    print('{}\t{}'.format(key, value))
    out_file.write('{}\t{}\n'.format(key, value))
input_file.close()
out_file.close()
