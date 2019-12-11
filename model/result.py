class result:


    def __init__(self,is_success=False,data=None,error_message=None):
        self.is_success = is_success
        self.data = data
        self.error_message = error_message


    def convert_to_json(self):
        return {
            "is_success": self.is_success,
            "data": self.data,
            "error_message": self.error_message
        }