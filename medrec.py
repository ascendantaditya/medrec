class HealthRecordSystem:
    def __init__(self):
        self.disease_medicines = {
            "cold": ["paracetamol", "ibuprofen", "cough syrup"],
            "fever": ["paracetamol", "ibuprofen"],
            "diarrhea": ["oral rehydration salts", "loperamide", "electrolyte solution"],
            "diabetes": ["insulin", "metformin", "glipizide"],
            "hypertension": ["amlodipine", "lisinopril", "hydrochlorothiazide"],
            # Add more chronic diseases and their corresponding medicines here
        }

    def get_medicine_requirements(self, disease):
        if disease.lower() in self.disease_medicines:
            return self.disease_medicines[disease.lower()]
        else:
            return "No specific medicines found for this disease."


def main():
    health_system = HealthRecordSystem()

    # Get user input for name and disease
    name = input("Enter your name: ")
    disease = input("Enter your disease: ")

    # Get medicine requirements for the specified disease
    medicine_requirements = health_system.get_medicine_requirements(disease)

    # Print medicine recommendations
    if isinstance(medicine_requirements, list):
        print(f"Dear {name}, here are the medicine requirements for {disease}:")
        for medicine in medicine_requirements:
            print("-", medicine)
    else:
        print(medicine_requirements)


if __name__ == "__main__":
    main()
