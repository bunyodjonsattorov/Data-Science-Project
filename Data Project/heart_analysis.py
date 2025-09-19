import pandas as pd
import matplotlib.pyplot as plt

# Load data
heart_df = pd.read_csv('cleaned_data/clean_heart.csv')

print("Heart Disease Analysis: Impact of Life Factors on Health Outcomes")
print("="*60)

# Focus on 3 meaningful insights
plt.figure(figsize=(15, 5))

# 1. CHOLESTEROL IMPACT ON HEART DISEASE (Your existing analysis - enhanced)
plt.subplot(1, 3, 1)
heart_df.boxplot(column='Cholesterol', by='Heart Disease', ax=plt.gca())
plt.suptitle('')  # Remove default title
plt.title('Cholesterol Distribution by Heart Disease')
plt.xlabel('Heart Disease Status')
plt.ylabel('Cholesterol (mg/dl)')

# 2. AGE IMPACT ON HEART DISEASE (Your selected code - enhanced)
plt.subplot(1, 3, 2)
heart_df['Age_Group'] = pd.cut(heart_df['Age'], bins=[0, 50, 60, 70, 100], 
                               labels=['Under 50', '50-60', '60-70', '70+'])
age_heart = heart_df.groupby('Age_Group')['Heart Disease'].apply(lambda x: (x == 'Presence').mean())
age_heart.plot(kind='bar', color='orange', alpha=0.7, ax=plt.gca())
plt.title('Heart Disease Risk by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Heart Disease Rate')
plt.xticks(rotation=45)

# 3. BLOOD PRESSURE IMPACT ON HEART DISEASE (New insight)
plt.subplot(1, 3, 3)
heart_df.boxplot(column='BP', by='Heart Disease', ax=plt.gca())
plt.suptitle('')  # Remove default title
plt.title('Blood Pressure Distribution by Heart Disease')
plt.xlabel('Heart Disease Status')
plt.ylabel('Blood Pressure (mmHg)')

plt.tight_layout()
plt.savefig('heart_disease_insights.png', dpi=300, bbox_inches='tight')
plt.show()

# Summary statistics
print(f"\nKey Insights:")
print(f"1. Higher cholesterol levels associated with heart disease")
print(f"2. Heart disease risk increases significantly with age")
print(f"3. Higher blood pressure associated with heart disease")

# Statistical summary
heart_summary = heart_df.groupby('Heart Disease').agg({
    'Cholesterol': 'mean',
    'BP': 'mean',
    'Age': 'mean'
}).round(2)
print(f"\nAverage Values by Heart Disease Status:")
print(heart_summary)

# Additional insights
print(f"\nDataset Overview:")
print(f"• Total Records: {len(heart_df)}")
print(f"• Heart Disease Rate: {(heart_df['Heart Disease'] == 'Presence').mean()*100:.1f}%")
print(f"• Average Cholesterol: {heart_df['Cholesterol'].mean():.0f} mg/dl")
print(f"• Average Blood Pressure: {heart_df['BP'].mean():.0f} mmHg")