from os import read
f = open("input.txt")
input = f.readlines()
testCase = [199,
200,
208,
210,
200,
207,
240,
269,
260,
263]
def main1(readings):
    descents, prevReading = 0, None;
    print(readings)
    for reading in readings:
        print(reading)
        print(bool(reading.strip()))
    #     if prevReading is not None and bool(reading.strip()):
    #         if int(reading) > prevReading:
    #             descents += 1

    #     if bool(reading.strip()):
    #         print(reading)
    #         prevReading = int(reading)

    # return descents

# def analyze_depths(measurements):
#     increased = 0
#     prevIndex = None
#     for measurement in measurements:
#         print("measurement following")
#         print(measurement.isnumeric())
#         if measurement.strip():
#             print("measurement following")
#             print(measurement)
#             # if(prevIndex is not None and int(measurement) > prevIndex):
#             #     increased+=1
#             # prevIndex = int(measurement)
      
#     return increased
print(main1(input))