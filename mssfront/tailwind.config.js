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
      },
    },
  },
  plugins: [],
}
