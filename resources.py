resources = {
    "AI": 1289527408709341286,
    "Artificial Intelligence": 1289527408709341286,
    "Open Source": 1289539897258016850,
    "DSA": 1289573390734196836,
    "Web Development": 1289573446434422914,
    "App Development": 1289527408709341286,
    "Machine Learning": 1289527408709341286,
    "Frontend": 1289573446434422914,
    "Backend": 1289573446434422914,
    "Full Stack": 1289573446434422914,
    "Mobile Development": 1289573344391462985,
    "Android Development": 1289573344391462985,
    
   
}

def get_resource(search_key):
    # Search for the keyword in the resources dictionary
    for key, thread_id in resources.items():
        if key.lower() in search_key.lower():  # Case-insensitive matching
            return thread_id
    return None  # Return None if no match is found
    

