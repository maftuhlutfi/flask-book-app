const form = document.getElementById('signup-form')

form.addEventListener('submit', async e => {
    e.preventDefault()

    const data = new FormData(form)
    data.append('name', 'name')
    data.append('email', 'email')
    data.append('password', 'password')
    data.append('confirm_password', 'confirm_password')


    const name = data.get('name'),
        email = data.get('email'),
        password = data.get('password'),
        confirm_password = data.get('confirm_password')

    if (!email || !password || !confirm_password) {
        createMessage('error', 'Please fill all form')
        return
    }

    if (!validateEmail(email)) {
        createMessage('error', 'Email is not valid')
        return
    }

    if (password != confirm_password) {
        createMessage('error', 'Password confirmation is not same')
        return
    }

    try {
        const res = await axios.post('/user/signup', {
            name,
            email,
            password
        })
        const { message } = await res.data
        createMessage('success', message)
        const t = setTimeout(() => {
            window.location.href = '/login'
            clearTimeout(t)
        }, 2000)
    } catch (err) {
        createMessage('error', err.response.data.error)
    }
})