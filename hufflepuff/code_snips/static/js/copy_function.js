buttons = document.getElementsByClassName("copy")

for (let button of buttons) {
    button.addEventListener("mouseover", (e) => {
        console.log("On Copy Button")
    })
    button.addEventListener("mouseout", (e) => {
        console.log("Off Copy Button")
    })
}