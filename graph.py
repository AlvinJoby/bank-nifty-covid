import matplotlib.pyplot as plt
import os

def generate_graph(pre_covid, covid, post_covid):
    os.makedirs("outputs", exist_ok=True)

    plt.figure(figsize=(15,10))

    plt.subplot(3,1,1)
    plt.plot(pre_covid["Date"], pre_covid["Close"])
    plt.title("Pre-COVID")
    plt.ylabel("Price")
    plt.grid()

    plt.subplot(3,1,2)
    plt.plot(covid["Date"], covid["Close"])
    plt.title("COVID")
    plt.ylabel("Price")
    plt.grid()

    plt.subplot(3,1,3)
    plt.plot(post_covid["Date"], post_covid["Close"])
    plt.title("Post-COVID")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid()

    plt.suptitle("NIFTY Bank Across Phases", fontsize=16)

    plt.tight_layout()
    plt.savefig("outputs/phases.png")

    plt.close()