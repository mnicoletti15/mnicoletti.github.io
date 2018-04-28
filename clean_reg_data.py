import csv

with open('census_sorted.csv', 'w') as census, open('regression_data.csv', 'w') as reg_data:

    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

with open("clean_data.csv", "w") as f:
    fileWriter = csv.writer(f, delimiter=',')
    fileWriter.writerow(["GEOID", "TRACTCE", "COUNTYFP", "NAME", "NAMELSAD", "INTPTLAT", "INTPTLON"])



column_names = {
            "Geo_NAME": "Geo_NAME",
            "T002_001": "Total Population",
            "T002_002": "Population Density (Per Sq. Mile)",
            "T002_003": "Area (Land)",
            "T215_002": "15 to 24 Years",
            "T215_003": "25 to 34 Years",
            "T215_004": "35 to 44 Years",
            "T215_005": "45 to 54 Years",
            "T215_006": "55 to 59 Years",
            "T215_007": "60 to 64 Years",
            "T215_008": "65 to 74 Years",
            "T215_009": "75 to 84 Years",
            "T215_010": "85 Years and Over",
            "T104_001": "Median Gross Rent",
            "T013_002": "White Alone (Number of people)",
            "T013_003": "Black or African American Alone",
            "T013_004": "American Indian and Alaska Native Alone",
            "T013_005": "Asian Alone",
            "T013_006": "Native Hawaiian and Other Pacific Islander Alone",
            "T013_007": "Some Other Race Alone",
            "T013_008": "Two or More Races",
            "T014_002": "Not Hispanic or Latino",
            "T014_010": "Hispanic or Latino",
            "T236_001":   "Renter-Occupied Housing Units",
            "T236_002":      "Number of units Less than $300 (monthly)",
            "T236_003":      "$300 to $499",
            "T236_004":      "$500 to $799",
            "T236_005":      "$800 to $999",
            "T236_006":      "$1,000 to $1,499",
            "T236_007":      "$1,500 to $1,999",
            "T236_008":      "$2,000 to $2,499",
            "T236_009":      "$2,500 to $2,999",
            "T236_010":      "$3,000 or More",
            "T236_011":      "No Cash Rent",
            "T145_001":      "Total",
            "T145_002":      "No Health Insurance Coverage",
            "T145_003":      "With Health Insurance Coverage",
            "T145_004":      "Public Health Coverage",
            "T145_005":      "Private Health Insurance"
}