//document.getElementById("open-modal-btn").addEventListener("click", function(){
//    document.getElementById("my-modal").classList.add("open")
//})
//
//document.getElementById("close-my-modal-btn").addEventListener("click", function(){
//    document.getElementById("my-modal").classList.remove("open")
//})
//
//document.getElementById("open-modal-btn2").addEventListener("click", function(){
//    document.getElementById("my-modal").classList.add("open")
//})
//
//document.getElementById("close-my-modal-btn2").addEventListener("click", function(){
//    document.getElementById("my-modal").classList.remove("open")
//})

// Функция, которая меняет кнопки у которых айдишник занятости равен 0, 1 или 2
function colorChange(){
    for (let ret in arr_with_0){
        document.getElementById(`open-modal-btn-${arr_with_0[ret]}`).style.backgroundColor = "aliceblue";
    }

    for (let ret in arr_with_1){
        document.getElementById(`open-modal-btn-${arr_with_1[ret]}`).style.backgroundColor = "yellow";
    }

    for (let ret in arr_with_2){
        document.getElementById(`open-modal-btn-${arr_with_2[ret]}`).style.backgroundColor = "red";
    }
}

colorChange();