import hid


class MauvaisTypeDonneesHID(Exception):
    pass


class AucunPheripheriqueDisponible(Exception):
    pass


class SimpleHID:

    def __init__(self, chemin):

        self._device = hid.device()
        self._device.open_path(chemin)

    def fermer(self):
        if self._device is not None:
            self._device.close()
            self._device = None

    def ecrire(self, donnees):
        if not isinstance(donnees, bytes):
            raise MauvaisTypeDonneesHID('Il faut obligatoirement faire passer un tableau de bytes !')
        if self._device is None:
            raise AucunPheripheriqueDisponible('L\'appareil HID n\'est pas connecté.')
        self._device.write(donnees)
