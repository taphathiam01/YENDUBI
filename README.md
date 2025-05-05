# 🎮 Yendu Bi - Application Web 

Yendu Bi est une application web moderne (Django + React) conçue pour simplifier la gestion des clients dans un espace de jeux. Elle permet une expérience fluide tant pour les clients que pour les caissiers et administrateurs.

---

## 🚀 Objectif du projet

Créer une application web accessible depuis un téléphone ou un ordinateur, permettant la gestion complète des clients, avec des fonctionnalités telles que :

- Gestion des accès
- Paiement des entrées et consommations
- Suivi en temps réel des activités
- Notifications instantanées

---

## 🖥️ Technologies utilisées

- **Backend :** Django + Django REST Framework
- **Frontend :** React.js
- **Base de données :** PostgreSQL (ou SQLite pour le dev)
- **API :** RESTful API entre le backend et le frontend

---

## 👤 Interfaces de l'application

### 1. Interface Client
- Création de compte avec génération d’un QR code unique
- Paiement d’entrée et de consommation à l’avance
- Scan de QR codes des menus pour consommer
- Suivi du solde restant et de l’historique des consommations
- Notifications en temps réel (confirmation de paiements, solde...)

### 2. Interface Caissier
- Scan du QR code du client à l’arrivée
- Encaissement des entrées et consommations
- Consultation du solde client en temps réel
- Notification pour chaque consommation validée

### 3. Interface Admin
- Suivi journalier du nombre total de clients
- Suivi des encaissements par caissier
- Analyse des consommations
- Gestion des menus, caissiers et prix
- Export de statistiques

---

## 🔄 Fonctionnement global

1. **Inscription du client** → Génération d’un QR code unique
2. **Paiement** → Le caissier scanne le QR code, valide l'entrée et crédite la consommation
3. **Consommation** → Le client scanne les QR codes des menus, le solde est mis à jour automatiquement
4. **Solde insuffisant** → Affichage d’un message d’erreur et alerte pour recharge

---

## 📊 Statistiques & gestion

- Nombre de clients par jour
- Ventes par menu ou activité
- Historique des transactions
- Rapports par caissier

---

## 📱 Support et accessibilité

- Utilisable depuis un **téléphone**, une **tablette** ou un **ordinateur**
- Fonctionne comme une **Progressive Web App (PWA)**
- Aucune installation requise

---

## 📁 Structure du projet

