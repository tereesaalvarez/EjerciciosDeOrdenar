try:
    from .insercion_dicotomica import (
        ordenar, 
        ordenar_vacia,
    )

    from .ordenacion_topológica import(
        ordenacion_burbuja
    )

    from .esta_explorado import (
        segmento,
        explorar
    )

except ImportError:
    print("ImportError inesperado en __init__.py")
    pass