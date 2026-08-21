from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import LabelEncoder
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend (important for Flask)
import matplotlib.pyplot as plt
import seaborn as sns
import io, base64, warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# HELPER: Convert matplotlib figure → base64 PNG
def fig_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight',
                facecolor='#0f1117', edgecolor='none', dpi=120)
    buf.seek(0)
    img_b64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return img_b64

# Generate a realistic synthetic dataset
def generate_dataset():
    """
    We generate a synthetic housing dataset that mimics real-world data.
    In a real project you'd load a CSV with pd.read_csv('housing.csv').
    """
    np.random.seed(42)
    n = 500

    area       = np.random.randint(500, 5000, n)
    bedrooms   = np.random.randint(1, 6, n)
    bathrooms  = np.random.randint(1, 4, n)
    age        = np.random.randint(0, 50, n)
    location   = np.random.choice(['Urban', 'Suburban', 'Rural'], n)
    garage     = np.random.choice([0, 1], n)

    loc_map = {'Urban': 50000, 'Suburban': 20000, 'Rural': 0}
    price = (
        area * 150
        + bedrooms * 10000
        + bathrooms * 8000
        - age * 500
        + np.array([loc_map[l] for l in location])
        + garage * 15000
        + np.random.normal(0, 20000, n)
    ).astype(int)

    df = pd.DataFrame({
        'Area_sqft': area,
        'Bedrooms': bedrooms,
        'Bathrooms': bathrooms,
        'House_Age': age,
        'Location': location,
        'Garage': garage,
        'Price': np.clip(price, 50000, 900000)
    })

    # Inject some missing values & duplicates for realism
    df.loc[np.random.choice(df.index, 20, replace=False), 'Bedrooms'] = np.nan
    df.loc[np.random.choice(df.index, 15, replace=False), 'Area_sqft'] = np.nan
    df = pd.concat([df, df.sample(10)], ignore_index=True)  # duplicates
    return df

# API ROUTES — each step returns JSON

@app.route('/')
def index():
    return render_template('index.html')


# ── STEP 1 : Data Loading ──────────────────
@app.route('/api/step1')
def step1():
    df = generate_dataset()

    head      = df.head().to_html(classes='data-table', border=0, index=False)
    shape     = list(df.shape)
    columns   = list(df.columns)
    dtypes    = df.dtypes.astype(str).to_dict()
    nulls     = df.isnull().sum().to_dict()
    desc      = df.describe().round(2).to_html(classes='data-table', border=0)

    code = '''\
# ── Step 1: Load the Dataset ──────────────────────────────
import pandas as pd

# In a real project, load your CSV file:
# df = pd.read_csv('housing.csv')

# We generate a synthetic dataset for this demo
df = generate_dataset()

# View the first 5 rows
print(df.head())

# Shape: (rows, columns)
print(f"Dataset shape: {df.shape}")

# Data types and null counts
print(df.info())
print(df.describe())
'''

    explanation = (
        "We start by <strong>loading our dataset</strong> into a Pandas DataFrame — "
        "think of it as a smart Excel table in Python. "
        "<code>df.head()</code> shows the first 5 rows so we can get a quick look at the data. "
        "<code>df.describe()</code> gives us statistics like mean, min, max for every numeric column. "
        "This is the very first thing any data scientist does!"
    )

    return jsonify(head=head, shape=shape, columns=columns,
                   dtypes=dtypes, nulls=nulls, desc=desc,
                   code=code, explanation=explanation)


# ── STEP 2 : Data Cleaning ────────────────
@app.route('/api/step2')
def step2():
    df = generate_dataset()

    before_shape  = list(df.shape)
    before_nulls  = int(df.isnull().sum().sum())
    before_dups   = int(df.duplicated().sum())

    # Fill missing numeric values with column median
    for col in ['Bedrooms', 'Area_sqft']:
        df[col].fillna(df[col].median(), inplace=True)

    # Drop duplicate rows
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True, inplace=True)

    after_shape = list(df.shape)
    after_nulls = int(df.isnull().sum().sum())
    after_dups  = int(df.duplicated().sum())

    code = '''\
# ── Step 2: Clean the Data ───────────────────────────────

# 1. Check for missing values
print(df.isnull().sum())

# 2. Fill missing numeric values with the column MEDIAN
#    Why median? It's robust to outliers unlike mean.
for col in ["Bedrooms", "Area_sqft"]:
    df[col].fillna(df[col].median(), inplace=True)

# 3. Remove exact duplicate rows
df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)

print(f"After cleaning: {df.shape}")
print(f"Remaining nulls: {df.isnull().sum().sum()}")
'''

    explanation = (
        "Real-world data is messy! We need to <strong>handle missing values</strong> "
        "(NaN entries) and <strong>remove duplicate rows</strong>. "
        "We fill numeric nulls with the <em>median</em> (not mean) because the median "
        "is not affected by extreme outliers. "
        "Duplicates are dropped because they would bias our model — "
        "like counting the same house twice!"
    )

    return jsonify(
        before_shape=before_shape, after_shape=after_shape,
        before_nulls=before_nulls, after_nulls=after_nulls,
        before_dups=before_dups, after_dups=after_dups,
        code=code, explanation=explanation
    )


# ── STEP 3 : EDA ──────────────────────────
@app.route('/api/step3')
def step3():
    df = generate_dataset()
    for col in ['Bedrooms', 'Area_sqft']:
        df[col].fillna(df[col].median(), inplace=True)
    df.drop_duplicates(inplace=True)

    dark_bg   = '#0f1117'
    card_bg   = '#1a1d2e'
    accent    = '#6c63ff'
    text_clr  = '#e0e0e0'
    palette   = ['#6c63ff','#ff6584','#43e97b','#f7971e','#4facfe']

    sns.set_theme(style='dark', rc={
        'figure.facecolor': dark_bg,
        'axes.facecolor':   card_bg,
        'axes.edgecolor':   '#333',
        'text.color':       text_clr,
        'axes.labelcolor':  text_clr,
        'xtick.color':      text_clr,
        'ytick.color':      text_clr,
        'grid.color':       '#2a2d3e',
    })

    plots = {}

    # 1. Price Distribution
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.hist(df['Price'], bins=40, color=accent, edgecolor='#0f1117', alpha=0.9)
    ax.set_title('House Price Distribution', color=text_clr, fontsize=14, pad=12)
    ax.set_xlabel('Price ($)', color=text_clr)
    ax.set_ylabel('Count', color=text_clr)
    ax.yaxis.grid(True, linestyle='--', alpha=0.4)
    fig.tight_layout()
    plots['histogram'] = fig_to_base64(fig)

    # 2. Correlation Heatmap
    num_df = df.select_dtypes(include=np.number)
    fig, ax = plt.subplots(figsize=(8, 6))
    mask = np.triu(np.ones_like(num_df.corr(), dtype=bool))
    sns.heatmap(num_df.corr(), annot=True, fmt='.2f', cmap='coolwarm',
                mask=mask, ax=ax, linewidths=0.5,
                cbar_kws={'shrink': 0.8},
                annot_kws={'size': 10, 'color': text_clr})
    ax.set_title('Feature Correlation Heatmap', color=text_clr, fontsize=14, pad=12)
    fig.tight_layout()
    plots['heatmap'] = fig_to_base64(fig)

    # 3. Area vs Price scatter
    fig, ax = plt.subplots(figsize=(9, 4))
    scatter = ax.scatter(df['Area_sqft'], df['Price'],
                         c=df['Bedrooms'], cmap='plasma',
                         alpha=0.65, s=20, edgecolors='none')
    cbar = fig.colorbar(scatter, ax=ax)
    cbar.set_label('Bedrooms', color=text_clr)
    cbar.ax.yaxis.set_tick_params(color=text_clr)
    plt.setp(cbar.ax.yaxis.get_ticklabels(), color=text_clr)
    ax.set_title('Area vs Price (colored by Bedrooms)', color=text_clr, fontsize=14, pad=12)
    ax.set_xlabel('Area (sqft)', color=text_clr)
    ax.set_ylabel('Price ($)', color=text_clr)
    fig.tight_layout()
    plots['scatter'] = fig_to_base64(fig)

    # 4. Avg Price by Location
    fig, ax = plt.subplots(figsize=(7, 4))
    loc_avg = df.groupby('Location')['Price'].mean().sort_values(ascending=False)
    bars = ax.bar(loc_avg.index, loc_avg.values,
                  color=palette[:len(loc_avg)], edgecolor='#0f1117', width=0.5)
    ax.bar_label(bars, labels=[f"${v/1000:.0f}K" for v in loc_avg.values],
                 padding=5, color=text_clr, fontsize=10)
    ax.set_title('Average Price by Location', color=text_clr, fontsize=14, pad=12)
    ax.set_ylabel('Avg Price ($)', color=text_clr)
    ax.yaxis.grid(True, linestyle='--', alpha=0.4)
    fig.tight_layout()
    plots['bar'] = fig_to_base64(fig)

    code = '''\
# ── Step 3: Exploratory Data Analysis (EDA) ──────────────

import matplotlib.pyplot as plt
import seaborn as sns

# 1. Price Distribution Histogram
plt.figure(figsize=(9, 4))
plt.hist(df["Price"], bins=40, color="#6c63ff", edgecolor="white")
plt.title("House Price Distribution")
plt.xlabel("Price ($)")
plt.ylabel("Count")
plt.show()

# 2. Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.select_dtypes(include="number").corr(),
            annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

# 3. Scatter: Area vs Price
plt.figure(figsize=(9, 4))
plt.scatter(df["Area_sqft"], df["Price"],
            c=df["Bedrooms"], cmap="plasma", alpha=0.6)
plt.colorbar(label="Bedrooms")
plt.title("Area vs Price")
plt.xlabel("Area (sqft)")
plt.ylabel("Price ($)")
plt.show()

# 4. Avg Price by Location
df.groupby("Location")["Price"].mean().plot(kind="bar")
plt.title("Average Price by Location")
plt.show()
'''

    explanation = (
        "<strong>EDA = Exploratory Data Analysis</strong>. "
        "Before building any model, we visualize the data to understand patterns. "
        "The <em>histogram</em> shows how prices are distributed. "
        "The <em>heatmap</em> shows how strongly each feature correlates with Price — "
        "the closer to 1 or -1, the stronger the relationship. "
        "The <em>scatter plot</em> reveals that larger area → higher price. "
        "The <em>bar chart</em> confirms location has a big impact on price."
    )

    return jsonify(plots=plots, code=code, explanation=explanation)


# ── STEP 4 : Feature Engineering ──────────
@app.route('/api/step4')
def step4():
    df = generate_dataset()
    for col in ['Bedrooms', 'Area_sqft']:
        df[col].fillna(df[col].median(), inplace=True)
    df.drop_duplicates(inplace=True)

    before_cols = list(df.columns)

    # One-Hot Encode 'Location'
    df = pd.get_dummies(df, columns=['Location'], drop_first=True)
    after_cols = list(df.columns)

    sample = df.head(3).to_html(classes='data-table', border=0, index=False)

    code = '''\
# ── Step 4: Feature Engineering ──────────────────────────

# Machine Learning models understand NUMBERS, not text.
# We need to convert "Location" (Urban/Suburban/Rural) into numbers.

# One-Hot Encoding creates new binary (0 or 1) columns for each category.
df = pd.get_dummies(df, columns=["Location"], drop_first=True)
# drop_first=True avoids the "dummy variable trap" (multicollinearity)

print("Columns after encoding:")
print(df.columns.tolist())

# Select features (X) and target (y)
features = ["Area_sqft", "Bedrooms", "Bathrooms",
            "House_Age", "Garage",
            "Location_Suburban", "Location_Urban"]
X = df[features]
y = df["Price"]
'''

    explanation = (
        "<strong>Feature Engineering</strong> prepares data for the ML model. "
        "Algorithms can only work with numbers, so we convert the text column "
        "<em>Location</em> using <strong>One-Hot Encoding</strong>. "
        "This creates new binary columns like <code>Location_Urban</code> (1 if Urban, else 0). "
        "We use <code>drop_first=True</code> to avoid redundancy — if something is neither "
        "Suburban nor Urban, it must be Rural."
    )

    return jsonify(before_cols=before_cols, after_cols=after_cols,
                   sample=sample, code=code, explanation=explanation)


# ── STEP 5 : Model Building ───────────────
@app.route('/api/step5')
def step5():
    df = generate_dataset()
    for col in ['Bedrooms', 'Area_sqft']:
        df[col].fillna(df[col].median(), inplace=True)
    df.drop_duplicates(inplace=True)
    df = pd.get_dummies(df, columns=['Location'], drop_first=True)

    features = ['Area_sqft','Bedrooms','Bathrooms','House_Age','Garage',
                'Location_Suburban','Location_Urban']

    # Ensure all numeric cols are filled (safety pass)
    for col in df.select_dtypes(include=np.number).columns:
        df[col].fillna(df[col].median(), inplace=True)

    X = df[features].fillna(df[features].median())
    y = df['Price']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    coef_data = {feat: round(float(coef), 2)
                 for feat, coef in zip(features, model.coef_)}
    intercept = round(float(model.intercept_), 2)

    train_size = len(X_train)
    test_size  = len(X_test)

    code = '''\
# ── Step 5: Model Building ────────────────────────────────
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

features = ["Area_sqft","Bedrooms","Bathrooms","House_Age",
            "Garage","Location_Suburban","Location_Urban"]
X = df[features]
y = df["Price"]

# Split: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Linear Regression: fits a straight line through data
# Price = w1*Area + w2*Bedrooms + ... + intercept
model = LinearRegression()
model.fit(X_train, y_train)  # ← The model LEARNS here

print("Model trained! Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
'''

    explanation = (
        "We now <strong>build our ML model</strong>! "
        "First, we split data into 80% training and 20% testing — "
        "we train on 80% and evaluate on unseen 20%. "
        "<strong>Linear Regression</strong> finds the best straight-line relationship: "
        "<code>Price = w₁×Area + w₂×Bedrooms + ...</code>. "
        "Each coefficient (weight) tells us: "
        "<em>how much does price change per unit increase in that feature?</em>"
    )

    return jsonify(coef_data=coef_data, intercept=intercept,
                   train_size=train_size, test_size=test_size,
                   code=code, explanation=explanation)


# ── STEP 6 : Evaluation ───────────────────
@app.route('/api/step6')
def step6():
    df = generate_dataset()
    for col in ['Bedrooms', 'Area_sqft']:
        df[col].fillna(df[col].median(), inplace=True)
    df.drop_duplicates(inplace=True)
    df = pd.get_dummies(df, columns=['Location'], drop_first=True)

    features = ['Area_sqft','Bedrooms','Bathrooms','House_Age','Garage',
                'Location_Suburban','Location_Urban']
    X = df[features].fillna(df[features].median())
    y = df['Price']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mae  = round(float(mean_absolute_error(y_test, y_pred)), 2)
    mse  = round(float(mean_squared_error(y_test, y_pred)), 2)
    rmse = round(float(np.sqrt(mse)), 2)
    r2   = round(float(model.score(X_test, y_test)), 4)

    # Actual vs Predicted plot
    dark_bg = '#0f1117'; card_bg = '#1a1d2e'
    accent  = '#6c63ff'; text_clr = '#e0e0e0'
    fig, ax = plt.subplots(figsize=(9, 5), facecolor=dark_bg)
    ax.set_facecolor(card_bg)
    ax.scatter(y_test, y_pred, alpha=0.55, color=accent, s=22, edgecolors='none')
    mn = min(y_test.min(), y_pred.min())
    mx = max(y_test.max(), y_pred.max())
    ax.plot([mn, mx], [mn, mx], 'r--', lw=1.5, label='Perfect Prediction')
    ax.set_title('Actual vs Predicted Prices', color=text_clr, fontsize=14, pad=12)
    ax.set_xlabel('Actual Price ($)', color=text_clr)
    ax.set_ylabel('Predicted Price ($)', color=text_clr)
    ax.tick_params(colors=text_clr)
    ax.legend(facecolor=card_bg, labelcolor=text_clr)
    ax.yaxis.grid(True, linestyle='--', alpha=0.3, color='#2a2d3e')
    fig.tight_layout()
    pred_plot = fig_to_base64(fig)

    # Residuals plot
    residuals = y_test.values - y_pred
    fig, ax = plt.subplots(figsize=(9, 4), facecolor=dark_bg)
    ax.set_facecolor(card_bg)
    ax.scatter(y_pred, residuals, alpha=0.55, color='#ff6584', s=18, edgecolors='none')
    ax.axhline(0, color='#43e97b', lw=1.5, linestyle='--')
    ax.set_title('Residuals Plot (Errors)', color=text_clr, fontsize=14, pad=12)
    ax.set_xlabel('Predicted Price ($)', color=text_clr)
    ax.set_ylabel('Residual (Actual − Predicted)', color=text_clr)
    ax.tick_params(colors=text_clr)
    ax.yaxis.grid(True, linestyle='--', alpha=0.3, color='#2a2d3e')
    fig.tight_layout()
    resid_plot = fig_to_base64(fig)

    code = '''\
# ── Step 6: Model Evaluation ──────────────────────────────
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

y_pred = model.predict(X_test)

mae  = mean_absolute_error(y_test, y_pred)
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = model.score(X_test, y_test)

print(f"MAE  (Mean Absolute Error):  ${mae:,.0f}")
print(f"MSE  (Mean Squared Error):   ${mse:,.0f}")
print(f"RMSE (Root MSE):             ${rmse:,.0f}")
print(f"R²   Score:                  {r2:.4f}")

# Actual vs Predicted
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()], "r--")
plt.xlabel("Actual"); plt.ylabel("Predicted")
plt.title("Actual vs Predicted Prices")
plt.show()
'''

    explanation = (
        "How good is our model? We use three metrics: "
        "<strong>MAE</strong> (average dollar error — easy to understand), "
        "<strong>RMSE</strong> (penalizes large errors more — good for outliers), "
        "and <strong>R² Score</strong> (0–1, how much variance our model explains — "
        "closer to 1 is better!). "
        "The <em>Actual vs Predicted</em> chart: points close to the red dashed line = great predictions. "
        "The <em>Residuals plot</em>: random scatter around 0 = our model has no systematic bias."
    )

    return jsonify(mae=mae, mse=mse, rmse=rmse, r2=r2,
                   pred_plot=pred_plot, resid_plot=resid_plot,
                   code=code, explanation=explanation)


if __name__ == '__main__':
    app.run(debug=True, port=5050)