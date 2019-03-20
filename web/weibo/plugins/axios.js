import axios from 'axios'
// axios 配置
axios.defaults.timeout = 100000// 请求超时，适当修改

const $ajax = {
	async get(api, data) {
		try {
			let res = await axios.get(api, {
				params: data
			})
			res = res.data
			return new Promise((resolve) => {
                resolve(res)
			})
		} catch (err) {
			return err.message
		}
	},
	async post(api, data) {
		try {
			let res = await axios.post(api, data)
			return new Promise((resolve) => {
				res = res.data
                resolve(res)
			})
		} catch (err) {
			return err.message
		}
	},
}

export { $ajax }