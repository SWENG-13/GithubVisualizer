function test_request() {
  fetch("/testendpoint")
  .then((response) => {
    return response.text()
  })
  .then((text) => {
    alert(text)
  })
}
