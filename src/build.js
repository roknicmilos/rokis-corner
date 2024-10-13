const fs = require("fs");
const path = require("path");
const dotenv = require("dotenv");

dotenv.config({ path: path.resolve(__dirname, ".env") });
const htmlFilePath = path.join(__dirname, "..", "build", "index.html");
let html = fs.readFileSync(htmlFilePath, "utf-8");
html = html.replace(/@portfolioURL/g, process.env.PORTFOLIO_URL);
fs.writeFileSync(htmlFilePath, html, "utf-8");
