import streamlit as st
st.title('Title-->GeeksForGeeks')  #this is used to print the title

st.header('Header-->GeeksForGeeks') # this is used to print the header

st.subheader('subheader-->GeeksForGeeks') #this is the subheader

st.text('Text --> GeeksForGeeks') #text
                                      
st.markdown('# Hii')
st.markdown('## Hii')
st.markdown('### Hii')            # all for the markdown
st.markdown('#### Hii')
st.markdown('Hii')

st.success('success')             #success
st.info('Information')            #information
st.warning('warning')             #warning
st.error('Error!')                #error

st.exception(ZeroDivisionError('Divison not possible with 0'))  #exception
st.help(ZeroDivisionError)       #help

# """help function tells you about that function for which the help is 
# called it can be used in case if you want to query any problem regarding
# the functions and its properties"""

st.write("range(1,10)")  # this work same as the text function used to write on the st page

st.code('x = 10\n'
        'for i in range(x):\n'
        'print(i)')

# this will write the code on the streamlit page in the proper  code 
# format

st.checkbox('Male')

# Multiple checkbox cannot have same name  , if it is then it will throw error


if (st.checkbox('Adult')):
    st.write('You are an adult!')

radioButton  =  st.radio('select:',('Male','Female','Other'))
if radioButton == 'Male':
    st.write('You are a Male')
elif radioButton == 'Female':
    st.write('Your are a Female')
elif radioButton == 'Other':
    st.write('Your are other')


st.subheader('Select Box')
selectBox = st.selectbox("Data Science:",['Data Analysis','Web Scraping','Machine Learning'
                              ,'Deep Learning','Natural Language Processing',
                              'Computer Vision','Image Processing'])

st.write('You have selected: ',selectBox)


multiSelectBox = st.multiselect("Data Science:",['Data Analysis','Web Scraping','Machine Learning'
                              ,'Deep Learning','Natural Language Processing',
                              'Computer Vision','Image Processing'])

# st.write("You've selected: ",len(multiSelectBox),multiSelectBox)
st.write("You've selected: ",len(multiSelectBox),'courses')


st.subheader('Button')
if st.button('Click ME'):
    st.write('Thanks for clicking me')


st.subheader('Slider')
vol = st.slider('Select the level',1,100,step = 1)
st.write(vol)

st.subheader('Text Input')
name = st.text_input('Enter you name:')
if name:
    st.write('Hello ',name)

st.subheader('Text Input')
username = st.text_input('Username: ')
password = st.text_input('Passoword: ',type='password')

st.subheader('Text Area')
textarea = st.text_area('Write something interesting about yourself in 500 words')
st.write(textarea)

st.subheader('Input number')
st.number_input('select you age',18,110)

st.subheader('Input date')
st.date_input('select date')

st.subheader('Input Time')
st.time_input('Time input')