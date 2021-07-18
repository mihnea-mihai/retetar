var slider = document.getElementById("servings_slider");
var number = document.getElementById("servings_number");
var initial_number = number.innerHTML;

var qtys = document.getElementsByClassName("mutable qty");
var qtys_per_serving = Array(qtys.length)

for (let i = 0; i < qtys.length; i++) {
    qtys_per_serving[i] = qtys[i].innerHTML / initial_number;
}

slider.oninput = function() {
    number.innerHTML = this.value;
    
    for (let i = 0; i < qtys.length; i++) {
        qtys[i].innerHTML = parseFloat((qtys_per_serving[i] * number.innerHTML).toFixed(1));
    }
}
