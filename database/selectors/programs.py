from database.models import Programs
from mongoengine import DoesNotExist


def get_all_programs():
    return Programs.objects().all()


def delete_prg(program_name):
    return Programs.objects(program_name=program_name).delete()


def get_program_by_scope(domain):
    return Programs.objects(scopes=domain).first()

def get_program_by_program_name(program_name):
    try:
        return Programs.objects.get(program_name=program_name)
    
    except DoesNotExist:
        return "Pleas Enret Program name between \" Like: \"Walmart INC\""

