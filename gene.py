chromosome1=["BRCA1","her1","her2","vgfr"]
chromosome2=["cdk1","CDK2","cdk6"]
chromosome3=["p53","PAX","RB","BCL2","INK4A"]


name_gene=input("enter a name:")

if name_gene in chromosome1:
    print(f"{name_gene} is found in chromosome 1")
elif name_gene in chromosome2:
    print(f"{name_gene} is found in chromosome 2")
elif name_gene in chromosome3:
    print(f"{name_gene} is found in chromosome 3")
else:
    print("gene not found")
    print("amzaing chro,o")
