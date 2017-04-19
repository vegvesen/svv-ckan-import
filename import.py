from ckanapi import RemoteCKAN
import csv

#  ===> How to use this file <===
# 1) If you're importing into a local copy, uncomment the two first lines under Connection information  
#     (the ones containing "localhost") and comment out the next two (with an exernal URL)
# 2) Find the correct API key:
#    - Logg in to the CKAN portal with an account with neccessary credentials
#    - Go to user/admin and find the API-key in the left sidebar
#    and paste it over the "insert-correct-API-key"-text
# 3) Run the script

# ==== Connection information  ==== #

#ua = 'ckanapiexample/1.0 (+http://localhost:5000)'
#create = RemoteCKAN('http://localhost:5000', user_agent=ua, apikey='insert-correct-API-key')
ua = 'ckanapiexample/1.0 (+http://ckan-prod-874300540.eu-west-1.elb.amazonaws.com/)'
create = RemoteCKAN('http://ckan-prod-874300540.eu-west-1.elb.amazonaws.com/', user_agent=ua, apikey='insert-correct-API-key')


# ==== Data import  ==== #

create.action.organization_create(name='statens-vegvesen', title='Statens vegvesen')
print 'Organisasjonen Statens vegvesen opprettet'

file_name = 'package_create.csv'

csv_file = open(file_name, 'rb')
raw_data = csv.DictReader(csv_file, delimiter=';', skipinitialspace=True)

for row in raw_data:
    dataset_dict=row
    print dataset_dict
    # Remember: In create, package name = name, in patch it's id
    create.call_action('package_create',dataset_dict) 
    #create.call_action('package_patch',dataset_dict)

print '------------ Datasett opprettet --------------------'

file_name = 'resource_create.csv'

csv_file = open(file_name, 'rb')
raw_data = csv.DictReader(csv_file, delimiter=';', skipinitialspace=True)

for row in raw_data:
    dataset_dict=row
    print dataset_dict
    create.call_action('resource_create',dataset_dict) 
    
print '------------------ Ressurser opprettet --------------------'

raw_data = [
        {'id': 'trafikkinformasjon' , 'tags': [ {'name': 'trafikk'}]},
        {'id': 'fotoboks' , 'tags': [ {'name': 'trafikk'}]},
        {'id': 'trafikkulykker' , 'tags': [ {'name': 'trafikk'}, {'name': 'statistikk'}]},
        {'id': 'trafikkskilt' , 'tags': [ {'name': 'trafikk'}]},
        {'id': 'vegmeldinger' , 'tags': [ {'name': 'trafikk'}]},
        {'id': 'vardata' , 'tags': [ {'name': 'trafikk'}]},
        {'id': 'kjoretoyopplysninger' , 'tags': [ {'name': 'kjøretøy'}]},
        {'id': 'nybilvelger' , 'tags': [ {'name': 'kjøretøy'}]},
        {'id': 'godkjente-verksteder' , 'tags': [ {'name': 'kjøretøy'}]},
        {'id': 'nasjonal-vegdatabank' , 'tags': [ {'name': 'veg'}]},
        {'id': 'bomstasjoner' , 'tags': [ {'name': 'veg'}]},
        {'id': 'bruer' , 'tags': [ {'name': 'veg'}]},
        {'id': 'bruksklasser' , 'tags': [ {'name': 'veg'}]},
        {'id': 'driftskontrakter' , 'tags': [ {'name': 'veg'}]},
        {'id': 'elveg-vbase' , 'tags': [ {'name': 'veg'}]},
        {'id': 'rasteplasser' , 'tags': [ {'name': 'veg'}]},
        {'id': 'ruteplandata-bil' , 'tags': [ {'name': 'veg'}]},
        {'id': 'skredhendelser' , 'tags': [ {'name': 'veg'}]},
        {'id': 'tunneler' , 'tags': [ {'name': 'veg'}]},
        {'id': 'gravemeldinger-sor-trondelag' , 'tags': [ {'name': 'veg'}]},
        {'id': 'transportloyver' , 'tags': [ {'name': 'trafikant'}]},
        {'id': 'trafikkskoler' , 'tags': [ {'name': 'trafikant'}]},
        {'id': 'trafikkstasjoner' , 'tags': [ {'name': 'trafikant'}]},
        {'id': 'artsmangfold' , 'tags': [ {'name': 'miljø'}]},
        {'id': 'luftkvalitet' , 'tags': [ {'name': 'miljø'}]},
        {'id': 'stoykartlegging' , 'tags': [ {'name': 'miljø'}]},
        {'id': 'vilttiltak' , 'tags': [ {'name': 'miljø'}]},
        {'id': 'nasjonal-verneplan' , 'tags': [ {'name': 'kultur'}]},
        {'id': 'arsrapporter-nokkeltall' , 'tags': [ {'name': 'statistikk'}]},
        {'id': 'norsk-vegmuseum' , 'tags': [ {'name': 'kultur'}]},
        {'id': 'statistikk-sentralbyra' , 'tags': [ {'name': 'statistikk'}]},
        {'id': 'trafikk-statistikk' , 'tags': [ {'name': 'trafikk'}, {'name': 'statistikk'}]}
        ]
    
for row in raw_data:
    dataset_dict=row
    create.call_action('package_patch',dataset_dict)    
    print dataset_dict

print '------------ Stikkord opprettet --------------------'

create.action.group_create(name='eksempler', title='Eksempler', description='Noen datasett som er gode eksempler, verdt å kikke nærmere på')
print 'Gruppe Eksempel opprettet'

raw_data = [ {'id': 'eksempler' , 'packages': [ {'id': 'nasjonal-vegdatabank'}, {'id': 'bruer'}, {'id': 'test'}]} ]
    
for row in raw_data:
    dataset_dict=row
    create.call_action('group_patch',dataset_dict)    
    print dataset_dict

print '------------ Datasett lagt inn i gruppa Eksempel --------------------'

file_name = 'showcase_create.csv'

csv_file = open(file_name, 'rb')
raw_data = csv.DictReader(csv_file, delimiter=';', skipinitialspace=True)

for row in raw_data:
    dataset_dict=row
    print dataset_dict
    create.call_action('ckanext_showcase_create',dataset_dict) 

print '------------ Showcase opprettet --------------------'

file_name = 'showcase_association.csv'

csv_file = open(file_name, 'rb')
raw_data = csv.DictReader(csv_file, delimiter=';', skipinitialspace=True)

for row in raw_data:
    dataset_dict=row
    print dataset_dict
    create.call_action('ckanext_showcase_package_association_create',dataset_dict) 

print '------------ Showcase knyttet til datasett --------------------'

print 'Ferdig!'