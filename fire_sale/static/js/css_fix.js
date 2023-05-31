document.addEventListener('DOMContentLoaded', () => {
    // Bootstrap variables are unaccessible from main.css so we have to fetch them after content is loaded
    const navbarPaddingY = getComputedStyle(document.querySelector('.navbar')).getPropertyValue('--bs-navbar-padding-y');
    const navbarBrandPaddingY = getComputedStyle(document.querySelector('.navbar')).getPropertyValue('--bs-navbar-brand-padding-y');
    document.documentElement.style.setProperty('--nav-main-bar-height', `calc(max(var(--nav-item-size), var(--nav-item-min-size)) + 2*${navbarPaddingY} + 2*${navbarBrandPaddingY}`);
  });