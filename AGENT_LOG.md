# Agent log

Add a dated entry each time you work with your AI coding agent, with the newest entry at the bottom. Each entry records what you asked the agent, what it produced, and what you checked or changed. Paste your key prompts in exactly as you typed them. Include at least one time the agent got something wrong, and how you caught it.

Copy this outline for each entry:

```markdown
## 2026-11-17: Created the first tables and charts to publish first versions of the website

- **Asked:** "Read AGENTS.md and docs/data_description_sheet.md first. Then show the mean sale price by each city on index.html and round to whole dollars."
- **Agent produced:** A table broken down by each city in the left most column with the state abbreviations in the middle column and the mean sales price in the right most column for each city. It also included a title with a small description at the top and a small note at the bottom of the page.
- **Checked or changed:** I checked this by reading through the changes in the index.html file, which showed no flaws or inconsistencies.

- **Asked:** "Pull the latest main, read AGENTS.md, and read docs/data_description_sheet.md first. Then show two side by side bar charts where the first one is the median sales price broken down by city and the second is the average days on market broken down by city on index.html. For these bar charts round the sales price to whole numbers and the days on market to two decimal places. Also order both from highest to lowest with labels that show the city, state and the value. Include a dashed line for the overall median of sales prices and the overall average for days on market."
- **Agent produced:** This created two horizontal bar charts side by side displaying the median sales by city, state on the left and the average days on market on the right. Both charts contained a vertical dashed red line marking the overall average for the respective metrics with titles, descriptions, and labels of the figures along with a short note at the bottom. It also created two new files, the first was a new data file with all of the metrics used broken down by each city to use for reference rather then recalculating the values. It also created a script to generate the bar charts rather then doing so directly in index.html.
- **Checked or changed:** I checked this by reviewing the data file in depth which was used as the foundation for the script and index.html file. I then scanned through the script and the index.html files to find any flaws or inconsistencies and make sure that no lines of code were removed that should not have been. After this I looked at the output html in depth to ensure that the output matched what I wanted and as a final check to find any mistakes or errors that I had overlooked while looking through the files.
```
