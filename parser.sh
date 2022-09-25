#!/bin/bash

## Get price of Pirkka from PirkkaAPI

raw_price=$(curl https://kamppp-food-api-t8ayp.ondigitalocean.app/pirkka/price)
echo $raw_price | sed 's/[^0-9.]*//g' 

