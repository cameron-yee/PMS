document.mainForm.onclick = function(){
    var gender = document.querySelector('input[name = gender]:checked').value;
    result.innerHTML = 'You Gender: '+gender;
}