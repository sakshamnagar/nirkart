function Address() {
    var a = document.getElementById('addaddress');
    var b = document.getElementById('viewaddress');
    if (a.style.display === 'none') {
        b.style.display = 'none';
        a.style.display = 'block';
    }
}