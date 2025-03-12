document.addEventListener("DOMContentLoaded", function() {
    const video = document.getElementById("video");
    const canvasElement = document.createElement("canvas");
    const canvas = canvasElement.getContext("2d");
    const oldQRInput = document.getElementById("oldQR");
    const newQRInput = document.getElementById("newQR");

    async function startVideo() {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } });
            video.srcObject = stream;
            video.play(); // Ensure the video is playing
        } catch (error) {
            console.error("Error accessing the camera: ", error);
        }
    }

    async function scanQRCode() {
        canvasElement.width = video.videoWidth;
        canvasElement.height = video.videoHeight;
        canvas.drawImage(video, 0, 0, canvasElement.width, canvasElement.height);
        const imageData = canvas.getImageData(0, 0, canvasElement.width, canvasElement.height);
        const code = jsQR(imageData.data, imageData.width, imageData.height);

        if (code) {
            if (!oldQRInput.value) {
                oldQRInput.value = code.data; // Set old QR code value
            } else {
                newQRInput.value = code.data; // Set new QR code value
            }
        }

        requestAnimationFrame(scanQRCode);
    }

    document.getElementById("scanOldQR").addEventListener("click", async () => {
        await startVideo();
        scanQRCode();
    });

    document.getElementById("scanNewQR").addEventListener("click", async () => {
        await startVideo();
        scanQRCode();
    });
});
