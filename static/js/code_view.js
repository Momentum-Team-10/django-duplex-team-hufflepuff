console.log("I have JS")


console.log('HELLOOOO HI HEY')

function getCookie(name) {
  let cookieValue = null
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';')
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim()
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
        break
      }
    }
  }
  return cookieValue
}
const csrfToken = getCookie('csrftoken')

const favLink = document.querySelector('.fav-link')
favLink.addEventListener('click', (event) => {
  event.preventDefault()
  const url = event.target.parentNode.href
  // check the state of whether it is favorited or not in the DOM
  const favorited = event.target.parentNode.dataset['favorited']
  const starIcon = event.target
  const request_method = favorited === 'True' ? 'DELETE' : 'POST'
  fetch(url, {
    headers: {
      'X-Requested-With': 'XMLHttpRequest',
      'X-CSRFToken': csrfToken,
    },
    method: request_method,
  })
    .then((res) => res.json())
    .then((data) => {
      // here I can do stuff with that data!
      if (data['favorited']) {
        // replace the heart icon to solid to indicate that it IS favorited
        starIcon.classList.replace('far', 'fas')
        // update state in the DOM to show that it is favorited
        event.target.parentNode.dataset['favorited'] = 'True'
      } else {
        // replate the heart icon class to outline to indicate that it's NOT favorited
        starIcon.classList.replace('fas', 'far')
        // update state in the DOM to show that it is not favorited
        event.target.parentNode.dataset['favorited'] = 'False'
      }
    })
})
