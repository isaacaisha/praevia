// /Users/lesanebyby/Projects/praevia/static/js/theme-switcher.js

document.addEventListener('DOMContentLoaded', () => {
    const themeSwitcherBtn = document.getElementById('theme-switcher-btn');

    // Define SVG icons with the same fill color as the other header icons
    // The theme's CSS will handle changing this color in dark mode
    const moonIcon = `
        <svg width="28" height="28" viewBox="0 0 28 28" fill="#67636D" xmlns="http://www.w3.org/2000/svg">
            <path d="M14 24.5a10.5 10.5 0 0 1-10.5-10.5c0-2.316.732-4.468 1.984-6.223A.75.75 0 0 1 5.992 7.7a8.5 8.5 0 0 0 15.016-1.573a.75.75 0 0 1 1.258.468a10.5 10.5 0 0 1-10.5 17.805Z" />
        </svg>
    `;

    const sunIcon = `
        <svg width="28" height="28" viewBox="0 0 28 28" fill="#67636D" xmlns="http://www.w3.org/2000/svg">
            <path d="M14 1a.75.75 0 0 1 .75.75v1.5a.75.75 0 0 1-1.5 0v-1.5a.75.75 0 0 1 .75-.75ZM14 25.25a.75.75 0 0 1 .75.75v1.5a.75.75 0 0 1-1.5 0v-1.5a.75.75 0 0 1 .75-.75ZM22.182 5.091a.75.75 0 0 1 .53.22l1.06 1.06a.75.75 0 0 1-1.06 1.06l-1.06-1.06a.75.75 0 0 1 .53-.22ZM5.091 22.182a.75.75 0 0 1 .22.53l1.06 1.06a.75.75 0 0 1-1.06 1.06l-1.06-1.06a.75.75 0 0 1 .53-.22ZM2.75 14a.75.75 0 0 1 .75.75h1.5a.75.75 0 0 1 0-1.5h-1.5a.75.75 0 0 1-.75.75ZM24.5 14a.75.75 0 0 1 .75.75h1.5a.75.75 0 0 1 0-1.5h-1.5a.75.75 0 0 1-.75.75ZM5.091 5.091a.75.75 0 0 1 .53-.22l1.06 1.06a.75.75 0 0 1-1.06 1.06l-1.06-1.06a.75.75 0 0 1 .53-.22ZM22.182 22.182a.75.75 0 0 1 .22.53l1.06 1.06a.75.75 0 0 1-1.06 1.06l-1.06-1.06a.75.75 0 0 1 .53-.22ZM14 6.75a7.25 7.25 0 1 0 0 14.5a7.25 7.25 0 0 0 0-14.5Z" />
        </svg>
    `;

    // Check for a saved theme preference in local storage
    const savedTheme = localStorage.getItem('theme');

    // Function to set the theme based on user preference
    function setTheme(theme) {
        if (theme === 'dark') {
            if (typeof dezSettingsOptions !== 'undefined') {
                dezSettingsOptions.version = 'dark';
                new dezSettings(dezSettingsOptions);
            }
            // Set the sun icon when in dark mode
            themeSwitcherBtn.innerHTML = sunIcon;
        } else {
            if (typeof dezSettingsOptions !== 'undefined') {
                dezSettingsOptions.version = 'light';
                new dezSettings(dezSettingsOptions);
            }
            // Set the moon icon when in light mode
            themeSwitcherBtn.innerHTML = moonIcon;
        }
        localStorage.setItem('theme', theme);
    }

    // Set initial theme on page load
    setTheme(savedTheme || 'light');

    // Add click event listener to the button
    themeSwitcherBtn.addEventListener('click', () => {
        const currentTheme = localStorage.getItem('theme') || 'light';
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setTheme(newTheme);
    });
});
