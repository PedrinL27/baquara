document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('theme-toggle')
    if (!toggle) return
    const logo = document.getElementById('logo-img')

    const applyTheme = (theme) => {
        if (theme === 'dark') {
            document.body.setAttribute('data-theme', 'dark')
            toggle.classList.add('is-dark')
            toggle.setAttribute('aria-pressed', 'true')
            if (logo && logo.dataset && logo.dataset.dark) logo.src = logo.dataset.dark
        } else {
            document.body.removeAttribute('data-theme')
            toggle.classList.remove('is-dark')
            toggle.setAttribute('aria-pressed', 'false')
            if (logo && logo.dataset && logo.dataset.light) logo.src = logo.dataset.light
        }
    }

    const savedTheme = localStorage.getItem('theme')
    if (savedTheme) applyTheme(savedTheme)

    toggle.addEventListener('click', () => {
        const theme = document.body.getAttribute('data-theme')
        if (theme === 'dark') {
            applyTheme('light')
            localStorage.setItem('theme', 'light')
        } else {
            applyTheme('dark')
            localStorage.setItem('theme', 'dark')
        }
    })
})