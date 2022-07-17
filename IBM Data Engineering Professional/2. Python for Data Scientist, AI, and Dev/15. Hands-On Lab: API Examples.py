#To start using the API you can install the `randomuser` library running the `pip install` command.
!pip install randomuser
from randomuser import RandomUser
import pandas as pd
r = RandomUser()

#Then, using generate_users() function, we get a list of random 10 users.
some_list = r.generate_users(10)
some_list

#output
[<randomuser.RandomUser at 0x7fcd887383d0>,
 <randomuser.RandomUser at 0x7fcd88738410>,
 <randomuser.RandomUser at 0x7fcd88738f50>,
 <randomuser.RandomUser at 0x7fcd88738c50>,
 <randomuser.RandomUser at 0x7fcd887382d0>,
 <randomuser.RandomUser at 0x7fcd88738750>,
 <randomuser.RandomUser at 0x7fcd88738b50>,
 <randomuser.RandomUser at 0x7fcd88738f10>,
 <randomuser.RandomUser at 0x7fcd887389d0>,
 <randomuser.RandomUser at 0x7fcd88738bd0>]



#to get full name, we call get_full_name() function.
name = r.get_full_name()
for user in some_list:
    print (user.get_full_name()," ",user.get_email())

#output
Rose Bell   rose.bell@example.com
Ylva Eklund   ylva.eklund@example.com
Encarnacion Dominguez   encarnacion.dominguez@example.com
Joshua Beck   joshua.beck@example.com
Emilio Garcia   emilio.garcia@example.com
Bertolino Pires   bertolino.pires@example.com
Manuel Rodriguez   manuel.rodriguez@example.com
Alan Warren   alan.warren@example.com
Felix Christensen   felix.christensen@example.com
Jesus Burton   jesus.burton@example.com

------------------------------------------------------------------------------------
#In this Exercise, generate photos of the random 5 users.
for user in some_list:
    print(user.get_picture())
  
#output
https://randomuser.me/api/portraits/women/7.jpg
https://randomuser.me/api/portraits/women/59.jpg
https://randomuser.me/api/portraits/women/49.jpg
https://randomuser.me/api/portraits/men/4.jpg
https://randomuser.me/api/portraits/men/14.jpg
https://randomuser.me/api/portraits/men/38.jpg
https://randomuser.me/api/portraits/men/14.jpg
https://randomuser.me/api/portraits/men/86.jpg
https://randomuser.me/api/portraits/men/32.jpg
https://randomuser.me/api/portraits/men/93.jpg
  
------------------------------------------------------------------------------------
#generate a table with information about the users with functions

def get_users():
  users = []
  
  for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),
                      "Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
  
  return pd.DataFrame(users)

get_users()

#output
Name	Gender	City	State	Email	DOB	Picture
0	Onni Aro	male	Tammela	Northern Ostrobothnia	onni.aro@example.com	1946-10-29T12:02:18.100Z	https://randomuser.me/api/portraits/men/70.jpg
1	Adam Hughes	male	Napier	Auckland	adam.hughes@example.com	1989-10-31T23:10:06.296Z	https://randomuser.me/api/portraits/men/28.jpg
2	John Smith	male	Vallejo	Arkansas	john.smith@example.com	1946-06-28T18:10:49.941Z	https://randomuser.me/api/portraits/men/24.jpg
3	بیتا نجاتی	female	بیرجند	مرکزی	byt.njty@example.com	1977-10-27T00:24:35.447Z	https://randomuser.me/api/portraits/women/65.jpg
4	تینا كامياران	female	بیرجند	خراسان جنوبی	tyn.kmyrn@example.com	1987-05-01T04:15:44.574Z	https://randomuser.me/api/portraits/women/62.jpg
5	Samantha Boerman	female	Purmerend	Flevoland	samantha.boerman@example.com	1988-10-14T18:38:27.919Z	https://randomuser.me/api/portraits/women/31.jpg
6	Anaïs Le Gall	female	Eggerberg	Basel-Landschaft	anais.legall@example.com	1951-09-11T07:29:55.226Z	https://randomuser.me/api/portraits/women/78.jpg
7	Ronja Ollila	female	Joensuu	Finland Proper	ronja.ollila@example.com	1990-06-09T23:20:46.437Z	https://randomuser.me/api/portraits/women/69.jpg
8	Jack Hall	male	Taupo	West Coast	jack.hall@example.com	1978-06-11T04:47:53.053Z	https://randomuser.me/api/portraits/men/25.jpg
9	Özkan Avan	male	Sinop	Bolu	ozkan.avan@example.com	1955-12-12T19:26:44.720Z	https://randomuser.me/api/portraits/men/74.jpg
     
df1 = pd.DataFrame(get_users())
------------------------------------------------------------------------------------
#Example 2: Fruitvice API

import requests
import json
data = requests.get("https://www.fruityvice.com/api/fruit/all")
#We will retrieve results using json.loads() function.
results = json.loads(data.text)
pd.DataFrame(results)

#output
	genus	name	id	family	order	nutritions
0	Malus	Apple	6	Rosaceae	Rosales	{'carbohydrates': 11.4, 'protein': 0.3, 'fat':...
1	Prunus	Apricot	35	Rosaceae	Rosales	{'carbohydrates': 3.9, 'protein': 0.5, 'fat': ...
2	Musa	Banana	1	Musaceae	Zingiberales	{'carbohydrates': 22, 'protein': 1, 'fat': 0.2...
3	Rubus	Blackberry	64	Rosaceae	Rosales	{'carbohydrates': 9, 'protein': 1.3, 'fat': 0....
4	Fragaria	Blueberry	33	Rosaceae	Rosales	{'carbohydrates': 5.5, 'protein': 0, 'fat': 0....
5	Prunus	Cherry	9	Rosaceae	None	{'carbohydrates': 12, 'protein': 1, 'fat': 0.3...
6	Durio	Durian	60	Malvaceae	Malvales	{'carbohydrates': 27.1, 'protein': 1.5, 'fat':...
7	Ficus	Fig	68	Moraceae	Rosales	{'carbohydrates': 19, 'protein': 0.8, 'fat': 0...
8	Ribes	Gooseberry	69	Grossulariaceae	Saxifragales	{'carbohydrates': 10, 'protein': 0.9, 'fat': 0...
9	Vitis	Grapes	47	Vitaceae	Vitales	{'carbohydrates': 18.1, 'protein': 0.72, 'fat'...
10	Malus	GreenApple	72	Rosaceae	Rosales	{'carbohydrates': 3.1, 'protein': 0.4, 'fat': ...
11	Psidium	Guava	37	Myrtaceae	Myrtales	{'carbohydrates': 14, 'protein': 2.6, 'fat': 1...
12	Apteryx	Kiwi	66	Actinidiaceae	Struthioniformes	{'carbohydrates': 15, 'protein': 1.1, 'fat': 0...
13	Citrus	Lemon	26	Rutaceae	Sapindales	{'carbohydrates': 9, 'protein': 1.1, 'fat': 0....
14	Citrus	Lime	44	Rutaceae	Sapindales	{'carbohydrates': 8.4, 'protein': 0.3, 'fat': ...
15	Vaccinium	Lingonberry	65	Ericaceae	Ericales	{'carbohydrates': 11.3, 'protein': 0.75, 'fat'...
16	Litchi	Lychee	67	Sapindaceae	Sapindales	{'carbohydrates': 17, 'protein': 0.8, 'fat': 0...
17	Mangifera	Mango	27	Anacardiaceae	Sapindales	{'carbohydrates': 15, 'protein': 0.82, 'fat': ...
18	Cucumis	Melon	41	Cucurbitaceae	Cucurbitaceae	{'carbohydrates': 8, 'protein': 0, 'fat': 0, '...
19	Citrus	Orange	2	Rutaceae	Sapindales	{'carbohydrates': 8.3, 'protein': 1, 'fat': 0....
20	Carica	Papaya	42	Caricaceae	Caricacea	{'carbohydrates': 11, 'protein': 0, 'fat': 0.4...
21	Passiflora	Passionfruit	70	Passifloraceae	Malpighiales	{'carbohydrates': 22.4, 'protein': 2.2, 'fat':...
22	Pyrus	Pear	4	Rosaceae	Rosales	{'carbohydrates': 15, 'protein': 0.4, 'fat': 0...
23	Diospyros	Persimmon	52	Ebenaceae	Rosales	{'carbohydrates': 18, 'protein': 0, 'fat': 0, ...
24	Ananas	Pineapple	10	Bromeliaceae	Poales	{'carbohydrates': 13.12, 'protein': 0.54, 'fat...
25	Prunus	Plum	71	Rosaceae	Rosales	{'carbohydrates': 11.4, 'protein': 0.7, 'fat':...
26	Rubus	Raspberry	23	Rosaceae	Rosales	{'carbohydrates': 12, 'protein': 1.2, 'fat': 0...
27	Fragaria	Strawberry	3	Rosaceae	Rosales	{'carbohydrates': 5.5, 'protein': 0.8, 'fat': ...
28	Solanum	Tomato	5	Solanaceae	Solanales	{'carbohydrates': 3.9, 'protein': 0.9, 'fat': ...
29	Spondias	Umbu	73	Anacardiaceae	0	{'carbohydrates': 0, 'protein': 0, 'fat': 0, '...
30	Citrullus	Watermelon	25	Cucurbitaceae	Cucurbitales	{'carbohydrates': 8, 'protein': 0.6, 'fat': 0....

                                                           

                                                           
#The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.
df2 = pd.json_normalize(results)
df2
                                                           
#output
	genus	name	id	family	order	nutritions.carbohydrates	nutritions.protein	nutritions.fat	nutritions.calories	nutritions.sugar
0	Malus	Apple	6	Rosaceae	Rosales	11.40	0.30	0.40	52	10.30
1	Prunus	Apricot	35	Rosaceae	Rosales	3.90	0.50	0.10	15	3.20
2	Musa	Banana	1	Musaceae	Zingiberales	22.00	1.00	0.20	96	17.20
3	Rubus	Blackberry	64	Rosaceae	Rosales	9.00	1.30	0.40	40	4.50
4	Fragaria	Blueberry	33	Rosaceae	Rosales	5.50	0.00	0.40	29	5.40
5	Prunus	Cherry	9	Rosaceae	None	12.00	1.00	0.30	50	8.00
6	Durio	Durian	60	Malvaceae	Malvales	27.10	1.50	5.30	147	6.75
7	Ficus	Fig	68	Moraceae	Rosales	19.00	0.80	0.30	74	16.00
8	Ribes	Gooseberry	69	Grossulariaceae	Saxifragales	10.00	0.90	0.60	44	0.00
9	Vitis	Grapes	47	Vitaceae	Vitales	18.10	0.72	0.16	69	15.48
10	Malus	GreenApple	72	Rosaceae	Rosales	3.10	0.40	0.10	21	6.40
11	Psidium	Guava	37	Myrtaceae	Myrtales	14.00	2.60	1.00	68	9.00
12	Apteryx	Kiwi	66	Actinidiaceae	Struthioniformes	15.00	1.10	0.50	61	9.00
13	Citrus	Lemon	26	Rutaceae	Sapindales	9.00	1.10	0.30	29	2.50
14	Citrus	Lime	44	Rutaceae	Sapindales	8.40	0.30	0.10	25	1.70
15	Vaccinium	Lingonberry	65	Ericaceae	Ericales	11.30	0.75	0.34	50	5.74
16	Litchi	Lychee	67	Sapindaceae	Sapindales	17.00	0.80	0.44	66	15.00
17	Mangifera	Mango	27	Anacardiaceae	Sapindales	15.00	0.82	0.38	60	13.70
18	Cucumis	Melon	41	Cucurbitaceae	Cucurbitaceae	8.00	0.00	0.00	34	8.00
19	Citrus	Orange	2	Rutaceae	Sapindales	8.30	1.00	0.20	43	8.20
20	Carica	Papaya	42	Caricaceae	Caricacea	11.00	0.00	0.40	43	1.00
21	Passiflora	Passionfruit	70	Passifloraceae	Malpighiales	22.40	2.20	0.70	97	11.20
22	Pyrus	Pear	4	Rosaceae	Rosales	15.00	0.40	0.10	57	10.00
23	Diospyros	Persimmon	52	Ebenaceae	Rosales	18.00	0.00	0.00	81	18.00
24	Ananas	Pineapple	10	Bromeliaceae	Poales	13.12	0.54	0.12	50	9.85
25	Prunus	Plum	71	Rosaceae	Rosales	11.40	0.70	0.28	46	9.92
26	Rubus	Raspberry	23	Rosaceae	Rosales	12.00	1.20	0.70	53	4.40
27	Fragaria	Strawberry	3	Rosaceae	Rosales	5.50	0.80	0.40	29	5.40
28	Solanum	Tomato	5	Solanaceae	Solanales	3.90	0.90	0.20	74	2.60
29	Spondias	Umbu	73	Anacardiaceae	0	0.00	0.00	0.00	0	0.00
30	Citrullus	Watermelon	25	Cucurbitaceae	Cucurbitales	8.00	0.60	0.20	30	6.00                                                           
                                                           
                                                           
                                                           
#we need to know the family and genus of a cherry.
cherry = df2.log[df2['name'] == 'Cherry']
cherry
                                                           
#output
	genus	name	id	family	order	nutritions.carbohydrates	nutritions.protein	nutritions.fat	nutritions.calories	nutritions.sugar
5	Prunus	Cherry	9	Rosaceae	None	12.0	1.0	0.3	50	8.0
                                                           
#print fam and genus                                                                                                                     
fam = cherry.iloc[0]['family']      
gen = cherry.iloc[0]['genus']
print(fam,gen) 

#print
('Rosaceae', 'Prunus')    
                                                           
------------------------------------------------------------------------------------
#LAST EXERCISE
import requests
import json
import pandas as pd

data2 = requests.get('https://www.fishwatch.gov/api/species')
results = json.loads(data2.text)
df = pd.DataFrame(results)                                                           
