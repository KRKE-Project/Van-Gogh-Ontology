import rdflib

# Building the knowledge graph from .ttl
van_gogh_ont = rdflib.Graph()
van_gogh_ont.parse("Van_Gogh_Ontology.ttl", format="ttl")


# Formal competency questions (SPARQL queries) to the knowledge graph

# To the text "Van Gogh's Agony" by Lauren Soth :

# cq1) What is the interpretation of the "Starry Night" given by Lauren Soth? (Religious Meaning)
cq1 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?Interpretation
WHERE {
        :Starry_Night :hasInterpretation ?Interpretation .
        ?Interpretation rdf:type :Interpretation .
        ?Interpretation :isGivenBy :Lauren_Soth .    
}
'''

# cq2) Which biblical episode the “Starry Night” relates to? (The Agony in the Garden)
cq2 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?BiblicalEpisode
WHERE {  
        :Starry_Night :isRelatedTo ?BiblicalEpisode .   
        ?BiblicalEpisode rdf:type :Biblical_Episode .
}
'''

# cq3) When and where did the idea of Starry Night first come into Van Gogh's mind? (The spring of 1888. In Arles, France)
cq3 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?place ?date
WHERE {  
        ?Idea :isAbout :Starry_Night .
        ?Idea rdf:type :Idea_of_Artwork .
        ?Idea :occuredIn ?place .
        ?Idea :occuredOn ?date .
}
'''

# cq4) What is the real place that Van Gogh depicts in the "Starry Night"? (The Alpilles mountains)
cq4 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?place
WHERE {  
        ?place :isDepictedOn :Starry_Night .
        ?place rdf:type :Real_Place .
}
'''

# cq5) What were Van Gogh's artworks preceding the ‘Starry Night’ (sharing the same concept of starry night)? 
# (Cafe Terrace at Night, Starry Night Order the Rhone) 
cq5 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?Painting
WHERE {
        ?Painting rdf:type :Painting .
        ?Painting :hasConcept :Concept_StarryNight .
        ?Painting :preceded :Starry_Night .
}
'''

# cq6) What artistic approach does Vincent van Gogh use in the “Starry Night”? (Working from imagination)

cq6 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?ArtisticApproach
WHERE {
            ?ArtisticApproach :usedIn :Starry_Night .
            ?ArtisticApproach rdf:type :Artistic_Approach .
}
'''

# cq7) Who Van Gogh was sharing the idea of working from the imagination with? 
#(Eugène Henri Paul Gauguin and Émile Bernard)
cq7 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?Artist
WHERE {
            :Working_from_Imagination :isSupportedBy ?Artist .
            ?Artist rdf:type :Painter .
}
'''

# cqs8) What was the inspiration source for the “Starry Night”? (Images of crescents in art, Typical churches of Brabant Netherlands, 
# Imagination of something sublime, View From Bedroom Window)

cq8 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?Inspiration
WHERE {
      :Starry_Night :hasInspirationSource ?Inspiration.
}
'''

# cqs9) What are the colors used in the “Starry Night”? (Blue, Citron-yellow)

cq9 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?Color
WHERE {
        ?Color rdf:type :Complementary_Colors .
        ?Color :usedIn :Starry_Night .
}
'''

# cqs10) What determines the choice of colors for the “Starry Night”? (Religious meaning)

cq10 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?Meaning ?Color
WHERE {
        ?Color :usedIn :Starry_Night .
        ?Color rdf:type :Complementary_Colors .
        ?Color :hasMeaning ?Meaning .
}
'''

# To the text "Vincent van Gogh: The Starry Night" Richard Thomson :

# cqs11) What is the biography of Vincent Van Gogh? (Vincent Willem van Gogh, Dutch, 1853, post-Impressionist)
cq11 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?fullName ?nationality ?birthYear ?movement
WHERE {
                ?Artist :hasFullName ?fullName .
                ?Artist :hasNationality ?nationality .
                ?Artist :bornInYear ?birthYear .
                ?Artist :consideredAs ?movement .
}
'''

# cqs12) What are the different art movements that Van Gogh was associated with during his career? (Expressionism, Impressionism, Post-Impressionism)
cq12 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?movements
WHERE {
  :Vincent_van_Gogh :associatedWith ?movements
}
'''

# cqs13) What is the relationship between the post-Impressionist and Impressionist art movements? (Post-Impressionism was influenced by Impressionism)
cq13 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?movement1 ?property ?movement2 
WHERE {
  ?movement1 rdf:type :Post-Impressionism .
  ?movement2 rdf:type :Impressionism .
  ?movement1 ?property ?movement2 .
}
'''

# cqs14) What is the main focus of Impressionism? (Natural Colors, Use of Light)
cq14 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?characteristics
WHERE {
  :Impressionism :focusedOn ?characteristics .
}
'''

# cqs15) What are the key characteristics of Post-Impressionist art? (Structured Compositions, Subjective Emotional Expression)
cq15 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?characteristics
WHERE {
  :Post-Impressionism :emphasized ?characteristics .
}
'''

# cqs16) What is Van Gogh's use of colors like in his paintings? (Bright Colors, Contrasting Colors)
cq16 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?colors
WHERE {
  :Vincent_van_Gogh :applied ?colors.
}
'''

# cqs17) What are the different interpretations of "Starry Night"? (Personal Struggles with Mental Illness, 
# Transformative Power of Nature and Art)
cq17 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?interpretations
WHERE {
  :Starry_Night :interpretedAs ?interpretations.
}
'''

# cqs18) What is the association of the brushstrokes in “Starry Night” by Van Gogh? (Emotional State)
cq18 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT DISTINCT ?association
WHERE {
  ?brushstrokes :linkedWith ?association.
}
'''

# cqs19) What kind of brushstrokes did Van Gogh use in “Starry Night”? (Bold Brushstrokes, Expressive Brushstrokes)
cq19 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?brushstrokes
WHERE {
  :Vincent_van_Gogh :employed ?brushstrokes .
}
'''

# cqs20) What is the significance of the brushstrokes in “Starry Night”? (Unique Style)
cq20 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT DISTINCT ?significance
WHERE {
  ?brushstrokes :seenAs ?significance .
}
'''

# cqs21) What are the different elements of art that Van Gogh utilized in “Starry Night”? (Color, Line, Shape, Texture)
cq21 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT DISTINCT ?elements
WHERE {
  :Vincent_van_Gogh :utilized ?elements.
}
'''

# cqs22) What are some examples of popular culture references to “Starry Night”? (Films, Music, Television)
cq22 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?popular_culture
WHERE {
  :Starry_Night :referencedIn ?popular_culture .
}
'''

# cqs23) What impact did “Starry Night” have on the art world when it was first created? (Development of Modern Art)
cq23 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?contribution
WHERE {
  :Starry_Night :contributedIn ?contribution .
}
'''

# cqs24) What was the inspiration behind Van Gogh's “Starry Night”? (View From Bedroom Window)
cq24 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?inspiration
WHERE {
  :Starry_Night :inspiredBy ?inspiration .
}
'''

# cqs25) What was the setting or location of the inspiration for “Starry Night”? (France, Saint-Paul-de-Mausole Asylum, Saint-Rémy-de-Provence)
cq25 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?location
WHERE {
  :View_From_Bedroom_Window :locatedIn ?location .
}
'''

# cqs26) What are the effects of using complementary colors in “Starry Night”? (Balance, Visual Tension)
cq26 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT DISTINCT ?effect
WHERE {
  ?Complementary_colors :generated ?effect .
}
'''

# Questions of comparison / alignment to both texts

# cqs27)  What are the different interpretations of “Starry Night”? (Personal Struggles with Mental Illness, 
# Transformative Power of Nature and Art, Religious meaning)
cq27 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?interpretations
WHERE {
        :Starry_Night rdf:type :Painting .
        {:Starry_Night :hasInterpretation ?interpretations }
        UNION
        {:Starry_Night :interpretedAs ?interpretations }
}
'''

# cqs28) Which paintings by Van Gogh related to the post-Impressionist movement? (Cafe Terrace at Night, Irises, 
# Starry Night, Starry Night Order the Rhone, The Bedroom)
cq28 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT ?paintings
WHERE {
  ?paintings :relatedTo :Post-Impressionism .
}
'''

# cq29) What was the inspiration behind Van Gogh's “Starry Night”? (View From Bedroom Window, 
# Typical churches of Brabant Netherlands, Images of crescents in art, Imagination of something sublime)
cq29 = '''
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 

SELECT DISTINCT ?inspiration
WHERE {
  :Starry_Night rdf:type :Painting .
  {:Starry_Night :inspiredBy ?inspiration }
  UNION
  {:Starry_Night :hasInspirationSource ?inspiration }
}
'''

# Printing query results

cqs = [cq1, cq2, cq3, cq4, cq5, cq6, cq7, cq8, cq9, cq10, cq11, cq12, cq13, cq14, cq15, cq16, cq17, cq18, cq19, cq20, cq21, cq22, cq23, cq24, cq25, cq26, cq27, cq28, cq29]

for idx, cq in enumerate(cqs):
    print("Results for cq " + str(idx+1) + ":")
    results = van_gogh_ont.query(cq)
    for result in results:
        print(result)
