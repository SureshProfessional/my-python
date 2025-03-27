Jiva_dada = {
    "valabhai" : {
        "mafabhai": ["nagin","tinabhai"],
        "naranbhai":["ashokbhai","sureshbhai"],
        "dayabhai":["vitthalbhai","vijaybhai"],
        "bhagvanbhai":["ambarambhai","ramjibhai"],
        },
        
    "malabhai" : {
        "devchandbhai":["amratbhai"],
        "punmabhai": ["nagjibhai","pravinbhai"],
        "babubhai":["gopibhai","ashokbhai"],
        "joytabhai":["karnalbhai","prakashbhai"],
        "ishvarbhai":["kamleshbhai","gabrubhai"],  
        },
        
    "raymalbhai" : {
        "bhemabhai": ["sureshbhai","nagjibhai","ishvarbhai",],
        "mafabhai":["arvindbhai","manubhai","sureshbhai"],
        "rameshbhai":["ganeshbhai","havuubhai"],
        },

    "savdasbhai" : {
        "santibhai": ["gopibhai"],
        "natvarbhai":["naginbhai"],
        },
        
    "vihabhai" : {
        "chamanbhai": ["sanjaybhai","parbatbhai"],
        "lilabhai":["prakashbhai","nareshbhai"],
        "sodhabhai": ["ravibhai"],
        "pratapbhai": ["prakashbhai","govindbhai","kishanbhai"],
        },

    "magabhai" : {
        "javerbhai": ["nagjibhai","mahendrabhai","anilbhai"],
        "mevabhai":["gudabhai","rajubhai","arvindbhai"],
        "pratapbhai":["manojbhai","vinodbhai"],
        },
}


for name in Jiva_dada:
    print("\n",name,end="'s son : ")
    for i in Jiva_dada[name]:
        print(i,end=",")
        


