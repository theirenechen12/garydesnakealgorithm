# Summary
The Gary De’Snake Algorithm (GDSA) is an algorithm that I myself developed during my free time as a master's student at California State University, Los Angeles. I developed this algorithm not only as someone passionate about computer science wanting to apply it to the real world, but as someone passionate about social dynamics in film and entertainment as a whole. This algorithm combines my interests with the skills I learned in computer science to develop an algorithm that deterministically classifies the gender of an individual using various elements.

# Origin
This algorithm was first developed with one of my favorite characters, Gary De'Snake, in my mind and is named after her. Before getting into the algorithm, who is Gary De'Snake? Gary De'Snake is a female pit viper and the tritagonist of *Zootopia 2*, which was released on November 26, 2025. She is a 10-meter-long blue-scaled pit viper (*Trimeresurus insularis*), and in real life, these can be found in eastern Java and the Lesser Sunda Islands. While the pit viper is often seen as poisonous, her role as one of the heroines of *Zootopia 2* defies those stereotypes.

Ever since *Zootopia 2* came out, Gary has been rising in popularity, especially in Asian countries like China and Vietnam. While many claim that Gary is a male character and she is referred to with male pronouns throughout the film, there is proof that she is actually, in fact, a girl. 
1. Gary uses an autoinjector filled with antivenom in case her venomous fangs accidentally stab someone, known as the Anti-Venom Pen. On top of the autoinjector is a head resembling her own face. The autoinjector is voiced by Auliʻi Cravalho, who voices Moana in the Disney movie franchise of the same name.
2. Gary comes from a matriarchal family, descended from Agnes De'Snake, her great-grandmother, who is revealed to be the true founder of Zootopia, whose credit was stolen by Ebenezer Lynxley.
3. The De'Snake and Lynxley have an ongoing family feud, and because Ebenezer Lynxley successfully framed Agnes De'Snake for the murder of his tortoise maid, this led to the reputation of reptiles being destroyed and the families hating each other. Gary was the former "partner" turned archenemy of Pawbert Lynxley, the great-grandson of Ebenezer Lynxley and the son of Milton Lynxley (the film's main antagonist), and she was smuggled into Zootopia by Pawbert so he could manipulate her to protect his great-grandfather's "legacy" so he can be loved by his father. Meanwhile, Gary's motive was to prove her great-grandmother was the true founder of Zootopia. While the De'Snake family is a matriarchy, the Lynxley family is a patriarchy, and as such, Gary has feminist symbols.
4. While Gary was voiced by Ke Huy Quan (Jonathan Ke Quan), a Vietnamese-American male actor whose accolades include an Academy Award, a Golden Globe Award, and a Saturn Award, in addition to a BAFTA nomination, Quan's voice as Gary is more childlike and feminine/neutral compared to his normal voice in other roles.

All of that proves Gary De'Snake is a female character, and these traits build the foundation for this algorithm.

# The Algorithm

As previously discussed, this algorithm derives from the reasoning behind why Gary De'Snake is actually a female character. The main parameters we discussed include her Anti-Venom Pen (female), her family legacy (matriarchal), her opposing family due to family feud (patriarchal), and the extent to which her voice is feminized/feminine (greater than 5 on a scale from 0 to 10). This algorithm applies these four parameters in a general setting, respectively, where:

```
a = Gender of object posessed (0 = male, 1 for female)
b = Gender of lineage (0 = male, 1 = female)
c = Gender of opposing lineage (0 = male, 1 = female)
d = Femininity of voice (1–5 = masculine, 6–10 = feminine, inf = unknown)
```

These four parameters are stored in an array `[a, b, c, d]` where the array represents the individual we want to determine the gender of. If any of these four parameters are not defined, we define them as `float('inf')` in Python (INF), as when unknown, this leads to multiple possibilities, which are left unknown. A fifth parameter `e` can also be added, though `e = Name of character` and is optional, mostly for printing purposes. If `e` is added, the array would instead be `[a, b, c, d, e]`.

We define the `DetermineLineage(character)` function that determines the character's lineage. We need this function to merge b and c into a single variable, lineage. 

```
FUNCTION DetermineCharacterLineage(character):

    lineage = character[1]
    opposing_lineage = character[2]

    IF lineage == INF AND opposing_lineage == INF:
        RETURN INF

    ELSE IF lineage == opposing_lineage:
        RETURN INF

    ELSE IF lineage == INF OR opposing_lineage == INF:
        RETURN INF

    ELSE IF lineage == 0 AND opposing_lineage == 1:
        RETURN 0

    ELSE IF lineage == 1 AND opposing_lineage == 0:
        RETURN 1

    ELSE:
        RETURN INF

END FUNCTION
```
The `determine_character_lineage` function merges these two variables (b (lineage) and c (opposing lineage)) into a single factor: lineage. If both values are not defined (INF), it returns INF. If b and c are defined, but equal to each other, the result is still INF because the contrast between lineages is required for lineage to be a meaningful factor. If either b or c is not defined, the result is still INF because both must be known to determine dominance. If b and c are opposite (0 vs 1), then the lineage gender is returned based on the value of b. Any unexpected values default to INF. Thus, lineage only becomes deterministic when both lineages are known and opposite.

Now let's define the main function `DetermineGender(character)`:

```
FUNCTION DetermineGender(character):

    object_gender  = character[0]
    lineage_gender = DetermineCharacterLineage(character)
    voice_gender   = character[3]
    name           = character[4]

    ------------------------------------------------
    -- MALE CASES
    ------------------------------------------------

    IF object_gender == 0 AND lineage_gender == 0 AND 1 ≤ voice_gender ≤ 5:
        PRINT name + " is male by object, lineage, and voice"

    ELSE IF object_gender == 0 AND lineage_gender == 0 AND voice_gender == INF:
        PRINT name + " is male by object and lineage"

    ELSE IF object_gender == 0 AND lineage_gender == INF AND 1 ≤ voice_gender ≤ 5:
        PRINT name + " is male by object and voice"

    ELSE IF object_gender == 0 AND lineage_gender == INF AND voice_gender == INF:
        PRINT name + " is male by object alone"

    ELSE IF object_gender == INF AND lineage_gender == 0 AND 1 ≤ voice_gender ≤ 5:
        PRINT name + " is male by lineage and voice"

    ELSE IF object_gender == INF AND lineage_gender == 0 AND voice_gender == INF:
        PRINT name + " is male by lineage alone"

    ELSE IF object_gender == INF AND lineage_gender == INF AND 1 ≤ voice_gender ≤ 5:
        PRINT name + " is male by voice alone"

    ------------------------------------------------
    -- FEMALE CASES
    ------------------------------------------------

    ELSE IF object_gender == 1 AND lineage_gender == 1 AND 6 ≤ voice_gender ≤ 10:
        PRINT name + " is female by object, lineage, and voice"

    ELSE IF object_gender == 1 AND lineage_gender == 1 AND voice_gender == INF:
        PRINT name + " is female by object and lineage"

    ELSE IF object_gender == 1 AND lineage_gender == INF AND 6 ≤ voice_gender ≤ 10:
        PRINT name + " is female by object and voice"

    ELSE IF object_gender == 1 AND lineage_gender == INF AND voice_gender == INF:
        PRINT name + " is female by object alone"

    ELSE IF object_gender == INF AND lineage_gender == 1 AND 6 ≤ voice_gender ≤ 10:
        PRINT name + " is female by lineage and voice"

    ELSE IF object_gender == INF AND lineage_gender == 1 AND voice_gender == INF:
        PRINT name + " is female by lineage alone"

    ELSE IF object_gender == INF AND lineage_gender == INF AND 6 ≤ voice_gender ≤ 10:
        PRINT name + " is female by voice alone"

    ------------------------------------------------
    -- UNKNOWN / CONFLICTING CASE
    ------------------------------------------------

    ELSE:
        PRINT name + "'s gender cannot be determined"

END FUNCTION
```
We first define the parameters object_gender (derived from a), lineage_gender (derived from the merged variable obtained for b and c from the ``DetermineCharacterLineage(character)`` function), voice_gender (d), and the character’s name (e). These values are stored in a list and extracted individually inside the main function. The lineage value is obtained through a separate function that merges the lineage and opposing lineage into a single deterministic factor.

The algorithm does not prioritize one factor over another. Instead, it evaluates all three factors (object, lineage, and voice) simultaneously and matches them against fifteen explicitly defined cases. These cases represent all consistent male combinations, all consistent female combinations, and one final case for conflicting or fully unknown inputs.

If the object, lineage, and voice are consistent (e.g., all indicate female), the gender is determined with the strongest justification (by object, lineage, and voice). If only one or two deterministic factors are available and they agree, gender is determined based on those available factors. If the factors conflict or are entirely unknown, the gender cannot be determined.

For example, in Gary’s case:
	•	Object gender a = 1 (female)
	•	Lineage value = 1 (female, from matriarchy vs patriarchy)
	•	Voice score d = 6 (feminine range)

Since all three deterministic factors indicate female, the algorithm classifies Gary as female by object, lineage, and voice.

# Application

This algorithm is theoretical and requires several parameters to determine gender, so it is not always accurate. In addition, it is more used for symbolic gender. It does not only apply to gender, but to other real-world applications, such as:
1. Hiring or selection decisions for a job or college
   ```
   a = Candidate’s portfolio and achievements (0 = weak, 1 = strong, inf = unknown)
   b = Academic or mentorship background (0 = not competitive, 1 = competitive, inf = unknown)
   c = Academic or mentorship background of competitor (0 = not competitive, 1 = competitive, inf = unknown)
   d = Interview performance (1–5 = low, 6–10 = high, inf = unknown)
   ```
2. Survival analysis for a major disaster
   ```
   a = Lifeboat access or personal gear (0 = no, 1 = has, inf = unknown)
   b = Family or social group (0 = men-dominated (low priority), 1 = women/children-dominated (high priority), inf = unknown)
   c = Competing passengers for resources (0 = low competition, 1 = high competition, inf = unknown)
   d = Health / physical strength  (1–5 = low, 6–10 = high, inf = unknown)
   ```
3. Finance or credit risk
   ```
   a = Collateral / assets (0 = low, 1 = sufficient, inf = unknown)
   b = Credit history (0 = poor, 1 = strong, inf = unknown)
   c = Market risk / competing financial obligations (0 = low, 1 = high, inf = unknown)
   d = Income / cash flow strength (1–5 = low, 6–10 = high, inf = unknown)
   ```
4. Health risk prediction
   ```
   a = Lifestyle factors (exercise, diet) (0 = poor, 1 = healthy, inf = unknown)
   b = Family history / genetics (0 = high-risk, 1 = low-risk, inf = unknown)
   c = Environmental / social stressors (0 = low, 1 = high, inf = unknown)
   d = Biomarkers / clinical measurements (1–5 = low risk, 6–10 = high risk, inf = unknown)
   ```

All of these applications can help predict, though it has limitations, since only four factors are taken into account. If a factor is missing, it may give an incorrect solution due to missing factors.

