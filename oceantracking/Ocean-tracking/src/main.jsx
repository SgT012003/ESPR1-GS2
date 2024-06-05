import React from 'react';
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import App from './App.jsx';
import Home from './routes/Home.jsx';
import Tracking from './routes/Tracking.jsx';
import Info from './routes/Info.jsx';
import '/node_modules/bootstrap/dist/css/bootstrap.min.css';


const router = createBrowserRouter ([
  {
    path:'/', element:<App />,
    errorElement:<Error />,

    children: [
      {path: '/Home', element: <Home />},
      {path: '/Info', element: <Info />},
      {path: '/Tracking', element: <Tracking />},
    ]
  }
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router}/>
  </React.StrictMode>,
)
