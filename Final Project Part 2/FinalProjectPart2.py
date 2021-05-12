#Santiago Landaverde
#1856681

import csv
from operator import itemgetter


mfl = []
prl = []
sdl = []


with open("ManufacturerList.csv") as manlist:
    ml = csv.reader(manlist)
for line in ml:
    mfl.append(line)

with open("PriceList.csv") as pricelist:
    pl = csv.reader(pricelist)
for line in pl:
    prl.append(line)

with open("ServiceDatesList.csv") as sdlist:
    sl = csv.reader(sdlist)
for line in sl:
    sdl.append(line)

new_mfl = (sorted(mfl, key=itemgetter(0)))
new_prl = (sorted(prl, key=itemgetter(0)))
new_sdl = (sorted(sdl, key=itemgetter(0)))

for x in range(0, len(new_mfl)):
    new_mfl[x].append(prl[x][1])

for x in range(0, len(new_mfl)):
    new_mfl[x].append(sdl[x][1])

final_list = new_mfl

full_inventory = (sorted(final_list, key=itemgetter(1)))

with open('FullInventory.csv', 'w') as newfile:
    fiwrite = csv.writer(newfile)

for x in range(0, len(full_inventory)):
    fiwrite.writerow(full_inventory[x])


item_type = final_list
tower_list = []
laptop_list = []
phone_list = []

for x in range(0, len(item_type)):
    if item_type[x][2] == "tower":
        tower_list.append(item_type[x])
    elif item_type[x][2] == "phone":
        phone_list.append(item_type[x])
    elif item_type[x][2] == "laptop":
        laptop_list.append(item_type[x])


with open('LaptopInventory.csv', 'w') as newfile:
    liwrite = csv.writer(newfile)

for x in range(0, len(laptop_list)):
    liwrite.writerow(laptop_list[x])

with open('PhoneInventory.csv', 'w') as newfile:
    piwrite = csv.writer(newfile)

for x in range(0, len(phone_list)):
    piwrite.writerow(phone_list[x])

with open('TowerInventory.csv', 'w') as newfile:
    tiwrite = csv.writer(newfile)

for x in range(0, len(tower_list)):
    tiwrite.writerow(tower_list[x])



damagedlist = []

for x in range(0, len(item_type)):
    if item_type[x][3] == "damaged":
        damagedlist.append(item_type[x])

damagedlist = (sorted(damagedlist, key=itemgetter(4), reverse=True))

with open('DamagedInventory.csv', 'w') as newfile:
    diwrite = csv.writer(newfile)

for x in range(0, len(damagedlist)):
    diwrite.writerow(damagedlist[x])


user_manuf = str(input("Enter your manufacturer: "))

user_type = str(input("Please enter your item type: "))

your_item = []


while (user_manuf != "q"):
    for x in range(0, len(final_list)):
        if user_manuf in final_list[x] and user_type in final_list[x]:
            your_item.append(final_list[x])

    if len(your_item) != 0:
        your_item = sorted(your_item, key=itemgetter(4), reverse=True)
        print("Your Item is: ", your_item[0])
    else:
        print("No such item in Inventory")

    user_manuf = str(input("Enter your manufacturer, or q to exit query:"))

    user_type = str(input("Please enter your item type: "))
