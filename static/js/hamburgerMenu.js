// OBS: Cada navbar das páginas deve usar os mesmos ID nas tags HTML para poder reaproveitar este script! 

// Captura os elementos do DOM
const openMenu = document.getElementById('open-menu');
const closeMenu = document.getElementById('close-menu');
const menu = document.getElementById('menu');

// Ação para abrir o menu
openMenu.addEventListener("click", () => {
    menu.style.display = 'flex';
    menu.style.right = (menu.offsetWidth * -1) + 'px';
    openMenu.style.display = 'none';

    setTimeout(() => {
        menu.style.opacity = '1';
        menu.style.right = '0';
    }, 10);
});

// Ação para fechar o menu
closeMenu.addEventListener("click", () => {
    menu.style.opacity = '1';
    menu.style.right = (menu.offsetWidth * -1) + 'px';

    setTimeout(() => {
        menu.removeAttribute('style');
        openMenu.removeAttribute('style');
    }, 10);
});