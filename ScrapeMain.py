import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from lxml import etree
import urllib.request as urllib2
from urllib.request import Request, urlopen
from decimal import Decimal   
from _ScrapeEvolutionTypes import *


#This module will scrape the pokemons actual page

#url = 'https://pokeassistant.com/pokedex/3?locale=en'
urlprefix = 'https://pokeassistant.com/pokedex/'
urlsuffix = '?locale=en'

pokemon_image_prefix = 'https://pokeassistant.com'


start_pokemon = 1
last_pokemon = 10043  #493



while(start_pokemon <= last_pokemon):
    url = urlprefix + str(start_pokemon) + urlsuffix

    

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req)

    htmlparser = etree.HTMLParser()
    page_tree = etree.parse(webpage, htmlparser)

    poke_name = page_tree.xpath('/html/body/div/div[2]/div/div')
    poke_name = ''.join(poke_name[0].itertext()).strip()
    print("poke_name: ", poke_name, "      poke_number: ", start_pokemon)


    poke_img = page_tree.xpath('/html/body/div/div[3]/div[1]/div[1]/div/div/div[1]/img') 
    poke_img = pokemon_image_prefix + poke_img[0].get("src").strip()
    print("poke_img: ", poke_img)

    poke_type1 = page_tree.xpath('/html/body/div/div[3]/div[1]/div[2]/div/a[1]/div')
    poke_type1 = ''.join(poke_type1[0].itertext()).strip()
    print("poke_type1: ", poke_type1)
    
    poke_type2 = page_tree.xpath('/html/body/div/div[3]/div[1]/div[2]/div/a[2]/div')
    poke_type2 = ''.join(poke_type2[0].itertext()).strip()
    print("poke_type2: ", poke_type2)

    poke_gen = page_tree.xpath('/html/body/div/div[5]/div/div[1]/span')
    poke_gen = ''.join(poke_gen[0].itertext()).strip()
    print("poke_gen: ", poke_gen)

    poke_buddy_candy = page_tree.xpath('/html/body/div/div[5]/div/a/div/span')
    poke_buddy_candy = ''.join(poke_buddy_candy[0].itertext()).strip()
    print("poke_buddy_candy: ", poke_buddy_candy)


    poke_catch_rate = page_tree.xpath('/html/body/div/div[5]/div/div[2]/span')
    poke_catch_rate = ''.join(poke_catch_rate[0].itertext()).strip()
    print("poke_catch_rate: ", poke_catch_rate)

    
    poke_fast_moves_contained = page_tree.xpath('/html/body/div/div[7]/div/div[1]')
    poke_fast_moves_list_contained =  poke_fast_moves_contained[0].findall("a")
    
    
    for index in range(0, len(poke_fast_moves_list_contained)):
        fast_move_damage = Decimal(''.join(poke_fast_moves_list_contained[index].find("div").find("div").find("div").itertext())) #conversion may cause error
        move_damage_list = ''.join(poke_fast_moves_list_contained[index].find("div").find("div").itertext()).replace("\n", "").replace("\t", "").strip().split(" ")
        legacy_fast_move = True if "remtrue" in poke_fast_moves_list_contained[index].find("div").find("div").get('class') else False

        move = " ".join(move_damage_list[1:]) 
        
        print("Lagacy?: ", legacy_fast_move, "    Fast Damage: ", fast_move_damage,"      Move: ", move)


    poke_charge_moves_contained = page_tree.xpath('/html/body/div/div[7]/div/div[2]')
    poke_charge_moves_list_contained =  poke_charge_moves_contained[0].findall("a")

    for index in range(0, len(poke_charge_moves_list_contained)):
        charge_move_damage = Decimal(''.join(poke_charge_moves_list_contained[index].find("div").find("div").find("div").itertext())) #conversion may cause error
        move_damage_list = ''.join(poke_charge_moves_list_contained[index].find("div").find("div").itertext()).replace("\n", "").replace("\t", "").strip().split(" ")
        legacy_charge_move = True if "remtrue" in poke_charge_moves_list_contained[index].find("div").find("div").get('class') else False
        move = " ".join(move_damage_list[1:]).strip() 
        print("Lagacy?: ",legacy_charge_move, "    Charge Damage: ", charge_move_damage,"      Move: ", move)
    
    
    poke_weaknesses = page_tree.xpath('/html/body/div/div[8]/div/div[1]')
    poke_weaknesses_list = poke_weaknesses[0].findall('span')

    for index in range(0, len(poke_weaknesses_list)):
        weakness_type = "".join(poke_weaknesses_list[index].find('div').itertext())
        weakness_amount = "".join(poke_weaknesses_list[index].find('span').itertext())

        print("weakness_type: ", weakness_type, "       weakness_amount:", weakness_amount)


    poke_resistances = page_tree.xpath('/html/body/div/div[8]/div/div[2]')
    poke_resistances_list = poke_resistances[0].findall('span') 
    for index in range(0, len(poke_resistances_list)):
        resistance_type = "".join(poke_resistances_list[index].find('div').itertext())
        resistance_amount = "".join(poke_resistances_list[index].find('span').itertext())

        print("resistance_type: ", resistance_type, "       resistance_amount:", resistance_amount)
    
    
    # formtypes1 = page_tree.xpath('/html/body/div/div[9]')
    # formtypes1_family = formtypes1[0].findall("div")[0].findall("div")[0].findall("a")

    # for index in range(len(formtypes1_family)):
    #     formtype_type1 = "".join(formtypes1_family[index].itertext()).replace("\t", "").replace("\n\n", "").strip().split("\n")
    #     formtype1_poke_link = formtypes1_family[index].get("href")
    #     form_image = []
    #     if formtype_type1[0].strip() != "":
    #         form_image = formtypes1_family[1].findall("div")[0].findall("div")[0].find("img").get("src")
    #     else:
    #         form_image = formtypes1_family[0].find("img").get("src")

    #     print("formtypes1: " + str(formtype_type1) + " "+ formtype1_poke_link + " "+ form_image + " ")


    scrape_type(page_tree, 9)
    scrape_type(page_tree, 10)
    scrape_type(page_tree, 11)



    # poke_evolutions = page_tree.xpath('/html/body/div/div[11]/div/div')
    # evolution_family = [x for x in poke_evolutions[0].findall("div") if len(x.findall("a")) > 0]

    # for index in range(len(evolution_family)):
    #     evolve_num_and_candy = "".join(evolution_family[index].itertext()).replace("\t", "").replace("\n\n", "").split("\n")
    #     print("evolve_num_and_candy: " + str(evolve_num_and_candy))



    
    # poke_type1 = page_tree.xpath('')
    # poke_type1 = page_tree.xpath('')
    # poke_type1 = page_tree.xpath('')
    # poke_type1 = page_tree.xpath('')
    # poke_type1 = page_tree.xpath('')

    print("\n\n")
    start_pokemon += 1

    