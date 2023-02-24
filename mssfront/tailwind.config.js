/** @type {import('tailwindcss').Config} */
module.exports = {
  
  content: ["./src/**/*.{html,js,vue}",'./node_modules/tw-elements/dist/js/**/*.js'],
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
        "error-message-bg":"#ffe7e6",
        "success-message-bg":"#caf1d8",
        "success-message-color":"#1ea97c",
      },
      minHeight: {
        '3/4': '80vh',
      },
      textDecorationThickness: {
        3: '3px',
      },
      borderWidth: {
        '1':'1px',
        '3': '3px',
      }
    },
  },
  plugins: [
    require('tw-elements/dist/plugin')
  ]
}
