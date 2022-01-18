
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

const inputSearch = document.getElementById('search')

inputSearch.addEventListener('input', async e => {
    const { value } = e.target

    const res = await axios.get(`/books/search?query=${value}`)
    const { books } = await res.data

    const searchResult = document.getElementById('search-result')
    searchResult.innerHTML = ''

    await books.forEach(b => {
        const a = document.createElement('a')
        a.href = `/books/${b._id}`
        a.target = '_blank'
        a.classList.add('search-result-item')
        const img = document.createElement('img')
        img.src = b.image
        const p = document.createElement('p')
        p.textContent = b.title
        a.append(img)
        a.append(p)
        searchResult.append(a)
    })
})