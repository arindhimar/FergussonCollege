import React from 'react';
import { Outlet, Link } from 'react-router-dom';

export default function Navigate() {

    return (
        <div>
            <h1>Navigation</h1>
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/about">About</Link></li>
                <li><Link to="/contact">Contact</Link></li>
            </ul>
            <Outlet />
            
        </div>

    );


}