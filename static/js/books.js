const sort = document.getElementById('sort')
const url = new URL(window.location.href)
const s = url.searchParams

sort.value = s.get('sort') || 'date dsc'

sort.addEventListener('change', e => {
    const { value } = e.target

    s.set('sort', value)
    window.location.href = url.toString()
})

const applybtn = document.getElementById('apply-btn')

const genreInput = document.querySelectorAll('input[name="genre"]')
let genreParam = s.get('genre') ? s.get('genre').split(',') : []

genreInput.forEach(g => {
    g.checked = genreParam.includes(g.value)
})

const languagesInput = document.querySelectorAll('input[name="language"]')
let languagesParams = s.get('languages') ? s.get('languages').split(',') : []

languagesInput.forEach(l => {
    l.checked = languagesParams.includes(l.value)
})

const fromDate = document.getElementById("from-date")
const untilDate = document.getElementById("until-date")

fromDate.value = s.get('from') || ''
untilDate.value = s.get('until') || ''

applybtn.addEventListener('click', e => {
    const checkedGenre = document.querySelectorAll('input[name="genre"]:checked')
    let genreVal = []

    checkedGenre.forEach(l => {
        genreVal = [...genreVal, l.value]
    })

    if (genreVal.length) {
        s.set('genre', genreVal.join(','))
    } else {
        s.delete('genre')
    }

    const checkedLanguages = document.querySelectorAll('input[name="language"]:checked')
    let languagesVal = []

    checkedLanguages.forEach(l => {
        languagesVal = [...languagesVal, l.value]
    })

    if (languagesVal.length) {
        s.set('languages', languagesVal.join(','))
    } else {
        s.delete('languages')
    }

    if (fromDate.value) {
        s.set('from', fromDate.value)
    } else {
        s.delete('from')
    }


    if (untilDate.value) {
        s.set('until', untilDate.value)
    } else {
        s.delete('until')
    }

    window.location.href = url.toString()
})