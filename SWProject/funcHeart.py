### function uses input PatientData= [age(years), sex(1=male, 0=female), weight(kg), height(cm), cholesterol, sinThickness(mm), glucose]

### The model has as input Heart = [age, sex, cholesterol]

## Need to have numpy ans keras installed for the function to work 

def predict(patientData):
    from keras.models import load_model
    import numpy as np
    model = load_model('heart.h5')

        ##transform data to work in the model 
    myorder=[0,1,4]
    patientData = [ patientData[i] for i in myorder]
    x = np.array([patientData])

    prediction = model.predict_classes(x)

    return ( prediction[0][0])

