const form = document.getElementById('login-form')

form.addEventListener('submit', async e => {
    e.preventDefault()

    const data = new FormData(form)
    data.append('email', 'email')
    data.append('password', 'password')


    const email = data.get('email'),
        password = data.get('password')

    if (!email || !password) {
        createMessage('error', 'Please fill all form')
        return
    }

    if (!validateEmail(email)) {
        createMessage('error', 'Email is not valid')
        return
    }

    try {
        const res = await axios.post('/user/login', {
            email,
            password
        })
        const { message } = await res.data
        createMessage('success', message)
        const t = setTimeout(() => {
            window.location.href = '/'
            clearTimeout(t)
        }, 2000)
    } catch (err) {
        createMessage('error', err.response.data.error)
    }
})

if (window.location.href.includes('filter-sort')) {
    createMessage('error', 'Please login first.')
}