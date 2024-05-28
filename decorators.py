"""_summary_"""
import functools
from streamTypes.file.fileStream import FileStream


s = FileStream()

user_data = {"username": "Eder", "access_level": "admin"}


def make_secure(access_level: str):
    """ make_secure """
    def decorator(func):  # -> retorna función decorada
        """ decorator """
        # decorador que reemplaza la documentación de "def secure_function"
        # por la de "func", de este modo predomina la información de la función decorada
        @functools.wraps(func)
        def secured_function(*args, **kwarkg):
            """ secure_function """
            if user_data["access_level"] == access_level:
                # retorna la ejecución de la funcion decorada
                return func(*args, **kwarkg)
            # resultado de la funcion actual en caso de no cumpli condición
            return f"No admin permissions for {user_data['username']}."

        return secured_function  # retorno de funcion

    return decorator


@make_secure("admin")
def get_password(great) -> str:
    """ Args:
        great (str): greatting
    Returns:
        str: password
    """
    print(great)
    return "1234"


# estas dos ejecuciones son exactamente lo mismo
# - se manda a llamar la funcion decorada
R1 = get_password("hola")
print(f"func name: {get_password.__name__}")
print(R1)
# - se reescribe la funcion decorada
get_password_2 = make_secure("admin")(get_password)
R1 = get_password_2("hola")
print(f"func name: {get_password_2.__name__}")
print(R1)
