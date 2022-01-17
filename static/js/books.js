const sort = document.getElementById('sort')
const url = new URL(window.location.href)
const s = url.searchParams

sort.value = s.get('sort') || 'date dsc'

sort.addEventListener('change', e => {
    const { value } = e.target

    s.set('sort', value)
    window.location.href = url.toString()
})