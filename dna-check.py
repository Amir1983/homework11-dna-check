


#Hair color:
black = "CCAGCAATCGC"
brown = "GCCAGTGCCG"
blonde = "TTAGCTATCGC"

#Facial shape:

square = "GCCACGG"
round = "ACCACAA"
oval = "AGGCCTCA"

#Eye color:

blue = "TTGTGGTGGC"
green = "GGGAGGTGGC"
brown2 = "AAGTAGTGAC"

#Gender:
female = "TGAAGGACCTTC"
male = "TGCAGGAACTTC"

#Race:
white = "AAAACCTCA"
black = "CGACTACAG"
asian = "CGCGGGCCG"

eva = {
"gender": female,
"race": white,
"hair_color": blonde,
"eye_color": blue,
"face_shape": oval}


larisa = {
"gender": female,
"race": white,
"hair_color": brown,
"eye_color": brown2,
"face_shape": oval}


matej = {
"gender": male,
"race": white,
"hair_color": black,
"eye_color": blue,
"face_shape": oval}


miha = {
"gender": male,
"race": white,
"hair_color": brown,
"eye_color": green,
"face_shape": square,
}

with open("gangstar_dna.txt", "r") as gangstar_dna_file:

    gangstar_dna = gangstar_dna_file.read()

gangstar_finder  = {}

if black in gangstar_dna:

    gangstar_finder.update({"hair_color": black})
elif brown in gangstar_dna:

    gangstar_finder.update({"hair_color": brown})
elif blonde in gangstar_dna:

    gangstar_finder.update({"hair_color": blonde})

if square in gangstar_dna:

    gangstar_finder.update({"face_shape": square})
elif round in gangstar_dna:

    gangstar_finder.update({"face_shape": round})
elif oval in gangstar_dna:

    gangstar_finder.update({"face_shape": oval})


if blue in gangstar_dna:

    gangstar_finder.update({"eye_color": blue})
elif green in gangstar_dna:

    gangstar_finder.update({"eye_color": green})
elif brown2 in gangstar_dna:

    gangstar_finder.update({"eye_color": brown2})

if female in gangstar_dna:

    gangstar_finder.update({"gender": female})
elif male in gangstar_dna:

    gangstar_finder.update({"gender": male})

if white in gangstar_dna:

    gangstar_finder.update({"race": white})
elif black in gangstar_dna:

    gangstar_finder.update({"race": black})
elif asian in gangstar_dna:

    gangstar_finder.update({"race": asian})


if gangstar_finder == eva:
    print("Eva is the Ganstar")
elif gangstar_finder == larisa:
    print("Larisa is the Gangstar")
elif gangstar_finder == matej:
    print("matej is the Gangstar")
elif gangstar_finder == miha:
    print("Miha is the Gangstar")
else:
    print("Nobody")

