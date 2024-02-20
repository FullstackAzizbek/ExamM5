import pdfkit
from multiprocessing.dummy import Pool

# Internet ishlamaganligi bois pdf fayllar oxirigacha saqlanmadi faqat iktasi saqlandi xolos

url = "https://tilshunos.com/omonims/"

config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

def convert_to_pdf(url):
    pdfkit.from_url(url, f'omonimlar/{url.split("/")[-2]}.pdf', configuration=config)

def main():
    global url
    urls = []
    for i in range(1,11):
        urls.append(f"{url}{i}/")
    with Pool() as pool:
        pool.map(convert_to_pdf, urls)

if __name__ == '__main__':
    main()


# Internet ishlamaganligi bois pdf fayllar oxirigacha saqlanmadi