#!/usr/bin/env python2.7

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

# Note: This is a file for updating existing data, not importing into an empty installation

# ==== Connection information  ==== #

#ua = 'ckanapiexample/1.0 (+http://localhost:5000)'
#create = RemoteCKAN('http://localhost:5000', user_agent=ua, apikey='insert-correct-API-key')
#ua = 'ckanapiexample/1.0 (+http://ckan-prod-874300540.eu-west-1.elb.amazonaws.com/)'
#create = RemoteCKAN('http://ckan-prod-874300540.eu-west-1.elb.amazonaws.com/', user_agent=ua, apikey='insert-correct-API-key')
# Test-innstallasjonen:
print '------------------ Ressurser oppdatert --------------------'

print 'Ferdig!'