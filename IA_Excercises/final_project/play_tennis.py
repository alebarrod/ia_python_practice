# Artificial Intelligence
# Grado en Ingeniería Informática
# 2017-18
# play_tennis.py (Unit 3, slide 8)


attributes=[('Outlook',['Sunny','Overcast','Rainy']),
            ('Temperature',['High','Low','Mild']),
            ('Humidity',['High','Normal']),
            ('Wind',['Weak','Strong'])]

class_name='Play Tennis'
classes=['yes','no']



train=[['Sunny' ,  'High'       , 'High'    , 'Weak' ,  'no'],
       ['Sunny' ,  'High'       , 'High'    , 'Strong', 'no'],
       ['Overcast','High'       , 'High'    , 'Weak' ,  'yes'],
       ['Rainy'  , 'Mild'       , 'High'    , 'Weak' ,  'yes'],
       ['Rainy'  , 'Low'        , 'Normal'  , 'Weak' ,  'yes'],
       ['Rainy'  , 'Low'        , 'Normal'  , 'Strong', 'no'],
       ['Overcast','Low'        , 'Normal'  , 'Strong', 'yes'],
       ['Sunny' ,  'Mild'       , 'High'    , 'Weak' ,  'no'],
       ['Sunny' ,  'Low'        , 'Normal'  , 'Weak' ,  'yes'],
       ['Rainy'  , 'Mild'       , 'Normal'  , 'Weak' ,  'yes'],
       ['Sunny' ,  'Mild'       , 'Normal'  , 'Strong', 'yes'],
       ['Overcast','Mild'       , 'High'    , 'Strong', 'yes'],
       ['Overcast','High'        , 'Normal'  , 'Weak' , 'yes'],
       ['Rainy',   'Mild'       , 'High'    , 'Strong', 'no']]


