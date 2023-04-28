
import os

def create_folder_structure():
    # Create the main project directory
    if not os.path.exists('cloud-based-data-warehouse'):
        os.makedirs('cloud-based-data-warehouse')
        
    # Create the sub-directories
    sub_directories = ['aws-glue', 'apache-airflow', 'streamlit', 'great-expectations', 'redshift']
    
    for directory in sub_directories:
        # Create the sub-directory if it doesn't exist
        if not os.path.exists(os.path.join('cloud-based-data-warehouse', directory)):
            os.makedirs(os.path.join('cloud-based-data-warehouse', directory))
            
        # Create the empty files
        file_names = ['README.md', 'LICENSE', '.gitignore']
        for file_name in file_names:
            open(os.path.join('cloud-based-data-warehouse', directory, file_name), 'a').close()

if __name__ == '__main__':
    create_folder_structure()
