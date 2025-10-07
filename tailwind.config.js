/** @type {import('tailwindcss').Config} */
/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',   // 👈 tell Tailwind to use the .dark class
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          light: '#3b82f6',  // blue-500
          dark: '#1d4ed8',   // blue-700
        },
        background: {
          light: '#f9fafb',  // gray-50
          dark: '#111827',   // gray-900
        }
      },
    },
  },
  plugins: [],
}
