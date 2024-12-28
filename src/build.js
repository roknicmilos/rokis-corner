const fs = require("fs");
const path = require("path");
const dotenv = require("dotenv");

dotenv.config({ path: path.resolve(__dirname, ".env") });

const htmlFilePath = path.join(__dirname, "..", "build", "index.html");
let html = fs.readFileSync(htmlFilePath, "utf-8");

html = html.replace(/@myPortfolioURL/g, process.env.MY_PORTFOLIO_URL);

html = html.replace(/@portfolizerURL/g, process.env.PORTFOLIZER_URL);

fs.writeFileSync(htmlFilePath, html, "utf-8");
