# Suppose that we have performed B Cell epitopes prediction from two websites

bcell_iedb={"ANPYFSQRMTPYVPKQKKVTKKLRTTTSKPSNKKPDSVRAIDSNATN",
            "S","PSIPI","NEKVTKGAP","KVTKAAGAP","KVTKGAP","LSISDYFIPLEKSTLVPKK","GAPNLET",
            "WMDPQKLAALRELVPEIPKIWADL","LSISDYFIPLEKSTLVPKK","LRTTTSKPSN"
             }

bcell_bepipred={"ANPYFSQRMTPYVPKQKKVTKKKKPDSVRAIDSNATN",
                "S","PSIPI","NEKVTKGAP","KVTKGAP","LSISDYFIPLEKSTLVPKK","GAPNLET",
                "WMDPQKLAALRELVPEIPKIWADL","LSISDYFIPLEKSTLVPKK","LRTTTSKPSN"
               }

# 1. Count the no of epitopes that are common in iedb and bepipred prediction.

common_epitopes=bcell_iedb&bcell_bepipred
print("No. of epitopes that are common: ",len(common_epitopes))

#2. Count the no of epiotopes that are present in only iedb b cell prediction

only_in_iedb=bcell_iedb-bcell_bepipred
print("No. of epitopes only in iedb b cell prediction: ",len(only_in_iedb))

#3. Count the no of epiotopes that are present in any of the epitopes but not in both
singular_epitopes=bcell_iedb^bcell_bepipred
print("Epitopes that are not common: ",len(singular_epitopes))

# 4. Find the total no of uniques epitopes.

print("Unique to bcell_bepipred: ",bcell_bepipred-bcell_iedb)
print("Unique to bcell_iedb: ",bcell_iedb-bcell_bepipred)
singular_epitopes=bcell_iedb^bcell_bepipred
print("Total nuo. of unique epitopes: ",len(singular_epitopes))



