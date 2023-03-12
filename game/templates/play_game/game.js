
function Game() {
    document.getElementById('rock').addEventListener("click", function (){playGame('rock')});
    document.getElementById('paper').addEventListener("click", function (){playGame('rock')});
    document.getElementById('scissors').addEventListener("click", function (){playGame('rock')});
    var userScore = document.getElementById('userScore');
    var computerScore = document.getElementById('computerScore');
    var updatedUserScore = 0
    var updatedComputerScore = 0



    function playGame(userChoice) {
        const options = ['rock', 'paper', 'scissors'];
        var computerChoice = options[Math.floor(Math.random()*3)]
        console.log(computerChoice)
        const winning_combination = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }
        if(userChoice === computerChoice) {
            console.log('Its a tie');
        }

        else if(winning_combination[userChoice] === computerChoice){
            console.log('You Won')
            updatedUserScore++;
            userScore.textContent = updatedUserScore
        }
        else{
            console.log('You lost')
            updatedComputerScore++;
            computerScore.textContent = updatedComputerScore
        }
    }

}
Game();