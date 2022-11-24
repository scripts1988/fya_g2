import pandas
# Read data from csv file (done)
df = pandas.read_csv('Model/data.csv')

# data including id, name, position of employee

#add new data to csv file (done)
# data = [
    
# ]
# dataframe = pandas.DataFrame(data)
# dataframe.to_csv("Model/data.csv", index=False, mode='a', header=False)


#add new data from input (done)
def add_data():
    add_id = input ('Enter your ID: ')
    add_name = input ('Enter your name: ')
    add_position = input ('Enter your position: ')
    dataset = [[add_id,add_name,add_position]]
    dataframe = pandas.DataFrame(dataset)
    dataframe.to_csv("Model/data.csv", index=False, mode='a', header=False)



def main():
    counter = input ('How many data do you want to add: ')
    for x in counter:
        add_data()
        print ("success")
    print (pandas.read_csv('Model/data.csv'))

if __name__ == "__main__":
    main()