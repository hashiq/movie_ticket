vox ={
    "karuppu":{
    "Cast": ["Suriya","Indratrance"]
}
    }

for key , value in vox.items():
    for actor in value["Cast"]:
        print(actor)