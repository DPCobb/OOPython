function formValid(event){
    // This function validates that there is something in the inputs
    // Setting up vars to target form inputs
    var name = document.getElementById('user').value;
    var t = document.getElementById('total').value;
    var tip = document.getElementById('tip').value
    var g = document.getElementById('guests').value
    // check the inputs
    // if var == null or var is "" then prevent default action and alert user
    if(name == null || name == ""){
        event.preventDefault();
        alert('User name required.');
        return false;
    };
    if(t == null || t == ""){
        event.preventDefault();
        alert('Total required.');
        return false;
    };
    if(tip == null || tip == ""){
        event.preventDefault();
        alert('Tip required.');
        return false;
    };
    if(g == null || g == ""){
        event.preventDefault();
        alert('Number of guests required.');
        return false;
    };
};