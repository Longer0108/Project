// main.js

function uploadVideo() {
    const fileInput = document.getElementById('video-file');
    const videoPreview = document.getElementById('video-preview');

    if (fileInput.files.length > 0) {  // 檢查是否有選擇文件
        const file = fileInput.files[0];  // 第一個文件

        if (file.type.startsWith('video/')) {  // 檢查文件類型是否是影片
            const videoURL = URL.createObjectURL(file);
            const videoElement = document.createElement('video');  // 在網頁中顯示影片
            videoElement.src = videoURL;  // 設置先前創建的影片URL，將所選影片顯示在網頁上
            videoElement.controls = true;  // 在影片上顯示控制面板 例如播放、暫停...
            videoPreview.innerHTML = '';
            videoPreview.appendChild(videoElement);
        } // if
		else {
            alert('請選擇一個有效的影片文件！');
        }  // else
    }  // if
	else {
        alert('請選擇要上傳的影片文件！');
    }  // else
}  // uploadVideo()
