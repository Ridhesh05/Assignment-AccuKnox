Q1 : By default Django Signals executed in synchronously.This means that the signal handler function is executed as part of the request-response cycle and blocks the request until the signal handler completes.

Q2 : Yes Signals run on same thread as the caller . When signal is emitted , all connected signals handlers are executed in the same thread that triggered the signal. This is part of the default synchronous execution model of Django signals.

Q3 : Yes by default do django signals run in the same database transaction as the caller ensuring that any changes made by signal handlers are committed or rolled back along with the original transaction.


Question 2 
Output 

![WhatsApp Image 2024-09-24 at 05 38 18_3f58dbc1](https://github.com/user-attachments/assets/51278312-3058-476d-82e5-2635e01a0a2a)




Question 3
Output 

![WhatsApp Image 2024-09-24 at 06 01 27_c7d622ff](https://github.com/user-attachments/assets/3541bdcb-16d6-4a43-8686-8fa877e5be72)
