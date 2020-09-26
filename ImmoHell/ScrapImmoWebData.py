from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import time
import random
from random import randint
from datetime import datetime


log = open("immoweb_log.txt", "a")

try :
    with open("immoweb_house_links.txt", "r") as file :
        immo_links = file.read().splitlines()
except:
    texte="An error append with the document"
    print(texte)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log.write(current_time+" : "+texte+'\n')

###Property###
property_type=[] #(House/apartment)
property_subtype=[] #(Bungalow, Chalet, Mansion, ...)
bedroom_number=[]
bathroom_number=[]
habitable_surface=[]
room_number=[]
has_basement=[]
has_lift=[]
has_garden=[]
garden_surface=[]
toilet_number=[]
has_swimming_pool=[]
has_terrace=[]
terrace_surface=[]
fireplace_number=[]

###Location###
region=[]
locality=[]
post_code=[]
street=[]
number=[]

###Building###
condition=[]
construction_year=[]
facade_number=[]
floor_number=[]


###ConstructionPermit
buildable_floor_surface=[]

###Kitchen
kitchen_type=[]

###Land
land_surface=[]

###Sale
is_furnished=[]
cadastral_income=[]

###Price
price_type=[]
price=[]
price_additional_value=[]

json_error = 0

try :
    for link in immo_links :

        url=link

        time.sleep(1)
        r = requests.get(url)
        
        print(url, r.status_code)
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log.write(current_time +" : "+url+"  [STATUS CODE = "+str(r.status_code)+"]"+'\n')
        
        
        soup = BeautifulSoup(r.content,'html.parser')

        script = soup.find("div", id="container-main-content")
        script = script.find_next("script")
        text_script = str(script)
        start = text_script.find("{")
        end =  text_script.rfind("}")
        text_script = text_script[start:end+1]
        # cut_texte = texte.lstrip('{') why doesn't works ????
        
        try :
            immo_object = json.loads(text_script)
        except :
            
            texte ="Problems to load the Json datas from :" + url
            print(texte)
            
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log.write(current_time+" : "+texte+'\n')   
            json_error += 1 


    ###Property### 
        
        ###Type
        try :
            property_type.append(immo_object["property"]["type"])
        except :
            property_type.append(None)

        ###SubType
        try :
            property_subtype.append(immo_object["property"]["subtype"])
        except :
            property_subtype.append(None)

        ###BedroomNumber
        try :
            bedroom_number.append(immo_object["property"]["bedroomCount"])
        except :
            bedroom_number.append(None)
        
        ###BathroomNumber
        try :
            bathroom_number.append(immo_object["property"]["bathroomCount"])
        except :
            bathroom_number.append(None)

        ###NetHabitableSurface
        try :
            habitable_surface.append(immo_object["property"]["netHabitableSurface"])
        except :
            habitable_surface.append(None)

        ###RoomNumber
        try :
            room_number.append(immo_object["property"]["roomCount"])
        except :
            room_number.append(None)

        ###HasBasement
        try :
            has_basement.append(immo_object["property"]["hasBasement"])
        except :
            has_basement.append(None)

        ###HasLift
        try :
            has_lift.append(immo_object["property"]["hasLift"])
        except :
            has_lift.append(None)   

        ###HasGarden
        try :
            has_garden.append(immo_object["property"]["hasGarden"])
        except :
            has_garden.append(None)

        ###GardenSurface
        try :
            garden_surface.append(immo_object["property"]["gardenSurface"])
        except :
            garden_surface.append(None)

        ###ToiletNumber
        try :
            toilet_number.append(immo_object["property"]["toiletCount"])
        except :
            toilet_number.append(None)
        
        ###HasSwimmingPool
        try :
            has_swimming_pool.append(immo_object["property"]["hasSwimmingPool"])
        except :
            has_swimming_pool.append(None)

        ###HasTerrace
        try :
            has_terrace.append(immo_object["property"]["hasTerrace"])
        except :
            has_terrace.append(None)

        ###TerraceSurface
        try :
            terrace_surface.append(immo_object["property"]["terraceSurface"])
        except :
            terrace_surface.append(None)

        ###FireplaceCount
        try :
            fireplace_number.append(immo_object["property"]["fireplaceCount"])
        except :
            fireplace_number.append(None)


    ###Location###
        
        ###Region
        try :
            region.append(immo_object["property"]["location"]["region"])
        except :
            region.append(None)

        ###Locality
        try :
            locality.append(immo_object["property"]["location"]["locality"])
        except :
            locality.append(None)

        ###PostalCode
        try :
            post_code.append(immo_object["property"]["location"]["postalCode"])
        except :
            post_code.append(None)

        ###Street
        try :
            street.append(immo_object["property"]["location"]["street"])
        except :
            street.append(None)
        
        ###Number
        try :
            number.append(immo_object["property"]["location"]["number"])
        except :
            number.append(None)

    ###Building###

        ###Condition
        try :
            condition.append(immo_object["property"]["building"]["condition"])
        except :
            condition.append(None)

        ###ConstructionYear
        try :
            construction_year.append(immo_object["property"]["building"]["constructionYear"])
        except :
            construction_year.append(None)

        ###FacadeNumber
        try :
            facade_number.append(immo_object["property"]["building"]["facadeCount"])
        except :
            facade_number.append(None)

        ###FloorNumber
        try :
            floor_number.append(immo_object["property"]["building"]["floorCount"])
        except :
            floor_number.append(None)

    ### ConstructionPermit ###
        
        ### TotalBuildableGroundFloorSurface
        try :
            buildable_floor_surface.append(immo_object["property"]["constructionPermit"]["totalBuildableGroundFloorSurface"])
        except :
            buildable_floor_surface.append(None)

    ### Kitchen ###

        ###KitchenType
        try :
            kitchen_type.append(immo_object["property"]["kitchen"]["type"])
        except :
            kitchen_type.append(None)

    ### Land ###

        ###LandSurface
        try :
            land_surface.append(immo_object["property"]["land"]["surface"])
        except :
            land_surface.append(None)

    ### Transaction ###

    ### Sale ###

        ###IsFurnished
        try :
            is_furnished.append(immo_object["transaction"]["sale"]["isFurnished"])
        except :
            is_furnished.append(None)

        ###CadastralIncome
        try :
            cadastral_income.append(immo_object["transaction"]["sale"]["cadastralIncome"])
        except :
            cadastral_income.append(None)

    ### Price ###

        ###Type
        try :
            price_type.append(immo_object["price"]["type"])
        except :
            price_type.append(None)

        ###Price
        try :
            price.append(immo_object["price"]["mainValue"])
        except :
            price.append(None)

        ###PriceAdditionalValue
        try :
            price_additional_value.append(immo_object["price"]["additionalValue"])
        except :
            price_additional_value.append(None)

finally:
    log.close()

    data_frame= pd.DataFrame({'Property type':property_type})
    data_frame['Property subtype']=property_subtype
    data_frame['Bedroom number']=bedroom_number
    data_frame['Bathroom number']=bathroom_number
    data_frame['Habitable surface']=habitable_surface
    data_frame['Room number']=room_number
    data_frame['Has basement']=has_basement
    data_frame['Has lift']=has_lift
    data_frame['Has garden']=has_garden
    data_frame['Garden surface']=garden_surface
    data_frame['Toilet number']=toilet_number
    data_frame['Has swimming pool']=has_swimming_pool
    data_frame['Has terrace']=has_terrace
    data_frame['Terrace surface']=terrace_surface
    data_frame['Fireplace number']=fireplace_number
    data_frame['Region']=region
    data_frame['Locality']=locality
    data_frame['Post code']=post_code
    data_frame['Street']=street
    data_frame['Number']=number
    data_frame['Condition']=condition
    data_frame['Construction year']=construction_year
    data_frame['Facade number']=facade_number
    data_frame['Floor number']=floor_number
    data_frame['Buildable floor surface']=buildable_floor_surface
    data_frame['Kitchen type']=kitchen_type
    data_frame['Land surface']=land_surface
    data_frame['Is furnished']=is_furnished
    data_frame['Cadastral income']=cadastral_income
    data_frame['Price type']=price_type
    data_frame['Price']=price
    data_frame['Price additional value']=price_additional_value

    data_frame.index.name = "Id"
    data_frame.to_csv('Scrap_immoHELL_data.csv', index=True)

    print("Number of Json error during the scraping : " + str(json_error))