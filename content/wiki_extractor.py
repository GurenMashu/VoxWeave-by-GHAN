import wikipedia

class WikiExtractor():

    def __init__(self, topic):
        self.topic = topic
        wikipedia.set_lang("en")
    
    def get_all_sections(self, content)-> list:
        '''
        To extract sub-sections from the wikipedia page such as "history".
        Returns list of sections.
        '''
        lines = content.split("\n")
        sections = []
        for line in lines:
            if line.strips().startswith("==") and line.strip().endswith("=="):
                section_title = line.strip().replace("==","").strip()
                sections.append(section_title)
        return sections  

    def get_content_from_page(self):
        """
        To extract overall information of the page.
        Return a dictionary of structured information from the page
        """
        try:

            try:
                results = wikipedia.search(self.topic, result = 3)
                print(results)
            except wikipedia.exceptions.WikipediaException as e:
                print(f"[ERROR] Search for topic failed: {e}")    

            try:
                page = wikipedia.page(self.topic)
                sections = self.get_all_sections(page.content)
                return {
                    "title":page.title,
                    "content":page.content,
                    "url":page.url,
                    "summary":wikipedia.summary(self.topic, sentence=0),
                    "sections":sections
                }
        
            except wikipedia.exceptions.DisambiguationError as e:
                option_taken = e.options[0]
                print(f"[LOG] Multiple pages found: {e.options} | Using :{e.options[0]}")

                page = wikipedia.page(option_taken)
                sections = self.get_all_sections(page.content)
                return {
                    "title":page.title,
                    "content":page.content,
                    "url":page.url,
                    "summary":wikipedia.summary(option_taken, sentence=0),
                    "sections":sections
                }
            
        except wikipedia.exceptions.WikipediaException as e:
            print(f"[ERROR] Content extraction for '{self.topic}' failed: {e}")
            return None
        except Exception as e:
            print(f"[ERROR] Unexpected error for '{self.topic}': {e}")
            return None

    def get_section_content(self):
        """
        To extract content from each section present in the main page.
        """
        pass
    
    def combine_contents(self):
        """
        Combines all extracted text from the page into one while string.
        """
        pass

    def run_extraction(self):
        """
        The main worker function of this class.
        """
        pass