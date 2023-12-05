def parse_input():
    data = open('input.txt',"r").read().split("\n")
    return data

def parse_into_map(block):
    pass

def find_blocks(parsed_input):
    seed_block = []
    seed_to_soil_map = []
    soil_to_fertilizer_map = []
    fertilizer_to_water_map = []
    water_to_light_map = []
    light_to_temperature_map = []
    temperature_to_humidity_map = []
    humidity_to_location_map = []
    
    tmp_header = ""
    for line in parsed_input:
        if "seeds:" in line:
            separated = line.split(" ")
            for i in range(1,len(separated)):
                seed_block.append(int(separated[i]))
            
        if "seed-to-soil map" in line:
            tmp_header = "StS"
            continue
        if "soil-to-fertilizer map" in line:
            tmp_header = "StF"
            continue
        if "fertilizer-to-water map" in line:
            tmp_header = "FtW"
            continue
        if "water-to-light map" in line:
            tmp_header = "WtL"
            continue
        if "light-to-temperature map" in line:
            tmp_header = "LtT"
            continue
        if "temperature-to-humidity map" in line:
            tmp_header = "TtH"
            continue
        if "humidity-to-location map" in line:
            tmp_header = "HtL"
            continue
        line_block = []
        if tmp_header != "":
            for value in line.split(" "):
                line_block.append(int(value))
            if tmp_header == "StS":
                seed_to_soil_map.append(line_block)
            elif tmp_header == "StF":
                soil_to_fertilizer_map.append(line_block)
            elif tmp_header == "FtW":
                fertilizer_to_water_map.append(line_block)
            elif tmp_header == "WtL":
                water_to_light_map.append(line_block)
            elif tmp_header == "LtT":
                light_to_temperature_map.append(line_block)
            elif tmp_header == "TtH":
                temperature_to_humidity_map.append(line_block)
            elif tmp_header == "HtL":
                humidity_to_location_map.append(line_block)
    return seed_block, seed_to_soil_map[1:-1], soil_to_fertilizer_map[1:-1], fertilizer_to_water_map[1:-1], water_to_light_map[1:-1], light_to_temperature_map[1:-1], temperature_to_humidity_map[1:-1], humidity_to_location_map[1:-1]
                    
        
def get_result_from_val(value, description):
    destination = []
    source = []
    length = description[2]
    for i in range(length):
        destination.append(description[0] + i)
        source.append(description[1] + i)
    if value in source:
        return destination[source.index(value)]
    else:
        return value
    
    
            


def main():
    parsed = parse_input()
    seeds, StS, StF, FtW, WtL,LtT,TtH,HtL = find_blocks(parsed)
    for seed in seeds:
        for soil in StS:
            print(get_result_from_val(seed,soil))
   
    pass

if __name__ == "__main__":
    main()