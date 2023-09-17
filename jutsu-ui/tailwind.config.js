/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    colors: {
      nord: {
        frost: {
          light: "#7BACBF", // Slightly desaturated and darkened
          medium: "#5A949B", // More desaturated and darkened
          dark: "#23565E", // Darkened a bit more
        },
        meadow: "#a3be8c",
        golden: "#ebcb8b",
        aurora: {
          red: "#BF616A",
          pink: "#fff5fb",
        },
        snowstorm: {
          light: "#EADFD9", // Slightly desaturated with a hint of warmth
          medium: "#C9CCBF", // More desaturated with a touch of warmth
        },
        "polar-night": {
          dark: "#2E3440",
          medium: "#3e4451",
          light: "#575d6b",
        },
      },
      gruvbox: {
        rose: {
          base: "#B16286",
          light: "#e491b6",
          "extra-light": "#fff6ff",
        },
        gold: {
          base: "#D79921",
          dark: "#6e4000",
        },
        sand: {
          light: "#EBDBB2",
          medium: "#ccbd95",
        },
        bg: {
          dark: "#282828",
          medium: "#383838",
          light: "#505050",
        },
      },
      // ... other themes or colors
    },
  },
  plugins: [],
};
