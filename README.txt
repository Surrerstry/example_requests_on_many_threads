
# Example that sending from multiple threads by using just "requests" library works.


# requirements
A. Python3.9 or higher
B. requirements.txt


1. Run server:
python manage.py runserver

2. Run concurrent requests:
python mass_uploader.py

- logic is in views py:
views.py

3. Verify that content that was sent, is received properly:
./mass_uploader_xd/big_data_to_upload/*.txt
./th_upload/uploaded_data/*.txt

