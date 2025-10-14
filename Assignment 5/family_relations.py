import logic
import utils


def convertToList(generatorobj):
    completedlist = []
    for each in list(generatorobj):
        #print("each is", each)
        for key in each:
            completedlist.append(each[key])
    return completedlist





def __main__():
    #SETUP: initialize my family KB
    my_family_kb = logic.FolKB()
    
    #STEP 1: define mother/father/grandparent via parent/male/female predicates
    my_family_kb.tell(logic.expr('(Parent(y,x) & Female(y)) ==> Mother(y)'))
    my_family_kb.tell(logic.expr('(Parent(y,x) & Male(y)) ==> Father(y)'))
    my_family_kb.tell(logic.expr('(Parent(y,x) & Parent(z,y)) ==> Grandparent(z)'))


    #STEP 2: define brother, sister, aunt, uncle
    my_family_kb.tell(logic.expr('(Parent(z,x) & Parent(z,y))  ==> Sibling(x, y)'))
    my_family_kb.tell(logic.expr('(Sibling(y,x) & Male(y)) ==> Brother(y)'))#BROTHER
    my_family_kb.tell(logic.expr('(Sibling(y,x) & Female(y)) ==> Sister(y)'))#SISTER
    
    my_family_kb.tell(logic.expr('(Parent(y,x) & Sibling(z,y)) & Female(z) ==> Aunt(z)'))#AUNT
    my_family_kb.tell(logic.expr('(Parent(y,x) & Sibling(z,y)) & Male(z) ==> Uncle(z)'))#UNCLE
    
    
    #STEP 3: represent my family tree, add to my KB
    #Add females
    my_family_kb.tell(logic.expr('Female(Emma)'))
    my_family_kb.tell(logic.expr('Female(Kyra)'))
    my_family_kb.tell(logic.expr('Female(Kaela)'))
    my_family_kb.tell(logic.expr('Female(Katherine)'))
    my_family_kb.tell(logic.expr('Female(Meghan)'))
    my_family_kb.tell(logic.expr('Female(Jenna)'))
    my_family_kb.tell(logic.expr('Female(Ally)'))
    my_family_kb.tell(logic.expr('Female(Suzy)'))
    my_family_kb.tell(logic.expr('Female(Patrice)'))
    my_family_kb.tell(logic.expr('Female(Ellen)'))
    my_family_kb.tell(logic.expr('Female(Ann)'))
    my_family_kb.tell(logic.expr('Female(Pat)'))
    
    #Add males
    my_family_kb.tell(logic.expr('Male(Connor)'))
    my_family_kb.tell(logic.expr('Male(Trent)'))
    my_family_kb.tell(logic.expr('Male(Mikey)'))
    my_family_kb.tell(logic.expr('Male(Mike)'))
    my_family_kb.tell(logic.expr('Male(Joel)'))
    my_family_kb.tell(logic.expr('Male(Paul)'))
    my_family_kb.tell(logic.expr('Male(Bill)'))
    my_family_kb.tell(logic.expr('Male(John)'))
    
    #Add parental relations
    my_family_kb.tell(logic.expr('Parent(Ann,Mikey)'))
    my_family_kb.tell(logic.expr('Parent(Ann,Suzy)'))
    my_family_kb.tell(logic.expr('Parent(Ann,Patrice)'))
    my_family_kb.tell(logic.expr('Parent(Ann,Ellen)'))
    my_family_kb.tell(logic.expr('Parent(Bill,Mikey)'))
    my_family_kb.tell(logic.expr('Parent(Bill,Suzy)'))
    my_family_kb.tell(logic.expr('Parent(Bill,Patrice)'))
    my_family_kb.tell(logic.expr('Parent(Bill,Ellen)'))

    my_family_kb.tell(logic.expr('Parent(Pat,Mike)'))
    my_family_kb.tell(logic.expr('Parent(Pat,Joel)'))
    my_family_kb.tell(logic.expr('Parent(Pat,Paul)'))
    my_family_kb.tell(logic.expr('Parent(John,Mike)'))
    my_family_kb.tell(logic.expr('Parent(John,Joel)'))
    my_family_kb.tell(logic.expr('Parent(John,Paul)'))

    my_family_kb.tell(logic.expr('Parent(Ellen,Connor)'))
    my_family_kb.tell(logic.expr('Parent(Ellen,Emma)'))
    my_family_kb.tell(logic.expr('Parent(Ellen,Kaela)'))
    my_family_kb.tell(logic.expr('Parent(Ellen,Kyra)'))
    my_family_kb.tell(logic.expr('Parent(Mike,Connor)'))
    my_family_kb.tell(logic.expr('Parent(Mike,Emma)'))
    my_family_kb.tell(logic.expr('Parent(Mike,Kaela)'))
    my_family_kb.tell(logic.expr('Parent(Mike,Kyra)'))
    
    my_family_kb.tell(logic.expr('Parent(Suzy,Katherine)'))
    my_family_kb.tell(logic.expr('Parent(Suzy,Meghan)'))
    my_family_kb.tell(logic.expr('Parent(Suzy,Trent)'))
    
    my_family_kb.tell(logic.expr('Parent(Paul,Jenna)'))
    my_family_kb.tell(logic.expr('Parent(Paul,Ally)'))
    
    print("MY_FAMILY_KB'S CLAUSES:")
    print(my_family_kb.clauses)
    print("")
    print("")
    print("")
    

    #STEP 4: Ask kb for mother, father, sister, brother, aunt, uncle 
    print("Mothers are:", convertToList(logic.fol_fc_ask(my_family_kb, logic.expr('Mother(x)'))))
    print("")
    print("Fathers are:", convertToList(logic.fol_fc_ask(my_family_kb, logic.expr('Father(x)'))))
    print("")
    print("Sisters are:", convertToList(logic.fol_fc_ask(my_family_kb, logic.expr('Sister(x)'))))
    print("")
    print("Brothers are:", convertToList(logic.fol_fc_ask(my_family_kb, logic.expr('Brother(x)'))))
    print("")
    print("Aunts are:", convertToList(logic.fol_fc_ask(my_family_kb, logic.expr('Aunt(x)'))))
    print("")
    print("Uncles are:", convertToList(logic.fol_fc_ask(my_family_kb, logic.expr('Uncle(x)'))))
    print("")
    print("Grandparents are:", convertToList(logic.fol_fc_ask(my_family_kb, logic.expr('Grandparent(x)'))))

__main__()