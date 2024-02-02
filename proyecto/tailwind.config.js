/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js"
  ],
  theme: {
    extend: {
      textColor: {
        'orange-500': '#ff9900',
      },
    },
  },
  plugins: [],
}
