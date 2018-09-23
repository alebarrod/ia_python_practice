# ========================================================
# Data "Congressional Voting Record"
# Source: UCI Machine Learning Repository 
# (http://archive.ics.uci.edu/ml/)
# ========================================================


# Classification attribute
# -------------------------

class_name='Party'


# Classes:
# --------

classes=['republican','democrat']


# Attributes:
# -----------

# 16 votes carried out during 1984:

# 1. handicapped-infants
# 2. water-project-cost-sharing
# 3. adoption-of-the-budget-resolution
# 4. physician-fee-freeze
# 5. el-salvador-aid
# 6. religious-groups-in-schools
# 7. anti-satellite-test-ban
# 8. aid-to-nicaraguan-contras
# 9.  mx-missile
# 10. immigration
# 11. synfuels-corporation-cutback
# 12. education-spending
# 13. superfund-right-to-sue
# 14. crime
# 15. duty-free-exports
# 16. export-administration-act-south-africa

# To simplify, attributes will be calles "votex", for x from 1 to 16

# Possible values of each vote are y (yes), n (no) and ? (present). Present is
# similar to a blank vote.


attributes=[('vote1',["y","n","?"]),
           ('vote2',["y","n","?"]),
           ('vote3',["y","n","?"]),
           ('vote4',["y","n","?"]),
           ('vote5',["y","n","?"]),
           ('vote6',["y","n","?"]),
           ('vote7',["y","n","?"]),
           ('vote8',["y","n","?"]),
           ('vote9',["y","n","?"]),
           ('vote10',["y","n","?"]),
           ('vote11',["y","n","?"]),
           ('vote12',["y","n","?"]),
           ('vote13',["y","n","?"]),
           ('vote14',["y","n","?"]),
           ('vote15',["y","n","?"]),
           ('vote16',["y","n","?"])]



# Training examples:
# ------------------


train=[['n','y','n','y','y','y','n','n','n','y','?','y','y','y','n','y','republican'],
            ['n','y','n','y','y','y','n','n','n','n','n','y','y','y','n','?','republican'],
            ['?','y','y','?','y','y','n','n','n','n','y','n','y','y','n','n','democrat' ],
            ['n','y','y','n','?','y','n','n','n','n','y','n','y','n','n','y','democrat' ],
            ['y','y','y','n','y','y','n','n','n','n','y','?','y','y','y','y','democrat' ],
            ['n','y','y','n','y','y','n','n','n','n','n','n','y','y','y','y','democrat' ],
            ['n','y','n','y','y','y','n','n','n','n','n','n','?','y','y','y','democrat' ],
            ['n','y','n','y','y','y','n','n','n','n','n','n','y','y','?','y','republican'],
            ['n','y','n','y','y','y','n','n','n','n','n','y','y','y','n','y','republican'],
            ['y','y','y','n','n','n','y','y','y','n','n','n','n','n','?','?','democrat' ],
            ['n','y','n','y','y','n','n','n','n','n','?','?','y','y','n','n','republican'],
            ['n','y','n','y','y','y','n','n','n','n','y','?','y','y','?','?','republican'],
            ['n','y','y','n','n','n','y','y','y','n','n','n','y','n','?','?','democrat' ],
            ['y','y','y','n','n','y','y','y','?','y','y','?','n','n','y','?','democrat' ],
            ['n','y','n','y','y','y','n','n','n','n','n','y','?','?','n','?','republican'],
            ['n','y','n','y','y','y','n','n','n','y','n','y','y','?','n','?','republican'],
            ['y','n','y','n','n','y','n','y','?','y','y','y','?','n','n','y','democrat' ],
            ['y','?','y','n','n','n','y','y','y','n','n','n','y','n','y','y','democrat' ],
            ['n','y','n','y','y','y','n','n','n','n','n','?','y','y','n','n','republican'],
            ['y','y','y','n','n','n','y','y','y','n','y','n','n','n','y','y','democrat' ],
            ['y','y','y','n','n','?','y','y','n','n','y','n','n','n','y','y','democrat' ],
            ['y','y','y','n','n','n','y','y','y','n','n','n','?','?','y','y','democrat' ],
            ['y','?','y','n','n','n','y','y','y','n','n','?','n','n','y','y','democrat' ],
            ['y','y','y','n','n','n','y','y','y','n','n','n','n','n','y','y','democrat' ],
            ['y','n','y','n','n','n','y','y','y','n','n','n','n','n','y','?','democrat' ],
            ['y','n','y','n','n','n','y','y','y','y','n','n','n','n','y','y','democrat' ],
            ['y','n','y','n','n','n','y','y','y','n','y','n','n','n','y','y','democrat' ],
            ['y','y','y','n','n','n','y','y','y','n','y','n','n','n','y','y','democrat' ],
            ['y','n','n','y','y','n','y','y','y','n','n','y','y','y','n','y','republican'],
            ['y','y','y','n','n','n','y','y','y','n','y','n','n','n','y','y','democrat' ],
            ['n','y','n','y','y','y','n','n','n','n','n','y','y','y','n','n','republican'],
            ['y','y','y','n','n','n','y','y','y','n','y','n','n','n','y','?','democrat' ],
            ['y','y','y','n','n','n','y','y','y','y','n','n','y','n','y','y','democrat' ],
            ['n','y','n','y','y','y','n','n','n','n','n','y','y','y','n','y','republican'],
            ['y','y','y','n','n','n','y','y','y','n','n','n','n','n','y','y','democrat' ],
            ['n','y','n','y','y','y','n','n','n','n','n','y','y','y','n','n','republican'],
            ['y','?','n','y','y','y','n','n','n','y','n','y','?','y','n','y','republican'],
            ['y','y','n','y','y','y','n','n','n','n','n','n','y','y','n','y','republican'],
            ['n','y','n','y','y','y','n','n','n','y','n','y','y','y','n','n','republican'],
            ['y','n','y','n','n','n','y','y','y','y','y','n','y','n','y','y','democrat' ],
            ['y','y','y','n','n','n','y','y','y','n','?','n','n','n','n','?','democrat' ],
            ['y','y','y','n','n','n','y','y','y','n','n','n','n','n','y','?','democrat' ],
            ['y','n','y','n','n','n','y','y','y','n','n','n','n','n','n','y','democrat' ],
            ['y','n','y','n','n','n','y','y','y','n','n','n','n','n','y','y','democrat' ],
            ['y','y','y','n','n','n','y','y','y','n','y','n','n','n','n','?','democrat' ],
            ['y','y','y','n','n','n','y','y','?','n','y','n','n','n','y','?','democrat' ],
            ['y','y','y','n','n','n','y','y','y','n','n','n','n','n','n','y','democrat' ],
            ['y','n','y','n','n','n','y','y','?','n','n','n','n','n','n','?','democrat' ],
            ['y','y','y','n','n','n','y','y','n','n','n','n','n','y','n','y','democrat' ],
            ['n','?','n','y','y','y','n','n','n','n','n','y','y','y','n','n','republican'],
            ['y','y','y','n','n','n','y','y','y','n','y','n','n','n','y','y','democrat' ],
            ['n','y','n','y','y','y','n','?','n','n','n','y','y','y','n','y','republican'],
            ['y','y','y','n','n','n','y','y','y','n','n','n','n','n','?','?','democrat' ],
            ['y','y','n','y','y','y','n','n','n','y','n','y','y','y','n','n','republican'],
            ['y','y','y','n','n','y','?','y','n','n','y','y','n','y','n','?','democrat' ],
            ['n','y','n','y','y','y','n','n','n','y','y','y','y','y','n','n','republican'],
            ['n','y','n','y','y','y','n','n','n','y','y','y','y','y','n','y','republican'],
            ['n','y','n','y','y','y','n','n','n','y','n','y','y','y','n','y','republican'],
            ['n','y','n','y','y','y','n','n','n','y','n','y','y','y','n','y','republican'],
            ['n','y','n','y','y','y','n','n','n','y','n','y','y','y','n','?','republican'],
            ['y','y','y','n','n','?','y','y','y','y','n','n','n','n','y','?','democrat' ],
            ['n','y','n','y','y','y','n','n','n','n','n','y','y','y','n','n','republican'],
            ['y','y','y','n','n','n','y','y','y','n','n','n','n','n','n','?','democrat' ],
            ['y','y','y','n','n','n','y','y','y','n','y','n','n','n','n','y','democrat' ],
            ['y','y','y','n','n','n','y','y','y','n','y','?','n','n','n','y','democrat' ],
            ['y','y','n','y','y','y','y','n','n','n','n','y','y','y','n','y','republican'],
            ['n','y','n','y','y','y','y','n','n','n','y','y','y','y','n','y','republican'],
            ['n','y','n','y','y','y','n','n','n','y','n','y','y','y','n','n','republican'],
            ['y','?','y','n','n','n','y','y','y','n','n','n','y','n','y','y','democrat' ],
            ['y','y','y','n','n','n','y','y','y','n','n','n','n','n','y','y','democrat' ],
            ['y','n','y','n','n','n','y','y','y','n','n','n','y','n','y','?','democrat' ],
            ['y','y','y','y','n','n','y','y','y','y','y','n','n','y','n','y','republican'],
            ['y','y','y','n','n','n','y','y','y','n','y','n','n','n','y','?','democrat' ],
            ['y','n','y','y','y','n','y','n','y','y','n','n','y','y','n','y','republican'],
            ['y','n','y','n','n','y','y','y','y','y','y','n','n','y','y','y','democrat' ],
            ['n','y','y','y','y','y','n','n','n','y','y','n','y','y','n','n','democrat' ],
            ['n','y','y','n','y','y','n','n','n','y','y','y','y','y','n','?','democrat' ],
            ['n','y','y','y','y','y','n','y','y','y','y','y','y','y','n','y','democrat' ],
            ['y','y','y','n','y','y','n','n','n','y','y','n','y','y','n','y','democrat' ],
            ['n','n','n','y','y','n','n','n','n','y','n','y','y','y','n','n','republican'],
            ['y','n','y','n','n','y','y','y','y','y','n','y','n','y','n','?','democrat' ],
            ['y','n','y','n','n','n','y','y','?','y','y','y','n','y','n','y','democrat' ],
            ['n','n','n','y','y','y','n','n','n','y','n','y','y','y','n','y','republican'],
            ['n','n','n','y','y','y','n','n','n','n','n','y','y','y','n','n','republican'],
            ['n','?','n','y','y','y','n','n','n','y','n','y','y','y','n','n','republican'],
            ['n','n','y','n','y','y','n','n','n','y','y','y','y','y','n','y','democrat' ],
            ['n','n','n','y','y','y','n','n','n','y','n','y','y','y','n','n','republican'],
            ['n','n','n','y','y','y','n','n','n','n','n','y','y','y','n','n','republican'],
            ['n','y','y','n','y','y','y','n','y','y','y','n','y','y','n','y','democrat' ],
            ['n','n','n','y','y','y','n','n','n','y','n','?','y','y','n','?','republican'],
            ['y','n','y','n','n','n','y','y','y','y','n','n','n','n','y','y','democrat' ],
            ['y','n','y','n','n','n','y','y','y','y','y','n','n','n','y','y','democrat' ],
            ['y','y','y','n','n','n','y','y','n','y','y','n','n','?','y','y','democrat' ],
            ['y','n','y','n','n','n','y','n','y','y','y','n','n','n','y','y','democrat' ],
            ['y','n','y','n','y','y','n','n','n','n','n','n','n','n','n','y','democrat' ],
            ['y','n','y','n','y','y','n','?','?','n','y','?','?','?','y','y','democrat' ],
            ['n','n','?','n','y','y','n','n','n','n','y','y','y','y','n','y','democrat' ],
            ['y','n','n','n','y','y','y','n','n','y','y','n','n','y','n','y','democrat' ],
            ['y','y','y','n','n','y','y','y','y','y','n','n','n','n','n','y','democrat' ],
            ['n','n','n','y','y','y','n','n','n','y','?','y','y','y','n','n','republican'],
            ['y','n','n','n','y','y','n','n','n','n','y','y','n','y','n','y','democrat' ],
            ['y','n','y','n','y','y','y','n','n','n','y','n','n','y','n','y','democrat' ],
            ['y','n','y','n','y','y','y','n','?','n','y','n','y','y','y','?','democrat' ],
            ['y','n','n','n','y','y','?','n','?','n','n','n','n','y','?','n','democrat' ],
            ['?','?','?','?','n','y','y','y','y','y','?','n','y','y','n','?','democrat' ],
            ['y','y','y','n','n','n','n','y','y','n','y','n','n','n','y','y','democrat' ],
            ['n','y','n','y','y','y','n','n','n','n','n','y','y','y','n','y','republican'],
            ['n','?','?','?','?','?','?','?','?','?','?','?','?','y','?','?','republican'],
            ['y','?','y','n','n','n','y','y','y','n','n','n','n','n','y','?','democrat' ],
            ['y','?','y','n','n','n','y','y','y','n','n','n','n','n','y','?','democrat' ],
            ['n','n','y','n','n','n','y','y','y','y','n','n','n','n','y','y','democrat' ],
            ['n','?','n','y','y','y','n','n','n','y','n','y','y','y','n','y','republican'],
            ['n','?','y','n','n','y','y','y','n','y','n','n','n','n','y','?','democrat' ],
            ['n','?','n','y','y','y','n','n','n','y','n','y','y','y','n','n','republican'],
            ['y','?','y','n','n','n','y','y','y','n','n','n','n','n','y','?','democrat' ],
            ['n','?','y','n','?','?','y','y','y','y','?','?','n','n','y','y','democrat' ],
            ['y','n','y','n','n','n','y','y','y','n','y','n','n','n','y','y','democrat' ],
            ['y','y','y','y','y','n','y','n','n','n','n','y','y','y','n','y','republican'],
            ['n','y','y','n','n','n','n','y','y','y','y','n','n','n','y','y','democrat' ],
            ['n','n','n','y','y','y','n','n','n','n','n','y','y','y','n','n','republican'],
            ['n','?','?','y','y','y','n','n','n','y','n','y','y','y','?','y','republican'],
            ['n','?','n','y','y','y','n','n','n','y','n','y','y','y','n','y','republican'],
            ['n','n','n','y','y','y','n','n','n','y','n','y','n','y','n','y','republican'],
            ['y','?','n','y','y','y','n','y','n','n','n','y','y','y','n','y','republican'],
            ['n','?','y','n','n','n','y','y','y','n','n','n','n','n','y','y','democrat' ],
            ['n','?','n','y','y','y','n','n','n','y','n','y','y','y','n','y','republican'],
            ['n','?','n','y','y','y','n','n','n','n','n','y','y','y','n','n','republican'],
            ['n','?','y','n','n','n','y','y','y','y','y','n','n','y','y','y','democrat' ],
            ['n','?','y','n','n','y','n','y','n','y','y','n','n','n','y','y','democrat' ],
            ['?','?','y','n','n','n','y','y','?','n','?','?','?','?','?','?','democrat' ],
            ['y','?','y','n','?','?','y','y','y','n','n','n','n','n','y','?','democrat' ],
            ['n','n','y','n','n','y','n','y','y','y','n','n','n','y','n','y','democrat' ],
            ['n','n','n','y','y','y','n','n','n','y','n','y','y','y','n','?','republican'],
            ['n','n','n','y','y','y','n','n','n','y','n','y','y','y','n','y','republican'],
            ['n','n','n','y','y','y','n','n','n','n','n','y','y','y','n','?','republican'],
            ['n','n','n','y','y','y','n','n','n','y','n','y','y','y','n','n','republican'],
            ['n','y','n','y','y','y','n','n','n','y','y','y','y','n','n','y','republican'],
            ['n','?','y','n','n','y','y','y','y','y','n','n','n','y','y','y','democrat' ],
            ['n','n','y','n','n','y','y','y','y','y','n','n','n','y','n','y','democrat' ],
            ['y','n','y','n','n','y','y','y','y','n','n','n','n','n','y','y','democrat' ],
            ['n','n','n','y','n','n','y','y','y','y','n','n','y','y','n','y','republican'],
            ['n','n','n','y','y','y','y','y','y','y','n','y','y','y','?','y','republican'],
            ['n','n','n','y','y','y','y','y','y','y','n','y','y','y','n','y','republican'],
            ['?','y','n','n','n','n','y','y','y','y','y','n','n','y','y','y','democrat' ],
            ['n','?','n','n','n','y','y','y','y','y','n','n','n','y','n','?','democrat' ],
            ['n','n','y','n','n','y','y','y','y','y','n','n','n','y','?','y','democrat' ],
            ['n','y','n','y','y','y','n','n','n','n','n','y','y','y','n','y','republican'],
            ['n','n','n','n','n','n','y','y','y','y','n','y','y','y','y','y','democrat' ],
            ['n','y','n','y','y','y','n','n','n','y','y','y','y','y','n','y','republican'],
            ['n','n','y','n','n','n','y','y','y','y','n','n','y','n','y','y','democrat' ],
            ['y','y','n','y','y','y','n','n','n','y','n','y','y','y','n','y','republican'],
            ['y','y','?','y','y','y','n','n','y','n','y','?','y','y','n','n','democrat' ],
            ['n','y','y','n','n','y','n','y','y','y','y','n','y','n','y','y','democrat' ],
            ['n','n','y','n','n','y','y','y','y','y','y','n','y','y','n','y','democrat' ],
            ['n','y','n','y','y','y','n','n','n','n','n','y','y','y','n','n','republican'],
            ['y','y','n','y','y','y','n','?','n','n','y','y','y','y','n','n','republican'],
            ['y','y','n','y','y','y','y','n','n','n','n','y','y','y','n','n','republican'],
            ['n','y','y','n','n','y','n','y','y','n','y','n','?','?','?','?','democrat' ],
            ['n','y','n','y','y','y','n','n','n','y','n','y','y','y','n','n','republican'],
            ['n','y','y','n','?','y','y','y','y','y','y','n','n','?','n','?','democrat' ],
            ['n','y','n','n','y','y','n','n','n','n','n','y','y','y','y','y','democrat' ],
            ['n','n','n','n','y','y','y','n','n','n','n','y','y','y','n','y','democrat' ],
            ['n','y','y','n','y','y','y','n','n','n','y','y','y','y','n','y','democrat' ],
            ['n','y','n','y','y','y','y','n','n','n','n','y','y','y','n','y','republican'],
            ['y','y','n','n','y','y','n','n','n','y','y','y','y','y','n','?','democrat' ],
            ['n','y','y','n','n','y','y','y','y','y','y','n','y','n','y','?','democrat' ],
            ['y','n','y','y','y','y','y','y','n','y','n','y','n','y','y','y','republican'],
            ['y','n','y','y','y','y','y','y','n','y','y','y','n','y','y','y','republican'],
            ['n','n','y','y','y','y','n','n','y','n','n','n','y','y','y','?','democrat' ],
            ['y','n','y','n','n','n','y','y','y','y','y','n','n','y','n','y','democrat' ],
            ['y','n','y','n','n','n','?','y','y','?','n','n','n','n','y','?','democrat' ],
            ['n','?','n','y','y','y','n','n','n','y','n','y','y','y','n','y','republican'],
            ['n','y','y','n','n','n','y','y','y','y','n','n','?','n','y','y','democrat' ],
            ['n','n','n','n','y','y','n','n','n','y','y','y','y','y','n','y','democrat' ],
            ['y','?','y','n','n','n','y','y','y','n','n','n','n','n','y','?','democrat' ],
            ['n','y','y','n','n','n','y','y','y','y','n','n','n','n','y','y','democrat' ],
            ['n','n','y','y','n','n','y','y','y','y','n','n','n','y','y','y','republican'],
            ['n','n','y','n','n','n','y','y','y','y','y','?','n','n','y','y','democrat' ],
            ['?','n','y','n','n','n','y','y','y','y','y','?','n','n','y','?','democrat' ],
            ['y','n','y','n','n','n','y','y','y','y','n','n','n','n','y','y','democrat' ],
            ['?','?','y','n','n','n','y','y','y','?','?','n','n','n','?','?','democrat' ],
            ['n','n','y','n','n','n','y','y','y','y','y','n','n','n','y','y','democrat' ],
            ['y','?','y','n','n','n','y','y','y','n','n','n','n','n','y','y','democrat' ],
            ['?','?','?','?','?','?','?','?','y','?','?','?','?','?','?','?','democrat' ],
            ['n','n','y','n','n','n','y','y','y','y','y','n','n','n','y','y','democrat' ],
            ['y','n','y','n','n','n','y','y','y','y','n','?','n','n','y','y','democrat' ],
            ['n','y','y','n','n','n','y','y','y','y','y','n','n','n','y','y','democrat' ],
            ['y','n','y','n','n','n','y','y','y','n','n','n','n','n','y','?','democrat' ],
            ['y','?','n','y','y','y','y','y','n','n','n','y','?','y','?','?','republican'],
            ['y','n','y','n','n','n','y','y','y','n','n','n','n','n','y','y','democrat' ],
            ['n','?','n','y','y','y','n','n','n','n','n','y','y','y','n','?','republican'],
            ['n','y','n','y','y','y','n','?','n','y','n','y','y','y','n','?','republican'],
            ['n','n','n','n','n','y','y','y','y','n','y','n','n','y','y','y','democrat' ],
            ['n','n','y','n','n','n','y','y','y','n','n','n','n','n','y','y','democrat' ],
            ['n','n','y','n','n','y','y','?','y','y','y','n','n','n','y','y','democrat' ],
            ['n','n','n','y','y','y','n','n','n','n','n','y','y','y','n','?','republican'],
            ['n','n','y','n','n','y','y','y','y','n','y','y','n','y','y','?','democrat' ],
            ['n','?','y','y','y','y','n','n','n','y','n','n','n','y','n','y','republican'],
            ['n','n','y','n','n','n','y','y','y','y','y','n','?','n','y','?','democrat' ],
            ['y','y','n','n','n','n','y','y','?','n','y','n','n','n','y','?','democrat' ],
            ['n','n','y','n','n','n','y','y','y','n','n','n','n','y','y','y','democrat' ],
            ['y','y','y','n','n','n','y','y','y','n','n','n','n','n','y','y','democrat' ],
            ['y','n','y','n','n','y','y','y','y','y','y','n','n','n','y','y','democrat' ],
            ['y','n','y','n','n','n','y','y','y','y','n','n','n','n','y','y','democrat' ],
            ['n','n','y','y','y','y','y','n','n','n','n','y','y','y','n','y','republican'],
            ['n','n','y','n','n','y','y','y','y','y','n','y','n','n','n','y','democrat' ],
            ['n','n','n','y','y','y','n','n','n','y','n','y','n','y','n','y','republican'],
            ['y','?','n','y','y','y','y','n','n','y','n','y','y','y','n','y','republican'],
            ['n','n','y','n','n','n','y','y','y','n','n','?','n','n','y','y','democrat' ],
            ['y','y','y','n','n','n','y','y','y','y','y','n','n','n','n','y','democrat' ],
            ['n','n','y','n','n','y','y','y','y','n','n','n','n','n','y','y','democrat' ],
            ['n','y','n','y','y','y','n','n','n','y','n','y','y','y','n','y','republican'],
            ['n','n','y','n','n','n','y','y','y','n','y','n','n','n','y','y','democrat' ],
            ['n','y','y','n','n','y','n','y','y','n','y','n','y','n','y','y','democrat' ],
            ['y','y','n','y','y','y','n','n','n','y','n','y','y','y','n','y','republican'],
            ['n','y','y','y','y','y','n','n','n','y','y','y','y','y','y','?','democrat' ],
            ['y','y','y','n','y','y','n','n','?','y','n','n','n','y','y','?','democrat' ],
            ['n','y','n','y','y','y','n','n','n','y','n','y','y','y','n','n','republican'],
            ['y','?','y','n','n','n','y','y','y','n','?','n','n','n','y','?','democrat' ],
            ['n','y','y','n','n','n','n','y','y','n','y','n','n','y','y','y','democrat' ],
            ['n','n','y','n','n','n','y','y','y','n','n','n','n','n','y','?','democrat' ],
            ['n','y','y','n','y','y','n','n','n','n','y','n','n','n','y','?','democrat' ],
            ['y','n','y','n','n','n','y','y','y','n','y','n','n','n','y','?','democrat' ],
            ['n','n','n','y','y','n','n','n','n','n','n','y','y','y','n','y','republican'],
            ['n','y','n','y','y','y','n','n','n','y','n','?','y','y','n','n','republican'],
            ['n','?','n','y','y','y','n','n','n','n','n','y','y','y','n','y','republican'],
            ['n','n','y','n','n','y','y','y','y','n','y','n','n','y','y','y','democrat' ],
            ['y','n','y','n','n','n','y','y','y','n','n','n','n','n','?','y','democrat' ],
            ['n','y','n','y','y','y','n','n','n','n','n','y','y','?','n','y','republican'],
            ['n','y','y','y','y','y','y','n','y','y','n','y','y','y','n','y','republican'],
            ['n','y','n','y','y','y','n','n','n','n','n','y','y','y','n','y','republican'],
            ['n','y','n','y','y','y','n','n','y','y','n','y','y','y','n','y','republican'],
            ['n','y','y','n','n','n','y','y','n','n','y','n','n','n','y','?','democrat' ],
            ['n','y','n','y','y','y','n','n','n','y','n','y','y','y','n','y','republican'],
            ['n','n','y','n','n','y','y','y','y','y','n','y','n','y','y','?','democrat' ],
            ['n','n','n','y','y','y','n','n','n','y','n','y','n','y','n','y','republican'],
            ['n','n','y','n','n','n','y','y','y','n','n','n','n','n','y','y','democrat' ],
            ['y','n','y','n','n','y','y','y','n','n','n','y','y','n','n','y','democrat' ],
            ['y','y','y','n','n','n','y','y','?','y','n','n','n','n','y','?','democrat' ],
            ['n','n','n','y','y','y','y','n','n','y','n','n','n','y','y','y','republican'],
            ['n','n','n','y','n','y','y','?','y','n','n','y','y','y','n','y','republican'],
            ['y','n','y','n','n','n','y','y','y','y','y','n','n','y','y','y','democrat' ],
            ['n','n','n','n','y','y','y','n','n','n','n','?','n','y','y','y','republican'],
            ['n','y','y','n','n','n','y','y','?','y','n','n','y','n','y','y','democrat' ],
            ['y','n','y','n','n','n','n','y','y','y','n','n','n','n','y','y','democrat' ],
            ['y','n','y','n','n','n','y','y','y','y','y','n','n','n','y','y','democrat' ],
            ['n','n','y','n','y','n','y','y','y','n','n','n','n','y','?','y','democrat' ],
            ['n','y','n','y','y','y','?','n','n','n','n','?','y','y','n','n','republican'],
            ['?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','?','republican'],
            ['y','n','y','n','n','n','y','y','?','n','y','n','n','n','y','y','democrat' ],
            ['n','y','n','y','y','y','n','n','n','n','n','y','y','y','n','n','republican'],
            ['n','y','n','y','y','y','n','n','n','n','n','y','y','y','n','n','republican'],
            ['y','y','y','n','n','y','y','y','y','n','n','n','n','n','y','y','democrat' ],
            ['n','y','n','y','y','y','n','n','n','n','n','y','y','y','n','y','republican'],
            ['y','n','y','n','n','n','y','y','y','y','n','n','n','n','n','y','democrat' ],
            ['y','n','y','n','n','n','y','y','y','y','n','n','n','y','y','y','democrat' ],
            ['n','n','n','y','y','n','n','n','n','n','n','y','n','y','n','n','republican'],
            ['n','n','n','y','y','n','n','n','n','n','n','y','n','y','?','y','republican'],
            ['n','n','y','n','n','n','y','y','y','n','y','n','n','n','y','y','democrat' ],
            ['y','n','y','n','n','n','y','y','y','n','n','n','n','n','n','y','democrat' ],
            ['y','n','y','n','n','n','y','y','y','y','n','n','n','n','n','y','democrat' ],
            ['y','n','y','n','n','?','y','y','y','n','?','?','n','?','?','?','democrat' ],
            ['y','n','y','n','n','n','y','y','y','y','n','n','?','n','y','y','democrat' ],
            ['y','n','y','n','n','n','y','y','y','n','n','n','n','n','y','?','democrat' ],
            ['y','n','y','n','n','n','y','y','y','n','n','n','n','n','y','?','democrat' ],
            ['y','n','y','n','n','n','y','y','y','y','n','n','n','n','n','y','democrat' ],
            ['n','n','n','y','y','y','n','n','n','y','n','y','n','y','n','y','republican'],
            ['y','n','n','n','n','n','y','y','y','y','n','n','n','y','n','y','republican'],
            ['y','n','y','n','n','n','y','y','y','n','n','n','n','n','y','?','democrat' ],
            ['y','n','y','n','n','n','y','y','y','n','n','n','n','n','n','y','democrat' ],
            ['y','y','y','n','n','n','y','y','y','n','n','n','n','n','y','y','democrat' ],
            ['n','y','y','n','n','y','y','y','y','n','?','n','n','n','n','y','democrat' ],
            ['y','n','y','n','n','n','y','y','y','y','n','n','n','n','y','?','democrat' ],
            ['n','n','n','y','y','n','y','y','n','y','n','y','y','y','?','y','republican'],
            ['y','n','n','y','y','n','y','n','n','y','n','n','n','y','y','y','republican'],
            ['n','n','y','n','y','y','n','n','n','n','?','n','y','y','n','n','democrat' ],
            ['n','n','n','y','y','y','n','n','n','n','n','y','y','y','y','n','republican'],
            ['n','n','y','y','y','y','y','y','n','y','n','n','n','y','n','y','republican'],
            ['n','n','n','y','y','y','n','n','n','n','n','y','y','y','n','y','republican']]






# Validation:
# ------------------------------------


valid=[['n','n','n','y','y','y','n','n','n','y','n','y','y','y','n','n','republican'],
       ['n','n','y','n','n','n','y','y','y','y','n','n','n','y','n','y','democrat'  ],
       ['y','n','y','y','y','y','y','y','n','n','n','n','n','y','n','?','republican'],
       ['y','n','n','y','y','y','n','n','n','y','n','?','y','y','n','n','republican'],
       ['n','n','n','y','y','y','n','n','n','n','n','y','y','y','n','y','republican'],
       ['n','n','y','n','n','y','y','y','y','y','y','n','n','n','?','y','democrat'  ],
       ['n','n','y','n','n','y','y','y','y','y','y','n','n','n','y','y','democrat'  ],
       ['n','n','y','n','n','y','?','y','?','y','y','y','n','y','y','?','democrat'  ],
       ['y','y','y','?','n','y','y','y','y','n','y','n','y','n','?','y','democrat'  ],
       ['y','y','y','n','y','y','n','y','n','y','y','n','y','y','y','y','democrat'  ],
       ['y','y','y','n','y','y','n','y','n','y','y','n','y','y','n','?','democrat'  ],
       ['y','n','y','n','?','y','?','y','y','y','n','n','y','y','n','y','democrat'  ],
       ['y','n','y','n','n','y','y','y','y','y','n','?','n','y','n','y','democrat'  ],
       ['y','n','y','n','n','y','y','y','n','y','y','n','y','y','y','y','democrat'  ],
       ['y','y','y','n','n','y','y','y','y','y','y','n','y','y','y','y','democrat'  ],
       ['n','y','y','n','n','y','y','y','n','y','y','n','y','y','n','?','democrat'  ],
       ['n','y','n','y','y','y','?','?','n','y','n','y','?','?','?','?','republican'],
       ['n','n','y','y','y','y','n','n','n','y','n','y','y','y','y','y','republican'],
       ['y','y','y','n','n','y','y','y','y','y','n','n','?','n','y','?','democrat'  ],
       ['n','y','n','n','n','n','y','y','y','y','y','n','n','n','y','y','democrat'  ],
       ['n','y','y','n','n','y','y','y','y','y','n','n','y','y','y','y','democrat'  ],
       ['n','n','n','y','y','n','y','y','y','y','n','y','y','y','n','y','republican'],
       ['n','n','?','n','n','y','y','y','y','n','n','n','n','n','y','y','democrat'  ],
       ['n','n','n','y','y','y','y','n','n','y','n','y','y','y','n','y','republican'],
       ['n','n','n','y','y','y','n','n','n','n','n','y','y','y','n','n','republican'],
       ['n','y','n','y','y','y','n','n','n','y','n','y','y','y','n','?','republican'],
       ['n','n','n','y','y','y','n','n','n','y','n','y','y','y','n','n','republican'],
       ['n','n','n','y','y','y','n','n','n','n','n','y','y','y','n','n','republican'],
       ['y','n','y','n','n','y','y','y','y','n','n','n','n','y','n','?','democrat'  ],
       ['n','n','n','y','y','y','n','n','n','y','n','y','y','y','n','n','republican'],
       ['y','n','n','n','n','y','y','y','y','y','n','n','n','y','y','y','democrat'  ],
       ['n','n','n','y','y','y','n','n','n','y','n','y','y','y','y','n','republican'],
       ['n','n','y','n','n','y','y','y','y','y','n','n','y','n','n','y','democrat'  ],
       ['y','y','y','n','n','n','y','y','y','y','n','n','n','n','y','y','democrat'  ],
       ['n','y','y','y','y','y','n','n','n','y','n','y','y','y','n','y','republican'],
       ['n','y','n','y','y','y','y','y','n','n','y','y','y','y','y','y','republican'],
       ['n','y','y','y','y','y','y','?','n','n','n','n','?','?','y','?','republican'],
       ['n','n','n','n','n','y','n','y','y','n','y','y','y','y','y','n','democrat'  ],
       ['y','n','n','n','n','n','y','y','y','y','n','n','n','n','y','y','democrat'  ],
       ['n','n','y','n','n','n','y','y','y','n','n','n','n','n','y','?','democrat'  ],
       ['y','n','y','n','n','n','y','y','y','n','n','n','n','n','y','?','democrat'  ],
       ['n','y','y','n','n','y','n','y','y','y','n','n','y','y','n','y','democrat'  ],
       ['y','y','y','n','n','n','y','y','y','y','n','n','y','n','n','y','democrat'  ],
       ['y','y','y','n','?','y','n','?','n','n','y','n','y','y','n','?','democrat'  ],
       ['y','y','y','n','y','y','n','y','?','y','n','n','y','y','n','?','democrat'  ],
       ['n','y','n','y','y','y','n','n','n','n','y','y','y','y','n','n','republican'],
       ['n','y','n','n','y','y','n','n','?','n','n','y','y','y','n','y','democrat'  ],
       ['y','y','n','y','n','n','y','y','y','n','y','n','n','y','n','y','democrat'  ],
       ['n','y','n','y','y','y','n','n','n','n','n','y','y','y','n','y','republican'],
       ['y','y','y','n','n','n','y','y','y','n','y','n','n','n','n','y','democrat'  ],
       ['y','?','y','n','n','y','y','y','y','y','n','n','n','n','y','?','democrat'  ],
       ['n','y','n','y','y','y','n','n','n','y','n','y','y','y','n','n','republican'],
       ['y','?','y','n','n','n','y','y','y','n','n','n','n','n','y','?','democrat'  ],
       ['y','n','y','n','n','n','y','y','y','n','y','n','n','n','y','?','democrat'  ],
       ['n','n','y','n','n','n','y','y','y','n','n','n','n','n','y','y','democrat'  ],
       ['n','y','y','n','n','y','y','y','?','n','y','y','n','n','y','y','democrat'  ],
       ['n','n','n','y','y','y','n','n','n','y','y','y','y','y','n','?','republican'],
       ['n','n','y','n','n','y','y','y','n','n','y','n','n','y','?','y','democrat'  ],
       ['y','n','y','n','n','n','y','y','y','n','n','n','n','n','y','y','democrat'  ],
       ['y','n','y','n','n','n','y','y','y','y','n','n','n','y','y','y','democrat'  ],
       ['y','n','n','y','y','y','n','n','n','n','y','y','y','y','n','n','republican'],
       ['n','n','n','y','y','y','n','n','n','y','y','y','n','y','n','y','republican'],
       ['n','?','y','?','n','y','y','y','y','y','y','n','?','?','y','y','democrat'  ],
       ['n','y','y','n','y','?','y','n','n','y','y','n','y','n','y','y','democrat'  ],
       ['n','n','n','y','y','n','y','n','y','y','n','n','n','y','n','y','republican'],
       ['n','n','y','n','n','n','y','y','y','y','y','n','n','n','y','y','democrat'  ],
       ['n','n','n','y','y','y','y','n','n','y','n','y','n','y','y','y','republican'],
       ['n','n','n','y','y','y','n','n','n','y','n','y','y','y','n','y','republican'],
       ['y','n','n','y','y','y','n','n','n','y','n','y','y','y','n','n','republican']]


# Test set
# ========


test=[['y','n','y','n','n','n','y','y','y','y','n','y','n','n','y','?','democrat'  ],
            ['n','y','y','y','y','y','y','y','y','n','n','y','y','y','n','y','republican'],
            ['n','y','n','n','n','y','y','n','y','n','y','n','n','n','y','y','democrat'  ],
            ['n','n','y','y','y','y','y','y','y','y','n','y','y','y','y','y','republican'],
            ['n','y','n','y','n','y','y','y','y','n','y','n','y','n','y','?','democrat'  ],
            ['n','n','y','y','y','y','y','n','n','y','y','y','y','y','n','y','republican'],
            ['n','y','y','n','n','y','y','y','y','y','n','?','n','n','y','y','democrat'  ],
            ['y','n','y','y','n','n','n','y','y','y','n','n','n','y','y','y','republican'],
            ['n','n','n','y','y','y','n','n','n','n','n','y','y','y','n','n','republican'],
            ['n','n','n','y','y','y','n','n','n','n','n','y','y','y','n','n','republican'],
            ['y','y','y','n','n','y','y','y','y','y','y','y','y','y','n','?','democrat'  ],
            ['n','n','n','y','y','y','n','n','n','y','?','y','y','y','n','y','republican'],
            ['y','n','y','n','n','y','y','y','y','y','n','n','y','n','n','y','democrat'  ],
            ['y','n','y','n','y','y','y','n','y','y','n','n','y','y','n','?','democrat'  ],
            ['y','y','y','n','n','y','y','y','y','y','y','y','y','n','n','y','democrat'  ],
            ['y','y','n','y','y','y','n','n','n','y','y','n','y','n','n','n','republican'],
            ['y','y','n','y','y','y','n','n','n','n','y','n','y','y','n','y','republican'],
            ['n','y','n','n','y','y','n','n','n','y','y','n','y','y','n','n','democrat'  ],
            ['y','n','y','n','n','n','y','y','n','y','y','n','n','n','n','?','democrat'  ],
            ['y','y','y','n','y','y','y','y','n','y','y','n','n','n','y','?','democrat'  ],
            ['n','y','y','n','n','y','y','y','n','y','n','n','n','n','y','y','democrat'  ],
            ['n','y','n','y','y','y','n','n','n','n','n','n','y','y','n','y','republican'],
            ['y','y','y','n','?','y','y','y','n','y','?','?','n','n','y','y','democrat'  ],
            ['y','y','y','n','?','n','y','y','y','y','n','n','n','n','y','?','democrat'  ],
            ['n','y','y','y','y','y','n','n','n','n','y','y','?','y','n','n','democrat'  ],
            ['n','y','y','?','y','y','n','y','n','y','?','n','y','y','?','y','democrat'  ],
            ['n','y','n','y','y','y','n','n','n','n','n','y','y','y','n','y','republican'],
            ['n','y','n','y','y','y','n','n','n','n','y','y','n','y','n','n','democrat'  ],
            ['y','?','y','n','n','n','y','y','y','n','y','n','n','n','y','y','democrat'  ],
            ['n','y','n','y','y','y','?','?','n','n','?','?','y','?','?','?','republican'],
            ['n','n','n','y','y','y','n','n','n','n','n','y','y','y','n','y','republican'],
            ['n','n','n','y','y','y','n','n','n','n','n','y','y','y','n','y','republican'],
            ['y','y','y','n','n','y','?','y','y','n','y','n','y','n','y','y','democrat'  ],
            ['y','y','y','n','y','y','y','y','y','y','y','n','y','y','n','?','democrat'  ],
            ['y','y','n','y','y','y','n','n','n','n','y','n','y','y','n','?','democrat'  ],
            ['y','y','y','n','y','y','n','y','y','y','y','n','n','n','n','y','democrat'  ],
            ['y','y','y','y','y','y','n','n','n','n','y','y','y','y','n','y','democrat'  ],
            ['y','y','n','n','y','y','n','n','n','n','y','y','y','y','y','n','democrat'  ],
            ['n','?','y','n','y','y','n','y','n','n','y','n','n','n','n','?','democrat'  ],
            ['y','y','y','n','y','y','n','y','y','n','y','n','n','y','n','?','democrat'  ],
            ['n','y','y','y','y','y','n','n','n','n','n','y','y','y','n','?','democrat'  ],
            ['y','n','y','n','n','n','y','y','y','?','y','n','n','n','y','?','democrat'  ],
            ['?','?','n','n','?','y','?','n','n','n','y','y','n','y','n','?','democrat'  ],
            ['y','y','n','n','n','n','n','y','y','n','y','n','n','n','y','n','democrat'  ],
            ['y','y','n','y','y','y','n','n','n','n','y','y','y','y','n','y','republican'],
            ['?','?','?','?','n','y','n','y','y','n','n','y','y','n','n','?','republican'],
            ['y','y','?','?','?','y','n','n','n','n','y','n','y','n','n','y','democrat'  ],
            ['y','y','y','?','n','n','n','y','n','n','y','?','n','n','y','y','democrat'  ],
            ['y','y','y','n','y','y','n','y','n','n','y','n','y','n','y','y','democrat'  ],
            ['y','y','n','n','y','?','n','n','n','n','y','n','y','y','n','y','democrat'  ],
            ['n','y','y','n','y','y','n','y','n','n','n','n','n','n','n','y','democrat'  ],
            ['n','y','n','y','?','y','n','n','n','y','n','y','y','y','n','n','republican'],
            ['n','y','n','y','y','y','n','?','n','n','?','?','?','y','n','?','republican'],
            ['n','y','n','y','y','y','n','n','n','y','y','y','y','y','n','n','republican'],
            ['?','n','y','y','n','y','y','y','y','y','n','y','n','y','n','y','republican'],
            ['n','y','n','y','y','y','n','n','n','y','n','y','?','y','n','n','republican'],
            ['y','y','n','y','y','y','n','n','n','y','n','y','y','y','n','y','republican'],
            ['n','n','n','y','y','y','n','n','n','n','n','y','y','y','n','y','republican'],
            ['y','n','y','n','y','y','n','n','y','y','n','n','y','y','n','y','democrat'  ],
            ['n','n','n','y','y','y','n','n','n','n','y','y','y','y','n','n','democrat'  ],
            ['y','n','y','n','n','y','y','y','y','n','n','y','?','y','y','y','democrat'  ],
            ['n','n','n','y','y','y','n','n','n','n','n','y','y','y','n','n','republican'],
            ['n','n','n','y','y','y','n','n','n','n','y','y','y','y','n','y','republican'],
            ['y','n','y','n','n','y','y','y','y','y','y','n','n','n','n','y','democrat'  ],
            ['n','n','n','y','y','y','n','n','n','y','n','y','y','y','n','y','republican'],
            ['y','y','y','y','y','y','y','y','n','y','?','?','?','y','n','y','republican'],
            ['y','y','y','n','n','n','y','y','y','n','n','n','n','n','n','y','democrat'  ],
            ['n','y','y','n','n','y','y','y','?','y','n','n','n','n','n','y','democrat'  ],
            ['y','y','n','y','y','y','n','n','n','y','n','n','y','y','n','y','republican'],
            ['y','y','y','n','n','n','y','y','y','y','y','n','y','n','n','y','democrat'  ],
            ['y','y','y','n','n','n','y','y','n','y','n','n','n','n','n','y','democrat'  ],
            ['y','y','y','n','n','n','y','y','y','n','n','n','n','n','n','y','democrat'  ],
            ['y','y','y','y','y','y','y','y','n','y','n','n','y','y','n','y','republican'],
            ['n','y','y','n','y','y','y','y','n','n','y','n','y','n','y','y','democrat'  ],
            ['n','n','y','n','n','y','y','y','y','n','y','n','n','n','y','y','democrat'  ],
            ['n','y','y','n','n','y','y','y','y','n','y','n','n','y','y','y','democrat'  ],
            ['n','y','y','n','n','?','y','y','y','y','y','n','?','y','y','y','democrat'  ],
            ['n','n','y','n','n','n','y','y','n','y','y','n','n','n','y','?','democrat'  ],
            ['y','n','y','n','n','n','y','y','y','y','n','n','n','n','y','y','democrat'  ],
            ['n','n','n','y','y','y','y','y','n','y','n','y','y','y','n','y','republican'],
            ['?','?','?','n','n','n','y','y','y','y','n','n','y','n','y','y','democrat'  ],
            ['y','n','y','n','?','n','y','y','y','y','n','y','n','?','y','y','democrat'  ],
            ['n','n','y','y','y','y','n','n','y','y','n','y','y','y','n','y','republican'],
            ['n','n','y','n','n','n','y','y','y','y','n','n','n','n','n','y','democrat'  ],
            ['n','?','n','y','y','y','n','n','n','n','y','y','y','y','n','y','republican'],
            ['n','n','n','y','y','y','?','?','?','?','n','y','y','y','n','y','republican'],
            ['n','y','n','y','y','y','n','n','n','y','n','y','y','y','?','n','republican']]
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
