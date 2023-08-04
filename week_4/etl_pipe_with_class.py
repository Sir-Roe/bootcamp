import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
class Invoice:
    
    def __init__(self, filepath=r'C:\Users\Alex Lucchesi\coding-temple\coding_temple_data_analytics_ft\week-4\data\Invoices-with-Merged-Categories-and-Merged-Amounts.csv'):
        self.url = filepath
        self.sql_url = 'postgresql://oqtvbtjq:NZBDysGJc_iKTzVtTn5svCGKlezumfFk@mahmud.db.elephantsql.com/oqtvbtjq'
    
    def wrangle(self):
        self.df = pd.read_csv(self.url)
        self.df.columns = self.df.columns.str.lower().str.replace(' ', '_')
        try:

        # Now, we are going to separate out the pipe operands
            new_cat = [self.df['category'][index].split(sep='|') for index in range(len(self.df))]
            new_amount = [self.df['amount'][index].split(sep='|') for index in range(len(self.df))]
            order_ids = [self.df['order_id'][index] for index in range(len(self.df))]

            # Instantiating a counter object
            c = 0
            # Begin looping through
            for l1, l2 in zip(new_cat, new_amount):
                for cat, price in zip(l1,l2):
                    self.df.loc[len(self.df.index)] = [order_ids[c], cat, price]
                c += 1
            return self.df[4:].reset_index(drop=True)
        except:
            return self.df
    
    def create_vis(self):
        sns.histplot(data=self.df, y='category')
        return plt.savefig('data/histogram_of_category.png')    
    
    # def create_vis(self):
    #     for amount in self.df.amount:
    #         if amount >= '50':
    #             print(self.df.loc[self.df['amount'] == amount])
    
    def create_sql(self, df:pd.DataFrame):
        df.to_sql('invoices', con=self.sql_url, if_exists='replace')
    
    def create_csv(self, df: pd.DataFrame, filename:str):
        df.to_csv(f'data/{filename}.csv', index=False)

if __name__ == '__main__':
    c = Invoice(r'C:\Users\Alex Lucchesi\coding-temple\coding_temple_data_analytics_ft\week-4\data\Invoices-with-Merged-Categories-and-Merged-Amounts.csv')
    df = c.wrangle()
    print(c.create_vis())
    c.create_sql(df)
    c.create_csv(df, 'class_cleaned_data')