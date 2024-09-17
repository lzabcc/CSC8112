import matplotlib.pyplot as plt


def draw_chart(data_df):

    plt.figure(figsize=(8, 4), dpi=200)
    
    plt.plot(data_df["Timestamp"], data_df["Value"], color="#FF3B1D", marker='.', linestyle="-")
    
    plt.title("PM25 data for demonstration")
    plt.xlabel("DateTime")
    plt.ylabel("Value")
    
    plt.xticks(rotation=90,fontsize=3)
    plt.savefig("PM25_data.png")

    #plt.show()

