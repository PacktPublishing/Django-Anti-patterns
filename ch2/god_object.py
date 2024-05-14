class GodObject: 

    def __init__(self): 
        self.db = Database() 
        self.logger = Logger() 

    def get_data(self, id): 
        data = self.db.query(id) 
        self.logger.log(f"Data retrieved: {data}") 
        return data 

    def process_data(self, data): 
        processed_data = data.upper() 
        self.logger.log(f"Data processed: {processed_data}") 
        return processed_data 

    def render_data(self, processed_data): 
        return f"<h1>{processed_data}</h1>" 

    def run(self, id): 
        data = self.get_data(id) 
        processed_data = self.process_data(data) 
        html_output = self.render_data(processed_data) 
        return html_output 