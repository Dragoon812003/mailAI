import os
import joblib

# Get the directory where the current script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the paths to the saved model and vectorizer
model_path = os.path.join(current_directory, 'model.pkl')
vectorizer_path = os.path.join(current_directory, 'vectorizer.pkl')

model = joblib.load(model_path)
feature_extraction = joblib.load(vectorizer_path)

def developer_profile_pic_path(instance, filename):
    return f'profile_pic/{instance.timestamp}/{filename}'

def format_developer_names(info_list):
    count = len(info_list)
    
    if count == 0:
        return ""
    elif count == 1:
        name, linkedin_link = info_list[0]
        return f'<a href="{linkedin_link}" class="hover:underline">{name}</a>'
    elif count == 2:
        name1, linkedin_link1 = info_list[0]
        name2, linkedin_link2 = info_list[1]
        return f'<a href="{linkedin_link1}" class="hover:underline">{name1}</a> & <a href="{linkedin_link2}" class="hover:underline">{name2}</a>'
    else:
        formatted_names = []
        for name, linkedin_link in info_list[:-1]:
            formatted_names.append(f'<a href="{linkedin_link}" class="hover:underline">{name}</a>')
        last_name, last_link = info_list[-1]
        formatted_names.append(f'& <a href="{last_link}" class="hover:underline">{last_name}</a>')
        return ', '.join(formatted_names)
