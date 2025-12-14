from flask import Flask, send_from_directory, abort, render_template
import os

## Function and Class
## Function
def callAge(age):
    newAge = age + 1
    print(newAge)

callAge(77)
callAge(90)

class familyMember():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def calcAge(self):
        newAge = self.age + 1
        print(newAge)
        return newAge
    
class HA(familyMember):
    def calcAge(self):
        newAge = self.age + 10
        return newAge



ongTuan = familyMember("Tuan", 90)
DitXanh = HA("HoangAnh", 19)

#print(ongTuan.name, ongTuan.age)
print("Tuoi ong Tuan la: ", ongTuan.calcAge())
print("Tuoi HA la: ", DitXanh.calcAge())
#ongTuan.calcAge()

