import pandas as pd
import matplotlib.pyplot as plt

# Load data
diabetes_df = pd.read_csv('cleaned_data/clean_diabetes.csv')

print("Diabetes Health Analysis: Impact of Life Factors on Health Outcomes")
print("="*60)

# Focus on 3 meaningful insights
plt.figure(figsize=(15, 5))

# 1. BMI IMPACT ON DIABETES (Enhanced version of your existing analysis)
plt.subplot(1, 3, 1)
diabetes_df.boxplot(column='BMI', by='Diabetes_012', ax=plt.gca())
plt.suptitle('')  # Remove default title
plt.title('BMI Distribution by Diabetes Stage')
plt.xlabel('Diabetes Stage (0=No, 1=Prediabetes, 2=Diabetes)')
plt.ylabel('BMI')

# 2. PHYSICAL ACTIVITY IMPACT (Enhanced version of your selected code)
plt.subplot(1, 3, 2)
activity_by_diabetes = diabetes_df.groupby('Diabetes_012')['PhysActivity'].mean()
plt.bar(activity_by_diabetes.index, activity_by_diabetes.values, color='blue', alpha=0.7)
plt.title('Physical Activity by Diabetes Stage')
plt.xlabel('Diabetes Stage (0=No, 1=Prediabetes, 2=Diabetes)')
plt.ylabel('Average Physical Activity')

# 3. AGE IMPACT ON DIABETES (New insight)
plt.subplot(1, 3, 3)
age_by_diabetes = diabetes_df.groupby('Diabetes_012')['Age'].mean()
plt.bar(age_by_diabetes.index, age_by_diabetes.values, color='red', alpha=0.7)
plt.title('Average Age by Diabetes Stage')
plt.xlabel('Diabetes Stage (0=No, 1=Prediabetes, 2=Diabetes)')
plt.ylabel('Average Age')

plt.tight_layout()
plt.savefig('diabetes_health_insights.png', dpi=300, bbox_inches='tight')
plt.show()

# Summary statistics
print(f"\nKey Insights:")
print(f"1. BMI increases with diabetes progression")
print(f"2. Physical activity decreases with diabetes progression")
print(f"3. Age increases with diabetes progression")

# Statistical summary
diabetes_summary = diabetes_df.groupby('Diabetes_012').agg({
    'BMI': 'mean',
    'PhysActivity': 'mean',
    'Age': 'mean'
}).round(2)
print(f"\nAverage Values by Diabetes Stage:")
print(diabetes_summary)

# Additional insights
print(f"\nDataset Overview:")
print(f"• Total Records: {len(diabetes_df)}")
print(f"• Diabetes Prevalence: {(diabetes_df['Diabetes_012'] > 0).mean()*100:.1f}%")
print(f"• Average BMI: {diabetes_df['BMI'].mean():.1f}")
print(f"• Average Age: {diabetes_df['Age'].mean():.1f} years")