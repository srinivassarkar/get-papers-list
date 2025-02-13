import requests  
from lxml import etree
from typing import Dict, List

class PubMedClient:
    BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

    def search_papers(self, query: str, max_results: int = 10) -> List[str]:
        """Search for papers using PubMed API and return a list of paper IDs."""
        search_url = f"{self.BASE_URL}/esearch.fcgi"
        params = {
            "db": "pubmed",
            "term": query,
            "retmax": max_results,
            "retmode": "json"
        }
        response = requests.get(search_url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("esearchresult", {}).get("idlist", [])

    def fetch_paper_details(self, paper_id: str) -> Dict:
        """Fetch details for a specific paper using its PubMed ID."""
        fetch_url = f"{self.BASE_URL}/efetch.fcgi"
        params = {
            "db": "pubmed",
            "id": paper_id,
            "retmode": "xml"
        }
        response = requests.get(fetch_url, params=params)
        response.raise_for_status()

        # Parse XML response
        root = etree.fromstring(response.content)
        paper_details = {
            "id": paper_id,
            "title": root.findtext(".//ArticleTitle"),
            "date": root.findtext(".//PubDate/Year"),
            "authors": [],
            "affiliations": [],
            "corresponding_email": root.findtext(".//Author[@ValidYN='Y']/Email")
        }

        # Extract authors and affiliations
        for author in root.findall(".//Author"):
            last_name = author.findtext("LastName")
            fore_name = author.findtext("ForeName")
            if last_name and fore_name:
                paper_details["authors"].append(f"{fore_name} {last_name}")
            affiliation = author.findtext("AffiliationInfo/Affiliation")
            if affiliation:
                paper_details["affiliations"].append(affiliation)

        return paper_details