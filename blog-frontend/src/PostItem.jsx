import React from 'react';
import { Link } from 'react-router-dom';

const PostItem = () => {
    return(
        <div className = "post-item">
            <h2>{post.title}</h2>
            <p>{post.content.substring(0, 100)}...</p>
        </div>
    )
}