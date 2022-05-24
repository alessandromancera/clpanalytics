import axios from 'axios'

const api = axios.create({
  baseURL: 'https://dry-plateau-13546.herokuapp.com/'
})

export default api
