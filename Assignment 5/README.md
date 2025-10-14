# Assignment 5

## Libraries
"logic.py" and "utils.py" are used, which are available from the AIMA code repository on Github: https://github.com/aimacode/aima-python


## Python version
This program runs on version 3.9.1.


## Usage
All solutios will print automatically following the main function running. 

### Purpose:
The purpose of this code is to represent the familial relations of my family tree (back to grandparents) in a Horn Knowledge Base (using the class FolKB from logic.py), and then to query the KB to ask for all the mothers, fathers, sisters, brothers, aunts, uncles, and grandparents in the family.


### convertToList Function:
The function "convertToList" intakes a generator object (representing the substitution), and returns a list of the subbed-in elements only (the values in each dictionary).


### Process and Steps:
1. In family KB:
    use parent, male, female as predicates
    define mother+father+grandfather via terms parent/male/female only

2. Add definitions for the below relations:
    brother, sister, aunt, uncle
        (brother/sister in terms of parent/male/female)
        (uncle/aunt in terms of male/female/sibling/parent)
3. Represent my family tree back to grandparents:
    (state only with parent, male, and female predicates)

4. Query KB:
    ask using fol_fc_ask from logic.py to give the names of all mothers, fathers, sisters, brothers, aunts, and uncles. I also included grandparents.


### __main__ Function:
The main function will run steps 1-4 above in order. To achieve step 4, it will use the help of convertToList for each request. At the end, it will print each list in the form: "TYPEs are: [Name1, Name2, ....].


### My achieved printout:
MY_FAMILY_KB'S CLAUSES:
[((Parent(y, x) & Female(y)) ==> Mother(y)), ((Parent(y, x) & Male(y)) ==> Father(y)), ((Parent(y, x) & Parent(z, y)) ==> Grandparent(z)), ((Parent(z, x) & Parent(z, y)) ==> Sibling(x, y)), ((Sibling(y, x) & Male(y)) ==> Brother(y)), ((Sibling(y, x) & Female(y)) ==> Sister(y)), (((Parent(y, x) & Sibling(z, y)) & Female(z)) ==> Aunt(z)), (((Parent(y, x) & Sibling(z, y)) & Male(z)) ==> Uncle(z)), Female(Emma), Female(Kyra), Female(Kaela), Female(Katherine), Female(Meghan), Female(Jenna), Female(Ally), Female(Suzy), Female(Patrice), Female(Ellen), Female(Ann), Female(Pat), Male(Connor), Male(Trent), Male(Mikey), Male(Mike), Male(Joel), Male(Paul), Male(Bill), Male(John), Parent(Ann, Mikey), Parent(Ann, Suzy), Parent(Ann, Patrice), Parent(Ann, Ellen), Parent(Bill, Mikey), Parent(Bill, Suzy), Parent(Bill, Patrice), Parent(Bill, Ellen), Parent(Pat, Mike), Parent(Pat, Joel), Parent(Pat, Paul), Parent(John, Mike), Parent(John, Joel), Parent(John, Paul), Parent(Ellen, Connor), Parent(Ellen, Emma), Parent(Ellen, Kaela), Parent(Ellen, Kyra), Parent(Mike, Connor), Parent(Mike, Emma), Parent(Mike, Kaela), Parent(Mike, Kyra), Parent(Suzy, Katherine), Parent(Suzy, Meghan), Parent(Suzy, Trent), Parent(Paul, Jenna), Parent(Paul, Ally)]



Mothers are: [Pat, Suzy, Ellen, Ann]

Fathers are: [John, Mike, Bill, Paul]

Sisters are: [Meghan, Katherine, Kyra, Kaela, Emma, Ellen, Suzy, Patrice, Jenna, Ally]

Brothers are: [Mike, Paul, Joel, Trent, Connor, Mikey]

Aunts are: [Ellen, Suzy, Patrice]

Uncles are: [Mikey, Mike, Paul, Joel]

Grandparents are: [Ann, Bill, Pat, John]