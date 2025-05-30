import base64
import requests
import json

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def test_api(image1_path, image2_path):
    # Convert images to base64
    base64_1 = image_to_base64(image1_path)
    base64_2 = image_to_base64(image2_path)
    
    # API endpoint
    url = "http://l0koc0kss0oso8ow0ckkccgw.df.weskonek.com.sslip.io:8000/faces_base64/"
    
    # Prepare the data
    data = {
        "image1": base64_1,
        "image2": base64_2
    }
    
    # Make the request
    response = requests.post(url, data=data)
    
    # Print the response
    print("\nResponse Status Code:", response.status_code)
    print("Response Body:")
    print(json.dumps(response.json(), indent=2))

if __name__ == "__main__":
    # Replace these paths with your actual image paths
    image1_path = "path/to/your/first/image.jpg"
    image2_path = "path/to/your/second/image.jpg"
    
    test_api(image1_path, image2_path) 