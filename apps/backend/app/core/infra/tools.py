from .infra import Infra

infra: dict[str, Infra] = {}

def register_infra(new_infra: Infra):
    new_infra.init()
    infra[new_infra.name] = new_infra

async def load_infra():
    loaded_dict = dict()

    while len(loaded_dict.keys()) < len(infra):
        progress = False

        for name, ext in list(infra.items()):
            if name in loaded_dict.keys():
                continue

            reqs = ext.requirements or []

            if all(r in loaded_dict.keys() for r in reqs):
                loaded_dict[name] = ext.action(requirements=loaded_dict)

        if not progress:
            raise Exception("Circular or missing dependencies detected!")
