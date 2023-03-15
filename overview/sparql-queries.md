# 👾 SPARQL Queries

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
