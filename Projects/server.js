const express = require('express');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const app = express();
const PORT = 3000;
const cors = require('cors');
app.use(cors());


app.post('/send-video', async (req, res) => {
  const { video, to } = req.body;

  const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: 'neerajverma140204@gmail.com',
      pass: 'ghlt vzni boui ldop'
    }
  });

  const mailOptions = {
    from: 'neerajverma140204@gmail.com',
    to: to,
    subject: '🎥 Video Recording from Web App',
    text: 'Attached is the recorded video.',
    attachments: [
      {
        filename: 'video.webm',
        content: Buffer.from(video, 'base64'),
        contentType: 'video/webm'
      }
    ]
  };

  try {
    await transporter.sendMail(mailOptions);
    res.send('✅ Video sent successfully to ' + to);
  } catch (error) {
    console.error(error);
    res.status(500).send('❌ Failed to send email.');
  }
});


