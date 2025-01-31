import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import App from './App.jsx';
import ArrayCheckComponent from './components/ArrayCheckComponent.jsx';
import FirstElementsComponent from './components/FirstElementsComponent.jsx';
import MergeArraysComponent from './components/MergeArraysComponent.jsx';
import PairSumComponent from './components/PairSumComponent.jsx';
import SwapCaseComponent from './components/SwapCaseComponent.jsx';

const root = createRoot(document.getElementById('root'));

root.render(
  <StrictMode>
    <div>
      <h1>JavaScript Practice Questions</h1>
      <ArrayCheckComponent />
      <FirstElementsComponent />
      <MergeArraysComponent />
      <PairSumComponent />
      <SwapCaseComponent />
    </div>
  </StrictMode>
);