# PCOS Risk Assessment API Documentation

## Overview
This API provides a machine learning-based prediction service for assessing the risk of Polycystic Ovary Syndrome (PCOS) based on various health and lifestyle parameters.

## Deployment Status
The API is currently deployed on Render and may be experiencing temporary issues. For the latest status and endpoint, please check the deployment dashboard.

## Base URL
```
https://6c65-2409-40f3-1c-738c-545d-84d4-bf8b-2656.ngrok-free.app
```

> **Note**: This is a temporary ngrok URL that may change. For production use, please contact the API maintainers for the stable endpoint.

## API Health Check
Before making requests, please verify the API is operational by checking the deployment status. If you encounter any issues, please report them to the maintainers.

## Endpoints

### 1. Predict PCOS Risk
**Endpoint:** `/predict`  
**Method:** POST  
**Description:** Predicts the risk of PCOS based on provided health parameters.

#### Request Body
```json
{
    "Age": 25,
    "Weight": 65.5,
    "Height": 165.0,
    "BMI": 24.0,
    "Cycle_length": 28,
    "Cycle_regularity": 1,
    "Weight_gain": "yes",
    "Hair_growth": "no",
    "Skin_darkening": "no",
    "Pimples": "yes",
    "Fast_food": 2,
    "Exercise": 0
}
```

#### Parameters
| Parameter | Type | Description | Valid Values |
|-----------|------|-------------|--------------|
| Age | integer | Age in years | Positive integer |
| Weight | float | Weight in kilograms | Positive number |
| Height | float | Height in centimeters | Positive number |
| BMI | float | Body Mass Index | Positive number |
| Cycle_length | integer | Menstrual cycle length in days | Positive integer |
| Cycle_regularity | integer | Cycle regularity indicator | 0 or 1 |
| Weight_gain | string | Weight gain indicator | "yes" or "no" |
| Hair_growth | string | Hair growth indicator | "yes" or "no" |
| Skin_darkening | string | Skin darkening indicator | "yes" or "no" |
| Pimples | string | Pimples indicator | "yes" or "no" |
| Fast_food | integer | Fast food consumption frequency | Integer (e.g., 0-3) |
| Exercise | integer | Exercise frequency | Integer (e.g., 0-3) |

#### Response
```json
{
    "prediction": "Risk of PCOS",
    "confidence": 0.85
}
```

#### Response Fields
| Field | Type | Description |
|-------|------|-------------|
| prediction | string | Either "Risk of PCOS" or "No Risk of PCOS" |
| confidence | float | Confidence score between 0 and 1 |

#### Error Responses
- **500 Internal Server Error**: If there's an error in processing the request or making the prediction.
- **503 Service Unavailable**: If the API is temporarily unavailable or undergoing maintenance.

## Example Usage

### Using cURL
```bash
curl -X POST "https://6c65-2409-40f3-1c-738c-545d-84d4-bf8b-2656.ngrok-free.app/predict" \
     -H "Content-Type: application/json" \
     -d '{
         "Age": 25,
         "Weight": 65.5,
         "Height": 165.0,
         "BMI": 24.0,
         "Cycle_length": 28,
         "Cycle_regularity": 1,
         "Weight_gain": "yes",
         "Hair_growth": "no",
         "Skin_darkening": "no",
         "Pimples": "yes",
         "Fast_food": 2,
         "Exercise": 0
     }'
```

### Using Python
```python
import requests

url = "https://6c65-2409-40f3-1c-738c-545d-84d4-bf8b-2656.ngrok-free.app/predict"
data = {
    "Age": 25,
    "Weight": 65.5,
    "Height": 165.0,
    "BMI": 24.0,
    "Cycle_length": 28,
    "Cycle_regularity": 1,
    "Weight_gain": "yes",
    "Hair_growth": "no",
    "Skin_darkening": "no",
    "Pimples": "yes",
    "Fast_food": 2,
    "Exercise": 0
}

response = requests.post(url, json=data)
print(response.json())
```

## Notes
- The API uses a machine learning model trained on PCOS-related data
- All measurements should be in the specified units
- Boolean values should be provided as "yes" or "no" strings
- The confidence score indicates the model's certainty in its prediction
- The API is currently exposed through an ngrok tunnel and the URL may change
- For production use, please ensure you have the latest API endpoint URL
- If you encounter any issues with the API, please check the deployment status or contact the maintainers

## Troubleshooting
If you encounter issues with the API:
1. Verify the API is operational by checking the deployment status
2. Ensure all required parameters are provided in the correct format
3. Check that the values are within the expected ranges
4. If the issue persists, please contact the API maintainers with the error details 