import httpx

class TextBeeClient:
    def __init__(self, api_key, device_id):
        self.api_key = api_key
        self.device_id = device_id
        self.base_url = "https://api.textbee.dev/api/v1"

    def send_welcome_message(self, phone_number, message):
        """
        Send SMS message using TextBee API
        Returns: (success: bool, response: dict)
        """
        url = f"{self.base_url}/gateway/devices/{self.device_id}/send-sms"
        
        headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }
        
        payload = {
            "recipients": [phone_number],
            "message": message
        }
        
        try:
            response = httpx.post(url, headers=headers, json=payload)
            response_data = response.json()
            
            # Check if the API call was successful (200 OK or 201 Created)
            if response.status_code in [200, 201]:
                # TextBee API returns success info in the 'data' object
                if 'data' in response_data:
                    data = response_data['data']
                    # Check if success is True or if we have a valid smsBatchId (indicates success)
                    success_flag = data.get('success', False)
                    has_batch_id = 'smsBatchId' in data
                    
                    if success_flag or has_batch_id:
                        return True, response_data
                    else:
                        return False, response_data
                else:
                    # Fallback: if no 'data' object but 200/201 status, consider it success
                    return True, response_data
            else:
                return False, response_data
                
        except Exception as e:
            return False, {"error": str(e)}