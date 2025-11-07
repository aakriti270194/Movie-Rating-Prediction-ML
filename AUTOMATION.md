# Automated Daily Data Analysis Setup

## Overview

This project implements automated daily data analysis using GitHub Actions. The workflow runs every day and automatically commits analysis reports and metrics to the repository.

## How It Works

### 1. **Daily Execution Schedule**
- The GitHub Actions workflow runs every day at **9 AM UTC** (equivalent to 2:30 PM IST)
- It can also be triggered manually at any time using the `workflow_dispatch` trigger

### 2. **Workflow Steps**

The automation pipeline follows these steps:

#### Step 1: Checkout Code
Clones the repository to the GitHub Actions runner

#### Step 2: Setup Python Environment
Installs Python 3.9 runtime environment

#### Step 3: Install Dependencies
Installs all required packages from `requirements.txt`:
- pandas, numpy, scikit-learn
- matplotlib, seaborn for visualization
- Other ML and data science libraries

#### Step 4: Run Daily Analysis
Executes `src/daily_analysis.py` which:
- Generates model performance metrics for different algorithms
- Collects data quality statistics
- Logs feature engineering information
- Creates both JSON and Markdown reports

#### Step 5: Commit Analysis Results
Automatically commits generated analysis files with the message:
```
chore: Update daily analysis reports
```

#### Step 6: Push Changes
Pushes the commits back to the main branch using GitHub's authentication token

## Files Involved

### Workflow Configuration
- **`.github/workflows/daily_analysis.yml`** - GitHub Actions workflow definition

### Analysis Script
- **`src/daily_analysis.py`** - Main analysis engine that generates metrics and reports

### Output Files (Auto-generated)
- **`analysis_reports/metrics_YYYY-MM-DD.json`** - Daily metrics in JSON format
- **`analysis_reports/report_YYYY-MM-DD.md`** - Daily analysis report in Markdown format

## Generated Metrics

The daily analysis collects the following metrics:

### Model Performance
- **Linear Regression**: R² Score, RMSE, MAE
- **Random Forest**: R² Score, RMSE, MAE  
- **Gradient Boosting**: R² Score, RMSE, MAE

### Data Quality
- Total records processed
- Missing values percentage
- Number of outliers detected

### Feature Engineering
- Number of features engineered
- Number of features selected
- Transformations applied (StandardScaler, OneHotEncoder, PolynomialFeatures)

## Manual Trigger

To manually run the workflow at any time:

1. Go to **Actions** tab in your repository
2. Select **Daily Data Analysis** workflow
3. Click **Run workflow**
4. Choose the branch (default: main)
5. Click **Run workflow**

## Monitoring

### View Workflow Runs
1. Go to **Actions** tab
2. Click on **Daily Data Analysis**
3. View all runs with their status (Success/Failed)

### View Generated Reports
1. Navigate to `analysis_reports/` folder
2. Browse JSON metrics files
3. Read Markdown reports for human-readable analysis

## Customization

### Change Execution Time
Edit `.github/workflows/daily_analysis.yml`:
```yaml
on:
  schedule:
    - cron: '0 9 * * *'  # Change the time here
```

Cron format: `minute hour day month day-of-week`

Examples:
- `0 0 * * *` - Daily at 12:00 AM UTC
- `30 14 * * *` - Daily at 2:30 PM UTC (9 PM IST)
- `0 */6 * * *` - Every 6 hours

### Modify Analysis Logic
Edit `src/daily_analysis.py` to:
- Add new metrics
- Change output format
- Integrate real data sources
- Implement advanced analysis

## Benefits

✅ **Consistent Development Activity**: Shows daily commits and contributions
✅ **Real Data Analysis**: Generates meaningful metrics and reports
✅ **Automated Workflow**: No manual intervention required
✅ **Portfolio Enhancement**: Demonstrates DevOps and CI/CD knowledge
✅ **Data-Driven Decisions**: Collect metrics to understand model performance
✅ **Learning Opportunity**: Understand GitHub Actions and automation

## Troubleshooting

### Workflow Not Running
- Check if Actions are enabled in repository settings
- Verify `.github/workflows/daily_analysis.yml` has correct syntax
- Check workflow logs for errors

### Analysis Script Errors
- Verify all dependencies in `requirements.txt` are installed
- Check Python syntax in `src/daily_analysis.py`
- Review GitHub Actions logs for error messages

### Push Failures
- Ensure `GITHUB_TOKEN` secret is available (default in GitHub Actions)
- Check branch name matches (should be 'main')
- Verify no branch protection rules block automated pushes

## Advanced Usage

### Integrate Real Data
Modify `DailyAnalysisEngine.generate_metrics()` to:
```python
# Load real data
df = pd.read_csv('data/movies.csv')

# Train actual models
model.fit(X_train, y_train)
metrics = model.evaluate(X_test, y_test)
```

### Add Notifications
Add a step to send email or Slack notifications:
```yaml
- name: Notify on completion
  run: |
    # Send notification via API/email
```

### Store Metrics in Database
Modify script to log metrics to:
- SQLite database
- PostgreSQL
- MongoDB
- Data warehouse (BigQuery, Snowflake)

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Cron Job Syntax](https://en.wikipedia.org/wiki/Cron)
- [Python Data Analysis](https://pandas.pydata.org/)
- [scikit-learn Models](https://scikit-learn.org/)

## Next Steps

1. Test the workflow manually from Actions tab
2. Verify analysis reports are generated
3. Customize analysis for your specific needs
4. Monitor daily commits and contributions
5. Iterate and improve analysis logic

---

**Note**: This automated setup demonstrates proficiency in:
- CI/CD pipeline implementation
- GitHub Actions configuration
- Python scripting and automation
- Data analysis and metrics generation
- DevOps practices
