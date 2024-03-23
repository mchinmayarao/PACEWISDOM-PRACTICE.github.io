var turn = document.getElementById("turn");
var boxes = document.querySelectorAll(".box");
var currentTurn = 'X';
var gameEnded = false;
// console.log(boxes);


function selectWinnerBoxes(b1, b2, b3) {
    b1.classList.add("win");
    b2.classList.add("win");
    b3.classList.add("win");
    turn.innerHTML = b1.innerHTML + " is a winner";
    gameEnded = true;
}

function getWinner() {
    var box1 = document.getElementById("box1"),
        box2 = document.getElementById("box2"),
        box3 = document.getElementById("box3"),
        box4 = document.getElementById("box4"),
        box5 = document.getElementById("box5"),
        box6 = document.getElementById("box6"),
        box7 = document.getElementById("box7"),
        box8 = document.getElementById("box8"),
        box9 = document.getElementById("box9");


    if (!gameEnded && box1.innerHTML !== "" && box1.innerHTML === box2.innerHTML && box1.innerHTML === box3.innerHTML)
        selectWinnerBoxes(box1, box2, box3);
    else if (!gameEnded && box4.innerHTML !== "" && box4.innerHTML === box5.innerHTML && box4.innerHTML === box6.innerHTML)
        selectWinnerBoxes(box4, box5, box6);
    else if (!gameEnded && box7.innerHTML !== "" && box7.innerHTML === box8.innerHTML && box7.innerHTML === box9.innerHTML)
        selectWinnerBoxes(box7, box8, box9);
    else if (!gameEnded && box1.innerHTML !== "" && box1.innerHTML === box4.innerHTML && box1.innerHTML === box7.innerHTML)
        selectWinnerBoxes(box1, box4, box7);
    else if (!gameEnded && box2.innerHTML !== "" && box2.innerHTML === box5.innerHTML && box2.innerHTML === box8.innerHTML)
        selectWinnerBoxes(box2, box5, box8);
    else if (!gameEnded && box3.innerHTML !== "" && box3.innerHTML === box6.innerHTML && box3.innerHTML === box9.innerHTML)
        selectWinnerBoxes(box3, box6, box9);
    else if (!gameEnded && box1.innerHTML !== "" && box1.innerHTML === box5.innerHTML && box1.innerHTML === box9.innerHTML)
        selectWinnerBoxes(box1, box5, box9);
    else if (!gameEnded && box3.innerHTML !== "" && box3.innerHTML === box5.innerHTML && box3.innerHTML === box7.innerHTML)
        selectWinnerBoxes(box3, box5, box7);
    else if (isTie()) {
        turn.innerHTML = "It's a Tie!";
        gameEnded = true;
    }
}

function isTie() {
    for (var i = 0; i < boxes.length; i++) {
        if (boxes[i].innerHTML === "") {
            return false;
        }
    }
    return true;
}

for (var i = 0; i < boxes.length; i++) {
    boxes[i].onclick = function () {
        if (!gameEnded && this.innerHTML == "") {
            if (currentTurn === "X") {
                // console.log(currentTurn, turn);
                this.innerHTML = "X";
                turn.innerHTML = "O Turn Now";
                getWinner();
                currentTurn = "O";
            } else {
                // console.log(currentTurn, turn);
                this.innerHTML = "O";
                turn.innerHTML = "X Turn Now";
                getWinner();
                currentTurn = "X";
            }
        }
    };
}


