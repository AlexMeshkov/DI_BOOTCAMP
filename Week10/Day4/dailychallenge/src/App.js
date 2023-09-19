import React , {useState} from 'react';
import FormComponent from './components/FormComponent';
import './App.css';

const App = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    isSubscribed: false,
  });

const handleChange = (err) =>{
  const {name, value, type, checked} = err.target;
  setFormData(prevState => ({
    ...prevState,
    [name]: type === 'checkbox' ? checked : value
  }));
}

return(
  <div className='App'>
    <FormComponent
    formData={formData}
    handleChange={handleChange}
    />
  </div>
);

}

export default App;
