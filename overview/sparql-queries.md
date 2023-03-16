# 👾 SPARQL Queries

```sparql
PREFIX : <http://www.semanticweb.org/van_gogh_ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
```

## <mark style="color:purple;">Van Gogh's Agony by Lauren Soth</mark>

<table data-card-size="large" data-view="cards"><thead><tr><th align="center"></th><th></th><th></th><th></th></tr></thead><tbody><tr><td align="center"><em><mark style="color:blue;"><strong>What is the interpretation of the "Starry Night" given by Lauren Soth?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?Interpretation
WHERE {
        :Starry_Night :hasInterpretation ?Interpretation .
        ?Interpretation rdf:type :Interpretation .
        ?Interpretation :isGivenBy :Lauren_Soth .    
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Religious meaning</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>Which biblical episode the “Starry Night” relates to?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?BiblicalEpisode
WHERE {  
        :Starry_Night :isRelatedTo ?BiblicalEpisode .   
        ?BiblicalEpisode rdf:type :Biblical_Episode .
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>The Agony in the Garden</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>When and where did the idea of Starry Night first come into Van Gogh's mind?</strong></mark></em> </td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?place ?date
WHERE {  
        ?Idea :isAbout :Starry_Night .
        ?Idea rdf:type :Idea_of_Artwork .
        ?Idea :occuredIn ?place .
        ?Idea :occuredOn ?date .
}
'''
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>The spring of 1888. In Arles, France</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What is the real place that Van Gogh depicts in the "Starry Night"?</strong></mark></em> </td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?place
WHERE {  
        ?place :isDepictedOn :Starry_Night .
        ?place rdf:type :Real_Place .
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>The Alpilles mountains</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What were Van Gogh's artworks preceding the ‘Starry Night’ (sharing the same concept of starry night)?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?Painting
WHERE {
        ?Painting rdf:type :Painting .
        ?Painting :hasConcept :Concept_StarryNight .
        ?Painting :preceded :Starry_Night .
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Cafe Terrace at Night, Starry Night Order the Rhone</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What artistic approach does Vincent van Gogh use in the “Starry Night”?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?ArtisticApproach
WHERE {
            ?ArtisticApproach :usedIn :Starry_Night .
            ?ArtisticApproach rdf:type :Artistic_Approach .
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Working from imagination</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>Who Van Gogh was sharing the idea of working from the imagination with?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?Artist
WHERE {
            :Working_from_Imagination :isSupportedBy ?Artist .
            ?Artist rdf:type :Painter .
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Eugène Henri Paul Gauguin, Émile Bernard</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What was the inspiration source for the “Starry Night”?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?Inspiration
WHERE {
      :Starry_Night :hasInspirationSource ?Inspiration.
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Images of crescents in art, Typical churches of Brabant Netherlands, Imagination of something sublime, View From Bedroom Window</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What are the colors used in the “Starry Night”?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?Color
WHERE {
        ?Color rdf:type :Complementary_Colors .
        ?Color :usedIn :Starry_Night .
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Blue, Citron-yellow</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What determines the choice of colors for the “Starry Night”?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?Meaning ?Color
WHERE {
        ?Color :usedIn :Starry_Night .
        ?Color rdf:type :Complementary_Colors .
        ?Color :hasMeaning ?Meaning .
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Religious meaning</strong></mark></td></tr></tbody></table>

## <mark style="color:purple;">Vincent van Gogh: The Starry Night by Richard Thomson</mark>

<table data-card-size="large" data-view="cards"><thead><tr><th align="center"></th><th></th><th></th><th></th></tr></thead><tbody><tr><td align="center"><em><mark style="color:blue;"><strong>What is the biography of Vincent Van Gogh?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?fullName ?nationality ?birthYear ?movement
WHERE {
                ?Artist :hasFullName ?fullName .
                ?Artist :hasNationality ?nationality .
                ?Artist :bornInYear ?birthYear .
                ?Artist :consideredAs ?movement .
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Vincent Willem van Gogh, Dutch, 1853, post-Impressionist</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What are the different art movements that Van Gogh was associated with during his career?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?movements
WHERE {
  :Vincent_van_Gogh :associatedWith ?movements
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Expressionism, Impressionism, Post-Impressionism</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What is the relationship between the post-Impressionist and Impressionist art movements?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?movement1 ?property ?movement2 
WHERE {
  ?movement1 rdf:type :Post-Impressionism .
  ?movement2 rdf:type :Impressionism .
  ?movement1 ?property ?movement2 .
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Post-Impressionism was influenced by Impressionism</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What is the main focus of Impressionism?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?characteristics
WHERE {
  :Impressionism :focusedOn ?characteristics .
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Natural Colors, Use of Light</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What are the key characteristics of Post-Impressionist art?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?characteristics
WHERE {
  :Post-Impressionism :emphasized ?characteristics .
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Structured Compositions, Subjective Emotional Expression</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What is Van Gogh's use of colors like in his paintings?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?colors
WHERE {
  :Vincent_van_Gogh :applied ?colors.
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Bright Colors, Contrasting Colors</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What are the different interpretations of “Starry Night”?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?interpretations
WHERE {
  :Starry_Night :interpretedAs ?interpretations.
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Personal Struggles with Mental Illness, Transformative Power of Nature and Art</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What is the association of the brushstrokes in “Starry Night”?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT DISTINCT ?association
WHERE {
  ?brushstrokes :linkedWith ?association.
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Emotional State</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What kind of brushstrokes did Van Gogh use in “Starry Night”?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?brushstrokes
WHERE {
  :Vincent_van_Gogh :employed ?brushstrokes .
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Bold Brushstrokes, Expressive Brushstrokes</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What is the significance of the brushstrokes in “Starry Night” by Van Gogh?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT DISTINCT ?significance
WHERE {
  ?brushstrokes :seenAs ?significance .
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Unique Style</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What are the different elements of art that Van Gogh utilized in “Starry Night”?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT DISTINCT ?elements
WHERE {
  :Vincent_van_Gogh :utilized ?elements.
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Color, Line, Shape, Texture</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What are some examples of popular culture references to “Starry Night”?</strong></mark></em> </td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?popular_culture
WHERE {
  :Starry_Night :referencedIn ?popular_culture .
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Films, Music, Television</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What impact did "Starry Night" have on the art world when it was first created?</strong></mark></em> </td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?contribution
WHERE {
  :Starry_Night :contributedIn ?contribution .
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Development of Modern Art</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What was the inspiration behind Van Gogh's “Starry Night”?</strong></mark></em> </td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?inspiration
WHERE {
  :Starry_Night :inspiredBy ?inspiration .
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>View From Bedroom Window</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What was the setting or location of the inspiration for “Starry Night”?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?location
WHERE {
  :View_From_Bedroom_Window :locatedIn ?location .
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>France, Saint-Paul-de-Mausole Asylum, Saint-Rémy-de-Provence</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What are the effects of using complementary colors in “Starry Night”?</strong></mark></em> </td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT DISTINCT ?effect
WHERE {
  ?Complementary_colors :generated ?effect .
}
</code></pre></td><td>Output:</td><td> <mark style="color:orange;"><strong>Balance, Visual Tension</strong></mark></td></tr></tbody></table>

## <mark style="color:purple;">Comparison of Both Texts</mark>

<table data-card-size="large" data-view="cards"><thead><tr><th align="center"></th><th></th><th></th><th></th></tr></thead><tbody><tr><td align="center"><em><mark style="color:blue;"><strong>What are the different interpretations of “Starry Night”?</strong></mark></em> </td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?interpretations
WHERE {
        :Starry_Night rdf:type :Painting .
        {:Starry_Night :hasInterpretation ?interpretations }
        UNION
        {:Starry_Night :interpretedAs ?interpretations }
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Personal Struggles with Mental Illness, Transformative Power of Nature and Art, Religious meaning</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>Which paintings by Van Gogh related to the post-Impressionist movement?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?paintings
WHERE {
  ?paintings :relatedTo :Post-Impressionism .
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>Cafe Terrace at Night, Irises, Starry Night, Starry Night Order the Rhone, The Bedroom</strong></mark></td></tr><tr><td align="center"><em><mark style="color:blue;"><strong>What was the inspiration behind Van Gogh's “Starry Night”?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT DISTINCT ?inspiration
WHERE {
  :Starry_Night rdf:type :Painting .
  {:Starry_Night :inspiredBy ?inspiration }
  UNION
  {:Starry_Night :hasInspirationSource ?inspiration }
}
</code></pre></td><td>Output:</td><td><mark style="color:orange;"><strong>View From Bedroom Window, Typical churches of Brabant Netherlands, Images of crescents in art, Imagination of something sublime</strong></mark></td></tr></tbody></table>

{% file src="../.gitbook/assets/SPARQL_Queries.py" %}
