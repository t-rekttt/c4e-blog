$.delete = function(url, callback) {
  return $.ajax({
    url: url,
    type: 'DELETE',
    success: callback,
    contentType: 'application/json',
  });
}

function deletePost(postId) {
  $.delete(`/posts/${postId}`, function() {
    $(`#post_${postId}`).remove();
  });
}