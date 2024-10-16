const fs = require("fs");
const path = require("path");
const dotenv = require("dotenv");

dotenv.config({ path: path.resolve(__dirname, ".env") });

const htmlFilePath = path.join(__dirname, "..", "build", "index.html");
let html = fs.readFileSync(htmlFilePath, "utf-8");

html = html.replace(/@myPortfolioURL/g, process.env.MY_PORTFOLIO_URL);

html = html.replace(/@portfolizerURL/g, process.env.PORTFOLIZER_URL);

if (process.env.GOOGLE_ANALYTICS_TRACKING_ID) {
    const gaTemplatePath = path.join(__dirname, "google_analytics.html");
    let googleAnalyticsTemplate = fs.readFileSync(gaTemplatePath, "utf-8");
    googleAnalyticsTemplate = googleAnalyticsTemplate.replace(
        /@googleAnalyticsTrackingID/g, process.env.GOOGLE_ANALYTICS_TRACKING_ID
    );
    html = html.replace("</body>", `${googleAnalyticsTemplate}\n</body>`);
}

fs.writeFileSync(htmlFilePath, html, "utf-8");
