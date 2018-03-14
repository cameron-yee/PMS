document.onload = function() {
<<<<<<< HEAD
    if (document.getElementById('p0').checked) {
        document.getElementById('additional_quotes').innerHTML = '{% bootstrap_form quote_form2 %}\n{% bootstrap_form quote_form3 %}';
=======
    var price = document.getElementById('id_QPrice');
    var quantity = document.getElementById('id_quantity');
    var total = price * quantity;

    if (total >= 500) {
        document.getElementById('additional_quotes').innerHTML = '{% bootstrap_form quote_form_2 %}\n{% bootstrap_form quote_form_3 %}';
>>>>>>> fb6f23c9a0f9a8fb45931b9c59219143f269c2c2
    }
};