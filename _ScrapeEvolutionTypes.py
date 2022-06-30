

def scrape_type (page_tree, divint):
    
    formtypes1 = page_tree.xpath('/html/body/div/div['+  str(divint) + ']')
    formtypes1_family = formtypes1[0].findall("div")[0].findall("div")[0].findall("a")

    if len(formtypes1_family) > 0:
        for index in range(len(formtypes1_family)):
            formtype_type1 = "".join(formtypes1_family[index].itertext()).replace("\t", "").replace("\n\n", "").strip().split("\n")
            formtype1_poke_link = formtypes1_family[index].get("href")
            form_image = []
            if formtype_type1[0].strip() != "":
                form_image = formtypes1_family[1].findall("div")[0].findall("div")[0].find("img").get("src")
            else:
                form_image = formtypes1_family[0].find("img").get("src")

            print("formtypes1: " + str(formtype_type1) + " "+ formtype1_poke_link + " "+ form_image + " ")
    else:
        formtypes1_family = formtypes1[0].findall("div")[0].findall("div")[0]
        formtype_type1 = "".join(formtypes1_family.itertext()).replace("\t", "").replace("\n", "").replace(":", "")

        if formtype_type1 == "Shiny":
            form_image = formtypes1_family.findall("img")[0].get("src")
            print("formtypes2: " + str(formtype_type1) + " "+ form_image + " ")
        else:
            evolution_family = [x for x in formtypes1_family.findall("div") if len(x.findall("a")) > 0]
            for index in range(len(evolution_family)):
                evolve_num_and_candy = "".join(evolution_family[index].itertext()).replace("\t", "").replace("\n\n", "").split("\n")
                print("evolve_num_and_candy: " + str(evolve_num_and_candy))