class Database: 
    def query(self, id): 
        # Database query logic 
        pass 

class DataProcessor: 
    def process_data(self, data): 
        return data.upper() 

class HtmlRenderer: 
    def render_data(self, processed_data): 
        return f"<h1>{processed_data}</h1>" 

class Application: 
    def __init__(self): 
        self.db = Database() 
        self.processor = DataProcessor() 
        self.renderer = HtmlRenderer() 

    def run(self, id): 
        data = self.db.query(id) 
        processed_data = self.processor.process_data(data) 
        html_output = self.renderer.render_data(processed_data) 
        return html_output 