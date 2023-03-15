---
cover: ../.gitbook/assets/Starry-Night.jpg
coverY: 93.22603978300182
---

# ❓ Competency Questions

{% tabs %}
{% tab title="Van Gogh's Agony" %}
**What is the interpretation of the "Starry Night" given by Lauren Soth?**

```
Answer: Religious meaning
```

2. **Which biblical episode the “Starry Night” relates to?**

```
Answer: The Agony in the Garden
```

3. **When and where did the idea of Starry Night first come into Van Gogh's mind?**

```
Answer: The spring of 1888. In Arles, France
```

4. **What is the real place that Van Gogh depicts in the "Starry Night"?**

```
Answer: The Alpilles mountains
```

5. **What were Van Gogh's artworks preceding the ‘Starry Night’ (sharing the same concept of starry night)?**

```
Answer: Cafe Terrace at Night, Starry Night Order the Rhone
```

6. **What artistic approach does Vincent van Gogh use in the “Starry Night”?**

```
Answer: Working from imagination
```

7. **Who Van Gogh was sharing the idea of working from the imagination with?**

```
Answer: Eugène Henri Paul Gauguin and Émile Bernard
```

8. **What was the inspiration source for the “Starry Night”?**

{% code overflow="wrap" %}
```
Answer: Images of crescents in art, Typical churches of Brabant Netherlands, Imagination of something sublime, View From Bedroom Window
```
{% endcode %}

9. **What are the colors used in the “Starry Night”?**

```
Answer: Blue, Citron-yellow
```

10. &#x20;**What determines the choice of colors for the “Starry Night”?**

```
Answer: Religious meaning
```
{% endtab %}

{% tab title="Vincent van Gogh: The Starry Night" %}
1. **What is the biography of Vincent Van Gogh?**

```
Answer: Vincent Willem van Gogh, Dutch, 1853, post-Impressionist
```

2. **What are the different art movements that Van Gogh was associated with during his career?**

```
Answer: Expressionism, Impressionism, Post-Impressionism
```

3. **What is the relationship between the post-Impressionist and Impressionist art movements?**

```
Answer: Post-Impressionism was influenced by Impressionism
```

4. **What is the main focus of Impressionism?**

```
Answer: Natural Colors, Use of Light
```

5. **What are the key characteristics of Post-Impressionist art?**

```
Answer: Structured Compositions, Subjective Emotional Expression
```

6. **What is Van Gogh's use of colors like in his paintings?**

```
Answer: Bright Colors, Contrasting Colors
```

7. **What are the different interpretations of “Starry Night”?**

{% code overflow="wrap" %}
```
Answer: Personal Struggles with Mental Illness, Transformative Power of Nature and Art
```
{% endcode %}

8. **What is the association of the brushstrokes in “Starry Night”?**

```
Answer: Emotional State
```

9. **What kind of brushstrokes did Van Gogh use in “Starry Night”?**

```
Answer: Bold Brushstrokes, Expressive Brushstrokes
```

10. **What is the significance of the brushstrokes in “Starry Night” by Van Gogh?**

```
Answer: Unique Style
```

11. **What are the different elements of art that Van Gogh utilized in “Starry Night”?**

```
Answer: Color, Line, Shape, Texture
```

12. **What are some examples of popular culture references to “Starry Night”?**

```
Answer: Films, Music, Television
```

13. **What impact did "Starry Night" have on the art world when it was first created?**&#x20;

```
Answer: Development of Modern Art
```

14. **What was the inspiration behind Van Gogh's “Starry Night”?**

```
Answer: View From Bedroom Window
```

15. **What was the setting or location of the inspiration for “Starry Night”?**

```
Answer: France, Saint-Paul-de-Mausole Asylum, Saint-Rémy-de-Provence
```

16. **What are the effects of using complementary colors in “Starry Night”?**

```
Answer: Balance, Visual Tension
```
{% endtab %}

{% tab title="Comparison " %}
1. **What are the different interpretations of “Starry Night”?**

{% code overflow="wrap" %}
```
Answer: Personal Struggles with Mental Illness, Transformative Power of Nature and Art, Religious meaning
```
{% endcode %}

2. **Which paintings by Van Gogh related to the post-Impressionist movement?**

{% code overflow="wrap" %}
```
Answer: Cafe Terrace at Night, Irises, Starry Night, Starry Night Order the Rhone, The Bedroom
```
{% endcode %}

3. **What was the inspiration behind Van Gogh's “Starry Night”?**

{% code overflow="wrap" %}
```
Answer: View From Bedroom Window, Typical churches of Brabant Netherlands, Images of crescents in art, Imagination of something sublime
```
{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
### ‎Ontology Development of «Van Gogh's Agony»
{% endhint %}

<details>

<summary><strong>Turtle Serialization</strong></summary>

{% code title="Van_Gogh's_Agony.ttl" overflow="wrap" %}
```turtle
@prefix : <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix vga: <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony#> .

<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/createdBy
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/createdBy> rdf:type owl:ObjectProperty ;
                                                                                  rdfs:subPropertyOf owl:topObjectProperty ;
                                                                                  rdfs:domain <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artwork> ;
                                                                                  rdfs:range <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Person> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasCharacteristic
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasCharacteristic> rdf:type owl:ObjectProperty ;
                                                                                          rdfs:subPropertyOf owl:topObjectProperty ;
                                                                                          rdfs:domain <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artwork> ;
                                                                                          rdfs:range <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ArtworkCharacteristic> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasConcept
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasConcept> rdf:type owl:ObjectProperty ;
                                                                                   rdfs:subPropertyOf owl:topObjectProperty ;
                                                                                   rdfs:domain <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artwork> ;
                                                                                   rdfs:range <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ConceptOfArtwork> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasInspirationSource
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasInspirationSource> rdf:type owl:ObjectProperty ;
                                                                                             rdfs:subPropertyOf owl:topObjectProperty ;
                                                                                             rdfs:domain <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artwork> ;
                                                                                             rdfs:range <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ArtistInspirationSource> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasInterpretation
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasInterpretation> rdf:type owl:ObjectProperty ;
                                                                                          rdfs:subPropertyOf owl:topObjectProperty ;
                                                                                          rdfs:domain <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artwork> ;
                                                                                          rdfs:range <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ScholarlyInterpretation> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasMeaning
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasMeaning> rdf:type owl:ObjectProperty ;
                                                                                   rdfs:subPropertyOf owl:topObjectProperty ;
                                                                                   rdfs:domain <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artwork> ,
                                                                                               <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ArtworkCharacteristic> ;
                                                                                   rdfs:range <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Meaning> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/isAbout
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/isAbout> rdf:type owl:ObjectProperty ;
                                                                                rdfs:subPropertyOf owl:topObjectProperty ;
                                                                                rdfs:domain <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/IdeaOfArtwork> ;
                                                                                rdfs:range <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artwork> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/isDepictedOn
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/isDepictedOn> rdf:type owl:ObjectProperty ;
                                                                                     rdfs:subPropertyOf owl:topObjectProperty ;
                                                                                     rdfs:domain <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Place> ;
                                                                                     rdfs:range <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artwork> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/isGivenBy
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/isGivenBy> rdf:type owl:ObjectProperty ;
                                                                                  rdfs:subPropertyOf owl:topObjectProperty ;
                                                                                  rdfs:domain <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ScholarlyInterpretation> ;
                                                                                  rdfs:range <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Person> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/isRelatedTo
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/isRelatedTo> rdf:type owl:ObjectProperty ;
                                                                                    rdfs:subPropertyOf owl:topObjectProperty ;
                                                                                    rdf:type owl:InverseFunctionalProperty ;
                                                                                    rdfs:domain <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artwork> ,
                                                                                                <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/BiblicalEpisode> ;
                                                                                    rdfs:range <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artwork> ,
                                                                                               <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/BiblicalEpisode> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/isSupportedBy
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/isSupportedBy> rdf:type owl:ObjectProperty ;
                                                                                      rdfs:subPropertyOf owl:topObjectProperty ;
                                                                                      rdfs:domain <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ArtisticApproach> ,
                                                                                                  <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/IdeaOfArtwork> ;
                                                                                      rdfs:range <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Person> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/occuredIn
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/occuredIn> rdf:type owl:ObjectProperty ;
                                                                                  rdfs:subPropertyOf owl:topObjectProperty ;
                                                                                  rdfs:domain <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/IdeaOfArtwork> ;
                                                                                  rdfs:range <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Place> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/preceded
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/preceded> rdf:type owl:ObjectProperty ;
                                                                                 rdfs:subPropertyOf owl:topObjectProperty ;
                                                                                 rdfs:domain <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artwork> ;
                                                                                 rdfs:range <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artwork> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/usedIn
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/usedIn> rdf:type owl:ObjectProperty ;
                                                                               rdfs:subPropertyOf owl:topObjectProperty ;
                                                                               rdfs:domain <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ArtisticApproach> ;
                                                                               rdfs:range <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artwork> .


#################################################################
#    Data properties
#################################################################

###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasDescription
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasDescription> rdf:type owl:DatatypeProperty ;
                                                                                       rdfs:subPropertyOf owl:topDataProperty ;
                                                                                       rdfs:domain <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Place> ;
                                                                                       rdfs:range xsd:string .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasName
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasName> rdf:type owl:DatatypeProperty ;
                                                                                rdfs:subPropertyOf owl:topDataProperty ;
                                                                                rdfs:domain <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Person> ;
                                                                                rdfs:range xsd:string .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasSubject
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasSubject> rdf:type owl:DatatypeProperty ;
                                                                                   rdfs:subPropertyOf owl:topDataProperty ;
                                                                                   rdfs:domain <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ArtisticApproach> ,
                                                                                               <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/BiblicalEpisode> ;
                                                                                   rdfs:range xsd:string .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasTitle
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasTitle> rdf:type owl:DatatypeProperty ;
                                                                                 rdfs:subPropertyOf owl:topDataProperty ;
                                                                                 rdfs:domain <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artwork> ;
                                                                                 rdfs:range xsd:string .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/occuredOn
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/occuredOn> rdf:type owl:DatatypeProperty ;
                                                                                  rdfs:subPropertyOf owl:topDataProperty ;
                                                                                  rdfs:domain <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/IdeaOfArtwork> ;
                                                                                  rdfs:range xsd:dateTime .


#################################################################
#    Classes
#################################################################

###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artist
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artist> rdf:type owl:Class ;
                                                                               rdfs:subClassOf <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Person> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ArtistInspirationSource
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ArtistInspirationSource> rdf:type owl:Class .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ArtisticApproach
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ArtisticApproach> rdf:type owl:Class .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artwork
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artwork> rdf:type owl:Class .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ArtworkCharacteristic
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ArtworkCharacteristic> rdf:type owl:Class .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/BiblicalEpisode
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/BiblicalEpisode> rdf:type owl:Class .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Color
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Color> rdf:type owl:Class ;
                                                                              rdfs:subClassOf <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ArtworkCharacteristic> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ConceptOfArtwork
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ConceptOfArtwork> rdf:type owl:Class .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/DominantColor
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/DominantColor> rdf:type owl:Class ;
                                                                                      rdfs:subClassOf <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Color> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/IdeaOfArtwork
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/IdeaOfArtwork> rdf:type owl:Class .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ImagionaryPlace
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ImagionaryPlace> rdf:type owl:Class ;
                                                                                        rdfs:subClassOf <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Place> ;
                                                                                        owl:disjointWith <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/RealPlace> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Line
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Line> rdf:type owl:Class ;
                                                                             rdfs:subClassOf <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ArtworkCharacteristic> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/MainInterpretation
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/MainInterpretation> rdf:type owl:Class ;
                                                                                           rdfs:subClassOf <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ScholarlyInterpretation> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Meaning
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Meaning> rdf:type owl:Class .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Painter
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Painter> rdf:type owl:Class ;
                                                                                rdfs:subClassOf <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artist> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Painting
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Painting> rdf:type owl:Class ;
                                                                                 rdfs:subClassOf <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Artwork> ,
                                                                                                 [ rdf:type owl:Restriction ;
                                                                                                   owl:onProperty <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/createdBy> ;
                                                                                                   owl:someValuesFrom <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Painter>
                                                                                                 ] .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Person
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Person> rdf:type owl:Class .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Place
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Place> rdf:type owl:Class .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/RealPlace
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/RealPlace> rdf:type owl:Class ;
                                                                                  rdfs:subClassOf <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Place> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Scholar
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Scholar> rdf:type owl:Class ;
                                                                                rdfs:subClassOf <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Person> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ScholarlyInterpretation
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ScholarlyInterpretation> rdf:type owl:Class ;
                                                                                                rdfs:subClassOf [ rdf:type owl:Restriction ;
                                                                                                                  owl:onProperty <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/isGivenBy> ;
                                                                                                                  owl:someValuesFrom <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Scholar>
                                                                                                                ] .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Shape
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Shape> rdf:type owl:Class ;
                                                                              rdfs:subClassOf <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ArtworkCharacteristic> .


#################################################################
#    Individuals
#################################################################

###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Alpilles_mountains
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Alpilles_mountains> rdf:type owl:NamedIndividual ,
                                                                                                    <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/RealPlace> ;
                                                                                           <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/isDepictedOn> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Starry_Night> ;
                                                                                           <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasDescription> "The Chaîne des Alpilles is a small range of low mountains in Provence, southern France, located about 20 km south of Avignon."@en .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Arles
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Arles> rdf:type owl:NamedIndividual ,
                                                                                       <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/RealPlace> ;
                                                                              <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasDescription> "Arles is a coastal city and commune in the South of France, a subprefecture in the Bouches-du-Rhône department of the Provence-Alpes-Côte d'Azur region, in the former province of Provence."@en .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Blue
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Blue> rdf:type owl:NamedIndividual ,
                                                                                      <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/DominantColor> ;
                                                                             <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasMeaning> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Religious_meaning> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Cafe_Terrace_at_Night
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Cafe_Terrace_at_Night> rdf:type owl:NamedIndividual ,
                                                                                                       <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Painting> ;
                                                                                              <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/createdBy> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Vincent_Willem_van_Gogh> ;
                                                                                              <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasConcept> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Concept_StarryNight> ;
                                                                                              <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/preceded> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Starry_Night> ;
                                                                                              <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasTitle> "Cafe Terrace at Night"@en .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Citron-yellow
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Citron-yellow> rdf:type owl:NamedIndividual ,
                                                                                               <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/DominantColor> ;
                                                                                      <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasMeaning> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Religious_meaning> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Concept_StarryNight
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Concept_StarryNight> rdf:type owl:NamedIndividual ,
                                                                                                     <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ConceptOfArtwork> ;
                                                                                            <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasSubject> "Starry Night"@en .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Emile_Bernard
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Emile_Bernard> rdf:type owl:NamedIndividual ,
                                                                                               <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Painter> ;
                                                                                      <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasName> "Emile Bernard" .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Eugene_Henri_Paul_Gauguin
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Eugene_Henri_Paul_Gauguin> rdf:type owl:NamedIndividual ,
                                                                                                           <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Painter> ;
                                                                                                  <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasName> "Eugene Henri Paul Gauguin" .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/IdeaStarryNight
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/IdeaStarryNight> rdf:type owl:NamedIndividual ,
                                                                                                 <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/IdeaOfArtwork> ;
                                                                                        <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/isAbout> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Starry_Night> ;
                                                                                        <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/occuredIn> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Arles> ;
                                                                                        <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/occuredOn> "Spring 1888" .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Imagination
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Imagination> rdf:type owl:NamedIndividual ,
                                                                                             <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ArtistInspirationSource> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Lauren_Soth
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Lauren_Soth> rdf:type owl:NamedIndividual ,
                                                                                             <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Scholar> ;
                                                                                    <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasName> "Lauren Soth" .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Memory
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Memory> rdf:type owl:NamedIndividual ,
                                                                                        <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ArtistInspirationSource> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Observed_reality
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Observed_reality> rdf:type owl:NamedIndividual ,
                                                                                                  <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ArtistInspirationSource> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Religious_meaning
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Religious_meaning> rdf:type owl:NamedIndividual ,
                                                                                                   <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/MainInterpretation> ,
                                                                                                   <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Meaning> ;
                                                                                          <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/isGivenBy> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Lauren_Soth> .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/St-Remy
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/St-Remy> rdf:type owl:NamedIndividual ,
                                                                                         <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/RealPlace> ;
                                                                                <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasDescription> "Saint-Rémy-de-Provence is a commune in the Bouches-du-Rhône department, Provence-Alpes-Côte d'Azur, Southern France. Located in the northern part of the Alpilles, of which it is the main town, it had a population of 9,893 in 2017."@en .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Starry_Night
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Starry_Night> rdf:type owl:NamedIndividual ,
                                                                                              <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Painting> ;
                                                                                     <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/createdBy> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Vincent_Willem_van_Gogh> ;
                                                                                     <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasCharacteristic> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Blue> ,
                                                                                                                                                                               <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Citron-yellow> ;
                                                                                     <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasConcept> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Concept_StarryNight> ;
                                                                                     <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasInspirationSource> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Imagination> ,
                                                                                                                                                                                  <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Memory> ,
                                                                                                                                                                                  <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Observed_reality> ;
                                                                                     <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasInterpretation> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Religious_meaning> ;
                                                                                     <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/isRelatedTo> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/The_Agony_in_the_Garden> ;
                                                                                     <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasTitle> "Starry Night"@en .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Starry_Night_Order_the_Rhone
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Starry_Night_Order_the_Rhone> rdf:type owl:NamedIndividual ,
                                                                                                              <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Painting> ;
                                                                                                     <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/createdBy> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Vincent_Willem_van_Gogh> ;
                                                                                                     <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasConcept> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Concept_StarryNight> ;
                                                                                                     <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/preceded> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Starry_Night> ;
                                                                                                     <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasTitle> "Starry Night Order the Rhone"@en .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/The_Agony_in_the_Garden
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/The_Agony_in_the_Garden> rdf:type owl:NamedIndividual ,
                                                                                                         <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/BiblicalEpisode> ;
                                                                                                <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/isRelatedTo> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Starry_Night> ;
                                                                                                <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasSubject> """Christ with the Angel in Gethsemane
or The Agony in the Garden"""@en .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Vincent_Willem_van_Gogh
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Vincent_Willem_van_Gogh> rdf:type owl:NamedIndividual ,
                                                                                                         <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Painter> ;
                                                                                                <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasName> "Vincent Willem van Gogh" .


###  http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Working_from_imagination
<http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Working_from_imagination> rdf:type owl:NamedIndividual ,
                                                                                                          <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/ArtisticApproach> ;
                                                                                                 <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/isSupportedBy> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Emile_Bernard> ,
                                                                                                                                                                                       <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Eugene_Henri_Paul_Gauguin> ,
                                                                                                                                                                                       <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Vincent_Willem_van_Gogh> ;
                                                                                                 <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/usedIn> <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Starry_Night> ;
                                                                                                 <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/hasSubject> "Working from imagination"@en .


#################################################################
#    General axioms
#################################################################

[ rdf:type owl:AllDisjointClasses ;
  owl:members ( <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Color>
                <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Line>
                <http://www.semanticweb.org/poweruser/ontologies/2023/1/van_gogh_agony/Shape>
              )
] .


###  Generated by the OWL API (version 4.5.25.2023-02-15T19:15:49Z) https://github.com/owlcs/owlapi
```
{% endcode %}

</details>

{% file src="../.gitbook/assets/Van_Gogh's_Agony.ttl" %}

<figure><img src="../.gitbook/assets/Снимок экрана 2023-03-15 231914.jpeg" alt=""><figcaption><p>Graph Visualization</p></figcaption></figure>

{% file src="../.gitbook/assets/Van_Gogh's_Agony_Graph_Visualization.svg" %}

{% hint style="info" %}
### Ontology Development of «Vincent van Gogh: The Starry Nigh»
{% endhint %}

<details>

<summary><strong>Turtle Serialization</strong></summary>

{% code title="Vincent_van_Gogh_The_Starry_Nigh.ttl" overflow="wrap" lineNumbers="true" %}
```turtle
@prefix : <http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10/> .

<http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#contributedIn
:contributedIn rdf:type owl:ObjectProperty ;
               rdfs:domain :Painting1 ;
               rdfs:range :the_development_of_modern_art .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#emphasized
:emphasized rdf:type owl:ObjectProperty ;
            rdfs:domain :Post-Impressionism ;
            rdfs:range :structured_compositions ,
                       :subjective_emotional_expression .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#employed
:employed rdf:type owl:ObjectProperty ;
          rdfs:domain :Painter ;
          rdfs:range :complementary_colors .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#extendedFocusBeyond
:extendedFocusBeyond rdf:type owl:ObjectProperty ;
                     rdfs:domain :Post-Impressionism ;
                     rdfs:range :natural_colors ,
                                :use_of_light .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#generate
:generate rdf:type owl:ObjectProperty ;
          rdfs:domain :complementary_colors ;
          rdfs:range :balance ,
                     :visual_tension .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#hasBecome
:hasBecome rdf:type owl:ObjectProperty ;
           rdfs:domain :Painting1 ;
           rdfs:range :symbol .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#hasBecomeASymbolOf
:hasBecomeASymbolOf rdf:type owl:ObjectProperty ;
                    rdfs:domain :Painting1 ;
                    rdfs:range :artistic_legacy .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#interpretedAs
:interpretedAs rdf:type owl:ObjectProperty ;
               rdfs:domain :Painting1 ;
               rdfs:range :personal_struggles_with_mental_illness ,
                          :transformative_power_of_nature_and_art .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#isAssociatedWith
:isAssociatedWith rdf:type owl:ObjectProperty ;
                  rdfs:domain :Painting1 ,
                              :Painting2 ,
                              :Painting3 ;
                  rdfs:range :Post-Impressionism .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#isCitedAs
:isCitedAs rdf:type owl:ObjectProperty ;
           rdfs:domain :Painting1 ;
           rdfs:range :an_example_of_post-Impressionist_style .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#isEvidentInTheUse
:isEvidentInTheUse rdf:type owl:ObjectProperty ;
                   rdfs:domain :Technique ;
                   rdfs:range :blues ,
                              :oranges .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#isReferencedIn
:isReferencedIn rdf:type owl:ObjectProperty ;
                rdfs:domain :Painting1 ;
                rdfs:range :films ,
                           :music ,
                           :popular_culture ,
                           :television .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#isSignificantElementIn
:isSignificantElementIn rdf:type owl:ObjectProperty ;
                        rdfs:domain :Color ;
                        rdfs:range :Artworks .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#linkedWith
:linkedWith rdf:type owl:ObjectProperty ;
            rdfs:domain :bold_brushstrokes ,
                        :expressive_brushstrokes ;
            rdfs:range :emotional_state .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#locatedIn
:locatedIn rdf:type owl:ObjectProperty .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#resultedIn
:resultedIn rdf:type owl:ObjectProperty ;
            rdfs:domain :bright_colors ,
                        :contrasting_colors ;
            rdfs:range :emotion ,
                       :visual_impact .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#seenAs
:seenAs rdf:type owl:ObjectProperty ;
        rdfs:domain :bold_brushstrokes ,
                    :expressive_brushstrokes ;
        rdfs:range :unique_style .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#used
:used rdf:type owl:ObjectProperty ;
      rdfs:domain :Painter ;
      rdfs:range :bright_colors ,
                 :contrasting_colors .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#utilized
:utilized rdf:type owl:ObjectProperty ;
          rdfs:domain :Painter ;
          rdfs:range :Color ,
                     :Line ,
                     :Shape ,
                     :Texture .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#wasAdmittedTo
:wasAdmittedTo rdf:type owl:ObjectProperty ;
               rdfs:domain :Painter ;
               rdfs:range :asylum .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#wasInfluencedBy
:wasInfluencedBy rdf:type owl:ObjectProperty ;
                 rdfs:domain :Post-Impressionism ;
                 rdfs:range :Impressionism .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#wasInspiredBy
:wasInspiredBy rdf:type owl:ObjectProperty ;
               rdfs:domain :Painting1 ;
               rdfs:range :view_from_the_window .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#wasInterestedIn
:wasInterestedIn rdf:type owl:ObjectProperty ;
                 rdfs:domain :Painter ;
                 rdfs:range :Color_theory .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#wasRelatedTo
:wasRelatedTo rdf:type owl:ObjectProperty ;
              rdfs:domain :Painter ;
              rdfs:range :Expressionism ,
                         :Impressionism ,
                         :Post-Impressionism .


#################################################################
#    Data properties
#################################################################

###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#bornInYear
:bornInYear rdf:type owl:DatatypeProperty ;
            rdfs:domain :Painter ;
            rdfs:range xsd:integer .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#connectedWith
:connectedWith rdf:type owl:DatatypeProperty ;
               rdfs:domain :Art_Movement ,
                           :Painter ;
               rdfs:range xsd:string .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#hasFullName
:hasFullName rdf:type owl:DatatypeProperty ;
             rdfs:domain :Painter ;
             rdfs:range xsd:string .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#hasNationality
:hasNationality rdf:type owl:DatatypeProperty ;
                rdfs:domain :Painter ;
                rdfs:range xsd:string .


#################################################################
#    Classes
#################################################################

###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Art_Movement
:Art_Movement rdf:type owl:Class .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Artistic_Expression
:Artistic_Expression rdf:type owl:Class .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Artworks
:Artworks rdf:type owl:Class .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Color
:Color rdf:type owl:Class ;
       rdfs:subClassOf :Elements_of_Art .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Color_theory
:Color_theory rdf:type owl:Class .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Elements_of_Art
:Elements_of_Art rdf:type owl:Class .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Elements_of_Composition
:Elements_of_Composition rdf:type owl:Class .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Expressionism
:Expressionism rdf:type owl:Class ;
               rdfs:subClassOf :Art_Movement .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Historical_and_cultural_significance
:Historical_and_cultural_significance rdf:type owl:Class .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Impressionism
:Impressionism rdf:type owl:Class ;
               rdfs:subClassOf :Art_Movement .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Inspiration
:Inspiration rdf:type owl:Class .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Interpretation
:Interpretation rdf:type owl:Class .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Line
:Line rdf:type owl:Class ;
      rdfs:subClassOf :Elements_of_Art .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Painter
:Painter rdf:type owl:Class .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Painting1
:Painting1 rdf:type owl:Class ;
           rdfs:subClassOf :Artworks .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Painting2
:Painting2 rdf:type owl:Class ;
           rdfs:subClassOf :Artworks .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Painting3
:Painting3 rdf:type owl:Class ;
           rdfs:subClassOf :Artworks .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Post-Impressionism
:Post-Impressionism rdf:type owl:Class ;
                    rdfs:subClassOf :Art_Movement .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Shape
:Shape rdf:type owl:Class ;
       rdfs:subClassOf :Elements_of_Art .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Technique
:Technique rdf:type owl:Class ;
           rdfs:subClassOf :Color_theory .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Texture
:Texture rdf:type owl:Class ;
         rdfs:subClassOf :Elements_of_Art .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#an_example_of_post-Impressionist_style
:an_example_of_post-Impressionist_style rdf:type owl:Class ;
                                        rdfs:subClassOf :Historical_and_cultural_significance .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#artistic_legacy
:artistic_legacy rdf:type owl:Class ;
                 rdfs:subClassOf :Historical_and_cultural_significance .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#asylum
:asylum rdf:type owl:Class ;
        rdfs:subClassOf :institution .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#balance
:balance rdf:type owl:Class ;
         rdfs:subClassOf :Elements_of_Composition .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#blues
:blues rdf:type owl:Class ;
       rdfs:subClassOf :complementary_colors ;
       owl:disjointWith :oranges .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#bold_brushstrokes
:bold_brushstrokes rdf:type owl:Class ;
                   rdfs:subClassOf :Artistic_Expression .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#bright_colors
:bright_colors rdf:type owl:Class ;
               rdfs:subClassOf :Color .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#complementary_colors
:complementary_colors rdf:type owl:Class ;
                      rdfs:subClassOf :Technique .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#contrasting_colors
:contrasting_colors rdf:type owl:Class ;
                    rdfs:subClassOf :Color .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#country
:country rdf:type owl:Class ;
         rdfs:subClassOf :location .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#emotion
:emotion rdf:type owl:Class ;
         rdfs:subClassOf :Artistic_Expression .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#emotional_state
:emotional_state rdf:type owl:Class ;
                 rdfs:subClassOf :Artistic_Expression .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#expressive_brushstrokes
:expressive_brushstrokes rdf:type owl:Class ;
                         rdfs:subClassOf :Artistic_Expression .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#films
:films rdf:type owl:Class ;
       rdfs:subClassOf :popular_culture .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#institution
:institution rdf:type owl:Class ;
             rdfs:subClassOf :place .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#location
:location rdf:type owl:Class ;
          rdfs:subClassOf :view_from_the_window .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#music
:music rdf:type owl:Class ;
       rdfs:subClassOf :popular_culture .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#natural_colors
:natural_colors rdf:type owl:Class ;
                rdfs:subClassOf :Color .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#oranges
:oranges rdf:type owl:Class ;
         rdfs:subClassOf :complementary_colors .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#personal_struggles_with_mental_illness
:personal_struggles_with_mental_illness rdf:type owl:Class ;
                                        rdfs:subClassOf :Interpretation ;
                                        owl:disjointWith :transformative_power_of_nature_and_art .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#place
:place rdf:type owl:Class ;
       rdfs:subClassOf :location .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#popular_culture
:popular_culture rdf:type owl:Class ;
                 rdfs:subClassOf :Historical_and_cultural_significance .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#structured_compositions
:structured_compositions rdf:type owl:Class ;
                         rdfs:subClassOf :Elements_of_Composition .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#subjective_emotional_expression
:subjective_emotional_expression rdf:type owl:Class ;
                                 rdfs:subClassOf :emotional_state .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#symbol
:symbol rdf:type owl:Class ;
        rdfs:subClassOf :Artistic_Expression .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#television
:television rdf:type owl:Class ;
            rdfs:subClassOf :popular_culture .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#the_development_of_modern_art
:the_development_of_modern_art rdf:type owl:Class ;
                               rdfs:subClassOf :Historical_and_cultural_significance .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#town
:town rdf:type owl:Class ;
      rdfs:subClassOf :location .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#transformative_power_of_nature_and_art
:transformative_power_of_nature_and_art rdf:type owl:Class ;
                                        rdfs:subClassOf :Interpretation .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#unique_style
:unique_style rdf:type owl:Class ;
              rdfs:subClassOf :Artistic_Expression .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#use_of_light
:use_of_light rdf:type owl:Class ;
              rdfs:subClassOf :Elements_of_Composition .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#view_from_the_window
:view_from_the_window rdf:type owl:Class ;
                      rdfs:subClassOf :Inspiration .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#visual_impact
:visual_impact rdf:type owl:Class ;
               rdfs:subClassOf :Artistic_Expression .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#visual_tension
:visual_tension rdf:type owl:Class ;
                rdfs:subClassOf :Elements_of_Composition .


#################################################################
#    Individuals
#################################################################

###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#France
:France rdf:type owl:NamedIndividual ,
                 :country .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Irises
:Irises rdf:type owl:NamedIndividual ,
                 :Painting3 .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Saint-Paul-de-Mausole
:Saint-Paul-de-Mausole rdf:type owl:NamedIndividual ,
                                :asylum ;
                       :locatedIn :Saint-Rémy-de-Provence .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Saint-Rémy-de-Provence
:Saint-Rémy-de-Provence rdf:type owl:NamedIndividual ,
                                 :town ;
                        :locatedIn :France .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Starry_Night
:Starry_Night rdf:type owl:NamedIndividual ,
                       :Painting1 .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#The_Bedroom
:The_Bedroom rdf:type owl:NamedIndividual ,
                      :Painting2 .


###  http://www.semanticweb.org/anita/ontologies/2023/1/untitled-ontology-10#Vincent_van_Gogh
:Vincent_van_Gogh rdf:type owl:NamedIndividual ,
                           :Painter ;
                  :bornInYear 1853 ;
                  :connectedWith "post-Impressionists" ;
                  :hasFullName "Vincent Willem van Gogh" ;
                  :hasNationality "Dutch" .


#################################################################
#    General axioms
#################################################################

[ rdf:type owl:AllDisjointClasses ;
  owl:members ( :Expressionism
                :Impressionism
                :Post-Impressionism
              )
] .


[ rdf:type owl:AllDisjointClasses ;
  owl:members ( :an_example_of_post-Impressionist_style
                :popular_culture
                :the_development_of_modern_art
              )
] .


[ rdf:type owl:AllDisjointClasses ;
  owl:members ( :balance
                :structured_compositions
                :use_of_light
                :visual_tension
              )
] .


[ rdf:type owl:AllDisjointClasses ;
  owl:members ( :films
                :music
                :television
              )
] .


###  Generated by the OWL API (version 4.5.25.2023-02-15T19:15:49Z) https://github.com/owlcs/owlapi
```
{% endcode %}

</details>

{% file src="../.gitbook/assets/Vincent_van_Gogh_The_Starry_Nigh.ttl" %}

<figure><img src="../.gitbook/assets/Снимок экрана 2023-03-15 232718.jpeg" alt=""><figcaption><p>Graph Visualization</p></figcaption></figure>

{% file src="../.gitbook/assets/Vincent_van_Gogh_The_Starry_Nigh_Graph_Visualization.svg" %}

