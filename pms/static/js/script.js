document.onload = function() {
    if (document.getElementById('p0').checked) {
        document.getElementById('additional_quotes').innerHTML = '{% bootstrap_form quote_form2 %}\n{% bootstrap_form quote_form3 %}';
    }
};