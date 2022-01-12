const getTest = async () => {
    const res = await fetch('/test')
    const message = await res.json()
    console.log(message)
}