import os
import django
import sys
from decimal import Decimal

# Set up Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eConsultancy.settings')
django.setup()

from courses.models import College

def get_college_type(name):
    name_lower = name.lower()
    if any(k in name_lower for k in ['nursing', 'medical', 'dental', 'ayurvedic', 'speech', 'hearing', 'health']):
        return 'medical'
    elif any(k in name_lower for k in ['engineering', 'tech']):
        return 'engineering'
    elif any(k in name_lower for k in ['business', 'management', 'commerce']):
        return 'management'
    elif any(k in name_lower for k in ['law']):
        return 'law'
    elif any(k in name_lower for k in ['pharmacy']):
        return 'pharmacy'
    elif any(k in name_lower for k in ['art', 'science', 'education']):
        return 'arts'
    else:
        return 'management'

def run():
    raw_colleges = [
        "Atria University",
        "Sree Narayana nursing college",
        "Mathrushree nursing college",
        "Nalapad group of institutions",
        "Samvaad institute of speech & hearing",
        "krupanidhi group of institutions",
        "Gitam university",
        "MR Ambedkar dental college",
        "VS Dental college",
        "Nightingale college of nursing",
        "Prasanna Ayurvedic college",
        "Gopalan college of engineering",
        "R L Jalappa",
        "siddaganga medical college",
        "Banasawadi college of nursing",
        "Florence nursing college",
        "Goldfinch nursing college",
        "Manasa school & college of nursing college",
        "Karavali group of colleges",
        "Manjushree institutions",
        "Ranebennur college of nursing",
        "Sofia college of nursing",
        "Sri channe Gowda college of nursing",
        "The Capitol college of nursing",
        "Vagdevi college of nursing",
        "Basaveshwara medical college",
        "J. J. M Medical College",
        "S S Institute of medical science",
        "Bapuji Dental College",
        "Chettinad Academy",
        "Sri Hasanamba Dental College",
        "KLE Dental college, Bangalore",
        "GIBS Business School",
        "Christ Academy",
        "Amity University Bangalore",
        "ISBR Business Schools",
        "Mewa Vanguard Business school",
        "Charkos college of Nursing",
        "Sindhi college",
        "Presidency college",
        "Yenopaya universit, Bangalore",
        "ST. Hopkins college",
        "Silicon city college",
        "ICFAI Businees school",
        "Azim Premji university, Bangalore",
        "Hindustan Academy",
        "Alva’s Institution"
    ]

    colleges_created = 0

    print("Adding new colleges without deleting existing data...")

    for item in raw_colleges:
        parts = item.split(',')
        name = parts[0].strip()
        location = parts[1].strip() if len(parts) > 1 else 'Bangalore'
        
        c_type = get_college_type(name)
        
        college, created = College.objects.get_or_create(
            name=name,
            defaults={
                'location': location,
                'established': 2000,
                'type': c_type,
                'rating': Decimal('0.0'),
                'status': 'active'
            }
        )
        if created:
            colleges_created += 1
            print(f"Added: {name}")
        else:
            print(f"Already exists: {name}")

    print(f"Finished! Created {colleges_created} new colleges.")

if __name__ == '__main__':
    run()
