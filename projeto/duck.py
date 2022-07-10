# Para tudo funcionar como deve, nunca mexa nesse documento.
# Ele está todo comentado para fins de compreensão.
# Caso mofique algo, não nos responsabilizamos pelo não funcionamento do protocólo. 

import urequests
import uhashlib

class Duck:
    raw = "https://raw.githubusercontent.com"
    github = "https://github.com"

    def __init__(self, user, repo, url=None, branch="master", working_dir="app", files=["boot.py", "main.py"], headers={}):
        #Duck OTA.
        #Args:
        #user (str): usuário do GitHub.
        #repo (str): repositório do GitHub para buscar.
        #branch (str): Ramo de repositório do GitHub. (mestre)
        #working_dir (str): Diretório dentro do repositório GitHub onde está o aplicativo micropython.
        #url (str): URL para o diretório raiz.
        #files (list): Arquivos incluídos na atualização OTA.
        #headers (list, opcional): Cabeçalhos para urequests.
        
        self.base_url = "{}/{}/{}".format(self.raw, user, repo) if user else url.replace(self.github, self.raw)
        self.url = url if url is not None else "{}/{}/{}".format(self.base_url, branch, working_dir)
        self.headers = headers
        self.files = files

    def _check_hash(self, x, y):
        x_hash = uhashlib.sha1(x.encode())
        y_hash = uhashlib.sha1(y.encode())
        x = x_hash.digest()
        y = y_hash.digest()
        if str(x) == str(y):
            return True
        else:
            return False

    def _get_file(self, url):
        payload = urequests.get(url, headers=self.headers)
        code = payload.status_code
        if code == 200:
            return payload.text
        else:
            return None

    def _check_all(self):
        changes = []
        for file in self.files:
            latest_version = self._get_file(self.url + "/" + file)
            if latest_version is None:
                continue
        try:
            with open(file, "r") as local_file:
                local_version = local_file.read()
        except:
            local_version = ""
        if not self._check_hash(latest_version, local_version):
            changes.append(file)
        return changes

    def fetch(self):
        # Verifique se a versão mais recente está disponível.
        # Devoluções:
        # True - se for, False - se não.
        if not self._check_all():
            return False
        else:
            return True

    def update(self):
        #Substitui todos os arquivos alterados por um mais recente.
        #Retorno:
        #True - se as alterações foram feitas False - se não.
        changes = self._check_all()
        for file in changes:
            with open(file, "w") as local_file:
                local_file.write(self._get_file(self.url + "/" + file))
        if changes:
            return True
        else:
            return False
