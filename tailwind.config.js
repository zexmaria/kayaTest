/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '**/templates/**/*.html'
  ],
  theme: {
    extend: {
      colors: {
        verdeKaya: '#738252',
      },
      fontFamily: {
        marvinVisions: ['MarvinVisions', 'sans-serif'],
      },
    },
  },
  plugins: [],
}