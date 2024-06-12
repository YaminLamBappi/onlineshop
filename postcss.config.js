module.exports = {
  content: ["./templates/**/*.html", "./static/src/js/*.js"],
  theme: {
    extend: {
      colors: {
        dark: "#1a202c",
        light: "#ffffff",
      },
    },
  },
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
