try:
    from clases.insercion_dicotomica import (
        ordenar, 
        ordenar_vacia
    )

    from clases.ordenacion_topológica import(
        ordenacion_burbuja
    )

    from clases.esta_explorado import (
        segmento,
        explorar
    )

except ImportError:
    print("ImportError inesperado en __init__.py")
    pass