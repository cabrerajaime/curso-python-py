import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ["X", "Y", "Z"]
    values = [100, 200, 300]

    fig, ax = plt.subplots()

    ax.pie(values,labels=labels)
    plt.savefig("pie.png")
    plt.close()