/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}"
  ],
  theme: {
    extend: {
      colors: {
        botBg: "#343541",
        botBubble: "#444654",
        botUser: "#5f5f5fff",
        botBot: "#686868ff",
        botAccent: "#10a37f",
      },
    },
  },
  plugins: [],
}

