from .models import IngredientManager, Ingredients
import requests
import json
from xml.dom.minidom import parse, parseString
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
from json import dumps
import re
import xml.etree.cElementTree as et

data=[]
data.append(['Organic Baby Carrots',75640])
data.append(['80% Lean Ground Beef, 1.30 LB',39028])
data.append(['Oven Roasted Chicken Breast - 8 Oz',77351])
data.append(['Garlic Bread In Foil Bag',29149])
data.append(['Organice Garlic',70923])
data.append(['Tomatoes on the Vine',69932])
data.append(['Spaghetti Sauce Seasoning Mix - 1.5 Oz',31855])
data.append(['Spaghetti - 16 Oz',37909])
data.append(['Pure 100% Natural Canola Oil - 48 Fl Oz Plastic Bottle',77828])
data.append(['Oil Extra Virgin Olive Oil - 25.5 Oz',80029])
data.append(['Fine Sea Salt',32430])
data.append(['Ground Black Pepper',32406])
data.append(['Garlic Powder',32512])
data.append(['Seasoned Salt',32526])
data.append(['Soy Sauce',38439])
data.append(['Sesame Oil Pure',38405])
data.append(['Red Fresh Onion - 48 Oz. Mesh Bag',91984])
data.append(['Sweet Fresh Onion - 16 Oz. Mesh Bag',91986])
data.append(['Onion Powder',32522])
data.append(['Chicken Broth',30792])
data.append(['Beef Broth',30775])
data.append(['Tomato Sauce',30306])
data.append(['Parmesan Shredded',80709])
data.append(['Hot Dog Buns',29239])
data.append(['Beef Franks Bun Length',69932])
data.append(['Celery',37362])
data.append(['White Fresh Potato',92029])
data.append(['French Bread Baguette',29176])
data.append(['Tombstone Pepperoni Pizza',82858])
data.append(['Cream Cheese',34058])
data.append(['Grade AA Large Eggs',34337])
data.append(['Cheese Fish Goldfish',73386])
data.append(['Butter Half Sticks',33981])
data.append(['Organic 2% Reduced Fat Milk',34413])
data.append(['All Purpose Flour Enriched Bleached Presifted',70211])
data.append(['Fine Granulated Sugar',31215])
data.append(['Crushed Red Pepper',32342])
data.append(['Honey Crisp Apples',91686])
data.append(['Whole Kosher Dill Pickles',31753])
data.append(['2 LB Pork Shoulder Country Style Ribs',39393])
data.append(['Stubbs Regular Original Barbecue Sauce',73670])
data.append(['Orange Juice',27813])
data.append(['Whole Milk Mozzarella Cheese',34154])
data.append(['Long Grain White Rice',82810])
data.append(['Lettuce Green Leaf',37391])
data.append(['Bold and Spicy Brown Mustard',31437])
data.append(['Easy Squeeze Ketchup',31388])
data.append(['Bagels Plain',72611])
data.append(['Pepperoni Sliced',72611])
data.append(['Dry Yeast',70503])
data.append(['Specialty Herbs And Spices Ground',81493])
data.append(['Clover Honey Bear',70503])
data.append(['Water',0])


def startup():
    for item in data:
        Ingredients.objects.addIngredient(item[0],item[1])
    return True

def replace():
    for item in data:
        url='http://www.SupermarketAPI.com/api.asmx/SearchByItemID?APIKEY=6af0d05f87&ItemId='+str(item[1])
        stores=requests.get(url).content
        stores=re.sub(' xmlns="[^"]+"', '', stores, count=1)
        stores=dumps(bf.data(fromstring(stores)))
        sdata=json.loads(stores)
        pname=sdata['ArrayOfProduct']['Product']['Itemname']['$']
        item[1]=pname
    return True
