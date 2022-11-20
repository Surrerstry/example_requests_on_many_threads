from django.http import HttpResponse

import time
from datetime import datetime


def upload_view(request):

    start_time = time.time()

    form_key_value = list(request.FILES.items())[0][0]

    # clear file before upload (just for multiple retesting)
    with open(f"uploaded_data/{request.FILES[form_key_value].name}", 'w') as f:
        f.write('')

    while char_to_save := request.FILES[form_key_value].read(1):
        with open(f"uploaded_data/{request.FILES[form_key_value].name}", 'a') as f:
            f.write(char_to_save.decode('utf-8'))
            # time.sleep(1)

    end_time = time.time()

    return HttpResponse(f"uploaded: {request.FILES[form_key_value].name} at: {datetime.now()}, processed: ~{end_time - start_time:.2f} seconds")
