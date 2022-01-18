const statusSwitches = document.querySelectorAll("input[name='status']")

statusSwitches.forEach(s => {
    s.addEventListener('click', async e => {
        try {
            const res = await axios.patch(`/books/${e.target.id}/update-status`, {
                status: e.target.checked
            })
            const { message } = await res.data
            createToast('success', message)
            const t = setTimeout(() => {
                clearTimeout(t)
            }, 2000)
        } catch (err) {
            createToast('error', err.response.data.error)
        }
    })
})