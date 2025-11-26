# Utiliser l'image Python officielle
FROM python:3.13

# Définir le répertoire de travail dans le container
WORKDIR /app

# Copier les fichiers requirements.txt
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet dans le container
COPY . .

# Exposer le port Django
EXPOSE 8000

# Commande pour lancer Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
