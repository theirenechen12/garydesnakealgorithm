# Summary
The Gary De’Snake Algorithm (GDSA) is an algorithm that I developed, which deterministically classifies a person’s gender using various elements. It handles missing and conflicting data through decision rules

# Origin
Gary De'Snake is a pit viper and the tritagonist of *Zootopia 2*, which was released on November 26, 2025. She is a 10-meter-long blue-scaled pit viper (*Trimeresurus insularis*), and in real life, these can be found in eastern Java and the Lesser Sunda Islands. While the pit viper is often seen as poisonous, her role as one of the heroines of *Zootopia 2* defies those stereotypes.

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

These four parameters are stored in an array `[a, b, c, d]` where the array represents the character. If any of these four parameters are not defined, we define them as `float('inf')` in Python, as when unknown, this leads to multiple possibilities, which are left unknown. A fifth parameter `e` can also be added, though `e = Name of character` and is optional, mostly for printing purposes. If `e` is added, the array would instead be `[a, b, c, d, e]`.

We define the `DetermineObject(character)` function, which determines whether the character has an object.

```
FUNCTION DetermineObject(character):
    IF character.object == INF:
        RETURN False`
    ELSE:
        RETURN True
END FUNCTION
```

If the value for `character.object` is not defined (`INF`), it returns `False`. Otherwise, it returns `True`.

We then define the `DetermineLineage(character)` function, which determines the lineage of the character.

```
FUNCTION DetermineLineage(character):
    IF character.lineage == INF AND character.enemy_lineage == INF:
        RETURN INF  // Cannot determine gender
    ELSE IF character.lineage == character.enemy_lineage:
        RETURN INF  // Conflicting same-gender lineages
    ELSE IF character.lineage != INF AND character.enemy_lineage == INF:
        RETURN INF  // No enemy lineage to compare
    ELSE IF character.lineage == INF AND character.enemy_lineage != INF:
        RETURN INF  // No lineage to compare
    ELSE IF character.lineage == 0 AND character.enemy_lineage == 1:
        RETURN 0  // Male lineage vs female enemy
    ELSE IF character.lineage == 1 AND character.enemy_lineage == 0:
        RETURN 1  // Female lineage vs male enemy
    ELSE:
        RETURN INF  // Ambiguous
END FUNCTION
```
If both values for `character.object` are undefined, we return `INF` because the value is not defined. If the lineage gender values are equal, we also return the same value because if the lineages are the same, it does not affect the gender of the character. If either the character or enemy lineage is undefined, it also returns undefined as it also does not affect the gender of the character. If the lineages are opposite numbers 0 and 1, if the character lineage is female, it returns 1, otherwise it returns 0. If none of the parameter fits, it also returns undefined.

Now let's define the main function `DetermineGender(character)`:

```
FUNCTION DetermineGender(character):
    object_present = DetermineObject(character)
    lineage_value = DetermineLineage(character)
    voice = character.voice
    name = character.name

    IF voice == INF:  // No voice
        IF NOT object_present:  // No object
            IF lineage_value == INF:
                PRINT name + "'s gender cannot be determined"
            ELSE IF lineage_value == 0:
                PRINT name + " is male but no object or voice"
            ELSE IF lineage_value == 1:
                PRINT name + " is female but no object or voice"
        ELSE:  // Object exists
            IF lineage_value == INF:
                IF character.object == 0:
                    PRINT name + " is male but no lineage or voice"
                ELSE IF character.object == 1:
                    PRINT name + " is female but no lineage or voice"
            ELSE:
                IF character.object == 0 AND lineage_value == 0:
                    PRINT name + " is male but no voice"
                ELSE IF character.object == 1 AND lineage_value == 1:
                    PRINT name + " is female but no voice"
                ELSE:
                    PRINT name + "'s gender cannot be determined"
    ELSE:  // Voice exists
        IF NOT object_present:  // No object
            IF lineage_value == INF:
                IF voice <= 5:
                    PRINT name + " is male but no lineage or object"
                ELSE IF voice > 5:
                    PRINT name + " is female but no lineage or object"
            ELSE:
                IF lineage_value == 0 AND voice <= 5:
                    PRINT name + " is male but no object"
                ELSE IF lineage_value == 1 AND voice > 5:
                    PRINT name + " is female but no object"
                ELSE:
                    PRINT name + "'s gender cannot be determined"
        ELSE:  // Object exists
            IF lineage_value == INF:
                IF character.object == 0 AND voice <= 5:
                    PRINT name + " is male but no lineage"
                ELSE IF character.object == 1 AND voice > 5:
                    PRINT name + " is female but no lineage"
                ELSE:
                    PRINT name + "'s gender cannot be determined"
            ELSE:
                IF character.object == 0 AND lineage_value == 0 AND voice <= 5:
                    PRINT name + " is male in all ways"
                ELSE IF character.object == 1 AND lineage_value == 1 AND voice > 5:
                    PRINT name + " is female in all ways"
                ELSE IF character.object == 0 AND lineage_value == 0 AND voice <= 5:
                    PRINT name + " is male, object insignificant"
                ELSE IF character.object == 1 AND lineage_value == 1 AND voice > 5:
                    PRINT name + " is female, object insignificant"
                ELSE:
                    PRINT name + "'s gender cannot be determined"
END FUNCTION
```
We first define the parameters `object_present` (whether the object is present), `lineage value` (the value of lineage), the voice parameter scale (d), and the name of the character (e). We can add them to a list, or we can define them separately as revealed in the pseudocode. The case has several branches: whether the voice is deterministic and if so what it determines, then inside that branch is whether the object is deterministic, and a third branch for lineage. If none are deterministic, they do not affect the character's gender and therefore it cannot be determined. If the object AND lineage AND voice all are consistent, it determines the gender most accurately. If a parameter is missing it warns as to which parameter is missing. For the Gary example, lets assume her voice score is 6. Given her anti-venom pen (a = 1), her lineage value (1), and her voice range (6), all of that proves she is in fact a female.

# Application

This algorithm is theoretical and only uses several parameters to determine gender, so it is not always accurate. In addition, it is more used for symbolic gender. It does not only apply to gender, but to other real world applications, such as:
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

All of these applications can help predict, though it has limitations, since only four factors are taken into account. If a factor is missing it may give the wrong solution due to missing factors.

