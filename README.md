# 📊 Content Monetization Modeler

A Machine Learning project that predicts **YouTube Ad Revenue** using video performance metrics and contextual features.

This project helps content creators, media companies, and advertisers estimate potential revenue based on video engagement and performance.

---

## 📌 Project Overview

The **Content Monetization Modeler** predicts how much ad revenue a video may generate based on metrics such as:

- Views
- Likes
- Comments
- Watch Time
- Subscribers
- Video Category
- Viewer Country
- Device Type

The model is deployed using a **Streamlit interactive dashboard** where users can input video metrics and estimate potential revenue.

---

## 🎯 Business Problem

Content creators and media companies need to estimate how much revenue a video can generate.

This project answers:

- How much revenue will a video generate?
- What factors influence monetization?
- Does video category affect revenue?
- How important are engagement metrics?

---

## 💼 Business Use Cases

### Content Strategy Optimization
Helps creators identify which video characteristics lead to higher revenue.

### Revenue Forecasting
Media companies can estimate earnings before publishing videos.

### Creator Analytics Tools
Can be integrated into analytics platforms for YouTubers.

### Ad Campaign Planning
Advertisers can estimate ROI based on content performance.

---

## 📂 Dataset

Dataset Name: **YouTube Monetization Modeler**

Dataset Size: **~122,000 rows**

Each row represents performance metrics of a YouTube video.

### Features

| Feature | Description |
|------|------|
| video_id | Unique video identifier |
| date | Upload/report date |
| views | Number of views |
| likes | Number of likes |
| comments | Number of comments |
| watch_time_minutes | Total watch time |
| video_length_minutes | Length of the video |
| subscribers | Channel subscriber count |
| category | Video category |
| device | Viewing device |
| country | Viewer location |
| ad_revenue_usd | Ad revenue generated (target variable) |

---

## ⚙️ Feature Engineering

### Engagement Rate

```python
engagement_rate = (likes + comments) / views * 100
```

### Watch Time Rate

```python
watch_time_rate = watch_time_minutes / (views * video_length_minutes)
```

---

## 🧠 Custom Missing Value Handling

Instead of using a simple statistical imputer, a **domain-based imputation strategy** was implemented.

Missing `watch_time_minutes` values were estimated using:

```python
watch_time_minutes = video_length_minutes * views * average_retention
```

This approach uses viewer retention patterns to estimate missing watch time.

---

## 📊 Exploratory Data Analysis (EDA)

EDA was conducted to identify relationships between features and revenue.

Key analyses included:

- Revenue distribution
- Engagement vs revenue analysis
- Correlation heatmap
- Revenue comparison by category
- Country-wise revenue analysis
- Outlier detection

---

## 📈 Hypothesis Testing

A statistical test was performed to determine if **video category significantly affects ad revenue**.

### Result

The test indicated **no statistically significant relationship between category and revenue**.

This suggests revenue depends more on:

- watch time
- watch time rate
- engagement rate

rather than category alone.

---

## 🤖 Machine Learning Pipeline

A complete **Scikit-Learn Pipeline** was implemented to ensure consistent preprocessing and training.

### Preprocessing

- RobustScaler for numeric features
- BinaryEncoder for categorical features
- Custom feature engineering
- Custom missing value imputation

### Model

Gradient Boosting Regressor

```python
GradientBoostingRegressor(
    n_estimators=100,
    max_depth=5,
    learning_rate=0.1,
    min_samples_split=10
)
```

---

## 📉 Model Evaluation

The model was evaluated using regression metrics.

| Metric | Description |
|------|------|
| R² Score | Model accuracy |
| RMSE | Root Mean Squared Error |
| MAE | Mean Absolute Error |

 Results:

```
Confidence Score (R²): 0.93
RMSE: 16
MAE: 5
```

---

## 🚀 Streamlit Application

An interactive **Streamlit dashboard** was created for revenue prediction.

### Features

- Input video metrics
- Predict ad revenue
- Display insights
- Visualize revenue patterns

### Run the App

```bash
streamlit run app.py
```

---

## 🗄 PostgreSQL Integration

The cleaned dataset was uploaded into **PostgreSQL** for structured data storage.

Technologies used:

- PostgreSQL
- SQLAlchemy
- psycopg2
- Pandas

---

## 🛠 Tech Stack

### Programming
- Python

### Data Processing
- Pandas
- NumPy

### Machine Learning
- Scikit-Learn

### Encoding
- Category Encoders

### Visualization
- Matplotlib
- Seaborn

### Deployment
- Streamlit

### Database
- PostgreSQL

---

## 📁 Project Structure

```
Content_monetization_modeler
│
├── data
│   ├── raw
│   └── cleaned
│
├── notebooks
│   └── eda.ipynb
│
├── app.py
├── final_revenue_model.pkl
├── requirements.txt
└── README.md
```

---

## 🔍 Key Insights

- Higher engagement leads to increased ad revenue.
- Videos with longer watch time generate higher monetization.
- Watch time rate has impact on revenue.
- Video category alone does not significantly determine revenue.

---

## 🔮 Future Improvements

- Hyperparameter tuning
- Advanced feature engineering
- Deep learning models
- Real-time analytics
- Improved Streamlit UI

---

## 👨‍💻 Author

**Karthigeyan**

Data Science Portfolio Project
