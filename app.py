 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):   
 
    # Pre-processing user input    
    if Gender == "Male":
        Gender = 1
    else:
        Gender = 0
 
    if Married == "No":
        Married = 0
    else:
        Married = 1
 
    if Education == "Graduate":
        Education = 0
    else:
        Education = 1  

    if Self_Employed == "No":
        Self_Employed = 0
    else:
        Self_Employed = 1

    if Property_Area == "Urban":
        Property_Area = 2
    elif Property_Area == "Rural":
        Property_Area = 0
    elif Property_Area == "Semiurban":
        Property_Area = 1

 
    # Making predictions 
    prediction = classifier.predict( 
        [[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])
     
    if prediction == 1:
        pred = 'Approved'
    else:
        pred = 'Rejected'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:orange;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Loan Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    Gender = st.selectbox('Gender',("Male","Female"))
    Married = st.selectbox('Marital Status',("No","Yes"))
    Dependents = st.radio('Dependents',[0,1,2,3]) 
    Education = st.selectbox('Education',("Graduate","Not Graduate"))
    Self_Employed = st.selectbox('Self_Employed',("No","Yes"))
    ApplicantIncome = st.number_input("Applicants monthly income") 
    CoapplicantIncome = st.number_input("CoapplicantIncome Should be between 0-41000")
    LoanAmount = st.number_input("Total loan amount")
    Loan_Amount_Term = st.selectbox('Loan_Amount_Term(Most popular is 360)',[360,120,240,180,60,300,480,36,84,12])
    Credit_History = st.radio("What is your Credit_History",
                              [1,0])
    if Credit_History == 1:
      st.write("You Have Clear Debts")
    else:
      st.write("You Have Unclear Debts")
    
    Property_Area = st.radio('Property_Area',("Urban","Rural","Semiurban"))
    
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area) 
        st.success('Your loan is {}'.format(result))
        print(LoanAmount)
     
if __name__=='__main__': 
    main()
