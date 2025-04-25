from bs4 import BeautifulSoup
import pandas as pd

job_data = []

# Loop through downloaded HTML files for pages 1 to 10
serial_no = 1
for page in range(1, 101):
    print(f"Reading file: /Users/tabishbaig/Documents/Scraping Projects/naukri/naukri_page_{page}.html")
    with open(f"/Users/tabishbaig/Documents/Scraping Projects/naukri/naukri_page_{page}.html", "r", encoding="utf-8") as f:
        html_content = f.read()
        print(f"Length of file content: {len(html_content)} characters")
        soup = BeautifulSoup(html_content, "html.parser")

    # Extract job data (title, company, etc.)
    job_cards = soup.find_all('div', class_='srp-jobtuple-wrapper')
    print(f"Found {len(job_cards)} job cards on page {page}")

    for job in job_cards:
        try:
            job_title = job.find('h2').get_text(strip=True) if job.find('h2') else 'No Title Available'
            company_name = job.find('a', class_='comp-name').get_text(strip=True) if job.find('a', class_='comp-name') else 'No Company Name Available'
            company_url = job.find('a', class_='comp-name')['href'] if job.find('a', class_='comp-name') else 'No URL Available'
            salary = job.find('span', class_='sal-wrap').get_text(strip=True) if job.find('span', class_='sal-wrap') else 'Not Disclosed'
            location = job.find('span', class_='loc-wrap').get_text(strip=True) if job.find('span', class_='loc-wrap') else 'No Location Available'
            experience = job.find('span', class_='expwdth').get_text(strip=True) if job.find('span', class_='expwdth') else 'No Experience Info'
            description = job.find('span', class_='job-desc').get_text(strip=True) if job.find('span', class_='job-desc') else 'No Description Available'
            tags = [tag.get_text(strip=True) for tag in job.find_all('li', class_='tag-li')] if job.find_all('li', class_='tag-li') else []

            job_data.append({
                "S.No": serial_no,
                "Job Title": job_title,
                "Company Name": company_name,
                "Company URL": company_url,
                "Salary": salary,
                "Location": location,
                "Experience": experience,
                "Description": description,
                "Tags": ', '.join(tags)
            })
            serial_no += 1
        except Exception as e:
            print(f"Error extracting data for job {serial_no} on page {page}: {e}")

# Create DataFrame and save to CSV
df = pd.DataFrame(job_data)
df.to_csv("naukri_jobs_pages_1_to_10.csv", index=False)
