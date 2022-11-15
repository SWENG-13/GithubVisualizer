function test_request() {
  fetch("/test_endpoint")
  .then((response) => {
    return response.text()
  })
  .then((text) => {
    alert(text)
  })
}
