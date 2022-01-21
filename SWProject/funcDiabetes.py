### function uses input PatientData= [age(years), sex(1=male, 0=female), weight(kg), height(cm), cholesterol, sinThickness(mm), glucose]

### The model has as input Pima = [glucose, skinThickness, BodyMass, age]

## Need to have numpy ans keras installed for the function to work 

def predict(patientData):
    from keras.models import load_model
    import numpy as np
    model = load_model('diabetes.h5')

    ##transform data to work in the model 
    patientData[2] = patientData[2]/((patientData[3]/10)**2)# sub weight with BMI kg/(m^2)
    myorder=[6,5,2,0]
    patientData = [ patientData[i] for i in myorder]
    x = np.array([patientData])

    prediction = model.predict_classes(x)

    return (prediction[0][0])
