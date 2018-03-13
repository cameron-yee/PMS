document.onload = function() {
    var price = document.getElementById('id_QPrice');
    var quantity = document.getElementById('id_quantity');
    var total = price * quantity;

    if (total >= 500) {
        document.getElementById('additional_quotes').innerHTML = '{% bootstrap_form quote_form_2 %}\n{% bootstrap_form quote_form_3 %}';
    }
};