const buttons = document.getElementsByClassName("copy")
for (let button of buttons) {
    button.addEventListener("click", () => {
        const parent = button.parentNode;
        const codeBlock = parent.querySelector('code');
        navigator.clipboard.writeText(codeBlock.innerText);
    })
}