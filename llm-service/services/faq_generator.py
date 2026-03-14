"""
faq_generator.py

Generates Frequently Asked Questions (FAQs) for the
AI Student Support System.
"""

from typing import List, Dict


class FAQGenerator:
    """
    Class to generate and manage FAQs
    """

    def __init__(self):
        self.faqs: List[Dict[str, str]] = []

    def add_faq(self, question: str, answer: str):
        """
        Add a new FAQ entry
        """

        faq = {
            "question": question.strip(),
            "answer": answer.strip()
        }

        self.faqs.append(faq)

    def get_all_faqs(self) -> List[Dict[str, str]]:
        """
        Return all stored FAQs
        """
        return self.faqs

    def search_faq(self, query: str):
        """
        Search FAQs based on a keyword
        """

        query = query.lower()

        for faq in self.faqs:
            if query in faq["question"].lower():
                return faq["answer"]

        return None


# Default FAQ data related to Vignan University
def load_default_faqs(generator: FAQGenerator):
    """
    Load predefined FAQs into the system
    """

    generator.add_faq(
        "How can I apply for admission at Vignan University?",
        "Students can apply online through the Vignan admission portal using V-SAT, EAPCET, or JEE scores."
    )

    generator.add_faq(
        "What scholarships are available at Vignan University?",
        "Vignan University offers scholarships based on V-SAT rank, entrance exam scores, and academic merit."
    )

    generator.add_faq(
        "Does Vignan University provide hostel facilities?",
        "Yes, Vignan provides separate hostels for boys and girls with AC and non-AC rooms."
    )

    generator.add_faq(
        "What is the placement rate at Vignan University?",
        "Vignan University maintains around 85–90% placement rate with companies like TCS, Accenture, and Wipro."
    )

    generator.add_faq(
        "How can students contact the university?",
        "Students can contact the university office at 0863-2344777 or visit the official website."
    )


# Initialize FAQ generator
faq_generator = FAQGenerator()

# Load default FAQs
load_default_faqs(faq_generator)


def get_faq_answer(query: str):
    """
    Get answer from FAQs if available
    """

    return faq_generator.search_faq(query)