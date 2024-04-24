import car

print(dir(car))

#import argparse
#parser = argparse.ArgumentParser(
#description='Test command line parameters')
#parser.add_argument('--file',
#help='file name to work with', required=True)
#args = parser.parse_args()
#print(args.file)


mycar = car.Car()
print("Horn:", mycar.honk)
mycar.set_honk(True)
print("Horn:", mycar.honk)
print("make:", mycar.get_manufacturer())
mycar.set_manufacturer('smart car')
print("make:", mycar.get_manufacturer())
print(dir(mycar))