# encoding=utf-8
# Created by quazinafiulislam

"""
Having a little fun with matplotlib
"""

from matplotlib import pyplot as plt


# I call it the ADM function :)
def func(x):
    return (x - 37) ** 2


if __name__ == '__main__':
    # So that our graph looks like a web-comic
    with plt.xkcd():

        # We are going Set the right and top margins to invisible
        plt.axes().spines['right'].set_color('none')
        plt.axes().spines['top'].set_color('none')

        # We are going to give our graph a title
        plt.title('Will he bunk?')
        plt.plot([func(x) for x in range(0, 75)])

        # Going to get rid of x the markings on the axes
        plt.xticks([])
        plt.yticks([])

        # We are going to add labels to the
        plt.xlabel('Number of chores his wife will tell him to do')
        plt.ylabel('Probability that he will come')

        # Adding an annotation here, to point out when he is going to bunk
        plt.annotate(
            "The point at which he is going to bunk!",
            xy=(37, func(37)),
            arrowprops=dict(arrowstyle='->'),
            xytext=(13, 1000)
        )

        # Finally, we tell python to show us our mysterious function :)
        plt.show()