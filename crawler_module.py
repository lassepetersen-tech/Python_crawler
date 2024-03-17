import os
"""os.walk genererer 3 tuples, 
det foerste tuple indeholder elementer hvor hvert element indeholder en hel sti fra roden af, 
og det naeste tuple indeholder dir-navne og sidste tuple indeholder fil-navne
"""
def funcSearch(sti_arg="/", ext_arg="txt", ord_arg="malware"):
    for komplet_sti, dir_navne_list, fil_navne_list in os.walk(sti_arg, topdown=True, onerror=None):    
        """print("#" * 50, "\n")    
        print("en komplet sti :  ", komplet_sti)
        print("dir_navne_list :  ", dir_navne_list)
        print("fil_navne_list :  ", fil_navne_list) 
        """   
        for filnavn in fil_navne_list:                       
            if filnavn.endswith(ext_arg):                
                join_sti_filnavn = os.path.join(komplet_sti, filnavn)                
                try:
                    with open(join_sti_filnavn, "r", encoding="ISO-8859-1") as fil_pointer:
                        list_of_lines = fil_pointer.readlines()  # readlines returnerer datatypen list hvor hvert element er en hel linie                        
                        # jeg bruger list comprehension nedenfor bare uden at bygge en list
                        [print("\n"*5, f"\n{join_sti_filnavn}\n{line}") for line in list_of_lines if ord_arg in line]
                except OSError:
                    print("\n"*5, "Fil kan ikke laeses, INGEN adgang:> ", join_sti_filnavn, "\n"*5)
                
                



                





