import pandas as pd

# Läs in Excel-filen
filepath = "riket2023åk9_np.xlsx"

# Läs in specifikt sheet (exempel: "Matematik") och justera hoppa över rader
df = pd.read_excel(file_path, sheet_name="Matematik", skiprows=4, header=0)

# Sätt om kolumnnamnen så att de matchar uppgiften
df.columns = ["Plats", "Huvudman", "Totalt (A-F)", "Flickor (A-F)", "Pojkar (A-F)",
              "Totalt (A-E)", "Flickor (A-E)", "Pojkar (A-E)",
              "Totalt (poäng)", "Flickor (poäng)", "Pojkar (poäng)"]

# Droppa tomma rader om det fortfarande finns skräp
df = df.dropna(how="all")

# Visa resultat
print(df)
