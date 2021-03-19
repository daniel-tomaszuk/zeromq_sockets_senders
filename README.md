# TODO:

Use https://github.com/zeromq/pyzmq with FastAPI to create toy distributed applicaation montitoring.


1. Create multiple docker images with "microservices" and one docker compose file to run them all.
2. Create central monitoring server which will receive info from each service. Central server will serve montitoring page with data from each service.
3. Create web page that displays performance of each service in real time (use web sockets and zeromq). Use http://smoothiecharts.org/ to display performance graphs.

