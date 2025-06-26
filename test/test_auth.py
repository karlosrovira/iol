import iol

taccess_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6ImF0K2p3dCJ9.eyJzdWIiOiIxODcyNjkiLCJJRCI6IjE4NzI2OSIsImp0aSI6IjA1MmZiODY1LTRkZTMtNDljNS05ZmIzLTNjNjAwZmQ3OWI5ZSIsImNvbnN1bWVyX3R5cGUiOiIxIiwidGllbmVfY3VlbnRhIjoiVHJ1ZSIsInRpZW5lX3Byb2R1Y3RvX2J1cnNhdGlsIjoiVHJ1ZSIsInRpZW5lX3Byb2R1Y3RvX2FwaSI6IlRydWUiLCJ0aWVuZV9UeUMiOiJUcnVlIiwibmJmIjoxNzUwOTY0MzU1LCJleHAiOjE3NTA5NjUyNTUsImlhdCI6MTc1MDk2NDM1NSwiaXNzIjoiSU9MT2F1dGhTZXJ2ZXIiLCJhdWQiOiJJT0xPYXV0aFNlcnZlciJ9.V84_ZvFDJrhadNltelRk_DDh67Te2wpkjBVBMCvVXYLxm0YT9_m0bysGdN3QB_c9fEL4if2kSu7BEa2HgeukpXJtz2GN_7Psu3y6905S-27_2PiRHItpuK1qgoZH-vAJGjQ0MElIMqEuuYBmXYpC37fJQTHUJ0-QtNnBDWXI9LqB3irViAxfl44iNndCtNISEJNVn7Oq7Q2XScRbwc9sUWbSzHwbE3k6h1TS23RRDlBqXYWV5JMr8-uGVxhpW-y-BIK2fnKb9FofQz_aPYkGIVgr_eM-7g2DLnspPWB07f7YYvERrSYfRz8fatGpzsStOWpdIKQWMf7RTcGUul7TDg'

trefresh_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxODcyNjkiLCJqdGkiOiI2YWNlMzdmNy1lOTFhLTQ0NzctODdhMS1jODQ1ZDBjMDQ3NDgiLCJydF9mYW1pbHkiOiJhNDNkYWQ1NC1jZTEwLTQ5MDctYTVjOC05ZDlhNjJjYzNiZDIiLCJuYmYiOjE3NTA5NjQzNTUsImV4cCI6MTc1MDk2NTU1NSwiaWF0IjoxNzUwOTY0MzU1LCJpc3MiOiJJT0xPYXV0aFNlcnZlciIsImF1ZCI6IklPTE9hdXRoU2VydmVyIn0.mhJbP8qbFUJ572pr-SQzYaEPC20G8QRV0tt0ZVI00OSGvYdZM-rBf4OHpbZCvHSX1VkQHT780Xd1VxFRyu5WUDY__jn2xWJH19vbAxVkKcb15l2eOcY4DVokZhLaJJmzBmUDCQ5BzTNKqG2leL-IqvHQQmYNrpPnmbXB8dQxarlgWHP8QPK24I42Fpdn5mIH2aLTlBA5GXHaTyCR-w8PI_r6D_8K-M_oxCYUHHtNHnda9p1vvMz2IjoYYg6jSh8S11FDZfizRVXivrBAKFYGhd9NOYeExJkLrEG06_ioRbQA6RYqSr5hfUNXaLtkLTtWl7i98FlRT1v_b9jircqoSA'

ttoken_type = 'bearer'

texpires_in = 1200

tissued = 'Thu, 26 Jun 2025 18:59:15 GMT'

texpires = 'Thu, 26 Jun 2025 19:14:15 GMT'

trefresh_expires = 'Thu, 26 Jun 2025 19:19:15 GMT'

ttoken = {'access_token': taccess_token,
          'token_type': ttoken_type,
          'expires_in': texpires_in,
          'refresh_token': trefresh_token,
          '.issued': tissued,
          '.expires': texpires,
          '.refreshexpires': trefresh_expires}


def test_token():
    assert iol.date_to_str(iol.date_from_str(texpires)) == texpires

    auth = iol.Auth(ttoken)
    assert auth.access_token == taccess_token
    assert auth.token_type == ttoken_type
    assert auth.expires_in == texpires_in
    assert auth.refresh_token == trefresh_token
    # assert auth.issued == tissued
    # assert auth.expires == texpires
    # assert auth.refresh_expires == trefresh_expires
