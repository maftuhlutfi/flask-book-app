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

const deleteButtons = document.querySelectorAll('#delete-btn')

deleteButtons.forEach(d => {
    d.addEventListener('click', async e => {
        const id = e.target.dataset.bookId
        try {
            const res = await axios.delete(`/books/${id}/delete`)
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
})