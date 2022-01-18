
const createMessage = (type, message) => {
    const div = document.createElement('div')
    div.classList.add('msg', type == 'error' ? 'error-msg' : 'success-msg')
    div.textContent = message
    document.body.append(div)

    const t = setTimeout(() => {
        document.body.removeChild(div)
        clearTimeout(t)
    }, 3000)
}

const createToast = (type, message) => {
    const toastGroup = document.getElementById('toast-group')

    const toast = document.createElement('div')
    toast.classList.add('toast', type == 'error' ? 'error' : 'success')

    const div = document.createElement('div')
    toast.appendChild(div)

    const span = document.createElement('span')
    span.textContent = message

    toast.append(div)
    toast.append(span)

    toastGroup.appendChild(toast)

    const t = setTimeout(() => {
        toastGroup.removeChild(toast)
        clearTimeout(t)
    }, 2000)
}

const validateEmail = (email) => {
    return String(email)
        .toLowerCase()
        .match(
            /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        );
};