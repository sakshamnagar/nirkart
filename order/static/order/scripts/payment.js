function payment() {
    var a = document.getElementById('payment');
    var b = document.getElementById('payment2');
    if (a.style.display === 'none') {
        a.style.display = 'block';
        b.style.display = 'none';
    }
}


function payment2() {
    var a = document.getElementById('payment');
    var b = document.getElementById('payment2');
    if (b.style.display === 'none') {
        b.style.display = 'block';
        a.style.display = 'none';
    }
}


function payment3() {
    var a = document.getElementById('payment');
    var b = document.getElementById('payment2');
    if (b.style.display === 'block' || a.style.display === 'block') {
        b.style.display = 'none';
        a.style.display = 'none';
    }
}


function Address(radio) {
    var a = document.getElementById('newaddress');
    if (a.style.display === 'none') {
        a.style.display = 'block';
    }
    document.getElementById('address').required = radio.checked;
    document.getElementById('address2').required = radio.checked;
    document.getElementById('state').required = radio.checked;
    document.getElementById('city').required = radio.checked;
    document.getElementById('zip').required = radio.checked;
    
}


function HideAddress() {
    var a = document.getElementById('newaddress');
    if (a.style.display === 'block') {
        a.style.display = 'none';
    }
}

