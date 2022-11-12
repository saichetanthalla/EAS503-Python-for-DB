from operator import index
import pandas as pd

# Read the following link and complete this homework. https://www.codemag.com/Article/1711091/Implementing-Machine-Learning-Using-Python-and-Scikit-learn

# Make sure to install scikit-learn and Pandas

def step1():
    """
    # Step 1: Getting the Titanic Dataset
    Return a dataframe containing the Titantic dataset from the following URL
    # URL: https://gist.githubusercontent.com/mkzia/aa4f293661dba857b8c4459c0095ac95/raw/8075037f6f7689a1786405c1bc8ea9471d3aa9c3/train.csv

    """
    # BEGIN SOLUTION
    df=pd.read_csv('https://gist.githubusercontent.com/mkzia/aa4f293661dba857b8c4459c0095ac95/raw/8075037f6f7689a1786405c1bc8ea9471d3aa9c3/train.csv')
    return df
    # END SOLUTION
    # return df


def step2(df):
    """
    # Step 2: Clean data
    Modify df to drop the following columns:
    PassengerId
    Name
    Ticket
    Cabin
    Hint: Just pass all the columns to the .drop() method as an array
    return dataframe
    """
    # BEGIN SOLUTION
    drop_columns=['PassengerId','Name','Ticket','Cabin']
    df = df.drop(drop_columns, axis=1)
    return df
    # END SOLUTION
    # return df


def step3(df):
    """
    # Step 3: Drop NaNs and reindex
    You want to reindex so your index does not have missing values after you drop the NaNs. Remember, index is used 
    to access a row. Notice how many rows you dropped!
    Modify df to drop NaNs and reindex
    return dataframe
    """
    # BEGIN SOLUTION
    df = df.dropna()
    df.reset_index(drop=True, inplace=True)
    return df
    # END SOLUTION
    # return df


def step4(df):
    """
    # Step 4: Encoding the Non-Numeric Fields
    Encode text fields to numbers
    Modify df to encode Sex and Embarked to encoded values.
    return dataframe
    """
    # BEGIN SOLUTION
    encoding = {"Sex":     {"male": 0, "female": 1},
                "Embarked": {'S':2,'C':0,'Q':1}}
    df = df.replace(encoding)
    return df
    # END SOLUTION
    # return df


def step5(df):
    """
    # Step 5: Making Fields Categorical
    Turn values that are not continues values into categorical values
    Modify df to make Pclass, Sex, Embarked, and Survived a categorical field
    return dataframe
    """
    # BEGIN SOLUTION
    df['Pclass'] = pd.Categorical(df.Pclass)
    df['Sex'] = pd.Categorical(df.Sex)
    df['Embarked'] = pd.Categorical(df.Embarked)
    df['Survived'] = pd.Categorical(df.Survived)

    return df
    # END SOLUTION
    # return df


def step6(df):
    """
    1. Split dataframe into feature and label
    2. Do train and test split; USE: random_state = 1
    4. Use LogisticRegression() for classification
    3. Return accuracy and confusion matrix

    Use  metrics.confusion_matrix to calculate the confusion matrix
    # https://towardsdatascience.com/understanding-confusion-matrix-a9ad42dcfd62
    # https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
    # IMPORTANT !!!! 
    # https://stackoverflow.com/questions/56078203/why-scikit-learn-confusion-matrix-is-reversed

    From the confusion matrix get TN, FP, FN, TP

    return --> accuracy, TN, FP, FN, TP; 
    Hint: round accuracy to 4 decimal places

    """
    # BEGIN SOLUTION
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import accuracy_score
    from sklearn.linear_model import LogisticRegression
    y=df['Survived']   
    x=df.drop('Survived',axis=1)   
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=1,stratify =df["Survived"],shuffle=True)
    Logi_Reg = LogisticRegression()
    Logi_Reg.fit(x_train,y_train)
    y_pred=Logi_Reg.predict(x_test)
    conf_matrix = confusion_matrix(y_test,y_pred)    
    TN,FP,FN,TP = conf_matrix[0][0],conf_matrix[0][1],conf_matrix[1][0],conf_matrix[1][1]
    aa=round((TP+TN/TP+FP+FN+TN),4)
    print(aa)
    accuracy = accuracy_score(y_test,y_pred)
    accuracy_round=round(accuracy,4)
    print(accuracy_round,TN,FP,FN,TP)
    return accuracy_round,TN,FP,FN,TP 

    # END SOLUTION