import pandas as pd
import matplotlib.pyplot as plt

# Richiesta file
file_path = input("Inserisci il percorso del file CSV: ").strip()

try:
    # Caricamento dati
    df = pd.read_csv(file_path)

    # Mostra prime righe
    print(df.head())

    # 1. Score vs PlayTime
    plt.figure(figsize=(10, 6))
    plt.scatter(df['PlayTimeHours'], df['Score'], c='blue', alpha=0.7)
    plt.title("Score vs Ore di gioco")
    plt.xlabel("Ore di gioco")
    plt.ylabel("Punteggio")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 2. Media degli achievements per regione
    region_stats = df.groupby('Region')['AchievementsUnlocked'].mean().sort_values()
    region_stats.plot(kind='barh', color='green')
    plt.title("Achievements medi per Regione")
    plt.xlabel("Achievements medi")
    plt.tight_layout()
    plt.show()

    # 3. Top 5 giocatori per Score
    top_players = df.nlargest(5, 'Score')[['PlayerName', 'Score']]
    top_players.plot(kind='barh', x='PlayerName', y='Score', color='orange')
    plt.title("Top 5 Giocatori per Punteggio")
    plt.xlabel("Punteggio")
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"[Errore] File non trovato: {file_path}")
except Exception as e:
    print(f"[Errore] {e}")
