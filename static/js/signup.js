const form = document.getElementById('signup-form')

const createMessage = (message, type) => {
    const div = document.createElement('div')
    div.classList.add(['msg', type == 'error' ? 'error-msg' : 'success-msg'])
    div.textContent = message
}

form.addEventListener('submit', e => {
    e.preventDefault()

    const formData = new FormData(form)

    console.log(e.target.name)
})