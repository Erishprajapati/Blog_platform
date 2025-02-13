import React, {useState, useEffect} from 'react';

const PostList = () => {
    const [posts, setPosts] = useState([]);
    useEffect(() =>{
        fetch('') //should be replaced with backend API
        .then(response => response.json())
        .then(data =>setPosts(data));

    }, []);
    
    return(
        <div className = "post-list">
            {post.map(post => (
            <PostItem key = {posts.id} post = {post} />
        ))}
        </div>
        

    );
}
export default PostList;