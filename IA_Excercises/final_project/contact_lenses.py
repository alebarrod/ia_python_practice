# ------------------------------
# Artificial Intelligence.
# Grado Ingeniería Informática 
# credit.py
# ------------------------------

# Data describing when to recommend contact lenses, dpending on the following
#     attributes: 
 
#     * Age of the patient: (1) young, (2) pre-presbyopic, (3) presbyopic
#     * Spectacle prescription:  (1) myope, (2) hypermetrope
#     * Astigmatic:     (1) no, (2) yes
#     * Tear production rate:  (1) reduced, (2) normal


#     Classes:
#      Hard : the patient should be fitted with hard contact lenses,
#      Soft : the patient should be fitted with soft contact lenses,
#      None : the patient should not be fitted with contact lenses.
 




attributes=[("Age",["Young", "Pre-presbyopic", "Presbyopic"]),
           ("Prescription",['Myope','Hypermetrope']),
           ("Astigmatic",['+','-']),
           ("Tear rate",['Reduced','Normal'])]

class_name='Lens'
classes=['None','Soft','Hard']



train=[["Young","Myope","-","Reduced","None"],
      ["Young","Myope","-","Normal","Soft"], 
      ["Young","Myope", "+","Reduced","None"],
      ["Young","Myope","+","Normal","Hard"], 
      ["Young","Hypermetrope","-","Reduced","None"],
      ["Young","Hypermetrope","-","Normal","Soft"], 
      ["Young", "Hypermetrope","+","Reduced","None"],
      ["Young", "Hypermetrope","+","Normal","Hard"],
      ["Pre-presbyopic","Myope","-","Reduced","None"],
      ["Pre-presbyopic","Myope","-","Normal","Soft" ],
      ["Pre-presbyopic","Myope","+","Reduced","None"],
      ["Pre-presbyopic","Myope","+","Normal","Hard"],
      ["Pre-presbyopic","Hypermetrope","-","Reduced","None"],
      ["Pre-presbyopic","Hypermetrope","-","Normal","Soft"],
      ["Pre-presbyopic","Hypermetrope","+","Reduced","None"],
      ["Pre-presbyopic","Hypermetrope","+","Normal","None"],
      ["Presbyopic","Myope","-","Reduced","None"],
      ["Presbyopic","Myope","-","Normal","None"],
      ["Presbyopic","Myope","+","Reduced","None"],
      ["Presbyopic","Myope","+","Normal","Hard"],
      ["Presbyopic","Hypermetrope","-", "Reduced","None"],
      ["Presbyopic","Hypermetrope","-","Normal","Soft"], 
      ["Presbyopic","Hypermetrope","+","Reduced","None"],
      ["Presbyopic","Hypermetrope","+","Normal","None"]]


