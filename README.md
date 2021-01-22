# Usage

### Create a Virtual Envoronment
- virtualenv --python=python3 venv
- python3 -m virtualenv --python=python3 venv

### Activate virtual environment
source venv/Scripts/activate

### Install requirements
pip install -r requirements.txt

## Posible functions

- join_pdf: Function to join pdf files in a given folder into a single file
    - python main.py --join_pdfs --list_number n --location "" --destination ""
        -   list_number: file name ending, name is lista_n where n is the list # input
        -   location (optional): location of the folder with pdf files to join
        -   destination (optional): location to save new pdf file
    

- split_pdfs: Function to split a big pdf file into individual pdfs
    - python main.py --list_number n --split_n i
        - list_number: name of pdf file, must be named lista_n.pdf where n is the list number input
        - split_n: number of pages per new pdf file
    
