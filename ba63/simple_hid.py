import hid


class MauvaisTypeDonneesHID(Exception):
    pass


class AucunPheripheriqueDisponible(Exception):
    pass


class SimpleHID:

    def __init__(self, chemin):

        self._chemin = chemin
        self._device = hid.device()
        self._device.open_path(self._chemin)

    @property
    def chemin(self):
        return self._chemin

    def ouvrir(self):
        """
        Ouverture de l'appareil HID si disponible
        :return: None
        """
        if self._device is None:
            self._device.open_path(self._chemin)

    def fermer(self):
        """
        Fermeture de la communication avec l'appareil HID
        :return: None
        """
        if self._device is not None:
            self._device.close()
            self._device = None

    def ecrire(self, donnees):
        """
        Écriture de données raw sur le port de communication HID
        :param bytes donnees: Les données brutes
        :return: None
        """
        if not isinstance(donnees, bytes):
            raise MauvaisTypeDonneesHID('Il faut obligatoirement faire passer un tableau de bytes !')
        if self._device is None:
            raise AucunPheripheriqueDisponible('L\'appareil HID n\'est pas connecté.')
        self._device.write(donnees)
