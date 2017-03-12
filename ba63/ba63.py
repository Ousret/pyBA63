from hid import enumerate
from ba63.simple_hid import SimpleHID
from ba63.constant import SEQUENCE_MARQUEUR_DEBUT, SEQUENCES_CURSEUR, SEQUENCE_NETTOYAGE, SEQUENCE_SET_CHARSET, TAILLE_MESSAGE_MAX, NOMBRE_CARACTERES_PAR_LIGNE
from unidecode import unidecode
import platform


class FormatDonneesInvalideBA63(Exception):
    pass


class TailleMessageTropGrande(Exception):
    pass


class CharsetInvalideBA63(Exception):
    pass


class NumeroLigneInvalideBA63(Exception):
    pass


class FormatTexteInvalideBA63(Exception):
    pass


class BA63(SimpleHID):

    def __init__(self, chemin):
        super().__init__(chemin)

    def _paquet(self, donnees):
        """
        Construction d'un paquet à destination du BA63
        :param bytes donnees: Les données à transmettre sous forme de bytes
        :return: Séquence prête à l'envoie
        :rtype: bytes
        """
        if not isinstance(donnees, bytes):
            raise FormatDonneesInvalideBA63('La construction de paquet ne peux pas se faire sans un tableau de bytes.')
        if len(donnees) > TAILLE_MESSAGE_MAX:
            raise TailleMessageTropGrande('La construction de paquet a échoué car votre message est de taille %i '
                                          'octets mais la taille maximale est de %i octets' % (len(donnees),
                                                                                               TAILLE_MESSAGE_MAX))
        return SEQUENCE_MARQUEUR_DEBUT + bytes(len(donnees)) + donnees

    def imprimer(self, numero_ligne, message):
        """
        Imprime du texte à l'écran
        :param int numero_ligne: Numéro de la ligne
        :param str message: Texte à écrire
        :return: None
        """
        if not isinstance(message, str):
            raise FormatTexteInvalideBA63('Nous ne pouvons pas imprimer autre chose que du texte sur le BA63.')
        self.curseur(numero_ligne)
        message_sanitized = unidecode(message)
        if len(message_sanitized) > NOMBRE_CARACTERES_PAR_LIGNE:
            message_sanitized = message_sanitized[:(NOMBRE_CARACTERES_PAR_LIGNE-2)] + '..'
        super().ecrire(self._paquet(bytes(message_sanitized, 'ascii')))

    def nettoyer(self):
        """
        Efface l'écran du BA63.
        :return: None
        """
        super().ecrire(self._paquet(SEQUENCE_NETTOYAGE))

    def curseur(self, numero_ligne):
        """
        Déplace le curseur sur le début d'une ligne
        :param int numero_ligne: Le numéro de la ligne
        :return: None
        """
        if numero_ligne not in SEQUENCES_CURSEUR.keys():
            raise NumeroLigneInvalideBA63('La ligne numéro %i est invalide. Disponibles: %s.' % (numero_ligne, SEQUENCES_CURSEUR.keys()))
        super().ecrire(self._paquet(SEQUENCES_CURSEUR[numero_ligne]))

    def charset(self, target):
        """
        Change le charset du BA63
        :param target: Le type de charset (use. constant)
        :return: None
        """
        if len(target) != 3:
            raise CharsetInvalideBA63('Une séquence charset doit être codée sur 3 octets, votre séquence est de %i '
                                      'octet(s).' % len(target))
        super().ecrire(self._paquet(SEQUENCE_SET_CHARSET))
        super().ecrire(self._paquet(target))

    @staticmethod
    def get(identifiant_vendeur=2727, identifiant_materiel=512, interface_cible=1):
        """
        Recherche du BA63 et création d'une nouvelle instance BA63
        :param identifiant_vendeur: Identifiant du vendeur matériel
        :param identifiant_materiel: Identifiant du matériel chez le vendeur
        :param interface_cible: Numéro de l'interface
        :return: Nouvelle instance du BA63
        :rtype: BA63
        """
        hid_disponible = enumerate()
        noyau_systeme = platform.system()

        for dev in hid_disponible:
            if dev['vendor_id'] == identifiant_vendeur and dev['product_id'] == identifiant_materiel and dev['interface_number'] == interface_cible:
                return BA63(dev['path'])
            elif dev['vendor_id'] == identifiant_vendeur and dev['product_id'] == identifiant_materiel and dev['interface_number'] == -1:
                pass  # TODO: Vérifier le cas Darwin -> noyau_systeme

        return None
