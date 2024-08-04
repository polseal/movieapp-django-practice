import { useEffect } from "react";

const Logout = () => {
    useEffect(() => {
        const logout = async () => {
            try {
                await fetch('http://localhost:8000/authentification/logout/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        refresh_token: localStorage.getItem('refresh_token'),
                    }),
                    credentials: 'include',
                });
                localStorage.clear();
                window.location.href = '/';
            } catch (error) {
                console.error('Error:', error);
            }
        };
        logout();
    }, []);
    return null;
};
export default Logout;  