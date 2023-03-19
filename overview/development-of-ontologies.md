---
cover: ../.gitbook/assets/Starry-Night.jpg
coverY: 93.22603978300182
---

# 🛠 Development of Ontologies

{% hint style="info" %}
### <mark style="color:orange;">‎Ontology Development of «Van Gogh's Agony»</mark>
{% endhint %}

<details>

<summary><mark style="color:blue;"><strong>Turtle Serialization</strong></mark></summary>

{% code title="Van_Gogh's_Agony.ttl" overflow="wrap" %}
```turtle
@prefix : <http://www.semanticweb.org/van_gogh_agony#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://www.semanticweb.org/van_gogh_agony#> .

<http://www.semanticweb.org/van_gogh_agony> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  http://www.semanticweb.org/van_gogh_agony#createdBy
:createdBy rdf:type owl:ObjectProperty ;
           rdfs:subPropertyOf owl:topObjectProperty ;
           rdfs:domain :Artwork ;
           rdfs:range :Person .


###  http://www.semanticweb.org/van_gogh_agony#hasConcept
:hasConcept rdf:type owl:ObjectProperty ;
            rdfs:subPropertyOf owl:topObjectProperty ;
            rdfs:domain :Artwork ;
            rdfs:range :ConceptOfArtwork .


###  http://www.semanticweb.org/van_gogh_agony#hasInspirationSource
:hasInspirationSource rdf:type owl:ObjectProperty ;
                      rdfs:subPropertyOf owl:topObjectProperty ;
                      rdfs:domain :Artwork ;
                      rdfs:range :ArtistInspirationSource .


###  http://www.semanticweb.org/van_gogh_agony#hasInterpretation
:hasInterpretation rdf:type owl:ObjectProperty ;
                   rdfs:subPropertyOf owl:topObjectProperty ;
                   rdfs:domain :Artwork ;
                   rdfs:range :ScholarlyInterpretation .


###  http://www.semanticweb.org/van_gogh_agony#hasMeaning
:hasMeaning rdf:type owl:ObjectProperty ;
            rdfs:subPropertyOf owl:topObjectProperty ;
            rdfs:domain [ rdf:type owl:Class ;
                          owl:unionOf ( :Artwork
                                        :ArtworkCharacteristic
                                      )
                        ] ;
            rdfs:range :Meaning .


###  http://www.semanticweb.org/van_gogh_agony#isAbout
:isAbout rdf:type owl:ObjectProperty ;
         rdfs:subPropertyOf owl:topObjectProperty ;
         rdfs:domain :IdeaOfArtwork ;
         rdfs:range :Artwork .


###  http://www.semanticweb.org/van_gogh_agony#isDepictedOn
:isDepictedOn rdf:type owl:ObjectProperty ;
              rdfs:subPropertyOf owl:topObjectProperty ;
              rdfs:domain :Place ;
              rdfs:range :Artwork .


###  http://www.semanticweb.org/van_gogh_agony#isGivenBy
:isGivenBy rdf:type owl:ObjectProperty ;
           rdfs:subPropertyOf owl:topObjectProperty ;
           rdfs:domain :ScholarlyInterpretation ;
           rdfs:range :Person .


###  http://www.semanticweb.org/van_gogh_agony#isRelatedTo
:isRelatedTo rdf:type owl:ObjectProperty ;
             rdfs:subPropertyOf owl:topObjectProperty ;
             rdf:type owl:InverseFunctionalProperty ;
             rdfs:domain [ rdf:type owl:Class ;
                           owl:unionOf ( :Artwork
                                         :BiblicalEpisode
                                       )
                         ] ;
             rdfs:range [ rdf:type owl:Class ;
                          owl:unionOf ( :Artwork
                                        :BiblicalEpisode
                                      )
                        ] .


###  http://www.semanticweb.org/van_gogh_agony#isSupportedBy
:isSupportedBy rdf:type owl:ObjectProperty ;
               rdfs:subPropertyOf owl:topObjectProperty ;
               rdfs:domain [ rdf:type owl:Class ;
                             owl:unionOf ( :ArtisticApproach
                                           :IdeaOfArtwork
                                         )
                           ] ;
               rdfs:range :Person .


###  http://www.semanticweb.org/van_gogh_agony#occuredIn
:occuredIn rdf:type owl:ObjectProperty ;
           rdfs:subPropertyOf owl:topObjectProperty ;
           rdfs:domain :IdeaOfArtwork ;
           rdfs:range :Place .


###  http://www.semanticweb.org/van_gogh_agony#preceded
:preceded rdf:type owl:ObjectProperty ;
          rdfs:subPropertyOf owl:topObjectProperty ;
          rdfs:domain :Artwork ;
          rdfs:range :Artwork .


###  http://www.semanticweb.org/van_gogh_agony#usedIn
:usedIn rdf:type owl:ObjectProperty ;
        rdfs:subPropertyOf owl:topObjectProperty ;
        rdfs:domain [ rdf:type owl:Class ;
                      owl:unionOf ( :ArtisticApproach
                                    :ArtworkCharacteristic
                                  )
                    ] ;
        rdfs:range :Artwork .


#################################################################
#    Data properties
#################################################################

###  http://www.semanticweb.org/van_gogh_agony#hasDescription
:hasDescription rdf:type owl:DatatypeProperty ;
                rdfs:subPropertyOf owl:topDataProperty ;
                rdfs:domain :Place ;
                rdfs:range xsd:string .


###  http://www.semanticweb.org/van_gogh_agony#hasName
:hasName rdf:type owl:DatatypeProperty ;
         rdfs:subPropertyOf owl:topDataProperty ;
         rdfs:domain :Person ;
         rdfs:range xsd:string .


###  http://www.semanticweb.org/van_gogh_agony#hasSubject
:hasSubject rdf:type owl:DatatypeProperty ;
            rdfs:subPropertyOf owl:topDataProperty ;
            rdfs:domain [ rdf:type owl:Class ;
                          owl:unionOf ( :ArtisticApproach
                                        :BiblicalEpisode
                                      )
                        ] ;
            rdfs:range xsd:string .


###  http://www.semanticweb.org/van_gogh_agony#hasTitle
:hasTitle rdf:type owl:DatatypeProperty ;
          rdfs:subPropertyOf owl:topDataProperty ;
          rdfs:domain :Artwork ;
          rdfs:range xsd:string .


###  http://www.semanticweb.org/van_gogh_agony#occuredOn
:occuredOn rdf:type owl:DatatypeProperty ;
           rdfs:subPropertyOf owl:topDataProperty ;
           rdfs:domain :IdeaOfArtwork ;
           rdfs:range xsd:dateTime .


#################################################################
#    Classes
#################################################################

###  http://www.semanticweb.org/van_gogh_agony#Artist
:Artist rdf:type owl:Class ;
        rdfs:subClassOf :Person .


###  http://www.semanticweb.org/van_gogh_agony#ArtistInspirationSource
:ArtistInspirationSource rdf:type owl:Class .


###  http://www.semanticweb.org/van_gogh_agony#ArtisticApproach
:ArtisticApproach rdf:type owl:Class .


###  http://www.semanticweb.org/van_gogh_agony#Artwork
:Artwork rdf:type owl:Class .


###  http://www.semanticweb.org/van_gogh_agony#ArtworkCharacteristic
:ArtworkCharacteristic rdf:type owl:Class .


###  http://www.semanticweb.org/van_gogh_agony#BiblicalEpisode
:BiblicalEpisode rdf:type owl:Class .


###  http://www.semanticweb.org/van_gogh_agony#Color
:Color rdf:type owl:Class ;
       rdfs:subClassOf :ArtworkCharacteristic .


###  http://www.semanticweb.org/van_gogh_agony#ConceptOfArtwork
:ConceptOfArtwork rdf:type owl:Class .


###  http://www.semanticweb.org/van_gogh_agony#IdeaOfArtwork
:IdeaOfArtwork rdf:type owl:Class .


###  http://www.semanticweb.org/van_gogh_agony#Imagination
:Imagination rdf:type owl:Class ;
             rdfs:subClassOf :ArtistInspirationSource .


###  http://www.semanticweb.org/van_gogh_agony#ImagionaryPlace
:ImagionaryPlace rdf:type owl:Class ;
                 rdfs:subClassOf :Place ;
                 owl:disjointWith :RealPlace .


###  http://www.semanticweb.org/van_gogh_agony#Line
:Line rdf:type owl:Class ;
      rdfs:subClassOf :ArtworkCharacteristic .


###  http://www.semanticweb.org/van_gogh_agony#MainInterpretation
:MainInterpretation rdf:type owl:Class ;
                    rdfs:subClassOf :ScholarlyInterpretation .


###  http://www.semanticweb.org/van_gogh_agony#Meaning
:Meaning rdf:type owl:Class .


###  http://www.semanticweb.org/van_gogh_agony#Memory
:Memory rdf:type owl:Class ;
        rdfs:subClassOf :ArtistInspirationSource .


###  http://www.semanticweb.org/van_gogh_agony#Observed_Reality
:Observed_Reality rdf:type owl:Class ;
                  rdfs:subClassOf :ArtistInspirationSource .


###  http://www.semanticweb.org/van_gogh_agony#Painter
:Painter rdf:type owl:Class ;
         rdfs:subClassOf :Artist .


###  http://www.semanticweb.org/van_gogh_agony#Painting
:Painting rdf:type owl:Class ;
          rdfs:subClassOf :Artwork .


###  http://www.semanticweb.org/van_gogh_agony#Person
:Person rdf:type owl:Class .


###  http://www.semanticweb.org/van_gogh_agony#Place
:Place rdf:type owl:Class .


###  http://www.semanticweb.org/van_gogh_agony#RealPlace
:RealPlace rdf:type owl:Class ;
           rdfs:subClassOf :Place .


###  http://www.semanticweb.org/van_gogh_agony#Scholar
:Scholar rdf:type owl:Class ;
         rdfs:subClassOf :Person .


###  http://www.semanticweb.org/van_gogh_agony#ScholarlyInterpretation
:ScholarlyInterpretation rdf:type owl:Class .


###  http://www.semanticweb.org/van_gogh_agony#Shape
:Shape rdf:type owl:Class ;
       rdfs:subClassOf :ArtworkCharacteristic .


#################################################################
#    Individuals
#################################################################

###  http://www.semanticweb.org/van_gogh_agony#Alpilles_mountains
:Alpilles_mountains rdf:type owl:NamedIndividual ,
                             :Observed_Reality ,
                             :RealPlace ;
                    :isDepictedOn :Starry_Night ;
                    :hasDescription "The Chaîne des Alpilles is a small range of low mountains in Provence, southern France, located about 20 km south of Avignon."@en .


###  http://www.semanticweb.org/van_gogh_agony#Arles
:Arles rdf:type owl:NamedIndividual ,
                :RealPlace ;
       :isDepictedOn :Cafe_Terrace_at_Night ,
                     :Starry_Night_Order_the_Rhone ;
       :hasDescription "Arles is a coastal city and commune in the South of France, a subprefecture in the Bouches-du-Rhône department of the Provence-Alpes-Côte d'Azur region, in the former province of Provence."@en .


###  http://www.semanticweb.org/van_gogh_agony#Blue
:Blue rdf:type owl:NamedIndividual ,
               :Color ;
      :hasMeaning :Religious_meaning ;
      :usedIn :Starry_Night .


###  http://www.semanticweb.org/van_gogh_agony#Cafe_Terrace_at_Night
:Cafe_Terrace_at_Night rdf:type owl:NamedIndividual ,
                                :Painting ;
                       :createdBy :Vincent_Willem_van_Gogh ;
                       :hasConcept :Concept_StarryNight ;
                       :hasInspirationSource :Urban_landscapes_of_Arles ;
                       :preceded :Starry_Night ;
                       :hasTitle "Cafe Terrace at Night"@en .


###  http://www.semanticweb.org/van_gogh_agony#Citron-yellow
:Citron-yellow rdf:type owl:NamedIndividual ,
                        :Color ;
               :hasMeaning :Religious_meaning ;
               :usedIn :Starry_Night .


###  http://www.semanticweb.org/van_gogh_agony#Concept_StarryNight
:Concept_StarryNight rdf:type owl:NamedIndividual ,
                              :ConceptOfArtwork ;
                     :hasSubject "Starry Night"@en .


###  http://www.semanticweb.org/van_gogh_agony#Emile_Bernard
:Emile_Bernard rdf:type owl:NamedIndividual ,
                        :Painter ;
               :hasName "Emile Bernard" .


###  http://www.semanticweb.org/van_gogh_agony#Eugene_Henri_Paul_Gauguin
:Eugene_Henri_Paul_Gauguin rdf:type owl:NamedIndividual ,
                                    :Painter ;
                           :hasName "Eugene Henri Paul Gauguin" .


###  http://www.semanticweb.org/van_gogh_agony#Idea_StarryNight
:Idea_StarryNight rdf:type owl:NamedIndividual ,
                           :IdeaOfArtwork ;
                  :isAbout :Starry_Night ;
                  :occuredIn :Arles ;
                  :occuredOn "Spring 1888" .


###  http://www.semanticweb.org/van_gogh_agony#Images_of_crescents_in_art
:Images_of_crescents_in_art rdf:type owl:NamedIndividual ,
                                     :Memory .


###  http://www.semanticweb.org/van_gogh_agony#Imagination_of_something_sublime
:Imagination_of_something_sublime rdf:type owl:NamedIndividual ,
                                           :Imagination ;
                                  :hasSubject "Imagination of something more sublime and pure opposed to everyday reality" .


###  http://www.semanticweb.org/van_gogh_agony#Lauren_Soth
:Lauren_Soth rdf:type owl:NamedIndividual ,
                      :Scholar ;
             :hasName "Lauren Soth" .


###  http://www.semanticweb.org/van_gogh_agony#Religious_meaning
:Religious_meaning rdf:type owl:NamedIndividual ,
                            :MainInterpretation ,
                            :Meaning ;
                   :isGivenBy :Lauren_Soth .


###  http://www.semanticweb.org/van_gogh_agony#Saint-Rémy-de-Provence
:Saint-Rémy-de-Provence rdf:type owl:NamedIndividual ,
                                 :RealPlace ;
                        :hasDescription "Saint-Rémy-de-Provence is a commune in the Bouches-du-Rhône department, Provence-Alpes-Côte d'Azur, Southern France. Located in the northern part of the Alpilles, of which it is the main town, it had a population of 9,893 in 2017."@en .


###  http://www.semanticweb.org/van_gogh_agony#Starry_Night
:Starry_Night rdf:type owl:NamedIndividual ,
                       :Painting ;
              :createdBy :Vincent_Willem_van_Gogh ;
              :hasConcept :Concept_StarryNight ;
              :hasInspirationSource :Alpilles_mountains ,
                                    :Images_of_crescents_in_art ,
                                    :Imagination_of_something_sublime ,
                                    :Typical_churches_of_Brabant_Netherlands ;
              :hasInterpretation :Religious_meaning ;
              :isRelatedTo :The_Agony_in_the_Garden ;
              :hasTitle "Starry Night"@en .


###  http://www.semanticweb.org/van_gogh_agony#Starry_Night_Order_the_Rhone
:Starry_Night_Order_the_Rhone rdf:type owl:NamedIndividual ,
                                       :Painting ;
                              :createdBy :Vincent_Willem_van_Gogh ;
                              :hasConcept :Concept_StarryNight ;
                              :hasInspirationSource :Urban_landscapes_of_Arles ;
                              :preceded :Starry_Night ;
                              :hasTitle "Starry Night Order the Rhone"@en .


###  http://www.semanticweb.org/van_gogh_agony#The_Agony_in_the_Garden
:The_Agony_in_the_Garden rdf:type owl:NamedIndividual ,
                                  :BiblicalEpisode ;
                         :isRelatedTo :Starry_Night ;
                         :hasSubject """Christ with the Angel in Gethsemane
or The Agony in the Garden"""@en .


###  http://www.semanticweb.org/van_gogh_agony#Typical_churches_of_Brabant_Netherlands
:Typical_churches_of_Brabant_Netherlands rdf:type owl:NamedIndividual ,
                                                  :Memory .


###  http://www.semanticweb.org/van_gogh_agony#Urban_landscapes_of_Arles
:Urban_landscapes_of_Arles rdf:type owl:NamedIndividual ,
                                    :Observed_Reality .


###  http://www.semanticweb.org/van_gogh_agony#Vincent_Willem_van_Gogh
:Vincent_Willem_van_Gogh rdf:type owl:NamedIndividual ,
                                  :Painter ;
                         :hasName "Vincent Willem van Gogh" .


###  http://www.semanticweb.org/van_gogh_agony#Working_from_imagination
:Working_from_imagination rdf:type owl:NamedIndividual ,
                                   :ArtisticApproach ;
                          :isSupportedBy :Emile_Bernard ,
                                         :Eugene_Henri_Paul_Gauguin ,
                                         :Vincent_Willem_van_Gogh ;
                          :usedIn :Starry_Night ;
                          :hasSubject "Working from imagination"@en .


###  Generated by the OWL API (version 4.5.24.2023-01-14T21:28:32Z) https://github.com/owlcs/owlapi
```
{% endcode %}

</details>

{% file src="../.gitbook/assets/Van_Gogh's_Agony (2).ttl" %}

<figure><img src="../.gitbook/assets/Van_Gogh&#x27;s_Agony_Graph_Visualization (2).svg" alt=""><figcaption><p><em><mark style="color:purple;"><strong>WebVOWL</strong></mark></em> <em><mark style="color:purple;"><strong>Graph Visualization</strong></mark></em></p></figcaption></figure>

{% file src="../.gitbook/assets/Van_Gogh's_Agony_Graph_Visualization (3).svg" %}

{% hint style="info" %}
### <mark style="color:orange;">Ontology Development of «Vincent van Gogh: The Starry Nigh»</mark>
{% endhint %}

<details>

<summary><mark style="color:blue;"><strong>Turtle Serialization</strong></mark></summary>

{% code title="Vincent_van_Gogh_The_Starry_Night.ttl" overflow="wrap" %}
```turtle
@prefix : <http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#> .

<http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#admittedTo
:admittedTo rdf:type owl:ObjectProperty ;
            rdfs:domain :Artist ;
            rdfs:range :Institution .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#applied
:applied rdf:type owl:ObjectProperty ;
         rdfs:domain :Painter ;
         rdfs:range :Color .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#associatedWith
:associatedWith rdf:type owl:ObjectProperty ;
                rdfs:domain :Painter ;
                rdfs:range :Art_Movement .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#becameASymbolOf
:becameASymbolOf rdf:type owl:ObjectProperty ;
                 rdfs:domain :Artwork ;
                 rdfs:range :Historical_and_Cultural_Significance .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#citedAs
:citedAs rdf:type owl:ObjectProperty ;
         rdfs:domain :Artwork ;
         rdfs:range :Historical_and_Cultural_Significance .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#contains
:contains rdf:type owl:ObjectProperty ;
          rdfs:domain :Painting ;
          rdfs:range :Complementary_Colors .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#contributedIn
:contributedIn rdf:type owl:ObjectProperty ;
               rdfs:domain :Artwork ;
               rdfs:range :Historical_and_Cultural_Significance .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#createdBy
:createdBy rdf:type owl:ObjectProperty ;
           rdfs:subPropertyOf owl:topObjectProperty ;
           rdfs:domain :Artwork ;
           rdfs:range :Person .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#emphasized
:emphasized rdf:type owl:ObjectProperty ;
            rdfs:domain :Art_Movement ;
            rdfs:range :Elements_of_Composition ,
                       :Emotion .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#employed
:employed rdf:type owl:ObjectProperty ;
          rdfs:domain :Painter ;
          rdfs:range :Brushstroke .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#evidentInTheUse
:evidentInTheUse rdf:type owl:ObjectProperty ;
                 rdfs:domain :Pattern ;
                 rdfs:range :Complementary_Colors .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#focusedOn
:focusedOn rdf:type owl:ObjectProperty ;
           rdfs:domain :Art_Movement ;
           rdfs:range :Color ,
                      :Elements_of_Composition .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#generated
:generated rdf:type owl:ObjectProperty ;
           rdfs:domain :Complementary_Colors ;
           rdfs:range :Elements_of_Composition .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#influencedBy
:influencedBy rdf:type owl:ObjectProperty ;
              rdfs:domain :Post-Impressionism ;
              rdfs:range :Impressionism .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#inspiredBy
:inspiredBy rdf:type owl:ObjectProperty ;
            rdfs:domain :Artist ;
            rdfs:range :Inspiration .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#interestedIn
:interestedIn rdf:type owl:ObjectProperty ;
              rdfs:domain :Painter ;
              rdfs:range :Color_Theory .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#interpretedAs
:interpretedAs rdf:type owl:ObjectProperty ;
               rdfs:domain :Painting ;
               rdfs:range :Interpretation .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#isSignificantElementIn
:isSignificantElementIn rdf:type owl:ObjectProperty ;
                        rdfs:domain :Color ;
                        rdfs:range :Painting .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#linkedWith
:linkedWith rdf:type owl:ObjectProperty ;
            rdfs:domain :Brushstroke ;
            rdfs:range :Emotion .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#locatedIn
:locatedIn rdf:type owl:ObjectProperty ;
           rdfs:domain :View ;
           rdfs:range :Place .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#referencedIn
:referencedIn rdf:type owl:ObjectProperty ;
              rdfs:domain :Painting ;
              rdfs:range :Popular_Culture .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#relatedTo
:relatedTo rdf:type owl:ObjectProperty ;
           rdfs:domain :Painting ;
           rdfs:range :Art_Movement .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#resultedIn
:resultedIn rdf:type owl:ObjectProperty ;
            rdfs:domain :Color ;
            rdfs:range :Artistic_Approach ,
                       :Artistic_Expression .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#seenAs
:seenAs rdf:type owl:ObjectProperty ;
        rdfs:domain :Brushstroke ;
        rdfs:range :Artistic_Approach .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#used
:used rdf:type owl:ObjectProperty ;
      rdfs:domain :Painter ;
      rdfs:range :Complementary_Colors .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#utilized
:utilized rdf:type owl:ObjectProperty ;
          rdfs:domain :Artist ;
          rdfs:range :Elements_of_Art .


#################################################################
#    Data properties
#################################################################

###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#bornInYear
:bornInYear rdf:type owl:DatatypeProperty ;
            rdfs:domain :Person ;
            rdfs:range xsd:integer .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#consideredAs
:consideredAs rdf:type owl:DatatypeProperty ;
              rdfs:domain :Person ;
              rdfs:range xsd:string .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#hasFullName
:hasFullName rdf:type owl:DatatypeProperty ;
             rdfs:domain :Person ;
             rdfs:range xsd:string .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#hasNationality
:hasNationality rdf:type owl:DatatypeProperty ;
                rdfs:domain :Person ;
                rdfs:range xsd:string .


#################################################################
#    Classes
#################################################################

###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Art_Movement
:Art_Movement rdf:type owl:Class .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Artist
:Artist rdf:type owl:Class ;
        rdfs:subClassOf :Person .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Artistic_Approach
:Artistic_Approach rdf:type owl:Class .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Artistic_Expression
:Artistic_Expression rdf:type owl:Class .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Artwork
:Artwork rdf:type owl:Class .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Asylum
:Asylum rdf:type owl:Class ;
        rdfs:subClassOf :Institution .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Balance
:Balance rdf:type owl:Class ;
         rdfs:subClassOf :Elements_of_Composition .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Brushstroke
:Brushstroke rdf:type owl:Class ;
             rdfs:subClassOf :Artistic_Expression .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Color
:Color rdf:type owl:Class ;
       rdfs:subClassOf :Elements_of_Art .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Color_Theory
:Color_Theory rdf:type owl:Class .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Commune
:Commune rdf:type owl:Class ;
         rdfs:subClassOf :Place .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Complementary_Colors
:Complementary_Colors rdf:type owl:Class ;
                      rdfs:subClassOf :Pattern .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Country
:Country rdf:type owl:Class ;
         rdfs:subClassOf :Place .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Elements_of_Art
:Elements_of_Art rdf:type owl:Class .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Elements_of_Composition
:Elements_of_Composition rdf:type owl:Class .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Emotion
:Emotion rdf:type owl:Class ;
         rdfs:subClassOf :Artistic_Expression .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Expressionism
:Expressionism rdf:type owl:Class ;
               rdfs:subClassOf :Art_Movement .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Historical_and_Cultural_Significance
:Historical_and_Cultural_Significance rdf:type owl:Class .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Impressionism
:Impressionism rdf:type owl:Class ;
               rdfs:subClassOf :Art_Movement .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Inspiration
:Inspiration rdf:type owl:Class .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Institution
:Institution rdf:type owl:Class ;
             rdfs:subClassOf :Place .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Interpretation
:Interpretation rdf:type owl:Class .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Line
:Line rdf:type owl:Class ;
      rdfs:subClassOf :Elements_of_Art .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Painter
:Painter rdf:type owl:Class ;
         rdfs:subClassOf :Artist .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Painting
:Painting rdf:type owl:Class ;
          rdfs:subClassOf :Artwork .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Pattern
:Pattern rdf:type owl:Class ;
         rdfs:subClassOf :Color_Theory .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Person
:Person rdf:type owl:Class .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Place
:Place rdf:type owl:Class ;
       rdfs:subClassOf :View .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Popular_Culture
:Popular_Culture rdf:type owl:Class ;
                 rdfs:subClassOf :Historical_and_Cultural_Significance .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Post-Impressionism
:Post-Impressionism rdf:type owl:Class ;
                    rdfs:subClassOf :Art_Movement .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Shape
:Shape rdf:type owl:Class ;
       rdfs:subClassOf :Elements_of_Art .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Structured_Compositions
:Structured_Compositions rdf:type owl:Class ;
                         rdfs:subClassOf :Elements_of_Composition .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Texture
:Texture rdf:type owl:Class ;
         rdfs:subClassOf :Elements_of_Art .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Town
:Town rdf:type owl:Class ;
      rdfs:subClassOf :Place .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Use_of_Light
:Use_of_Light rdf:type owl:Class ;
              rdfs:subClassOf :Elements_of_Composition .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#View
:View rdf:type owl:Class ;
      rdfs:subClassOf :Inspiration .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Visual_Tension
:Visual_Tension rdf:type owl:Class ;
                rdfs:subClassOf :Elements_of_Composition .


#################################################################
#    Individuals
#################################################################

###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Artistic_Legacy
:Artistic_Legacy rdf:type owl:NamedIndividual ,
                          :Historical_and_Cultural_Significance .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Balance
:Balance rdf:type owl:NamedIndividual ,
                  :Balance .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Blue
:Blue rdf:type owl:NamedIndividual ,
               :Complementary_Colors ;
      :generated :Balance ,
                 :Visual_Tension .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Bold_Brushstrokes
:Bold_Brushstrokes rdf:type owl:NamedIndividual ,
                            :Brushstroke ;
                   :linkedWith :Emotional_State ;
                   :seenAs :Unique_Style .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Bright_Colors
:Bright_Colors rdf:type owl:NamedIndividual ,
                        :Color ;
               :resultedIn :Emotional_State ,
                           :Visual_Impact .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Color
:Color rdf:type owl:NamedIndividual ,
                :Color ;
       :isSignificantElementIn :Starry_Night .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Color_Theory
:Color_Theory rdf:type owl:NamedIndividual ,
                       :Color_Theory .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Contrasting_Colors
:Contrasting_Colors rdf:type owl:NamedIndividual ,
                             :Color ;
                    :resultedIn :Emotional_State ,
                                :Visual_Impact .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Development_of_Modern_Art
:Development_of_Modern_Art rdf:type owl:NamedIndividual ,
                                    :Historical_and_Cultural_Significance .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Emotional_State
:Emotional_State rdf:type owl:NamedIndividual ,
                          :Emotion .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Example_of_Post-Impressionist_Style
:Example_of_Post-Impressionist_Style rdf:type owl:NamedIndividual ,
                                              :Historical_and_Cultural_Significance .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Expressionism
:Expressionism rdf:type owl:NamedIndividual ,
                        :Expressionism .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Expressive_Brushstrokes
:Expressive_Brushstrokes rdf:type owl:NamedIndividual ,
                                  :Brushstroke ;
                         :linkedWith :Emotional_State ;
                         :seenAs :Unique_Style .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Films
:Films rdf:type owl:NamedIndividual ,
                :Popular_Culture .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#France
:France rdf:type owl:NamedIndividual ,
                 :Country .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Impressionism
:Impressionism rdf:type owl:NamedIndividual ,
                        :Impressionism ;
               :focusedOn :Natural_Colors ,
                          :Use_of_Light .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Irises
:Irises rdf:type owl:NamedIndividual ,
                 :Painting ;
        :createdBy :Vincent_van_Gogh ;
        :relatedTo :Post-Impressionism .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Line
:Line rdf:type owl:NamedIndividual ,
               :Line .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Music
:Music rdf:type owl:NamedIndividual ,
                :Popular_Culture .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Natural_Colors
:Natural_Colors rdf:type owl:NamedIndividual ,
                         :Color .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Orange
:Orange rdf:type owl:NamedIndividual ,
                 :Complementary_Colors ;
        :generated :Balance ,
                   :Visual_Tension .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Personal_Struggles_with_Mental_Illness
:Personal_Struggles_with_Mental_Illness rdf:type owl:NamedIndividual ,
                                                 :Interpretation .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Post-Impressionism
:Post-Impressionism rdf:type owl:NamedIndividual ,
                             :Post-Impressionism ;
                    :emphasized :Structured_Compositions ,
                                :Subjective_Emotional_Expression ;
                    :influencedBy :Impressionism .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Saint-Paul-de-Mausole_Asylum
:Saint-Paul-de-Mausole_Asylum rdf:type owl:NamedIndividual ,
                                       :Asylum ;
                              :locatedIn :Saint-Rémy-de-Provence .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Saint-Rémy-de-Provence
:Saint-Rémy-de-Provence rdf:type owl:NamedIndividual ,
                                 :Commune ;
                        :locatedIn :France .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Shape
:Shape rdf:type owl:NamedIndividual ,
                :Shape .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Starry_Night
:Starry_Night rdf:type owl:NamedIndividual ,
                       :Painting ;
              :associatedWith :Post-Impressionism ;
              :becameASymbolOf :Artistic_Legacy ;
              :citedAs :Example_of_Post-Impressionist_Style ;
              :contains :Blue ,
                        :Orange ;
              :contributedIn :Development_of_Modern_Art ;
              :createdBy :Vincent_van_Gogh ;
              :inspiredBy :View_From_Bedroom_Window ;
              :interpretedAs :Personal_Struggles_with_Mental_Illness ,
                             :Transformative_Power_of_Nature_and_Art ;
              :referencedIn :Films ,
                            :Music ,
                            :Television ;
              :relatedTo :The_Bedroom .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Structured_Compositions
:Structured_Compositions rdf:type owl:NamedIndividual ,
                                  :Structured_Compositions .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Subjective_Emotional_Expression
:Subjective_Emotional_Expression rdf:type owl:NamedIndividual ,
                                          :Emotion .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Television
:Television rdf:type owl:NamedIndividual ,
                     :Popular_Culture .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Texture
:Texture rdf:type owl:NamedIndividual ,
                  :Texture .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#The_Bedroom
:The_Bedroom rdf:type owl:NamedIndividual ,
                      :Painting ;
             :createdBy :Vincent_van_Gogh ;
             :relatedTo :Post-Impressionism .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Transformative_Power_of_Nature_and_Art
:Transformative_Power_of_Nature_and_Art rdf:type owl:NamedIndividual ,
                                                 :Interpretation .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Unique_Style
:Unique_Style rdf:type owl:NamedIndividual ,
                       :Artistic_Approach .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Use_of_Light
:Use_of_Light rdf:type owl:NamedIndividual ,
                       :Use_of_Light .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#View_From_Bedroom_Window
:View_From_Bedroom_Window rdf:type owl:NamedIndividual ,
                                   :View ;
                          :locatedIn :France ,
                                     :Saint-Paul-de-Mausole_Asylum ,
                                     :Saint-Rémy-de-Provence .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Vincent_van_Gogh
:Vincent_van_Gogh rdf:type owl:NamedIndividual ,
                           :Painter ;
                  :admittedTo :Saint-Paul-de-Mausole_Asylum ;
                  :applied :Bright_Colors ,
                           :Contrasting_Colors ;
                  :associatedWith :Expressionism ,
                                  :Impressionism ,
                                  :Post-Impressionism ;
                  :employed :Bold_Brushstrokes ,
                            :Expressive_Brushstrokes ;
                  :inspiredBy :View_From_Bedroom_Window ;
                  :interestedIn :Color_Theory ;
                  :used :Blue ,
                        :Orange ;
                  :utilized :Color ,
                            :Line ,
                            :Shape ,
                            :Texture ;
                  :bornInYear 1853 ;
                  :consideredAs "Post-Impressionist" ;
                  :hasFullName "Vincent Willem van Gogh" ;
                  :hasNationality "Dutch" .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Visual_Impact
:Visual_Impact rdf:type owl:NamedIndividual ,
                        :Artistic_Approach .


###  http://www.semanticweb.org/Vincent_van_Gogh_The_Starry_Night#Visual_Tension
:Visual_Tension rdf:type owl:NamedIndividual ,
                         :Visual_Tension .


#################################################################
#    General axioms
#################################################################

[ rdf:type owl:AllDisjointClasses ;
  owl:members ( :Balance
                :Structured_Compositions
                :Use_of_Light
                :Visual_Tension
              )
] .


[ rdf:type owl:AllDisjointClasses ;
  owl:members ( :Expressionism
                :Impressionism
                :Post-Impressionism
              )
] .


###  Generated by the OWL API (version 4.5.25.2023-02-15T19:15:49Z) https://github.com/owlcs/owlapi
```
{% endcode %}

</details>

{% file src="../.gitbook/assets/Vincent_van_Gogh_The_Starry_Night.ttl" %}

<figure><img src="../.gitbook/assets/Vincent_van_Gogh_The_Starry_Night_Graph_Visualization (1).jpg" alt=""><figcaption><p><em><mark style="color:purple;"><strong>WebVOWL</strong></mark></em> <em><mark style="color:purple;"><strong>Graph Visualization</strong></mark></em></p></figcaption></figure>

{% file src="../.gitbook/assets/Vincent_van_Gogh_The_Starry_Night_Graph_Visualization (2).svg" %}

