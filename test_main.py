"""
Test goes here

"""
from main import summary, histogram_blood_pressure


def test_summary():
    """Function calling summary which tests the mean and standard deviation value of the dataset"
    the dataset"""
    # mean of age column in heart dataset
    # print(summary("heart.csv")["age"][0])
    assert summary("heart.csv")["age"][0] == 54.366336633663366
    # print(summary("heart.csv")["age"][1])
    # standard deviation of age column in heart dataset
    assert summary("heart.csv")["age"][1] == 9.082100989837857
    # median of age column in heart dataset
    assert summary("heart.csv")["age"][4] == 55.0


def test_histogram_blood_pressure():
    """Function calling histogram_blood_pressure()"""
    histogram_blood_pressure("heart.csv")


if __name__ == "__main__":
    test_summary()
    test_histogram_blood_pressure()
