const form = document.getElementById('scrap-form')

form.addEventListener('submit', async e => {
    e.preventDefault()

    const data = new FormData(form)
    data.append('title', 'title')
    data.append('links', 'links')


    const title = data.get('title'),
        links = data.get('links')

    try {
        const res = await axios.post('/scrap', {
            title,
            links: links.split(';')
        })
        const { message } = await res.data
        createMessage('success', message)
        const t = setTimeout(() => {
            window.location.reload()
            clearTimeout(t)
        }, 2000)
    } catch (err) {
        createMessage('error', err.response.data.error)
    }
})