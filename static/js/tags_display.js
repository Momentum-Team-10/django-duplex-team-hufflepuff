const tags = document.querySelectorAll('label')
for (let tag of tags) {
    tag.classList.add("pa3")
}

const unlist = document.getElementById('id_tags')
unlist.setAttribute("class", "list courier flex flex-wrap justify-center items-center")