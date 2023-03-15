# 👾 SPARQL Queries

<table data-card-size="large" data-view="cards"><thead><tr><th align="center"></th><th></th><th></th></tr></thead><tbody><tr><td align="center"><em><mark style="color:blue;"><strong>What is the interpretation of the "Starry Night" given by Lauren Soth?</strong></mark></em></td><td><pre class="language-sparql" data-overflow="wrap"><code class="lang-sparql">SELECT ?Interpretation
WHERE {
        :Starry_Night :hasInterpretation ?Interpretation .
        ?Interpretation rdf:type :Interpretation .
        ?Interpretation :isGivenBy :Lauren_Soth .    
}
</code></pre></td><td></td></tr><tr><td align="center"></td><td></td><td></td></tr><tr><td align="center"></td><td></td><td></td></tr></tbody></table>
