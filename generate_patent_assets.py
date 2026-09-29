import os
import subprocess

folder = r'c:\Users\LENOVO\Documents\oto\patent_files'
os.makedirs(folder, exist_ok=True)

chrome_paths = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'
]
browser_exe = next((p for p in chrome_paths if os.path.exists(p)), None)

for name in ['ozet', 'istemler', 'tarifname', 'resimler']:
    in_html = os.path.join(folder, f'{name}.html')
    out_pdf = os.path.join(folder, f'{name}.pdf')
    cmd = f'"{browser_exe}" --headless --disable-gpu --print-to-pdf="{out_pdf}" "{in_html}"'
    subprocess.run(cmd, shell=True)
    print(f'{name}.pdf OK')

in_resim = os.path.join(folder, 'resimler.html')
out_png = os.path.join(folder, 'bulten_resim.png')
cmd_jpg = f'"{browser_exe}" --headless --disable-gpu --screenshot="{out_png}" --window-size=1200,800 "{in_resim}"'
subprocess.run(cmd_jpg, shell=True)

with open(out_png, 'rb') as f_in:
    with open(os.path.join(folder, 'bulten_resim.jpg'), 'wb') as f_out:
        f_out.write(f_in.read())

print('bulten_resim.jpg OK')
