/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js,vue}"],
  theme: {
    extend: {
      colors:{
        "custom-dark-blue": "#13305e",
        "custom-ligh-blue":"#0A2E66",
        "custom-dark-aqua":"#2C9C9C",
        "error-color":"#724b4b",
        "header-dark-blue":"#102039",
        "custom-menu-color":"#184ea5",
        "custom-deep-purple":"#4b32b0",
      },
      minHeight: {
        '3/4': '80vh',
      },
      textDecorationThickness: {
        3: '3px',
      },
      borderWidth: {
        '3': '3px',
      }
    },
  },
  plugins: [],
}
