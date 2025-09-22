const HOST = import.meta.env.VITE_TO_FASTAPI_HOST
const PORT = import.meta.env.VITE_TO_FASTAPI_PORT
const URL = `http://${HOST}:${PORT}/`

const API_SERVICE = {
    get: async(params)=>{
        return await fetch(URL+params,
            {
                method: "get",
                headers: {'Content-Type': 'application/json',}
            })
        .then(res=>res.json())
        .then(res=>res)
        .catch(err=>{
            console.error(err)
            return null
        })
    }
}

export default API_SERVICE