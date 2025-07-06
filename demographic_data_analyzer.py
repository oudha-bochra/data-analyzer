import pandas as pd

def calculate_demographic_data():
    df = pd.read_csv("C:/Users/info/Desktop/data_project/demographic_data.csv")

    race_count = df["race"].value_counts()
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    higher_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    lower_education = ~higher_education

    higher_edu_rich = round((df[higher_education]["salary"] == ">50K").mean() * 100, 1)
    lower_edu_rich = round((df[lower_education]["salary"] == ">50K").mean() * 100, 1)

    min_work_hours = df["hours-per-week"].min()

    num_min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_min_workers = round((num_min_workers["salary"] == ">50K").mean() * 100, 1)

    highest_country = (df[df["salary"] == ">50K"]["native-country"]
                       .value_counts(normalize=True)
                       .mul(100).round(1).idxmax())

    highest_percentage = (df[df["salary"] == ">50K"]["native-country"]
                          .value_counts(normalize=True)
                          .mul(100).round(1).max())

    top_IN_occupation = df[(df["native-country"] == "India") & 
                           (df["salary"] == ">50K")]["occupation"].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_min_workers,
        'highest_earning_country': highest_country,
        'highest_earning_country_percentage': highest_percentage,
        'top_IN_occupation': top_IN_occupation
    }
