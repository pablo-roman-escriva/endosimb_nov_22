import pandas as pd

def extract_genomes(filename, sheet_name, column, value):
    df = pd.read_excel(filename, sheet_name=sheet_name, skiprows=1)
    df2 = df[df[column]==value]
    df2 = df2[["Accession", "Habitat"]]
    df3 = pd.read_excel(filename, sheet_name="metrics", skiprows=1)
    df3 = df3[["Genome", "GS"]]
    df3 = df3.rename(columns={"Genome":"Accession"})
    print(df3)
    df4 = pd.merge(df2, df3, on="Accession")
    print(df4)    
