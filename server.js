const express = require('express');
const cors = require('cors');
const fs = require('fs');
const app = express();

app.use(cors());

let auditData = [];

try {
    // Sync read kora thik ache jeheto eta server start-er shomoy ekbar-i hobe
    const rawData = fs.readFileSync('audit_data.json', 'utf8');
    auditData = JSON.parse(rawData);
    console.log(`Successfully loaded ${auditData.length} records.`);
} catch (error) {
    console.error("Error loading JSON file:", error.message);
}

app.get('/search/:tin', (req, res) => {
    const searchTin = req.params.tin.trim(); // space thakle remove korbe
    const result = auditData.find(item => item.tin === searchTin);

    if (result) {
        res.json({ found: true, data: result });
    } else {
        res.json({ found: false });
    }
});

app.listen(5000, () => console.log("Server running on http://localhost:5000"));