"""
AUTHOR: IRENE CHEN
GITHUB: theirenechen12.github.io
DATE: 2025-03-03

This Python code implements the Gary De'Snake Algorithm. This algorithm determines the gender of a character based on the following factors:

a = Gender of object posessed (0 = male, 1 = female, inf = unknown))
b = Gender of lineage (0 = male, 1 = female, inf = unknown)
c = Gender of opposing lineage (0 = male, 1 = female, inf = unknown)
d = Femininity of voice (1–5 = masculine, 6–10 = feminine, inf = unknown)
e = Name of character (optional for output purposes)

The algorithm is used to prove that Gary De'Snake is actually female rather than male. However, this is a general algorithm that can also be applied to other characters (test cases). 

In addition, not only is this algorithm used to determine the gender of a character, like in this example, but it can also be applied to real-world scenarios such as:
1. Hiring or selection decisions for a job or college
2. Survival analysis for a major disaster
3. Finance or credit risk
4. Health risk prediction

All of these scenarios involve making a decision based on multiple factors, some of which may be ambiguous or unknown, which is represented by float('inf'). The Gary De'Snake Algorithm provides a systematic approach for making decisions based on these factors.
"""

"""
This function combines the factors b (gender of lineage) and c (gender of opposing lineage) to determine the lineage's gender and assess whether the lineage is a deterministic factor in the character's gender. 
The returned value merges b and c into a single factor: lineage gender.
We need a separate function to extract the lineage gender as a single factor for the determine_gender function, which is the main function for determining the character's gender based on the object, lineage, and voice factors. 
"""
def determine_character_lineage(character):
    if character[1] == float('inf') and character[2] == float('inf'): #Genders of the lineage and opposing lineage unknown
        return float('inf') #If the gender of the lineages are unknown, then the gender of lineage is unknown.
    elif character[1] == character[2]: #Gender of the lineage and opposing lineage are the same
        return float('inf') #If the gender of the lineages are the same, then the gender of lineage is unknown because they must be opposite to impact gender. For Gary De'Snake, her lineage is a matriarchy and her opposing lineage is a patriarchy, so they are opposite, which is why her lineage is female, but if they were the same, then the gender of lineage would be unknown because they would not impact the gender of the character.
    elif character[1] != float('inf') and character[2] == float('inf'): #Gender of the lineage is known but the gender of the opposing lineage is unknown
        return float('inf') #If the gender of the lineage is known but the gender of the opposing lineage is unknown, then the gender of lineage is unknown because both the lineage and opposing lineage must be known to impact the gender of the character. 
    elif character[1] == float('inf') and character[2] != float('inf'): #Gender of the lineage is unknown but the gender of the opposing lineage is known
        return float('inf') #If the gender of the lineage is unknown but the gender of the opposing lineage is known, then the gender of lineage is unknown because both the lineage and opposing lineage must be known to impact the gender of the character.
    elif (character[1] == 0 and character[2] == 1): #Gender of the lineage is male and the gender of the opposing lineage is female
        return 0  #If the gender of the lineage is male and the gender of the opposing lineage is female, then the gender of lineage is male because the male lineage is dominant in determining the gender of the character.
    elif (character[1] == 1 and character[2] == 0): #Gender of the lineage is female and the gender of the opposing lineage is male
        return 1 #If the gender of the lineage is female and the gender of the opposing lineage is male, then the gender of lineage is female because the female lineage is dominant in determining the gender of the character.  
    else: #This case accounts for any other cases that may arise that are not accounted for in the above cases, such as if the values of lineage and opposing lineage are not 0, 1, or float('inf'), which is not expected but is included for completeness.
        return float('inf') #If the values of lineage and opposing lineage are not accounted for in the above cases, then the gender of lineage is unknown because it does not fit into any of the expected cases.

"""
This function determines the gender of the character based on the object possessed, lineage, and voice. 
Object possessed is obtained from object element of the character list
Lineage is obtained from the determine_character_lineage function, which merges the factors of lineage and opposing lineage together to
Voice is obtained from voice element of the character list

We define the following variables for the factors of the character to make the code more readable:
object_gender = Gender of object possessed
lineage_gender = Gender of lineage
voice_gender = Gender of voice
name = Name of character (optional for output purposes)

It uses the list to evaluate different cases and determine the character's gender based on the factors of object, lineage, and voice. It also accounts for cases where some of the factors are ambiguous or unknown.
It then prints the character's gender based on the specified factors.

There are 7 cases for male, 7 for female, and 1 for unknown/conflicting, for a total of 15 cases used to determine the character's gender based on the factors of object, lineage, and voice. The cases are as follows:

Object male, lineage male, voice masculine
Object male, lineage male, voice unknown/conflicting
Object male, lineage unknown/conflicting, voice masculine
Object male, lineage unknown/conflicting, voice unknown/conflicting
Object unknown, lineage male, voice masculine
Object unknown, lineage male, voice unknown/conflicting
Object unknown, lineage unknown/conflicting, voice masculine

Object female, lineage female, voice feminine
Object female, lineage female, voice unknown/conflicting
Object female, lineage unknown/conflicting, voice feminine
Object female, lineage unknown/conflicting, voice unknown/conflicting
Object unknown, lineage female, voice feminine
Object unknown, lineage female, voice unknown/conflicting
Object unknown, lineage unknown/conflicting, voice feminine

Object unknown, lineage unknown/conflicting, voice unknown/conflicting
"""

def determine_gender(character):
    object_gender = character[0] #Define variable for the gender of the object possessed
    lineage_gender = determine_character_lineage(character) #Define variable for the gender of the lineage
    voice_gender = character[3] #Define variable for the gender of the voice
    name = character[4] #Define variable for the name of the character

    #Object male, lineage male, voice masculine
    if(object_gender == 0 and lineage_gender == 0 and voice_gender <= 5 and voice_gender >= 1):
        print("The gender of",name,"is male by object, lineage, and voice")

    #Object male, lineage male, voice unknown/conflicting
    elif(object_gender == 0 and lineage_gender == 0 and voice_gender == float('inf')):
        print("The gender of",name,"is male by object and lineage, but the voice is unknown")

    #Object male, lineage unknown/conflicting, voice masculine
    elif(object_gender == 0 and lineage_gender == float('inf') and voice_gender <= 5 and voice_gender >= 1):
        print("The gender of",name,"is male by object and voice, but the lineage is unknown")

    #Object male, lineage unknown/conflicting, voice unknown/conflicting
    elif(object_gender == 0 and lineage_gender == float('inf') and voice_gender == float('inf')):
        print("The gender of",name," is male by object alone, but the lineage and voice are unknown")

    #Object unknown/conflicting, lineage male, voice masculine
    elif(object_gender == float('inf') and lineage_gender == 0 and voice_gender <= 5 and voice_gender >= 1):
        print("The gender of",name,"is male by lineage and voice, but the object is unknown")

    #Object unknown/conflicting, lineage male, voice unknown/conflicting
    elif(object_gender == float('inf') and lineage_gender == 0 and voice_gender == float('inf')):
        print("The gender of",name,"is male by lineage alone, but the object and voice are unknown")

    #Object unknown/conflicting, lineage unknown/conflicting, voice masculine
    elif(object_gender == float('inf') and lineage_gender == float('inf') and voice_gender <= 5 and voice_gender >= 1):
        print("The gender of",name,"is male by voice alone, but the object and lineage are unknown")   

    #Object female, lineage female, voice feminine
    elif (object_gender == 1 and lineage_gender == 1 and voice_gender <= 10 and voice_gender >= 6):
        print("The gender of",name,"is female by object, lineage, and voice") 

    #Object female, lineage female, voice unknown/conflicting
    elif(object_gender == 1 and lineage_gender == 1 and voice_gender == float('inf')):
        print("The gender of",name,"is female by object and lineage, but the voice is unknown")

    #Object female, lineage unknown/conflicting, voice feminine
    elif(object_gender == 1 and lineage_gender == float('inf') and voice_gender <= 10 and voice_gender >= 6):
        print("The gender of",name,"is female by object and voice, but the lineage is unknown")

    #Object female, lineage unknown/conflicting, voice unknown/conflicting 
    elif(object_gender == 1 and lineage_gender == float('inf') and voice_gender == float('inf')):
        print("The gender of",name,"is female by object alone, but the lineage and voice are unknown")

    #Object unknown/conflicting, lineage female, voice feminine
    elif(object_gender == float('inf') and lineage_gender == 1 and voice_gender <= 10 and voice_gender >= 6):
        print("The gender of",name,"is female by lineage and voice, but the object is unknown")

    #Object unknown/conflicting, lineage female, voice unknown/conflicting
    elif(object_gender == float('inf') and lineage_gender == 1 and voice_gender == float('inf')):
        print("The gender of",name,"is female by lineage alone, but the object and voice are unknown")       

    #Object unknown/conflicting, lineage unknown/conflicting, voice feminine
    elif(object_gender == float('inf') and lineage_gender == float('inf') and voice_gender <= 10 and voice_gender >= 6):
        print("The gender of",name,"is female by voice alone, but the object and lineage are unknown")
    
    #Object unknown/conflicting, lineage unknown/conflicting, voice unknown/conflicting
    else:
        print("The gender of",name,"cannot be determined based on the given factors of object, lineage, and voice")

    
        
#Test cases for the algorithm. All are Zootopia characters.
gary = [1,1,0,6,"Gary De'Snake"] #Base case. We are developing an algorithm to disprove Gary De'Snake's claim to be male. In the story, she has an anti-venom pen, which is a feminine object because it is voiced by Auliʻi Cravalho, a female voice actor, and because she comes from a matriarchy and opposes patriarchy, her lineage is female. Although she is voiced by Ke Huy Quan, who is male, he made her voice more feminine, which exceeds the 5 threshold due to the pitch, so her voice is feminine. Therefore, by object, lineage, and voice, Gary De'Snake is female, disproving the claim that Gary De'Snake is male. This is the base case the algorithm aims to prove, laying the foundation for the algorithm.
judy = [1,float('inf'),float('inf'),10,"Judy Hopps"] #Judy Hopps has a carrot pen, which is a feminine object, but her lineage and opposing lineage are unknown, and her voice is feminine. Therefore, by object and voice, Judy Hopps is female.
nick = [float('inf'),1,float('inf'),3,"Nick Wilde"] #Nick Wilde does not have a clear gendered object; his lineage and opposing lineage are unknown, but his voice is masculine. Therefore, by voice, Nick Wilde is male.
pawbert = [float('inf'),0,1,4, "Pawbert Lynxley"] #Pawbert Lynxley has no object to determine gender, but his lineage is male, and his opposing lineage is female, and his voice is masculine. Therefore, by lineage and voice, Pawbert Lynxley is male.
pawbert_and_gary = [1,float('inf'),float('inf'),5, "Pawbert and Gary"] #Pawbert and Gary have a shared object, Gary's Anti-venom pen, which is feminine, but their lineage and opposing lineage are unknown because the two are opposites. Their voice is the average of both, which is male because it equals 5. Therefore, the gender of Pawbert and Gary cannot be determined.
nibbles = [float('inf'),float('inf'),float('inf'),6, "Nibbles Maplestick"]#Nibbles Maplestick has no object to determine gender; she has no lineage, but her voice is feminine. Therefore, by voice, Nibbles Maplestick is female. 

determine_gender(gary) #base case
determine_gender(judy)
determine_gender(nick)
determine_gender(pawbert)
determine_gender(pawbert_and_gary)
determine_gender(nibbles)
